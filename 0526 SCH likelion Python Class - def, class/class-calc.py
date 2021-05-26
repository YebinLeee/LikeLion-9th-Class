class Calculator:
    def __init__(self, n1, n2):
        self.n1=n1
        self.n2=n2
    def add(self):
        return self.n1+self.n2
    def min(self):
        return self.n2-self.n1
    def mul(self):
       return self.n1*self.n2
    def div(self):
        return self.n2/self.n1

c=Calculator(1,2)
print(f'더하기 : {c.n1} + {c.n2} = {c.add()}')
print(f'빼기 : {c.n2} - {c.n1} = {c.min()}')
print(f'곱셈 : {c.n1} * {c.n2} = {c.mul()}')
print(f'나눗셈 : {c.n2} / {c.n1} = {c.div()}')