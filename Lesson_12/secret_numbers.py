import datetime
import json
import random



def get_top_scores():
    score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
    with open("score_list.txt", "w") as score_file:
        score_file.write(json.dumps(score_list))

    print("You've guessed it - congratulations! It's number " + str(secret))
    print("Attempts needed: " + str(attempts))

def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())

    print("Top scores: " + str(score_list))

    for score_dict in score_list:
        print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))



def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    while True:
        attempts += 1
        if guess == secret:
            get_top_scores()
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")

get_score_list()

guess = int(input("Guess the secret number (between 1 and 30): "))


play_game()