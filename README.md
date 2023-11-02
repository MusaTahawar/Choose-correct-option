# Python Quiz Game

A simple Python quiz game where you can test your knowledge by answering questions. You can easily add your own questions and answers to the game.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Adding Questions](#adding-questions)
- [License](#license)

## Features

- Randomly selects questions from a predefined list.
- Provides multiple-choice options for each question.
- Gives instant feedback on the correctness of your answer.
- Easily customizable by adding your own questions and answers.

## Usage

1. Clone this repository:

   ```sh
   git clone https://github.com/your-username/python-quiz-game.git
Navigate to the project directory:

sh
Copy code
cd python-quiz-game
Run the Python script:

sh
Copy code
python quiz_game.py
Answer the questions by selecting the correct option. If your answer is correct, you will see "True." If it's incorrect, you will see "False."

## Adding Questions
You can add your own questions and answers to the game by editing the main_dict and options_dict dictionaries in the quiz_game.py file. Here's how to do it:


main_dict = {
    "Your question 1": "Correct answer 1",
    "Your question 2": "Correct answer 2",
    # Add more questions and answers as needed
}

options_dict = {
    "Your question 1": ["Option A", "Option B", "Correct answer 1", "Option D"],
    "Your question 2": ["Option A", "Correct answer 2", "Option C", "Option D"],
     */Add more options for other questions/*
}
Save your changes and run the script to play the quiz with your added questions.

## License
This project is licensed under the MIT License. For details, see the LICENSE file.

