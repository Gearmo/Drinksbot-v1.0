# -- Drinksbot v1.0

# -*- coding: UTF-8 -*-

commons = [
"a ð¥¤ Glass of Water.",
"a ð Lasagna Milkshake.",
"a â Dark Roast Coffee.",
"a â Skinny Latte.",
"an â Oatmilk Latte.",
"some ð¤® Soylent.",
"some ðµ Chai Tea.",
"some ð¿ Herbal Tea.",
"ð literally nothing.",
"some ð¥ Horchata.",
"a ð±epsi.",
"a ðº Norrlands Guld."
]

uncommons = [
"some ð¯ð» Sticky, Tasty Honey.",
"a ðð¸ Margarita.",
"some ððº Beer.",
"some ð¥ð³ Vodka.",
"some ð§ð· Fine Wine.",
"some ð¥´ð¥ Tequila.",
"some ðð¹ Cider."
]

rares = [
"a ð¾ðð« 7-Up.",
"a ð¾ðð« Sprite.",
"a ð¾ðð« Mt Dew.",
"a ð¥«ð«ð Pibb Extra.",
"a ð¿ðºð³ Root Beer."
]

epics = [
"a ð¥¶ð¥¤ð¤ð® Baja Blast.",
"ð«ðð¦ð¥ Quan's Vietnamese Coffee.",
"ððð§ðâ Dad's Armpit Sweat.",
"a â­ð§ð¼ð Starbucks Frapp.",
"some ð¤°ððð¥ Breast Milk."
]

legendaries = [
"a â¨ð²ð¹ð³ð Shiny Drink. WOAH!!!"
]

onestar = 4368/len(commons)
twostar = 2183/len(uncommons)
threestar = 1091/len(rares)
fourstar = 545/len(epics)

while onestar >0:
    for A in commons:
        print(A, file=open("List of Drinks.txt", "a", encoding='utf-8'))
    onestar -= 1
    
while twostar >0:
    for B in uncommons:
        print(B, file=open("List of Drinks.txt", "a", encoding='utf-8'))
    twostar -= 1
    
while threestar >0:
    for C in rares:
        print(C, file=open("List of Drinks.txt", "a", encoding='utf-8'))
    threestar -= 1
    
while fourstar >0:
    for D in epics:
        print(D, file=open("List of Drinks.txt", "a", encoding='utf-8'))
    fourstar -= 1
    
for E in legendaries:
    print(E, file=open("List of Drinks.txt", "a", encoding='utf-8'))
    
# -- Make sure to run the code JUST ONCE. Running it multiple times will create an unnecessarily long txt file.