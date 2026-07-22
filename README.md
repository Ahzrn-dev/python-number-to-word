# Python Number to Word

A simple command-line Python application that converts numbers into their English word representation.

## Features

- Convert numbers from **0 to 999**
- Input validation
- Clear error messages
- Repeat conversion without restarting the program
- Unit tests with pytest
- Clean and readable code

## Technologies

- Python 3
- Pytest

## Project Structure

```
python-number-to-word/
│
├── src/
│   └── main.py
│
├── tests/
│   └── test_main.py
│
├── LICENSE
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Ahzrn-dev/python-number-to-word.git
cd python-number-to-word
```

## Usage

Run the application:

```bash
python src/main.py
```

Example:

```
Enter a number between 0 and 999: 342

three hundred forty-two

Do you want to continue? (y/n): y
```

## Running Tests

```bash
pytest
```

or

```bash
python -m pytest -v
```

## Example Output

```
Enter a number between 0 and 999: 105

one hundred five
```

## Future Improvements

- Support numbers larger than 999
- Support negative numbers
- Support decimal numbers
- Multiple language support
- Command-line arguments
- Web interface using Streamlit

## License

This project is licensed under the MIT License.
