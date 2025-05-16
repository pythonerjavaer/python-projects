class Person:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
        self.children = []

    def add_child(self, child):
        self.children.append(child)
    
    def get_children_names(self):
        return [child.name for child in self.children]
    
    def dies(self):
        self.is_alive = False
        print(f"{self.name} has died :(")
    
    def count_living_descendants(self):
        count = 0
        for child in self.children:
            count += child.count_living_descendants()
            if child.is_alive:
                count += 1
        return count

    def __repr__(self):
        return self.name