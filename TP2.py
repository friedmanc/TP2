"""TP2
Caleb Friedman Groupe 402"""
import random

nb_random = random.randint(0, 100)


nb_essaie = 0


prompt = input("Voulez-vous jouer le jeu de devinette? (o/n)")


while prompt == 'o':
    nb_choisis = int(input("J'ai choisis un nombre entre 0 et 100"))

