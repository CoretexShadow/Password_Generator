import sys
import nltk
import random
from abc import ABC, abstractmethod
try:
        nltk.data.find('corpora/words')
except LookupError:
        nltk.download('words', quiet=True)
except ImportError:
    sys.exit("NLTK is not installed. Please install it with: pip install nltk")


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words : int = 8 , capitalize : bool = False, separator : str = "-", vocabulary : list = None):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()
        self.separator = separator
        self.vocabulary = vocabulary
        self.capitalize = capitalize
        self.num_of_words = num_of_words
    def generate(self):
        password = [random.choice(self.vocabulary) for _ in range(self.num_of_words)]
        if self.capitalize :
            password = (word.upper() if random.choice([True , False]) else word for word in password)
        return self.separator.join(password)
if __name__ == "__main__" :
    try :
            user_separator = input("Enter your separator, type q if you dont want ")
            user_num_of_words = input("Enter the number of words in password, type q if you dont want default = 8 ")
            separator = "" if user_separator == "q"  else user_separator
            num_of_words = 8 if user_num_of_words == "q" else int(user_num_of_words)
            pass_obj = MemorablePasswordGenerator(separator = separator , num_of_words = num_of_words )
            print(pass_obj.generate())
    except Exception as e:
            print("an error occurred" ,e)
