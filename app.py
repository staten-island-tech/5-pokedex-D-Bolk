import json
import os

POKEDEX_FILE = "./pokedex.json"

def load_pokedex():
    if not os.path.exists(POKEDEX_FILE):
        print(f"Error: File '{POKEDEX_FILE}' not found.")
        return None

    with open(POKEDEX_FILE, encoding="utf8") as file:
        data = json.load(file)

    if not isinstance(data, list):
        print("Error: Expected JSON to be a list of Pokémon.")
        return None

    return data

def print_pokemon_names(pokemon_list):
    print("\n--- Pokémon Names ---")
    for pokemon in pokemon_list:
        print(pokemon["name"]["english"])
    print("--- End of List ---\n")

def print_by_language(pokemon_list):
    language = input("Choose language (english/japanese/chinese/french): ").lower()

    print(f"\n--- Pokémon Names in {language.capitalize()} ---")

    found = False
    for pokemon in pokemon_list:
        if language in pokemon["name"]:
            print(pokemon["name"][language])
            found = True

    if not found:
        print("Language not found in data.")

    print()

def search_by_type(pokemon_list):
    search_type = input("Enter Pokémon type: ").capitalize()

    results = []

    for pokemon in pokemon_list:
        if search_type in pokemon["type"]:
            results.append(pokemon["name"]["english"])

    if results:
        print(f"\nPokémon with type '{search_type}':")
        for name in results:
            print(name)
    else:
        print(f"\nNo Pokémon found with type '{search_type}'.")

    print()

def search_by_name(pokemon_list):
    search_text = input("Enter name to search: ").lower()

    results = []

    for pokemon in pokemon_list:
        name = pokemon["name"]["english"]
        if search_text in name.lower():
            results.append(name)

    if results:
        print("\nMatching Pokémon:")
        for name in results:
            print(name)
    else:
        print("\nNo Pokémon found matching that name.")

    print()

def main():
    pokemon_list = load_pokedex()
    if not pokemon_list:
        return

    while True:
        print("==== Pokédex Menu ====")
        print("1. Print all Pokémon")
        print("2. Print Pokémon by language")
        print("3. Search Pokémon by type")
        print("4. Search Pokémon by name")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_pokemon_names(pokemon_list)
        elif choice == "2":
            print_by_language(pokemon_list)
        elif choice == "3":
            search_by_type(pokemon_list)
        elif choice == "4":
            search_by_name(pokemon_list)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

main()

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found.

#Show all moves of pokemon and types by searching it.