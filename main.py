import pandas


df_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
df_alphabet = pandas.DataFrame(df_alphabet)

dict_alphabet = {row.letter:row.code for (index, row) in df_alphabet.iterrows()}

print(dict_alphabet)

user_word = input("Enter the word you want to phonetically say > ")
user_word = user_word.upper()

result = [dict_alphabet[char] for char in user_word]

print(result)
