from typing import Tuple
import csv

INPUT_FILE_PATH="./src/night-two.txt"

def parse_input(): 
    with open(INPUT_FILE_PATH) as csv_file:
        data = csv.reader(csv_file, delimiter=" ")
        input_list = []
        for row in data:
            input_list.append((row[0], row[1]))
        return input_list 

class PaperRockScissors:
    move_score = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    outcome_of_round_score = {
        "WIN": 6,
        "LOSE": 0,
        "DRAW": 3
    }

    round_outcome_map = {
        "AX": "DRAW", #ROCK ROCK
        "BY": "DRAW", #PAPER PAPER
        "CZ": "DRAW", #SCISSORS SCISSORS
        "AY": "WIN", #ROCK PAPER
        "BZ": "WIN", #PAPER SCISSORS
        "CX": "WIN", #SCISSORS ROCK
        "AZ": "LOSE", #ROCK SCISSORS
        "BX": "LOSE", #PAPER ROCK 
        "CY": "LOSE" #SCISSORS PAPER 
    } 

    def get_score_for_round(self, opponents_move, my_move):
        my_move_score = self.move_score[my_move] 
        score_of_round = self.outcome_of_round_score[self.round_outcome_map[f'{opponents_move}{my_move}']]
        return score_of_round + my_move_score
    
    def sum_scores(self, rounds: list[Tuple[str, str]]):
        scores = []
        for round in rounds:
            score = self.get_score_for_round(round[0], round[1])
            scores.append(score)
        return sum(scores)

prs = PaperRockScissors()

score = prs.sum_scores(parse_input())
print(score)
