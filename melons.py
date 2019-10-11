"""Classes for melon orders."""
class AbstracMelonOrder():
    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        international_fee = 0 

        if self.species == 'Christmas melon':
            base_price = base_price * 1.5 
        
        if self.country_code and self.qty < 10 :
            international_fee = 3 

        total = (1 + self.tax) * self.qty * base_price + international_fee

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstracMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstracMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        """Initialize melon order attributes."""
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
