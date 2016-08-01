import operator
import string
import nltk
from nltk.util import ngrams
import json
import re
import visualizer


SOURCE_FILE = './scrapping-results.json'

# Returns the top "limit" users with the most questions asked
def get_most_active_users(data, limit):
	names = {}
	for q in data:
		if q['author'] not in names:
			names[q['author']] = 1
		else:
			names[q['author']] += 1
	return sorted(names.items(), reverse=True, key=operator.itemgetter(1))[:limit]

def get_node_content(node):
	return ' '.join([x[0] for x in node])

# Tries to extract the most common topics from the question's titles
def get_most_active_topics(data, limit):
	body = flatten_questions_titles(data)
	sentences = nltk.sent_tokenize(body) 
	sentences = [nltk.word_tokenize(sent) for sent in sentences]
	sentences = [nltk.pos_tag(sent) for sent in sentences]
	grammar = "NP: {<JJ>?<NN.*>}"
	cp = nltk.RegexpParser(grammar)	
	results = {}
	for sent in sentences:
		parsed = cp.parse(sent)
		trees = parsed.subtrees(filter=lambda x: x.label() == 'NP')
		for t in trees:
			key = get_node_content(t)
			if key in results:
				results[key] += 1
			else:
				results[key] = 1
	return sorted(results.items(), reverse=True, key=operator.itemgetter(1))[:limit]

# Returns the user that has the most answers
def get_most_helpful_user(data, limit):
	helpful_users = {}
	for q in data:
		for a in q['answers']:
			if a['author'] not in helpful_users:
				helpful_users[a['author']] = 1
			else:
				helpful_users[a['author']] += 1

	return sorted(helpful_users.items(), reverse=True, key=operator.itemgetter(1))[:limit]

# returns the top "limit" questions with the most amount of answers
def get_most_answered_questions(d, limit):
	questions = {}

	for q in d:
		questions[q['title']] = len(q['answers'])
	return sorted(questions.items(), reverse=True, key=operator.itemgetter(1))[:limit]


# Creates a single, lower cased string from the bodies of all questions
def flatten_questions_body(data):
	body = []
	for q in data:
		body.append(q['body'])
	return '. '.join(body)


# Creates a single, lower cased string from the titles of all questions
def flatten_questions_titles(data):
	body = []
	pattern = re.compile('(\[|\])')
	for q in data:
		lowered = string.lower(q['title'])
		filtered = re.sub(pattern, ' ', lowered)
		body.append(filtered)
	return '. '.join(body)

# Finds a list of the most common phrases of 'length' length
def get_most_common_phrases(d, limit, length):
	body = flatten_questions_body(d)
	phrases = {}
	for sentence in nltk.sent_tokenize(body):
		words = nltk.word_tokenize(sentence)
		for phrase in ngrams(words, length):
			if all(word not in string.punctuation for word in phrase):
				key = ' '.join(phrase)
				if key in phrases:
					phrases[key] += 1
				else:
					phrases[key] = 1

	return sorted(phrases.items(), reverse=True, key=operator.itemgetter(1))[:limit]

# Finds the answer with the least amount of characters
def get_shortest_answer(d):
	
	shortest_answer = {
		'body': '',
		'length': -1
	}
	for q in d:
		for a in q['answers']:
			if len(a['body']) < shortest_answer['length'] or shortest_answer['length'] == -1:
				shortest_answer = {
					'question': q['body'],
					'body': a['body'],
					'length': len(a['body'])
				} 
	return shortest_answer

# Load the json file and return the resulting dict
def load_json_data(file):
	with open(file) as input_file:
		return json.load(input_file)

def analyze_data(d):
	return {
		'shortest_answer': get_shortest_answer(d),
		'most_active_users': get_most_active_users(d, 10),
		'most_active_topics': get_most_active_topics(d, 10),
		'most_helpful_user': get_most_helpful_user(d, 10),
		'most_answered_questions': get_most_answered_questions(d, 10),
		'most_common_phrases':  get_most_common_phrases(d, 10, 4),
	}


data_dict = load_json_data(SOURCE_FILE)

results = analyze_data(data_dict)

print "=== ( Shortest Answer ) === "
visualizer.displayShortestAnswer(results['shortest_answer'])

print "=== ( Most Active Users ) === "
visualizer.displayMostActiveUsers(results['most_active_users'])

print "=== ( Most Active Topics ) === "
visualizer.displayMostActiveTopics(results['most_active_topics'])

print "=== ( Most Helpful Users ) === "
visualizer.displayMostHelpfulUser(results['most_helpful_user'])

print "=== ( Most Answered Questions ) === "
visualizer.displayMostAnsweredQuestions(results['most_answered_questions'])

print "=== ( Most Common Phrases ) === "
visualizer.displayMostCommonPhrases(results['most_common_phrases'])
