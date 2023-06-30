import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

# for (index,row) in nato_data.iterrows():
#     nato_dictionary[row.letter] = row.code
#     print(row.letter)
#     print(row.code)

nato_dictionary = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ")
    try:
        user_list = list(user_input.upper())
        output = [nato_dictionary[letter] for letter in user_list]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()



