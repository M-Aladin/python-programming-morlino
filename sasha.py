class Bottle:

    def __init__(self):
        self.color = "white"
        self.valuem = 1.0

    def emty(self):
        self.valuem = 0


if __name__ == "__main__":
    his_bottle = Bottle()
    print(his_bottle.valuem, " ", his_bottle.color)
    his_bottle.emty()
    print(his_bottle.valuem, " ", his_bottle.color)