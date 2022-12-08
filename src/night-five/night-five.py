import re
import json

INPUT_FILE_PATH = "./src/night-five/night-five.txt"


def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        sanitized_lines = list(map(lambda line: line.replace("\n", ""), lines))
        box_rows = []
        moves = []

        for line in sanitized_lines:
            if line.__contains__("["):
                box_rows.append(line)

            if line.startswith("move"):
                moves.append(line)

        return {"boxes": parse_box_values(box_rows), "moves": parse_moves(moves)}


def parse_box_values(box_rows):
    box_map = {}

    for current_row in box_rows:
        n = 4
        columns = [(current_row[i: i + n])
                   for i in range(0, len(current_row), n)]

        for i in range(len(columns)):
            col = columns[i].replace("]", "").replace("[", "").replace(" ", "")

            val = col if len(col) > 0 else None
            key = f"{i + 1}"

            if val is not None:
                if key not in box_map:
                    box_map[key] = [val]
                else:
                    box_map[key].append(val)
    return box_map


def parse_moves(moves):
    move_maps = []
    for move in moves:
        quantity_value = find_move_value("move", move)
        from_value = find_move_value("from", move)
        to_value = find_move_value("to", move)
        move_maps.append(
            {"quantity": quantity_value, "from": from_value, "to": to_value}
        )
    return move_maps


def find_move_value(search, move):
    pattern = rf"(?<=\b{search}\s)(\w+)"
    regex = re.search(pattern, move)
    value = int(regex.group()) if regex is not None else None
    return value


def main():
    data = parse_input()
    moves = data["moves"]
    boxes = data["boxes"]

    for move in moves:
        quantity: int = move["quantity"]
        move_from: int = move["from"]
        move_to: int = move["to"]
        from_box_column: list[str] = boxes[f"{move_from}"]
        to_box_column = boxes[f"{move_to}"]
        updated_from_box_column = []
        moved = 0
        for i in range(len(from_box_column)):
            current = from_box_column[i]

            if current is not None:
                if moved < quantity:
                    to_box_column.insert(0, current)
                else:
                    updated_from_box_column.append(current)

                moved = moved + 1

        boxes[f"{move_from}"] = updated_from_box_column
        boxes[f"{move_to}"] = to_box_column

    return boxes


print(json.dumps(main(), indent=4))
