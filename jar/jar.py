class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not capacity:
            raise ValueError("Wrong capacity")
        self.capacity = capacity

    def __str__(self):
        return f"🍪" * self._capacity

    def deposit(self, n):
        ...

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