import pandas as pd
import requests
import json
import sys
import os
import csv
from difflib import SequenceMatcher

def firstLevelProcessor(separator,inputFile,columnName,keywords):
    separator = separator
    keywords = keywords
    inputFile = inputFile
    newList = []
    columnName = columnName

    file = pd.read_csv(inputFile, dtype=str)

    if columnName in file.columns:
        selected_column = file[columnName]
        for session in selected_column:
            subsession = session.split(separator)
            for sub in subsession:
                for key in keywords:
                    if key in sub:
                        newList.append([sub, key])
                        break

    return newList
