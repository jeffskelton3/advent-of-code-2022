INPUT_FILE_PATH = "./src/night-six/night-six.txt"


def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        sanitized_lines = list(map(lambda line: line.replace("\n", ""), lines))
        joined = "".join(sanitized_lines)
        return list(joined)


chars = parse_input()
count = 0
for i in range(len(chars)):
    count = count + 1
    one = chars[i]
    two = chars[i + 1] if len(chars) > i + 1 else None
    three = chars[i + 2] if len(chars) > i + 2 else None
    four = chars[i + 3] if len(chars) > i + 3 else None
    chunk = {one, two, three, four}
    if len(chunk) == 4:
        print(count + 3)
        break
