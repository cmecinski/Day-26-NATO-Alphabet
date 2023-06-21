import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

# for (index,row) in nato_data.iterrows():
#     nato_dictionary[row.letter] = row.code
#     print(row.letter)
#     print(row.code)

nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}

user_input = input("Enter a word: ")
user_list = list(user_input.upper())
output = [nato_dictionary[letter] for letter in user_list]

print(output)
