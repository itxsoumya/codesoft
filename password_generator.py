import random


class Password_generator:
    numbers = '0123456789'
    alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbols = '~!@#$%^&*()-_+='

    mode = None
    length = None

    def __init__(self) -> None:
        self.prompt()
        if self.mode == 1:
            self.strong()
        elif self.mode == 2:
            self.medium()
        elif self.mode == 3:
            self.weak()

    def prompt(self):
        print('''
    Select password complexity
              1) Strong
              2) Medium
              3) Weak
''')
        self.mode = int(input('> '))
        self.length = int(input('Password Length: '))

    def strong(self):
        password = ''
        for i in range(self.length):
            choice = random.randint(1, 3)

            if choice == 1:
                password += random.choice(self.numbers)
            elif choice == 2:
                password += random.choice(self.alphabets)
            else:
                password += random.choice(self.symbols)

        print('\n> Generated Password: ', password)

    def medium(self):
        password = ''
        for i in range(self.length):
            choice = random.randint(1, 2)

            if choice == 1:
                password += random.choice(self.numbers)
            else:
                password += random.choice(self.alphabets)

        print('\n> Generated Password: ', password)

    def weak(self):
        password = ''
        for i in range(self.length):

            password += random.choice(self.alphabets)

        print('\n> Generated Password: ', password)


if __name__ == '__main__':
    pg = Password_generator()
