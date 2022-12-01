import csv

INPUT_FILE_PATH="./src/night-one.txt"

def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines() 
        collected_lines: list[list[int]] = []
        current_line: list[int] = []
        for line in lines:
            is_empty = line == "\n"
            if is_empty:
                collected_lines.append(current_line)
                current_line = []
            else:
                current_line.append(int(line))
    return collected_lines


def sum_collection(collected_lines: list[list[int]]): 
    return list(map(lambda line: sum(line), collected_lines))
    
def get_top_hit(collection: list[int]):
    collection.sort(reverse=True)
    return collection[0]

def get_top_three(collection: list[int]):
    N = 3
    collection.sort(reverse=True)
    return sum(collection[:N])

top_hit = get_top_hit(
 sum_collection(
        parse_input()
    )
)

top_three = get_top_three(
 sum_collection(
        parse_input()
    )
)

print(top_hit)
print(top_three)
