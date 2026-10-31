class Singleton:

    # In python consider this method as the 'getInstance'
    _unique_instance = None 
    def __new__(cls):
        if cls._unique_instance is None:
            cls._unique_instance = super().__new__(cls)
        return cls._unique_instance

    def __init__(self):
        if not hasattr(self, "value"):
            self.value = None 

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
