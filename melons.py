"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """ An abstract base class that other Melon Orders inherit from. """
    # if there were class attributes they would declared here

    def __init__(self, species, qty, country_code):
        """ Initializes melon order attributes. """
        # instance attributes (self. indicates this)
        self.order_type = None
        self.tax = None
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    # methods (mark_shipped, get_total)
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        # adjusts base price if melon species is a christmas melon
        if self.species == 'christmas melon':
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        # adjusts shipping cost if international order and quantity is less than 10
        if self.qty < 10 and self.country_code != 'USA':
            total += 3

        return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        # super function allows you to get the super class instance attributes. 
        # Self is instance of the DomesticMelonOrder class, and the dunder init 
        # arguments are being passed in the parent dunder init.
        super(DomesticMelonOrder, self).__init__(species, qty, 'USA')

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty, country_code)

        self.order_type = "international"
        self.tax = 0.17

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order from the US government. """

    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super(GovernmentMelonOrder, self).__init__(species, qty, 'USA')

        self.order_type = 'domestic'
        self.tax = 0

    def mark_inspection(self, passed):
        """Pass security inspection."""

        if passed is True:
            self.passed_inspection = passed
            return self.passed_inspection
