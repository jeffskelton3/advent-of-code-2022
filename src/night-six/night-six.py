INPUT_FILE_PATH = "./src/night-six/night-six.txt"


def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        sanitized_lines = list(map(lambda line: line.replace("\n", ""), lines))
        joined = "".join(sanitized_lines)
        return list(joined)


chars = parse_input()
char_len = len(chars)
START_OF_MARKER = 14
count = 0
for i in range(char_len):
    if START_OF_MARKER < i < char_len + START_OF_MARKER:
        chunk = []
        for r in range(0, START_OF_MARKER):
            chunk.insert(0, chars[i - r])
        deduped_chunk_len = len(set(chunk))
        if deduped_chunk_len == 14:
            print(i + 1)
            break
