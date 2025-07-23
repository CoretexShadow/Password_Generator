from abc import ABC, abstractmethod
class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

import string
import random


class RandomPasswordGenerator(PasswordGenerator):
    def __init__ (self, include_numbers : bool = False , include_symbols : bool = False ,length = 8 ):
        self.password = string.ascii_letters
        self.length = length
    def generate(self):
        if include_numbers :
            self.password += string.digits
        if include_symbols :
            self.password += string.punctuation
        return "".join(random.choice(self.password) for _ in range(self.length))
if __name__ == "__main__":
    try :
            user_length = int(input("Enter the length of the password"))
            user_symbols = input("Do you want symbols in your password?, type no if you dont want")
            user_number = input("Do you want numbers in your password?, type no if you dont want")
            include_symbols = user_symbols.lower() != "no"
            include_numbers = user_number.lower() != "no"

            user_password = RandomPasswordGenerator(include_numbers=include_numbers, include_symbols=include_symbols, length=user_length)
            print(user_password.generate())
    except Exception as e:
        print("Error occurred:", e)
