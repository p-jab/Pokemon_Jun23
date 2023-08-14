import matplotlib.pyplot as plt

def pie_chart(pokedex = []):
    """
    Task 27: Create a Pie Chart showing pokemon from pokedex sorted by their generation

    Access the pokedex, sort out pokemon by generation and plot this data in a
    pie chart format. Add labels to clearly identify each generation.

    :param pokedex: list of pokemon
    :return: None
    """
    p_dict = {}# {"1":3, "2": 1, "7":2}
    for pokemon in pokedex:
        p_dict[pokemon[11]] = p_dict.get(pokemon[11], 0) + 1
    p_labels = [f"Generation {x}" for x in p_dict.keys()] #List comprehension
    plt.pie(p_dict.values(), labels=p_labels, autopct="%.0f%%")
    plt.title("Pokemon by Generation")
    plt.show()

def bar_chart(pokedex = []):
    """
    Task 28: Create a Bar Chart showing pokemon from pokedex sorted by their type

    Access the pokedex, sort out pokemon by type and plot this data in a
    bar chart format. Add axis labels and main title.

    :param pokedex: list of pokemon
    :return: None
    """