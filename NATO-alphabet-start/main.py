import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter: row.code for (idx, row) in df.iterrows()}
while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(output_list)
        break