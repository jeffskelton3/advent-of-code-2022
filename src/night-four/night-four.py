INPUT_FILE_PATH = "./src/night-four/night-four.txt"


class RangePair:
    def __init__(self, lower_bound: int, upper_bound: int):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def fits_within_range(self, range_pair):
        return (
            self.lower_bound >= range_pair.lower_bound
            and self.upper_bound <= range_pair.upper_bound
        )


def parse_input():
    with open(INPUT_FILE_PATH) as file:
        lines = file.readlines()
        sanitized_lines = list(map(lambda line: line.replace("\n", ""), lines))
        range_pair_list = []

        for line in sanitized_lines:
            line_pair = line.split(",")
            range_pair = []
            for pair in line_pair:
                pair_list = pair.split("-")
                range_pair.append(
                    RangePair(
                        lower_bound=int(pair_list[0]), upper_bound=int(pair_list[1])
                    )
                )
            range_pair_list.append(range_pair)

        return range_pair_list


# In how many assignment pairs does one range fully contain the other?
# expected output with sample: 2
range_pair_list: list[list[RangePair]] = parse_input()

fits_within_ranges = []

for range_pair in range_pair_list:
    pair_left = range_pair[0]
    pair_right = range_pair[1]
    left_fits_right = pair_left.fits_within_range(pair_right)
    right_fits_left = pair_right.fits_within_range(pair_left)
    if left_fits_right or right_fits_left:
        fits_within_ranges.append(range_pair)

print(len(fits_within_ranges))
