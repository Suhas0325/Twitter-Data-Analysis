import csv

def preprocess_csv(input_file, output_file):
    seen_entries = set()  # For detecting duplicates

    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if not row or len(row) < 3:  # Skip empty or incomplete lines
                continue

            # Combine columns into a tuple to check for duplicates
            entry_tuple = tuple(row)
            if entry_tuple in seen_entries:
                continue  # Skip duplicate entries
            seen_entries.add(entry_tuple)

            # Remove quotes around text and special characters
            processed_row = [
                row[0],  # Keep the timestamp
                row[1].replace('"', '').replace('⛔', '').strip(),  # Process tweet content
                row[2].replace('"', '').strip()  # Location
            ]
            writer.writerow(processed_row)

# Usage
input_file = './TwitterData/tweets_preprocessed.csv'
output_file = './TwitterData/final_tweets_preprocessed.csv'
preprocess_csv(input_file, output_file)
