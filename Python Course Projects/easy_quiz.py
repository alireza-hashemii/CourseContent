import requests

difficulty_levels = "hard", "medium", "easy"
difficulty = input(f"{difficulty_levels} which one do you choose? ")

url = f"https://opentdb.com/api.php?amount=20&category=9&difficulty={difficulty}"

response = requests.get(url)
if response.status_code == 200:
    # main question
    result = response.json()
    question = result['results'][0]['question']
    
    # collect options
    option_list = []
    correct_answer = result["results"][0]['correct_answer']
    option_list.append(correct_answer)
    option_list.extend(result["results"][0]['incorrect_answers'])

    # show the question first
    print(question)

    # express options in graceful way
    for index, option in enumerate(option_list, start=1):
        print(index, '.', option)

    # catch any exceptions
    try:
        user_choice = int(input(": "))
        user_choice_item = option_list[user_choice - 1]
        if user_choice_item == correct_answer:
            print("correct answer. great performance")
        else:
            print("wrong answer. maybe next time")
    except:
        print("not a valid input.")
    
    