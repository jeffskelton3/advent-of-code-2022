from typing import Tuple
import csv

INPUT_FILE_PATH = "./src/night-two.txt"


def parse_input():
    with open(INPUT_FILE_PATH) as csv_file:
        data = csv.reader(csv_file, delimiter=" ")
        input_list = []
        for row in data:
            input_list.append((row[0], row[1]))
        return input_list


class PaperRockScissors:
    OPPONENT_ROCK = "A"
    OPPONENT_PAPER = "B"
    OPPONENT_SCISSORS = "C"

    ROCK = "X"
    PAPER = "Y"
    SCISSORS = "Z"

    WIN = "Z"
    LOSE = "X"
    DRAW = "Y"

    move_score = {ROCK: 1, PAPER: 2, SCISSORS: 3}

    outcome_of_round_score = {"WIN": 6, "LOSE": 0, "DRAW": 3}

    move_to_outcome_key_map = {LOSE: "LOSE", DRAW: "DRAW", WIN: "WIN"}

    round_outcome_map = {
        f"{OPPONENT_ROCK}{ROCK}": "DRAW",
        f"{OPPONENT_PAPER}{PAPER}": "DRAW",
        f"{OPPONENT_SCISSORS}{SCISSORS}": "DRAW",
        f"{OPPONENT_ROCK}{PAPER}": "WIN",
        f"{OPPONENT_PAPER}{SCISSORS}": "WIN",
        f"{OPPONENT_SCISSORS}{ROCK}": "WIN",
        f"{OPPONENT_ROCK}{SCISSORS}": "LOSE",
        f"{OPPONENT_PAPER}{ROCK}": "LOSE",
        f"{OPPONENT_SCISSORS}{PAPER}": "LOSE",
    }

    move_needed_from_outcome_map = {
        f"{OPPONENT_ROCK}{WIN}": PAPER,
        f"{OPPONENT_PAPER}{WIN}": SCISSORS,
        f"{OPPONENT_SCISSORS}{WIN}": ROCK,
        f"{OPPONENT_ROCK}{LOSE}": SCISSORS,
        f"{OPPONENT_PAPER}{LOSE}": ROCK,
        f"{OPPONENT_SCISSORS}{LOSE}": PAPER,
        f"{OPPONENT_ROCK}{DRAW}": ROCK,
        f"{OPPONENT_PAPER}{DRAW}": PAPER,
        f"{OPPONENT_SCISSORS}{DRAW}": SCISSORS,
    }

    def get_score_for_round(self, opponents_move, outcome):
        outcome_key = self.move_to_outcome_key_map[outcome]
        outcome_score = self.outcome_of_round_score[outcome_key]
        my_move = self.move_needed_from_outcome_map[f"{opponents_move}{outcome}"]
        my_score = self.move_score[my_move]
        return outcome_score + my_score

    # def get_score_for_round(self, opponents_move, my_move):
    #     my_move_score = self.move_score[my_move]
    #     score_of_round = self.outcome_of_round_score[self.round_outcome_map[f'{opponents_move}{my_move}']]
    #     return score_of_round + my_move_score

    def sum_scores(self, rounds: list[Tuple[str, str]]):
        scores = []
        for round in rounds:
            score = self.get_score_for_round(round[0], round[1])
            scores.append(score)
        return sum(scores)


prs = PaperRockScissors()

score = prs.sum_scores(parse_input())
print(score)
