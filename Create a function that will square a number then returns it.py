class Squareroot:
    def __init__(self, num1):
        self.num1 = num1

    def square(self):
        return self.num1 ** 0.5, ' | ', self.num1 * self.num1
        
calc = Squareroot(5)
result = calc.square()
print(result)