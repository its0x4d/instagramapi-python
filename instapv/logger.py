from colorama import Fore, Back
from datetime import datetime
from time import sleep

class Logger:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


    def warn(self, text: str, ask: bool = False, error_code: int = None):
        now = datetime.now()
        CLOCK = '{}[{}{}{}{}{}]{}{} '.format(
            Fore.BLUE, Fore.RESET, Fore.GREEN, now.strftime("%H:%M:%S"), Fore.RESET, Fore.BLUE, Fore.RESET, self.END
        )
        if not error_code:
            if not ask:
                print(self.YELLOW + '[!]' + CLOCK + self.BOLD + Fore.YELLOW + text + Fore.RESET + self.END)     

            else:
                return self.YELLOW + '[!]' + CLOCK + self.BOLD + Fore.YELLOW + text + Fore.RESET + self.END

        else:
            if not ask:
                print(CLOCK + f'[{error_code}] ' + text)

            else:
                return CLOCK + f'[{error_code}] ' + text

    
    def error(self, text: str, error_code: str = None):
        now = datetime.now()
        CLOCK = f'{Fore.BLUE}[{Fore.RESET}{Fore.GREEN}{now.strftime("%H:%M:%S")}{Fore.RESET}{Fore.BLUE}]{Fore.RESET}{self.END} '
        if not error_code:
            print(self.RED + '[!]' + CLOCK + self.BOLD + Fore.RED + text + Fore.RESET + self.END)
        elif text2:
            print(self.RED + '[!]' + CLOCK + self.BOLD + Fore.RED + text + Fore.RESET + self.END)
        else:
            print(CLOCK + f'[{error_code}] ' + text)
    
    def info(self, text: str, bold: bool = False):
        now = datetime.now()
        CLOCK = f'{Fore.BLUE}[{Fore.RESET}{Fore.GREEN}{now.strftime("%H:%M:%S")}{Fore.RESET}{Fore.BLUE}]{Fore.RESET}{self.END} '
        if bold:
            print(self.BLUE + '[+]' + CLOCK + self.BOLD + Fore.WHITE + text + Fore.RESET + self.END)
        else:
            print(self.BLUE + '[+]' + CLOCK + Fore.WHITE + text + Fore.RESET + self.END)
