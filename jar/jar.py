class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity

    def __str__(self):
        return (f"🍪")
        
    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Jar is full")
    
    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Not enough cookies")
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        self._size = size


def main():
    jar = Jar()
    cap = jar.capacity
    print(jar.size)
    print(cap)
    print(jar)
    



if __name__ == "__main__":
    main()