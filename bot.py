import random

class Bot:
    def __init__(self, word_lst):
        self.world_lst = word_lst

    def temporary_guess(self):
        return self.world_lst[random.randint(0, len(self.world_lst) - 1)]