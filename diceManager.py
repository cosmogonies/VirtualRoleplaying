import sys
import random

def chooseBetwween(_choices):
    return random.choices(_choices)

def chooseJanken():
    return chooseBetwween([":rock:Pierre", ":page_facing_up:Feuille", ":scissors:Ciseau"])[0]



    
    #return chooseBetwween(["Pierre", "Feuille", "Ciseau"])[0]

    # :punch :v    :raised_hand

def chooseTarotCard():
    return chooseBetwween(["I. Le Bateleur","II. la Grande Prêtresse","III. L'Impératrice","IV. L'Empereur","V. Le Hiérophante","VI. Les Amoureux","VII. Le Chariot","VIII. La Justice","IX. L'Ermite","X. La Roue de Fortune","XI. La Force","XII. Le Pendu","XIII. La Mort","XIV. Tempérance","XV. Le Diable","XVI. La Tour","XVII. L'Étoile","XVIII. La Lune","XIX. Le Soleil","XX. Le Jugement","XXI. Le Monde","XXII. Le Fou"])[0]


def rollDice(_sideNumber):
    values = range(1,_sideNumber+1)
    return chooseBetwween(values)


#MET "rolls"
def chooseChallengeSimple():
    return chooseBetwween(["Succès !", "Égalité", "Échec..."])[0]

def chooseChallengeComplex():
    return chooseBetwween(["Succès !", "Échec...", "Échec..."])[0]

