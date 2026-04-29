class Calculator:
    
    def add(self, a, b, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5, 10))
print(calc.add(5, 10, 20))