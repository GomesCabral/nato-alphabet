import pandas


#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#print(data)

new_data = {row.letter:row.code for (index, row) in data.iterrows()}
#print(new_data)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [new_data[letter] for letter in word]

#output_list = []
#for letter in word:
 #   output_list.append(new_data[letter])

print(output_list)