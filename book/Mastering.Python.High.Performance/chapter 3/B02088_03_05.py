import sys

#Turns a list of entries from the index file into a dictionary indexed
#by words
def list2dict(l):
	retDict = {}
	for item in l:
		lineParts = item.split(',(')
		word = lineParts[0]
		indexDataParts = [x.replace(")","") for x in lineParts[1:]]
		retDict[word] = indexDataParts
	return retDict

#Load the index's content into memory and parse it
def loadIndex():
	indexFilename = "./index-file.txt"
	with open(indexFilename, 'r') as fh:
		#instead of looping through every line to append it into an array, we use the readlines method which does that already
		indexLines = fh.readlines()
		index = list2dict(indexLines)
		return index

#Reads the content of a file, takes care of fixing encoding issues with utf8 and removes unwanted characters (the ones we didn't want when generating the index)#
def readFileContent(filepath):
    with open(filepath, 'r') as f:
    	return [x.replace(",", "").replace(".","").replace("\t","").replace("\r","").replace("|","").strip(" ") for x in f.read().decode("utf-8-sig").encode("utf-8").split( '\n' )]

def findMatch(results):
	matches = []
	for r in results:
		parts = r.split(',')

		filepath = parts[0]
		del parts[0]
		fileContent = ' '.join(readFileContent(filepath))
		for offset in parts:
			ioffset = int(offset)
			if ioffset > 0:
				ioffset -= 1
			matchLine = fileContent[ioffset:(ioffset + 100)]
			matches.append(matchLine)
	return matches

#Search for the word inside the index
def searchWord(w):
	index = None	
	index = loadIndex()
	result = index.get(w)
	if result:
		return findMatch(result)
	else:
		return []

#Let the user define the search word...
searchKey = sys.argv[1] if len(sys.argv) > 1 else None

if searchKey is None: #if there is none, we output a usage message
	print "Usage: python search.py <search word>"
else: #otherwise, we search
	results = searchWord(searchKey)
	if not results:
		print "No results found for '%s'" % (searchKey)
	else:
		for r in results:
			print r