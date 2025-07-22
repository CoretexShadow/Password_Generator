from abc import ABC, abstractmethod
class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

import random
import string

class PinGenerator:
    def __init__(self, length):
        self.length = length
    def generate(self):
        return "".join(random.choice(string.digits) for _ in range(self.length))
if __name__ == "__main__":
    try:
        user_input = int(input("Enter the length of the PIN: "))
        if user_input <= 0:
            print("Length must be a positive integer.")
        else:
            pin_password = PinGenerator(user_input)
            print("Your generated PIN:", pin_password.generate())
    except ValueError:
        print("Invalid input! Please enter a valid number.")
