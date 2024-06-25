

class Calculator:
    first_num = None
    second_num = None
    operation_choice = None

    def __init__(self) -> None:
        self.start()

    def start(self):
        self.prompt()
        self.calculate()

        choice = int(input('0 for exit 1 for continue: '))
        if choice == 1:
            print()
            self.start()
        else:
            exit(0)

    def prompt(self):
        self.first_num = int(input('Enter 1st Number: '))
        self.second_num = int(input('Enter 2nd Number: '))

        print('\n ** operation choice **')
        print('''
            1) addition +
            2) substraction -
            3) multiplication x
            4) division /        
''')
        self.operation_choice = int(input('option> '))

    def calculate(self):
        solution = None
        if self.operation_choice == 1:
            solution = self.first_num+self.second_num
        elif self.operation_choice == 2:
            solution = self.first_num-self.second_num
        elif self.operation_choice == 3:
            solution = self.first_num*self.second_num
        elif self.operation_choice == 4:
            solution = self.first_num/self.second_num

        print("> Result: ", solution)


if __name__ == '__main__':
    cal = Calculator()
