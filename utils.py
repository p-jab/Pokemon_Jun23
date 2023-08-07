'''Task 0: Import the modules csv and random'''


def startup():    
    """
    Task 1: Display an entry message.

    The message should consist of the of the name of your application centered in the middle of the console.

    :return: Does not return anything.
    """


def options():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Check your Pokemon', 'Add a new Pokemon', 'Show all Pokemon', 'Visualise' ,'Save your Pokedex' and 'Exit'

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """


def check_poke():
    """
    Task 3: Display a menu of options for how a Pokemon should be searched. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By name', 'By type'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """


def add_poke():
    """
    Task 4: Display a menu of options for how a Pokemon should be added. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Add specific', 'Add at random'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """

def visualise():
    """
    Task 5: Display a menu of options for how a graph should be produced. Read in the user's response.

    A menu should be displayed that contains the following options:
        'By Generation (Pie Chart)', 'By Type (Bar Chart)'

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """

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

def add_specific_poke():
    
    """
    Task 8: Search for pokemon in the database, and return it if it's found.

    Access pokemon_database.csv using appropriate module.
    Search through this database, looking for a pokemon by it's name.
    If no such pokemon exists, then display appropriate message and return None.

    :param: None
    :return: A list representing a pokemon or None
    """

def add_random_poke():
    
    """
    Task 9: Search for a random pokemon in the database, and return it.

    Access pokemon_database.csv using appropriate module.
    Pick out a random pokemon and return it.

    :param:  None
    :return: A list representing a pokemon
    """

def show_all(pokedex = []):
    """
    Task 10: Print all pokemon from pokedex.

    Print key information about all the pokemon in the pokedex. Include their
    name, type, total, hp and generation.

    :param p_list: None
    :return: None
    """

def save_pokes(pokedex = []):
    """
    Task 11: Save content of the pokedex to a suitable file format
    Print "Saving complete" at the end.

    :param p_list: pokedex: a list of pokemon
    :return: None
    """

def load_pokes(path):
    """
    Task 11.5: Load up pokemon from a CSV file into a list structure
    :param path: A relative file path to CSV file in string format
    :return: A list of pokemon
    """