import json
pokedex = open("./pokedex.json", encoding="utf8")
pokedex = json.load(pokedex)
data=json.load(pokedex)
import json
items = open("./items.json", encoding="utf8")
items=json.load(items)
import json
moves = open("./moves.json",encoding="utf8")
moves=json.load(moves)
import json
types = open("./types.json",encoding="utf8")
types=json.load(types)




# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.