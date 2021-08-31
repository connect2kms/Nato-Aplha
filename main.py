import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

#Loop through rows of a data frame
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

print(nato_dict)
{"A": "Alfa", "B": "Bravo"}

word = input("Enter your name: ").upper()

out_list = [nato_dict[letter] for letter in word]

print(out_list)