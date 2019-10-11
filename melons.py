from random import randint

"""Classes for melon orders."""
class AbstractMelonOrder():
    """Abstract class to hold shared attributes and functions for inheritance
    """

    def __init__(self, species, qty, order_type, tax, country_code = None):
        
        def get_base_price(self):

            return randint(5, 10)

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code
        self.base_price = get_base_price(self)


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.base_price
        international_fee = 0 

        if self.species == 'Christmas melon':
            base_price = base_price * 1.5 
        
        if self.country_code and self.qty < 10 :
            international_fee = 3 

        total = (1 + self.tax) * self.qty * base_price + international_fee

        return total
    #take get_base_price in get_total 
    #

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'domestic', 0.08)
        """Initialize melon order attributes."""



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty, 'international', 0.17)
        """Initialize melon order attributes."""

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order. Not taxed, requires inspection. """

    def __init__(self, species, qty):
        super().__init__(species, qty, 'government', 0)
        """Initialize melon order attributes."""

        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Updates inspection status"""

        self.passed_inspection = passed
