from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    products = []
    for i in range(0, num_products):
        generated_name = ''.join(sample(ADJECTIVES, 1)) + \
                         " " + ''.join(sample(NOUNS, 1))
        prod = Product(None)
        prod.name = generated_name
        prod.price = randint(5, 100)
        prod.weight = randint(5, 100)
        prod.flammability = uniform(0.0, 2.5)

        products.append(prod)
    return products


def inventory_report(products):

    names = []
    prices = []
    weights = []
    flammability_vals = []
    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammability_vals.append(product.flammability)

    def median(lst):
        n = len(lst)
        if n < 1:
            return None
        if n % 2 == 1:
            return sorted(lst)[n // 2]
        else:
            return sum(sorted(lst)[n // 2 - 1:n // 2 + 1]) / 2.0
    print(prices)

    unique = set(names)
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")

    unique_product_names = len(unique)
    print("Unique product names: " + str(len(unique)))

    avg_price = sum(prices)/len(prices)
    print("Average price: " + str(sum(prices)/len(prices)))

    print("Median price: " + str(median(prices)))

    avg_weight = sum(weights)/len(weights)
    print("Average weight: " + str(sum(weights)/len(weights)))

    print("Median weight: " + str(median(weights)))

    avg_flammability = sum(flammability_vals)/len(flammability_vals)
    print("Average flammability: " +
          str(sum(flammability_vals)/len(flammability_vals)))

    print("Median flammability: " + str(median(flammability_vals)))


    return {'products': products, 'unique_product_names': unique_product_names,
            'avg_price': avg_price, 'avg_weight': avg_weight,
            'avg_flammability': avg_flammability}
if __name__ == '__main__':
    inventory_report(generate_products())
