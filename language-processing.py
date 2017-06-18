#!/usr/bin/python

from nltk.stem import porter
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from PyDictionary import PyDictionary

def lemmatizing(word_list, lemmatizer, dictionary):
    lemmatized = []
    for word in word_list:
        type_word = typeWord(word, dictionary)
        if type_word != "Ignore":
            if type_word == "Noun":
                lemmatized.append(lemmatizer.lemmatize(word, pos='n'))
            else:
                lemmatized.append(lemmatizer.lemmatize(word, pos='v'))
    return lemmatized

def stemming(word_list, stemmer):
    stemmed = []
    for word in word_list:
        stemmed.append(stemmer.stem(word))
    return stemmed

def tokenizing(string):
    return word_tokenize(string)

def typeWord(word, dictionary):
    print(word)
    meaning = dictionary.meaning(word)
    gmeaning = dictionary.googlemeaning(word)
    if (meaning == None and gmeaning == None):
        return "Ignore"
    else:
        if meaning != None and meaning.keys()[0] == "Verb":
            return "Verb" 
        else:
            return "Noun"

def removeStopWords(tokenizedString, stopWords):
    wordsFiltered = []
    for word in tokenizedString:
        if word not in stopWords:
            wordsFiltered.append(word)
    return wordsFiltered
            
def closestSynonym(noun1, noun2, dictionary):
    synonym1 = dictionary.synonym(noun1)
    synonym2 = dictionary.synonym(noun2)
    if (synonym1 != None and synonym2 != None):
        for synonym in synonym1:
            try: 
                synonym2.index(synonym)
                return synonym
            except ValueError:
                continue
    return None

def synonymList(wordList1, wordList2, dictionary):
    synonymList1 = []
    synonymList2 = []
    for (word1, word2) in zip(wordList1, wordList2):
        synonym = closestSynonym(word1, word2, dictionary)
        if (synonym == None):
            synonymList1.append(word1)
            synonymList2.append(word2)
        else:
            synonymList1.append(synonym)            
            synonymList2.append(synonym)
    return synonymList1,synonymList2

def twoListOp(list1, list2, arithOperation):
    score = 0;
    for ele1 in list1:
        try: 
            list2.index(ele1)
            score = arithOperation(score)
        except ValueError:
            continue
    return score

def sentenceDistance(wordList1, wordList2):
    numberWords = max(len(wordList1), len(wordList2))
    sameWords = twoListOp(wordList1, wordList2, lambda x:x+1)
    diferentWords = numberWords - sameWords
    scoreDistance = (sameWords/float(numberWords))*0.2 + (diferentWords/float(numberWords))*0.8
    return scoreDistance

def isSameQuestion(wordList1, wordList2):
    scoreDistance = sentenceDistance(wordList1, wordList2)
    print(scoreDistance)
    if (scoreDistance > 0.5):
        return False
    else:
        return True

with open("train-sample.csv", "r") as tests:
    stemmer = porter.PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    dictionary = PyDictionary()
    stopWords = set(stopwords.words('english'))
    line = tests.readline()
    while(line):
        line = tests.readline()
        line = line.split(",")
        question_1 = tokenizing(line[3])
        question_2 = tokenizing(line[4])
        question_1 = question_1[1:-1]
        question_2 = question_2[1:-1]

        question_1 = lemmatizing(question_1, lemmatizer, dictionary)
        question_2 = lemmatizing(question_2, lemmatizer, dictionary)

        print(question_1)
        print(question_2)
        print(isSameQuestion(question_1, question_2))