import pandas

letter_df = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index,row) in letter_df.iterrows()}

# for (index,row) in letter_df.iterrows():
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}

on_call = True

while on_call:
    word = input('Enter word').upper()
    try:
        output = [phonetic_dict[letter] for letter in word]

    except KeyError:
        print("Sorry, only letters in the alphabet please")

    else:
        print(output)

