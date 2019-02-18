class Factor(object):
    def __init__(self, number):
        self.number = number

    @property
    def numb(self):
        if self.number % 3 == 0:
            return "pling"
        return str(self.number)

    @property
    def getFactor(self):
        factors=[];

        for i in range(1, self.number + 1):
            if self.number % i == 0:
                factors.append(i)

        return factors
