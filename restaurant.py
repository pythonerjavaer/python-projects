from dish import Dish

class Restaurant:
    def __init__(self, num_guests: int):
        """
        Initializes a restaurant with a given number of guests and an empty fridge.
        """
        self.num_guests = num_guests
        self.fridge: list[Dish] = []

    def add_dish(self, dish: Dish):
        """
        Adds a Dish object to the fridge.
        """
        if isinstance(dish, Dish):
            self.fridge.append(dish)

    def get_fridge(self) -> list[Dish]:
        """
        Returns the list of Dish objects in the fridge.
        """
        return self.fridge

    def serve_food(self) -> list[str]:
        """
        Serves the first available dish to each of the guests and returns a list of dish names served.
        If there is not enough food available for all guests, feed as many guests as possible.
        """
        served_dishes = []
        guests_served = 0
        
        for dish in self.fridge:
            while dish.get_quantity() > 0 and guests_served < self.num_guests:
                dish.consume()
                served_dishes.append(dish.name)
                guests_served += 1
        
        return served_dishes

    def has_stock(self) -> bool:
        """
        Returns True if there is at least one dish that can be consumed in the fridge.
        Returns False otherwise.
        """
        return any(dish.get_quantity() > 0 for dish in self.fridge)
    
if __name__ == "__main__":
    # Sample test cases
    salad = Dish("Salad", 2)
    curry = Dish("Curry", 4)
    restaurant = Restaurant(3)
    restaurant.add_dish(salad)
    restaurant.add_dish(curry)

    print(restaurant.serve_food()) # Example output: ['Salad', 'Salad', 'Curry']
    print(restaurant.has_stock()) # Example output: True