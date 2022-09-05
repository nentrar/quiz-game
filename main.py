"""
Name: The Capital & Countries Guessing Game
Author: Piotr Semeniuk
Version: 0.3
"""

import requests
import random


class Quiz:
    """
    Implementation of game in capitals and countries.
    When new object is made, user can set a number of questions which will be ask in the game.
    For every right answer she will be given 1 point. The results are shown at the end of the game.
    """

    def __init__(self, questions=10):
        self.data = self._fetch_data(self)
        self.base = self._create_city_base()
        self.points = 0
        self.questions = input("How many questions do You want to be in the game? \n")

    @staticmethod
    def _fetch_data(self):
        url = "https://countriesnow.space/api/v0.1/countries/capital"
        response = requests.request("GET", url)
        return response.json()

    @staticmethod
    def _print_right_answer(self):
        print("That is right answer!")

    @staticmethod
    def _print_wrong_answer(self, random_choice, right_answer):
        print(f"Wrong answer! The capital of {random_choice} is {right_answer}")

    def _create_city_base(self):
        keys = [n['name'] for n in self.data['data']]
        values = [n['capital'] for n in self.data['data']]
        return {keys[i]: values[i] for i in range(len(keys))}

    def guess_capital(self):
        """
        Take a single input from user and check the answer.
        If the answer is right, user points increase by 1.
        Wrong answer return only the correct value.
        """
        random_choice = random.choice(list(self.base.keys()))
        right_answer = self.base[random_choice]
        answer = input(f"What is the capital of {random_choice}\n")
        if answer == right_answer:
            self._print_right_answer(self)
            self.points += 1
        else:
            self._print_wrong_answer(self, random_choice, right_answer)

    def start_game(self):
        """
        Start a game which loop a number of questions based on a param.
        At the end of the game, overall points of the player are printed and user is
        asked if she want to try again. If positive, the game start again.
        If negative the loop breaks.

        :param questions: number of question to be asked in the row
        """

        while True:
            self.points = 0
            for n in range(int(self.questions)):
                self.guess_capital()
            if self.points > 0:
                print(f"Congratulations! You scored {self.points} points! \n")
            else:
                print("Sadly you scored 0 this time. Try harder! \n")
            if input("Do You want to start again?\n").lower() == "no":
                break


if __name__ == '__main__':
    quiz = Quiz()
    quiz.start_game()

