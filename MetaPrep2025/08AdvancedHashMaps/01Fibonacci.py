class Fibonacci:
    def __init__(self):
        self.cache = {0:0, 1:1}
    
    def fibonacci(self, n):
        if n < 0:
            return -1
        
        if n in self.cache:
            return self.cache[n]
        
        value = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        self.cache[n] = value

        return value
    
if __name__=="__main__":
    solution = Fibonacci()

    for i in range(1,100):
        print(i, solution.fibonacci(i))
