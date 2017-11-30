#!/usr/bin/python

import sys

dict_words = {}

def preprocess():
    dict_file = open(sys.argv[1], "r")
    list_words = [line.rstrip('\n').lower() for line in dict_file.readlines()]

    for word in list_words:
        word_list = list(word)
        word_list.sort()
        index = "".join(word_list)

        if index in dict_words:
            dict_words[index].append(word)
        else:
            anagrams = [word]
            dict_words[index] = anagrams

    for index in dict_words:
        for i in range(1, len(index)):
            if index[i:] in dict_words:
                dict_words[index].append(dict_words[index[i:]])

    for index in dict_words:
        dict_words[index].sort()
        dict_words[index] = " ".join(dict_words[index])


def anagram_finder():
    while True:
        word = raw_input("").lower()
        
        if word == "":
            return

        word_list = list(word)
        word_list.sort()
        index = "".join(word_list)

        if index in dict_words:
            print(dict_words[index])
        else:
            print("-")


preprocess()
anagram_finder()
