#store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'lore': ['python', 'java'],
    'chris': ['ruby', 'r'],
    'ju': ['scala', 'julia'],
    'italo': ['c', 'c++'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


languages = {
    'lore': 'python',
    'chris': 'java',
    'ju': 'julia',
}

for nome, lan in languages.items():
  print(f"{nome.title()}, {lan.title()}")




