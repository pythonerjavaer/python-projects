class Dish:
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def get_quantity(self) -> int:
        """
        Returns the quantity remaining.
        """
        return self.quantity

    def consume(self) -> bool:
        """
        Consumes food by decreasing the quantity by 1.

        Returns True if the dish can be consumed.

        Returns False if no more dishes are available.
        """
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False