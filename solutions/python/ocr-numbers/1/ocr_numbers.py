DIGITS = {
    (
        " _ ",
        "| |",
        "|_|",
        "   ",
    ): "0",

    (
        "   ",
        "  |",
        "  |",
        "   ",
    ): "1",

    (
        " _ ",
        " _|",
        "|_ ",
        "   ",
    ): "2",

    (
        " _ ",
        " _|",
        " _|",
        "   ",
    ): "3",

    (
        "   ",
        "|_|",
        "  |",
        "   ",
    ): "4",

    (
        " _ ",
        "|_ ",
        " _|",
        "   ",
    ): "5",

    (
        " _ ",
        "|_ ",
        "|_|",
        "   ",
    ): "6",

    (
        " _ ",
        "  |",
        "  |",
        "   ",
    ): "7",

    (
        " _ ",
        "|_|",
        "|_|",
        "   ",
    ): "8",

    (
        " _ ",
        "|_|",
        " _|",
        "   ",
    ): "9",
}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError("Number of input columns is not a multiple of three")

    result = []

    for row_start in range(0, len(input_grid), 4):
        current_rows = input_grid[row_start:row_start + 4]
        line_result = ""

        for start in range(0, len(current_rows[0]), 3):
            digit = []

            for row in current_rows:
                digit.append(row[start:start + 3])

            line_result += DIGITS.get(tuple(digit), "?")

        result.append(line_result)

    return ",".join(result)