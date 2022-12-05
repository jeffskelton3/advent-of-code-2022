from typing import Tuple
import string


INPUT_FILE_PATH = "./src/night-three.txt"


def parse_compartments_from_input():
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


def parse_groups_from_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        collected_lines = []
        sanitized_lines = list(map(lambda line: line.replace("\n", ""), lines))
        current_group = []

        for line in sanitized_lines:
            if len(current_group) < 3:
                current_group.append(list(line))
            else:
                collected_lines.append(current_group)
                current_group = [list(line)]

        collected_lines.append(current_group)
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
compartments = parse_compartments_from_input()
groups = parse_groups_from_input()


def find_common_items_in_groups():
    priority_scores = []
    for group in groups:
        common = list(set(group[0]) & set(group[1]) & set(group[2]))
        for c in common:
            priority_scores.append(priority_lookup_table[c])
    return priority_scores


def find_common_items_in_compartments():
    priority_scores = []
    for item in compartments:
        common = find_common_elements_in_lists(item[0], item[1])
        for c in common:
            priority_scores.append(priority_lookup_table[c])
    return priority_scores


# print(sum(find_common_items_in_compartments()))
print(sum(find_common_items_in_groups()))
