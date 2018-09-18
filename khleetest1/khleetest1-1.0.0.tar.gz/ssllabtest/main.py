
class Caculator:
    def __init__(self, isAdd, isSub, isMul, isDiv, isRem):
        self.isAdd = isAdd
        self.isSub = isSub
        self.isMul = isMul
        self.isDiv = isDiv
        self.isRem = isRem

    def adder(self, num1, num2):
        if self.isAdd == True:
            sum = num1 + num2
            return sum
        else:
            raise("Adder is not true.")

    def substraction(self, num1, num2):
        if self.isSub == True:
            return (num1 - num2)
        else:
            raise("Substrator is not true.")

    def multiplication(self, num1, num2):
        if self.isMul == True:
            return (num1 * num2)
        else:
            raise("Multiplication is not true.")

    def division(self, num1, num2):
        if self.isDiv == True:
            try:
                n = num1 / num2
                r = num1 % num2

                if self.isRem == True:
                    return n, r
                else:
                    return n

            except ZeroDivisionError as error:
                print(error)
                return 0
        else:
            raise("Division is not true.")

    def getStatus(self):
        return {
            "add": self.isAdd,
            "sub": self.isSub,
            "mul": self.isMul,
            "div": self.isDiv,
            "rem": self.isRem
        }