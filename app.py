import json
import os
pokedex = open("./pokedex.json", encoding="utf8")
pokedexes = json.load(pokedex)
data=json.load(pokedex)

items = open("./items.json", encoding="utf8")
itemslist=json.load(items)

moves = open("./moves.json",encoding="utf8")
movesamount = json.load(moves)

def print_pokemon_names(pokedex.json):
    if not os.path.exists(pokedex.json):
        print(f"Error: The file '{pokedex.json}' was not found.")
        return
    if "pokemon_list" in data and isinstance["pokemon_list"]
            print(f"--- Pokémon Names from {pokedex.json} ---")
            # Iterate through the list and print each name
            for pokemon in pokedex.json:
                if "name" in pokemon:
                    print(pokemon["name"])
                else:
                    print("Found a Pokémon entry without a name.")
            print("--- End of List ---")
elif print("Error: JSON structure invalid. Expected a list under the key 'pokemon_list'.")
if __name__ == "__main__":
    print_pokemon_names(pokedex.json)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.
