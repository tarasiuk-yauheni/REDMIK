print('Czesc, jest developerem tego programu. To jest slownik meme-slowek ')
print('\n')

meme_dict = {
            "LOL": 'odpowiedź na coś zabawnego',
            "CRINGE":  'coś dziwnego lub wstydliwego',
            "ROFL": 'odpowiedź na żart',
            "SHEESH": 'lekka dezaprobata',
            "CREEPY": 'straszny, złowieszczy',
            "AGGRO": 'stać się agresywnym/zły',
    
}
word = input('Wpisz slowo, ktorego nie razumiesz(uzywaj wielkich liter!): ')
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('tego slowka nie ma :(')
