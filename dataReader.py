import pandas as pd 
import requests
import json
import sys
import os
import csv
from firstLayerProcessor import firstLevelProcessor
from secondLevelProcessor import secondLevelProcessor

outPutcolumnName=[]
columnName=""
separator = []
keywords =[]
inputFile= ""
outputFile =""
rateOfSimlarity =0.0
roughList=[]
fineList = []
for a in range(len(sys.argv)):
	if sys.argv[a] == "-s":
		separator.append(sys.argv[a+1])
	if sys.argv[a] == "-k":
		keywords.append(sys.argv[a+1])
	if sys.argv[a] == "-i":
	    inputFile = sys.argv[a+1]
	if sys.argv[a] == "-o":
		outputFile = sys.argv[a+1]
	if sys.argv[a] == "-r":
	    rateOfSimlarity = float(sys.argv[a+1])
	if sys.argv[a] == "-c":
	    columnName = sys.argv[a+1]
	if sys.argv[a] =="-oc":
	    outPutcolumnName.append(sys.argv[a+1])


roughList=firstLevelProcessor(separator[0], inputFile, columnName, keywords)

newList = []
for a in range(1,len(separator)):
	if a < len(separator)-1:
	    for row in roughList:
		    newRow = row.split(separator[a])
		    newList.append(newRow)
	else:
	    fineList = secondLevelProcessor(roughList, rateOfSimlarity, separator[a])


outPutFilePath =  outputFile

outFile = pd.DataFrame(fineList, columns=[outPutcolumnName[0],outPutcolumnName[1]])

outFile.to_csv(outPutFilePath, index=False)

