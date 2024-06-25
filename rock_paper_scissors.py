import random

# Assuming
# 1 represents Rock
# 2 represnts Paper
# 3 represnts Scissors


class RockPaperScissor:
    rps = [None, 'Rock', 'Paper', 'Scissors']
    computer_score = 0
    your_score = 0

    def __init__(self) -> None:
        self.game()

    def game(self):

        print(f'''
        -------------------
        You: {self.your_score}
        vs.
        Computer: {self.computer_score}
        -------------------
''')

        print('''
            1) Rock
            2) Paper
            3) Scissors
            4) exit the game
              
''')

        your_choice = int(input('option> '))
        computer_choice = random.randint(1, 3)

        if your_choice == 4:
            exit(0)

        print()
        if your_choice == computer_choice:
            print(
                f'[Draw] (You: {self.rps[your_choice]}, Computer: {self.rps[computer_choice]})')
        elif your_choice == 1 and computer_choice == 3:
            print(
                f'[You Won] (You: {self.rps[your_choice]}, Computer: {self.rps[computer_choice]})')
            self.your_score+=1
        elif your_choice == 3 and computer_choice == 2:
            print(
                f'[You Won] (You: {self.rps[your_choice]}, Computer: {self.rps[computer_choice]})')
            self.your_score+=1
        elif your_choice == 2 and computer_choice == 1:
            print(
                f'[You Won] (You: {self.rps[your_choice]}, Computer: {self.rps[computer_choice]})')
            self.your_score+=1
        else:
            print(
                f'[You Lost] (You: {self.rps[your_choice]}, Computer: {self.rps[computer_choice]})')
            self.computer_score+=1
        
        self.game()
        


if __name__ == '__main__':
    game = RockPaperScissor()
