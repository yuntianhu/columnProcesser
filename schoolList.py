import pandas as pd
import sys


def extract_schools_from_affiliations(affiliations, keywords, splitter):
    schools = []
    for session in affiliations.split(splitter):
        for clause in session.split(','):
            if any(keyword in clause for keyword in keywords):
                school_name = clause.strip().lower()
                schools.append(school_name)
    return schools

def main(file_path, column_name, output_file_path, keywords, splitter):
    try:
        df = pd.read_csv(file_path, dtype=str)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    if column_name not in df.columns:
        print(f"Error: Column '{column_name}' not found in the file.")
        sys.exit(1)

    affiliations_column = df[column_name]
    school_list = []

    for value in affiliations_column:
        schools = extract_schools_from_affiliations(value, keywords, splitter)
        school_list.extend(schools)

    school_counts = pd.Series(school_list).value_counts().reset_index()
    school_counts.columns = ["School", "Count"]

    school_counts.to_csv(output_file_path, index=False)

    print("CSV was written")

if __name__ == "__main__":
    input_file = sys.argv[0]
    column_name = sys.argv[1]
    keywords = []
    splitter = []
    for item in sys.argv:
        if item[0] == "-" AND item[1] == 'k':
            keywords.append[item]

    for item in sys.argv:
            if item[0] == "-" AND item[1] == 's':
                keywords.append[item]

    main(input_file, column_name, output_file, keywords, splitter)
