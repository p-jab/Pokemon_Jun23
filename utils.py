'''Task 0: Import the modules csv and random'''
import csv, random

def startup():
    print("\t"*7, "Pokemon Trainer App")

def options():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Check your Pokemon', 'Add a new Pokemon', 'Show all Pokemon', 'Visualise' ,'Save your Pokedex' and 'Exit'

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    print("Choose an option:\n1-Check your Pokemon\n2-Add a new Pokemon\n3-Show all Pokemon\n4-Visualise\n5-Save your Pokedex\n0-Exit\nYour choice:")
    opt = int(input())
    if opt in [0, 1, 2 ,3, 4, 5]:
        return opt

def check_poke():
    """
    Task 3: Display a menu of options for how a Pokemon should be searched. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By name', 'By type'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("How would you like to search? :\n1-By name\n2-By type\nYour choice:")
    opt = int(input())
    if opt in [1, 2]:
        return opt

def add_poke():
    """
    Task 4: Display a menu of options for how a Pokemon should be added. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Add specific', 'Add at random'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("Who shall we add? :\n1-Add specific\n2-Add at random\nYour choice:")
    opt = int(input())
    if opt in [1, 2]:
        return opt

def visualise():
    """
    Task 5: Display a menu of options for how a graph should be produced. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By Generation (Pie Chart)', 'By Type (Bar Chart)'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """
    print("What to display? :\n1-By Generation (Pie Chart)\n2-By Type (Bar Chart)\nYour choice:")
    opt = int(input())
    if opt in [1, 2]:
        return opt

def by_name(p_list = []):
    
    """
    Task 6: Display a pokemon from the list, searching by name.

    The p_list is a list of pokemon.
    Prompt the user to enter name of the pokemon they are searching for.
    The function should display all the details related only to that single pokemon, if it's on the p_list.
    If pokemon of such name does not exist on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_name = input("Enter name of Pokemon: ")
    for pokemon in p_list:
        if pokemon[1].lower() == p_name.lower():
            print(pokemon)
            return
    print(f"Sorry, {p_name} is not on the list")

def by_type(p_list = []):
    
    """
    Task 7: Display pokemon from the list, searching by type.

    The p_list is a list of pokemon.
    Prompt the user to enter type of the pokemon they are searching for.
    The function should display all the details related only to pokemon of that type,
    if it's on the p_list.
    If no such pokemon of that type exists on the p_list, then display appropriate message.

    :param p_list: A list of pokemon
    :return: does not return anything
    """
    p_type = input("Enter type of Pokemon: ")
    types =[]
    for pokemon in p_list:
        if pokemon[2].lower() == p_type.lower() or pokemon[3].lower() == p_type.lower():
            types.append(pokemon)
    if len(types) == 0:
        print(f"Sorry, no Pokemon of type {p_type} is on the list")
    else:
        for poke in types:
            print(poke)

def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """
    p_name = input("Enter Pokemon name: ")
    p_list = load_pokes("pokemon_database.csv")
    for pokemon in p_list:
        if pokemon[1].lower() == p_name.lower():
            return pokemon
    print("Pokemon does not exist!")

def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """
    numb = random.randint(1, 801)
    return load_pokes("pokemon_database.csv")[numb]

def show_all(pokedex = []):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, total, hp and generation.

    :param p_list: None
    :return: None
    """
    for pokemon in pokedex:
        print(f"Name:{pokemon[1]:10}\tType:{pokemon[2]:6} {pokemon[3]:6}\tTotal:{pokemon[4]:4}\tHP:{pokemon[5]:3}\tGen:{pokemon[11]:1}")

def save_pokes(pokedex = []):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
        """
    with open("pokedex.csv", "w", newline="") as pdex:
        writer = csv.writer(pdex)
        for pokemon in pokedex:
            writer.writerow(pokemon)
    print("Saving complete")

def load_pokes(path):
    """
    Task 11.5: Load up pokemon from a CSV file into a list structure
    :param path: A relative file path to CSV file in string format
    :return: A list of pokemon
    """
    p_list = []
    with open(path) as f:
        reader = csv.reader(f)
        for pokemon in reader:
            p_list.append(pokemon)
    return p_list
