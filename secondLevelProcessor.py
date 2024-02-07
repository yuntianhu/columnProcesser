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
    addressLIst = ["Way","Street","Avenue","Station","Park"]

    for oldWords in newList:
        words = oldWords[0]
        key = oldWords[1]
        word = words.split(separator)
        print(word)
        for subword in word:
            if key in subword and addressFilter(addressLIst,subword) and stringCleaner(subword) != stringCleaner(key):
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



def addressFilter (addressLIst, word):
    for a in addressLIst:
        if a in word:
             checkAddress = False
             break
        else:
            checkAddress = True

    return checkAddress
