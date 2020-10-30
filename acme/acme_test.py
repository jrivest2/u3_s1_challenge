import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_product_defaults(self):
        """Do the default inputs get expected outputs from member methods?"""
        prod = Product("Product_Name")
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
        self.assertEqual(prod.explode(), '...boom!')

    def test_product_varied(self):
        """Do explode and stealability methods output correctly given inputs"""
        # The default method above checks for the middle range outputs
        # so I just need the low range and high range outputs checked.
        prod1 = Product("Product_Name", price=1, weight=5, flammability=1)
        prod2 = Product("Product_Name", price=5, weight=1, flammability=51)

        self.assertEqual(prod1.stealability(), "Not so stealable...")
        self.assertEqual(prod1.explode(), "...fizzle.")
        self.assertEqual(prod2.stealability(), "Very stealable!")
        self.assertEqual(prod2.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Making sure the Acme reports are correct"""
    def test_default_num_products(self):
        """Make sure there really are 30 products being reported"""
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        """Make sure all the products produced have legal names"""
        # First generate a sample selection of products
        prods = generate_products()

        # Then loop through the products and assert that each product
        # has a legal name
        for prod in prods:
            adj, noun = prod.name.split()
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
