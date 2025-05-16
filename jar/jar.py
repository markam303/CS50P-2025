class Jar:
    def __init__(self, capacity=12):
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
        return self._capacity

    @property
    def size(self):
        ...


def main():
    jar = Jar()
    cap = Jar.capacity()
    print(cap)
    
    



if __name__ == "__main__":
    main()