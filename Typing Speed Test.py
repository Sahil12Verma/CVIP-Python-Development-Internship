import random
import time

phrases = [
    "Cricket world cup is here",
    "Excess gaming is harmful for health", 
    "Good things come to those who wait",
    "Bite off more than you can chew",
    "Better late than never",
]

def get_random_phrase():
    return random.choice(phrases)

def typing_speed_test():
    print("Welcome to the Typing Speed Tester")

    input("Press Enter to start.......")

    phrase = get_random_phrase()
    print("\nType these following::")
    print(phrase)

    start_time = time.time()

    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time

    words = user_input.split()
    word_count = len(words)

    wpm = (word_count / elapsed_time) * 60

    print("\nYou typed {} words in {:.2f} seconds.".format(word_count, elapsed_time))
    print("Your typing speed is {:.2f} WPM.".format(wpm))

    if wpm < 20:
        print("Need to practice more.")
    elif 20 <= wpm < 40:
        print("Keep practicing to improve.")
    else:
        print("Great typing speed.")

if __name__ == "__main__":
    typing_speed_test()
