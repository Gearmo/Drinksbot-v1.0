# -- Drinksbot v1.0 --
# -- This is a code designed for a Twitch.tv command bot, such as NightBot or StreamElements. Upon typing "!drink" in chat, the bot pulls from a txt file with roughly 8192 possible drinks for the user to enjoy. That txt file is an export of this script, which first identifies a rarity (common, uncommon, rare, epic, or legendary), and then creates a unique drink from that rarity pool. Each drink rarity is defined my the number of emoji, 1 being common, 2 being uncommon, and so on. The highest rarity, with 5 emoji, only contains a single drink -- the shiny drink. This is reminiscent of finding a shiny Pokemon in the main line Pokemon games, at least until Generation 6 where the odds were halved.

# -*- coding: UTF-8 -*-

commons = [
"a 🥤 Glass of Water.",
"a 😂 Lasagna Milkshake.",
"a ☕ Dark Roast Coffee.",
"a ☕ Skinny Latte.",
"an ☕ Oatmilk Latte.",
"some 🤮 Soylent.",
"some 🍵 Chai Tea.",
"some 🌿 Herbal Tea.",
"😀 literally nothing.",
"some 🥛 Horchata.",
"a 🅱epsi.",
"a 🍺 Norrlands Guld."
]

uncommons = [
"some 🍯🐻 Sticky, Tasty Honey.",
"a 🍋🍸 Margarita.",
"some 😏🍺 Beer.",
"some 🥃😳 Vodka.",
"some 🧐🍷 Fine Wine.",
"some 🥴🥃 Tequila.",
"some 🍎🍹 Cider."
]

rares = [
"a 🍾😂😫 7-Up.",
"a 🍾😂😫 Sprite.",
"a 🍾😂😫 Mt Dew.",
"a 🥫😫👌 Pibb Extra.",
"a ⬛🍺🌳 Root Beer."
]

epics = [
"a 🥶🥤🤗🌮 Baja Blast.",
"😫🍆💦🥛 Quan's Vietnamese Coffee.",
"👌😍💧🙋‍ Dad's Armpit Sweat.",
"a ⭐🧊🍼💚 Starbucks Frapp.",
"some 🤰🍈🍈🥛 Breast Milk."
]

legendaries = [
"a ✨😲🍹😳🌟 Shiny Drink. WOAH!!!"
]

onestar = 4368/len(commons)
twostar = 2183/len(uncommons)
threestar = 1091/len(rares)
fourstar = 545/len(epics)

while onestar >0:
    for A in commons:
        print(A, file=open("drinks.txt", "a", encoding='utf-8'))
    onestar -= 1
    
while twostar >0:
    for B in uncommons:
        print(B, file=open("drinks.txt", "a", encoding='utf-8'))
    twostar -= 1
    
while threestar >0:
    for C in rares:
        print(C, file=open("drinks.txt", "a", encoding='utf-8'))
    threestar -= 1
    
while fourstar >0:
    for D in epics:
        print(D, file=open("drinks.txt", "a", encoding='utf-8'))
    fourstar -= 1
    
for E in legendaries:
    print(E, file=open("drinks.txt", "a", encoding='utf-8'))
    
        