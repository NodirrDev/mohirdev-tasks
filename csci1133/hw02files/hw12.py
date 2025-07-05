from math import trunc

# Problem A

class Item:
    '''
    Purpose:
    It represents a single item available for purchase in a store
    Instance variables:
    name (str): name of the item
    price (float): the price of item
    category (str): category of the item, it must be one of the following:
    'Head' , 'Torso', 'Legs', or 'Feet'.
    store (str): name of the store where the item is sold
    Methods:
    __init__(self, csv_string, store) (constructor): Initializes Item object using
    CSV-formatted string and  store name.
    __str__(self): Returns string representation of the item in the format
    "<name> (<category>): $<price>".
    __lt__(self, other): Compares two Item objects based on their price. Returns True if current item's price
      is less than other item's price, otherwise returns False.

    '''

    def __init__(self, cvs_string, store):
        cvs_string_list = cvs_string.split(',')
        self.name = cvs_string_list[0]
        self.price = float(cvs_string_list[1])
        self.category = cvs_string_list[2]
        self.store = store

    def __str__(self):
        return f'{self.name} ({self.category}): ${self.price}'

    def __lt__(self, other):
        if self.price < other.price:
            return True
        return False





# Problem B

class Store:
    '''
    Purpose:
    Represents a store containing several items.
    Instance variables:
    name (str): the name of store
    items (list of Item objects): A list containing Item objects that represent the store's inventory.
    Methods:
    __init__(self, name, filename) (constructor): Initializes the Store object with
    a name and list of items containing Item objects
    __str__(self): Returns string representation of the store, including the name of the store and the
    string representation of each item separated by newlines.
    '''

    def __init__(self, name, filename):
        self.name = name
        temp_list = []
        fp = open(filename)
        fp.readline()
        for line in fp:
            temp_list.append(Item(line.strip(), name))
        self.items = temp_list

    def __str__(self):
        name_of_store = self.name + '\n'

        items_string = ''
        for item in self.items:
            items_string += str(item) + '\n'

        return name_of_store + items_string



# Problem C

def cheap_outfit(store_list):
    cheapest_outfit_dic = {}

    for store in store_list:
        for item in store.items:
            if item.category not in cheapest_outfit_dic:
                cheapest_outfit_dic[item.category] = item
            elif item < cheapest_outfit_dic[item.category]:
                cheapest_outfit_dic[item.category] = item
    return cheapest_outfit_dic













