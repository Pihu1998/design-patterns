class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, *kwargs)
        return instances[cls]

class SingletonClass:
    def __init__(self, data):
        self.data = data

    def display(self):
        print("Singleton instance with data: {}".format(self.data))

Instance1 = SingletonClass("instance1")
Instance2 = SingletonClass("instance2")
Instance1.display()
Instance2.display()



