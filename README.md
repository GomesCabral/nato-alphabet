# NATO Phonetic Alphabet Converter

This is a simple Python script that converts each letter of a word entered by the user into its corresponding NATO phonetic code word. The app uses a CSV file containing the NATO phonetic alphabet and creates a dictionary to map letters to their phonetic codes.

## Features
- **Phonetic Code Conversion**: Converts each letter of the input word to its corresponding NATO phonetic code.
- **User Input**: Allows users to input any word, and it will display the corresponding phonetic codes for each letter.
- **Data from CSV**: The phonetic codes are read from a CSV file (`nato_phonetic_alphabet.csv`), making it easy to update or change the data source.

## Technologies Used
- **Python**: The programming language used for this script.
- **Pandas**: A Python library used for reading and manipulating CSV data.

## Requirements
Before running the script, make sure you have the following libraries installed:

```bash
pip install pandas
````
Usage
Clone this repository to your local machine:
  git clone https://github.com/your-username/nato-phonetic-alphabet-converter.git
Make sure the CSV file nato_phonetic_alphabet.csv is in the same directory as the script. The CSV file should have two columns: one for the letters (A-Z) and another for the corresponding phonetic code.

Run the script:
  python nato_phonetic_converter.py

The script will prompt you to enter a word. Once you enter the word, it will output the corresponding phonetic code words for each letter.
How the Script Works
Reading the CSV: The script loads the NATO phonetic alphabet from a CSV file (nato_phonetic_alphabet.csv) using the pandas.read_csv method.
Dictionary Creation: A dictionary (new_data) is created that maps each letter of the alphabet to its corresponding phonetic code.
User Input: The user is prompted to enter a word, and the script converts the word to uppercase to ensure uniformity.
Phonetic Code Generation: For each letter of the entered word, the corresponding phonetic code is retrieved from the dictionary and stored in a list.
Output: The list of phonetic code words is displayed as the final output.
Example
If the user enters the word hello, the output might look like this:
  Enter a word: hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
