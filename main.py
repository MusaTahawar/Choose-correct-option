import random

main_dict = {
    "What is the second planet to Earth?": "venus",
    "Who is Musa?": "pro",
    "What is the largest continent on Earth?": "asia",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the tallest mountain in the world?": "mount everest",
    "What is the chemical symbol for water?": "h2O",
    "Who wrote the 'Harry Potter' book series?": "j.k. rowling",
    "Which gas do plants absorb during photosynthesis?": "carbon dioxide",
    "What is the currency of Japan?": "japanese yen",
    "Who is known as the father of modern physics?": "albert einstein",
    "What is the main ingredient in chocolate?": "cocoa",
    "What is the largest desert in the world?": "antarctica",
    "What is the capital of France?": "paris",
    "Who wrote the play 'Romeo and Juliet'?": "william shakespeare",
    "What is the largest mammal in the world?": "blue whale",
    "In which year did the Titanic sink?": "1912",
    "What is the chemical symbol for gold?": "au",
    "Who is the current President of the United States?": "joe biden"

}
options_dict = {
    "What is the second planet to Earth?": ["Mars", "Venus", "Jupiter", "Saturn"],
    "Who is Musa?": ["Teacher", "Doctor", "Engineer", "Pro"],
    "What is the largest continent on Earth?": ["Africa", "Australia", "Asia", "South America"],
    "Who painted the Mona Lisa?": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
    "What is the tallest mountain in the world?": ["Mount Kilimanjaro", "Mount McKinley", "Mount Everest", "Mount Fuji"],
    "What is the chemical symbol for water?": ["H2O", "CO2", "O2", "CH4"],
    "Who wrote the 'Harry Potter' book series?": ["George Orwell", "J.R.R. Tolkien", "J.K. Rowling", "Stephen King"],
    "Which gas do plants absorb during photosynthesis?": ["Oxygen", "Carbon Monoxide", "Carbon Dioxide", "Methane"],
    "What is the currency of Japan?": ["Yuan", "Dollar", "Yen", "Euro"],
    "Who is known as the father of modern physics?": ["Isaac Newton", "Galileo Galilei", "Albert Einstein", "Stephen Hawking"],
    "What is the main ingredient in chocolate?": ["Cocoa", "Sugar", "Milk", "Vanilla"],
    "What is the largest desert in the world?": ["Gobi Desert", "Sahara Desert", "Arabian Desert", "Antarctica"],
    "What is the capital of France?": ["London", "Berlin", "Madrid", "Paris"],
    "Who wrote the play 'Romeo and Juliet'?": ["Mark Twain", "Charles Dickens", "William Shakespeare", "Jane Austen"],
    "What is the largest mammal in the world?": ["Dolphin", "Elephant", "Blue Whale", "Giraffe"],
    "In which year did the Titanic sink?": ["1907", "1912", "1920", "1935"],
    "What is the chemical symbol for gold?": ["Ag", "Au", "Ge", "Fe"],
    "Who is the current President of the United States?": ["Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush"]
    # Add more options for other questions
}

options = list(main_dict.keys())

while True:
    main_choice = random.choice(options)
    answer = main_dict[main_choice]
    options_for_question = options_dict[main_choice]

    print(main_choice)

    for i, option in enumerate(options_for_question, start=1):
        print(f"{i}. {option}")

    user_choice = input("Select the correct option (1-4): ")

    if user_choice.isdigit():
        user_choice = int(user_choice)
        if 1 <= user_choice <= len(options_for_question) and options_for_question[user_choice - 1].lower() == answer:
            print("True")
            break
    print("False")
