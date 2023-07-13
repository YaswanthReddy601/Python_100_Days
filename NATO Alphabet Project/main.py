import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

# phonetic_dict = {}
# for index, row in data.iterrows():
#     phonetic_dict[row.letter] = row.code
# print(phonetic_dict)

letters_data = {row.letter : row.code for (index, row) in data.iterrows()}

def phonetic():
    try:
        name = input("Enter your name : ").upper()
        name_list = [letters_data[x] for x in name]
    except KeyError:
        print("You have given numeric charecters in the name. Please try again ")
        phonetic()
    else:
        print(name_list)

phonetic()