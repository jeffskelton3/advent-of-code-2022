from typing import Tuple
import string


INPUT_FILE_PATH = "./src/night-three.txt"


def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        collected_lines: list[Tuple[list[str], list[str]]] = []

        for line in lines:
            sanitized_line = line.replace("\n", "")
            line_len = len(sanitized_line)
            first_half = sanitized_line[0 : line_len // 2]
            second_half = sanitized_line[line_len // 2 :]
            collected_lines.append((list(first_half), list(second_half)))

    return collected_lines


def build_priorty_lookup_table():
    letter_map: dict[str, int] = {}
    alpha_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)

    for x in range(len(alpha_list)):
        letter_map[alpha_list[x]] = x + 1

    return letter_map


def find_common_elements_in_lists(list1, list2):
    return list(set(list1) & set(list2))


priority_lookup_table = build_priorty_lookup_table()

input: list[Tuple[list[str], list[str]]] = parse_input()

priority_scores = []

for item in input:
    common = find_common_elements_in_lists(item[0], item[1])
    for c in common:
        priority_scores.append(priority_lookup_table[c])

print(sum(priority_scores))
