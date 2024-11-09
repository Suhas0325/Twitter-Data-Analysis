import csv

input_file = './TwitterData/twitter_dataset.csv'  # Your input file with raw data
output_file = './TwitterData/cleaned_twitter_data.csv'  # Your output file for cleaned data

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
     
    reader = csv.reader(infile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for row in reader:
        # Join lines that are split incorrectly (this assumes tweets are not empty)
        # Adjust according to your needs; here we join if the tweet is not complete
        if len(row) < 6:  # Adjust the number of fields based on your actual structure
            continue  # Skip incomplete rows
        
        # Clean tweet text
        row[2] = row[2].replace('\n', ' ')  # Replace newlines with space
        row[2] = row[2].replace('""', '"')  # Remove nested quotes

        # Write the cleaned row to the new CSV
        writer.writerow(row)
