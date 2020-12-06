import sys


class Menu:
    def __init__(self):
        self.choices = {
            "1": self.display_menu,
            "2": self.exit,
        }

    def display_menu(self):
        print("""
    1. One hundred years of solitude
    2. The alchemist
            """)

    def run(self):
        while True:
            print("""
    Welcome to the library! You have the following options
    1. Display Menu
    2. Exit
            """)
            choice = input('Enter your choice: ')
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print("{} is not a valid choice.".format(choice))

    def exit(self):
        print("""
    Thank you for using the library application. Goodbye!
    """)
        sys.exit(1)


if __name__ == '__main__':
    menu = Menu()
    menu.run()
