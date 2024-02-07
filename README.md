this program is used for the read the a column from a csv file, and produce another csv with a column of unique row proudced by idenical or similar rows merged orginal column, and counts of the row next to it.
the current program can be reused and be solve scable similar issues


to use the program, you can do the following steps 
1. download the folder from the github. 
2. unzip the folder
3. start the termial
4. go the folder which contains this program: cd your_file_path
5. type the command line python3 dataReader -flags value
6. we have 7 flags for the program currtly:-s, -k, -o, -r,-oc, -c, -i, you can insert those flags with however order you like. you can insert -s, -k as many time as you need. -c,-i,-o,-r are single values, -oc is 2 values
7. -s is for separaters. suchs ; or , or . you need to use "" around the charater since they are special charators. You should insert the first level separator first, then second level separator and so on. for example, to use it you can do : python3 dataReader -s ";" -s "," 
8. -k is for keywords you like to search, such as "University", or "College". it is a hierarchical command. You should insert the highest hierarchy keyword first, then second level keyword and so on. for example, to use it you can do : python3 dataReader -k University -s College
9.  -i is a input file, so far, we support csv file as input file. to be easier, you can put the input file into this folder and you can type the file name instead of who file path. for example, to use it you can do : python3 dataReader -i your_file_path.csv
10. -o is a output file, so far, we support csv file as output file. it will out the file into this folder for example, to use it you can do : python3 dataReader -o your_file_name.csv
11. -c  is for column you'd like to read from input file.  for example, to use it you can do : python3 dataReader -i your_file_path.csv -c column_name
12. -oc is for define the columns name on your output file for example, to use it you can do : python3 dataReader -o your_file_name.csv -oc column_name -oc column_name
13. -r is set the lowest similarity to merge different rows from the input column. for example Univeristy of Masschusetts: Amherst and Univeristy of Masschusetts-Amherst and Univeristy of Masschusetts-Amhrest are greater than 0.8 similarty. If the set the -r 8.0 those 3 different row will merge to Univeristy of Masschusetts: Amherst. to use it you can do : python3 dataReader -o your_file_name.csv -r 0.8

A complete command line can be like python3 dataReader.py -k University -k College -i 2024.csv -c Affiliations -s ";" -s "," -r 0.80 -oc school -oc countted -o newShoolrow.csv -k School

this program can further developed. let me what function you need, please. thank you 
      
