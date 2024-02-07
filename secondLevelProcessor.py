import pandas as pd
import requests
import json
import sys
import os
import csv
from difflib import SequenceMatcher

schoolList = []

def secondLevelProcessor(newList, similarity, separator):

    newList=newList

    for oldWords in newList:
        words = oldWords[0]
        print(words)
        key = oldWords[1]
        print(key)
        word = words.split(separator)
        print(word)
        for subword in word:
            if key in subword and "Way" not in subword and "Street" not in subword and "Avenue" not in subword and "Station" not in subword and len(subword)>len(key):
                print("in the third loop")
                newSubword = stringCleaner(subword)
                count =0
                found = False
                for school in schoolList:
                    newSchool = stringCleaner(school[0])
                    if SequenceMatcher(None, newSubword, newSchool).ratio() > similarity:
                        school[1]=school[1]+1
                        found = True
                        break
                if found == False:
                    initCount = 1
                    schoolList.append([subword,initCount])
    return schoolList


def stringCleaner (word):
     word = word.replace(" - ", " ").replace("at", " ").replace(
                        ".", " ").replace(":", " ").replace("/", " ").replace("\\", " ").lower().strip()
     return word
