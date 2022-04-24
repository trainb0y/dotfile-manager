import shutil


# Credit for this class goes to https://codereview.stackexchange.com/a/206233
# Modified a little

class Menu:

    def __init__(self, title: str, options: [()]):
        self.title = title
        self.options = options

    def display(self) -> str:
        """
        :return: A formatted text display of this menu
        """
        string = self.title + ":\n"
        for i, option in enumerate(self.options):
            string += f"-  {i + 1}) {option[0]}\n"

        # Add header and footer
        max_width = shutil.get_terminal_size()[0]
        string = f'{"-" * max_width}\n{string}\n{"-" * max_width}'

        return string

    def callback(self, i: int):
        """
        :param i:
        :return: The option's function output, or false if there was no option corresponding to i
        """
        if i <= len(self.options):
            return self.options[i - 1][1]
        else:
            return False

    def select(self):
        """
        Force the user to select an option from the menu
        """
        while True:
            print(self.display())
            try:
                result = self.callback(int(input(">> ")))
                if result:
                    return result
                else:
                    print(f"Please enter a number corresponding to an option!")
            except ValueError:
                print(f"Please enter a number!")
            print()
