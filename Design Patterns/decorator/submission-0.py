class Coffee(ABC):
    @abstractmethod
    def getCost(self):
        pass

class SimpleCoffee(Coffee):
    def getCost(self):
        return 1.1

class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def getCost(self):
        return self.decoratedCoffee.getCost()


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    def getCost(self) -> float:
        return super().getCost() + 0.5
    

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getCost(self) -> float:
        return super().getCost() + 0.2

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)
    
    def getCost(self) -> float:
        return super().getCost() + 0.7


# The Decorator Pattern allows us to extend an object's behaviour dynamically without modifying its original class or creating multiple subclasses for every combination.

# In my coffee example, SimpleCoffee provides the base implementation, while MilkDecorator, SugarDecorator, and CreamDecorator wrap an existing Coffee object and add their own cost.

# Each decorator implements the same Coffee interface, so decorators can be chained together.

# Remember: Decorator = Wrapping an existing object and adding behaviour without modifying the original object.