import requests
import html
import random
from pprint import pprint

# Get a pool of trivia questions
def get_question_pool(amount: int, category: int)-> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]

# Shuffle the answer choices in the console
def shuffle_choices(choices: list)-> None:
    random.shuffle(choices)
    return choices


#Print the answer choices in the console
def print_choices(choices: list)->None:
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index+1}. {html.unescape(choice)}")

        
#Get user's choice in the console
def get_user_choice()-> int:
    while True:
        user_choice = int(input("Enter the number of your choice: "))
        if user_choice in range(1,5):
            return user_choice -1
        else:
            print("Invalid input. Enter the number of your choice. ")
            
            
#Play the game
def play_game(amount: int, category: int):
    question_pool = get_question_pool(amount, category)
    total_sum = 0
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
        choices = question["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffled_choices = shuffle_choices(choices)
        print_choices(shuffled_choices)
        user_choice_index = get_user_choice()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])
        if user_choice_text == correct_choice_text:
            print(f"Correct! You answered: {correct_choice_text}\n")
            total_sum = total_sum + 1
        else:
            print(f"Incoorect. the correct answer is: {correct_choice_text}")
    print(f"Your Total score is: {total_sum}")
            
#Call main function
if __name__ == "__main__":
    amount = int(input("Enter the number of questions you want to answer: \n"))
    link = "https://opentdb.com/api_category.php"
    response = requests.get(link)
    response_json = response.json()
    pprint(response.json())
    category = int(input("Enter the ID of the Category you want to play in.\n"))
    play_game(amount, category)