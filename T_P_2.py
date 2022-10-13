"""TP2
Caleb Friedman 402"""



import random
keep_playing = str(input('voulez-vous jouer un jeu de devinette(encore)? o/n '))
minimum = int(input('choisisez un nombre minimal '))
maximum = int(input('choisisez un nombre maximum '))
nb_random = random.randint(minimum,maximum)
nb_essai= 0



while keep_playing == 'o' :
   nb_choisis = int(input('devinez le nombre que jai choisis. '))
   if nb_choisis == nb_random :
       print('félicitations, vous lavait deviner!')
       print( 'nombre dessaie(s): ')
       nb_essai
       keep_playing = str(input('voulez-vous jouer un jeu de devinette(encore)? o/n '))
   elif nb_choisis > nb_random :
       print('votre nombre deviner est plus grand que le nombre que jai choisis')
       nb_essai = nb_essai + 1
   else :
       print('votre nombre deviner est plus petit que le nombre que jai choisis')
       nb_essai = nb_essai + 1
else:
   print('Bye!')

