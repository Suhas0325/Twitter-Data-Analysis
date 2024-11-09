import re

def preprocess_csv(input_file, output_file):
    # Regular expression to detect the start of a new record (e.g., starts with a date)
    timestamp_pattern = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        current_entry = []
        
        for line in infile:
            # Check if the line matches the start of a new record
            if timestamp_pattern.match(line):
                # If we already have data in current_entry, write it to the file
                if current_entry:
                    outfile.write(" ".join(current_entry).replace('\n', ' ').strip() + "\n")
                    current_entry = []  # Reset for the new entry
                current_entry.append(line.strip())
            else:
                # It's a continuation of the previous tweet
                current_entry.append(line.strip())

        # Write the last entry if any
        if current_entry:
            outfile.write(" ".join(current_entry).replace('\n', ' ').strip() + "\n")

# Usage
input_file = './TwitterData/Tweet-Immigration_1.csv'
output_file = './TwitterData/tweets_preprocessed.csv'
preprocess_csv(input_file, output_file)
