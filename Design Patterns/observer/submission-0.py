class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observers : List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.observers.append(observer)
        

    def unsubscribe(self, observer: Observer) -> None:
        self.observers.remove(observer)
        

    def updateStock(self, newStock: int) -> None:
        old_stock = self.stock
        self.stock = newStock
        if old_stock == 0 and self.stock > 0:
            self.notify_observers()
    
    def notify_observers(self) -> None:
        for observer in self.observers:
            observer.notify(self.itemName)
        
