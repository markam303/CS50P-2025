class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not capacity:
            raise ValueError("Wrong capacity")
        if capacity > 12:
            raise ValueError("Jar is full")
        self.capacity = capacity

    def __str__(self):
        return f"🍪" * self.size

    def deposit(self, n):
        self.size += n
        return self.size 
    
    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return Jar.capacity

    @property
    def size(self):
        ...


def main():
    print(Jar.capacity())
    


if __name__ == "__main__":
    main()