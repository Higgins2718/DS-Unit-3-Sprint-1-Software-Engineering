import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
from acme_report import inventory_report, generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

        """Test default product weight being 20."""
        self.assertEqual(prod.weight, 20)
        prod_2 = Product('Test Product no. 2')
        prod_2.flammability = 0.5
        prod_2.weight = 41
        prod_2.price = 26
        self.assertEqual(prod.explode(), "...boom!")
        self.assertEqual(prod.stealability(), "Kinda stealable.")


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_num_products(self):
        products = generate_products(30)
        report = inventory_report(products)

        self.assertEqual(len(report['products']), 30)

    def test_legal_names(self):
        products = generate_products(30)

        ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        SPACE = [' ']
        concatenated = ADJECTIVES + NOUNS + SPACE

        for product_val in products:
            name_split = product_val.name.split(" ", 2)
            for component in name_split:

                self.assertIn(component, concatenated)


if __name__ == '__main__':
    unittest.main()
