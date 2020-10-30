"""Report Acme Outputs"""

from acme import Product, BoxingGlove
from random import *

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(n=30):
    """Generate n random products"""
    # Begin with an empty product list
    prods = []

    # Make lists for each of the attributes
    names = []
    prices = []
    weights = []
    flam_stats = []

    # Use a loop to populate each attribute list with random values
    for i in range(n):
        # Make an instance of each attribute
        newName = choice(ADJECTIVES) + " " + choice(NOUNS)
        newPrice = randint(5, 101)
        newWeight = randint(5, 101)
        newFlam_stat = uniform(0.0, 2.5)

        # Append attributes instances to their respective lists
        names.append(newName)
        prices.append(newPrice)
        weights.append(newWeight)
        flam_stats.append(newFlam_stat)

        # Add the new product to the product list
        prods.append(Product(names[i], prices[i], weights[i], flam_stats[i]))

    return prods


def inventory_report(prods):
    # Calculate the number of unique product names in prods list
    names = set()
    for i in range(len(prods)):
        names.add(prods[i].name)

    # Calculate the average price, weight, and flam_stat of prods list products
    total_prices = 0
    total_weights = 0
    total_flam_stats = 0
    for prod in prods:
        total_prices += prod.price
        total_weights += prod.weight
        total_flam_stats += prod.flammability

    avgPrice = total_prices / len(prods)
    avgWeight = total_weights / len(prods)
    avgFlam_stat = total_flam_stats / len(prods)

    # Prettily print the title of the report
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")

    # Print number of unique product names in prods list
    print(f"Unique product names: {len(names)}")

    # Print the averages of price, weight, and flam_stat
    print(f"Average price: {avgPrice}")
    print(f"Average weight: {avgWeight}")
    print(f"Average flammability: {avgFlam_stat}")

if __name__ == '__main__':
    inventory_report(generate_products())
