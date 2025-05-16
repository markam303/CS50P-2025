class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not capacity:
            raise ValueError("Wrong capacity")
        self.capacity = capacity

    def __str__(self):
        return f"🍪" * self.capacity

    def deposit(self, n):
        self.capacity += n
        return self.capacity 
    def withdraw(self, n):
        ...

    @property
    def capacity(self):
        ...

    @property
    def size(self):
        ...


def main():
    ...


if __name__ == "__main__":
    main()