import pandas as pd
import requests
import json
import sys
import os
import csv
from difflib import SequenceMatcher

def arrayProcessor(separator,inputList):
    separator = separator
    inputList = inputLit
    newList = []

    for session in inputList:
        subsession = session[0].split(separator)
        key = session[1]
        for sub in subsession:
            if key in sub:
               newList.append([sub, key])
               break

    return newList
