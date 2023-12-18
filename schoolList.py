import pandas as pd 
import requests
import json
import sys
import os
import csv

file_path ="2024.csv"
columnName = "Affiliations"
schoolList =[]
file = pd.read_csv("2024.csv", dtype=str)
library =["University","School","College","Institute"]
if columnName in file.columns:
	selected_column =file[columnName]
	for value in selected_column:
		sessions= value.split(';')
		for session in  sessions:
			clauses = session.split(',')
			for clause in clauses:
				if "University" in clause or "College" in clause or "School" in clause or "Institute" in clause:
					print(clause.strip().lower())
					found = False;
					for school in schoolList:
						clause=clause.strip()
						if clause in school:
							currentCount= school[1]
							school[1]=currentCount+1
							found = True
							break
					if found == False:
						iniCount= 1
						schoolList.append([clause.strip(), iniCount] )
for thisSchool in schoolList:
	print(thisSchool)

outPutFilePath= "schoolListResult.csv"

outFile=pd.DataFrame(schoolList, columns =["School","Count"])

outFile.to_csv(outPutFilePath, index=False)

print("csv was wrote")

