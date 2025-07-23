import random
from abc import ABC, abstractmethod
from tkinter.ttk import Separator


class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass


class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(self, num_of_words : int = 8 , capitalize : bool = False, separator : str = "-", vocabulary : list = None):
        if vocabulary is None:
            vocabulary = ["Air", "Animal", "Answer", "Apple", "Art", "Beautiful", "Big", "Black", "Blue", "Book", "Car", "Change", "City", "Cold", "Communication", "Complex", "Country", "Courage", "Darkness", "Day", "Death", "Destination", "Different", "Drink", "Dream", "Earth", "Eat", "Failure", "Family", "Fast", "Fear", "Fire", "Forest", "Freedom", "Friend", "Future", "Green", "Happy", "History", "Hope", "Hot", "House", "Human", "Idea", "Important", "Impossible", "Journey", "Justice", "Knowledge", "Language", "Life", "Light", "Love", "Memory", "Moment", "Money", "Moon", "Mountain", "Music", "Nature", "Night", "Noise", "Ocean", "Past", "Peace", "Play", "Possible", "Power", "Present", "Problem", "Question", "Reality", "Red", "River", "Run", "Sad", "School", "Science", "Silence", "Similar", "Simple", "Sleep", "Slow", "Small", "Solution", "Student", "Success", "Sun", "Teacher", "Technology", "Time", "Tree", "Ugly", "Walk", "War", "Water", "White", "Work", "World", "Yellow"]
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
