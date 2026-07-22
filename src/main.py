ONES = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

TENS = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def number_to_words(number: int) -> str:
    """Convert an integer from 0 to 999 into English words."""

    if not 0 <= number <= 999:
        raise ValueError("Number must be between 0 and 999.")

    if number < 20:
        return ONES[number]

    if number < 100:
        tens, remainder = divmod(number, 10)
        result = TENS[tens * 10]

        if remainder:
            result += f"-{ONES[remainder]}"

        return result

    hundreds, remainder = divmod(number, 100)
    result = f"{ONES[hundreds]} hundred"

    if remainder:
        result += f" {number_to_words(remainder)}"

    return result


def main() -> None:
    """Run the command-line application."""

    while True:
        try:
            number = int(input("Enter a number between 0 and 999: "))
            print(number_to_words(number))

        except ValueError as error:
            print(f"Error: {error}")

        continue_choice = input(
            "Do you want to continue? (y/n): "
        ).strip().lower()

        if continue_choice != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()