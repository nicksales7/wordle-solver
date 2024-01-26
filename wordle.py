import random

class WordleFunctions:
    def __init__(self, words):
        self.words = words

    def guess_loop(self, lst):
        while True:
            guess = input("Guess: ").strip()
            if guess in lst:
                return guess
            else:
                print(f"Word not in list!") 

    def return_words_lst(self):
        with open(self.words, "r") as f:
            return [line.strip() for line in f.read().splitlines()]
    
    def choose_word(self, lst):
        return lst[random.randint(0, len(lst))]
    
    def guess_correctness(self, word, guessed_word):
        word = [x for x in word]
        guessed_word = [x for x in guessed_word]

        if guessed_word == word:
            print(f"Correct guess!")
            return True
        else:
            for i in range(len(guessed_word)):
                if guessed_word[i] == word[i]:
                    print(f"Green: {guessed_word[i]}")
                elif guessed_word[i] in word:
                    print(f"Yellow: {guessed_word[i]}")
                else:
                    print(f"Grey: {guessed_word[i]}") 

if __name__ == "__main__":
    wordle = WordleFunctions("possible_words.txt")
    word = wordle.choose_word(wordle.return_words_lst())
    print(word)

    count = 0
    while count < 5:
        guess = wordle.guess_loop(wordle.return_words_lst())
        guess_test = wordle.guess_correctness(word, guess)
        if guess_test:
            break
        count += 1

