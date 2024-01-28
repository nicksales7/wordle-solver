from wordle import WordleFunctions
from bot import RandomBot

if __name__ == "__main__":
    wordle = WordleFunctions("possible_words.txt")
    word = wordle.choose_word(wordle.return_words_lst())
    bot = RandomBot(wordle.return_words_lst())
    print(word)

    for i in range(1000000):
        for i in range(5):
            # guess = wordle.guess_loop(wordle.return_words_lst())
            guess = bot.temporary_guess()
            guess_test = wordle.guess_correctness(word, guess)
            with open("word_value.txt", "a") as f:
                f.write(f"{guess}:{wordle.points}\n")
            if guess_test:
                break