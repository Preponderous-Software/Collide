import datetime
import random
import os


keywords = []
pairs = []
ideas = []

def getKeywords():
    # get 10 keywords from user
    numKeywords = 10
    for i in range(numKeywords):
        if i == 0:
            keyword = input("Enter 1st keyword: ")
            keywords.append(keyword)
        elif i == 1:
            keyword = input("Enter 2nd keyword: ")
            keywords.append(keyword)
        elif i == 2:
            keyword = input("Enter 3rd keyword: ")
            keywords.append(keyword)
        else:
            keyword = input("Enter " + str(i+1) + "th keyword: ")
            keywords.append(keyword)

    # randomize keywords
    random.shuffle(keywords)


def createPairs():
    # match keywords in pairs
    for i in range(0, len(keywords), 2):
        pair = []
        pair.append(keywords[i])
        pair.append(keywords[i+1])
        pairs.append(pair)

def promptForIdeas():
    # show pairs to user and prompt for ideas
    for i in range(len(pairs)):
        print("Enter an idea based off of these keywords: " + str(pairs[i]))
        idea = input("Enter an idea: ")
        ideas.append(idea)
    
def writeToFile():
    # make folder if nonexistent
    if not os.path.exists("ideas"):
        os.makedirs("ideas")

    # get timestamp for filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")
    filename = "ideas/ideas-" + timestamp + ".txt"

    # write idea to file
    with open(filename, "a") as f:
        for i in range(len(pairs)):
            f.write(str(pairs[i]) + ": " + ideas[i] + "\n")

def main():
    getKeywords()
    createPairs()
    promptForIdeas()
    writeToFile()

main()