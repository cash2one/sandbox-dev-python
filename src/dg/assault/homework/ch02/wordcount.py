def word_count(statment):
    word_dict = {}

    for item in statment.split(" "):
        if item not in word_dict:
            word_dict[item] = 1
        else:
            word_dict[item] += 1
    return word_dict

if __name__ == "__main__":
    statment = "i am a student i am chinese"
    print(word_count(statment))
