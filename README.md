# BookBot — CLI Text Analysis Tool

BookBot is a command-line Python application that analyzes a plain-text file and produces:
- Total word count
- Frequency of each alphabetical character
- Character counts sorted in descending order

It is structured as a small, modular tool with clear separation between CLI handling and analysis logic.

BookBot is my first [Boot.dev](https://www.boot.dev) project!

bookbot/
├── main.py          # CLI entry point
├── stats.py         # word count, char count, sorting logic
├── books/           # ignored by git; user-supplied text files
└── README.md

# Installation and Setup

Clone the repository:
git clone https://github.com/rdowning07/bookbot
cd bookbot

Create a directory for book files (this folder is intentionally excluded from version control):
mkdir -p books

Download sample books (used by the Boot.dev CLI tests):

wget -O books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt

wget -O books/mobydick.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/mobydick.txt

wget -O books/prideandprejudice.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/prideandprejudice.txt

# Running the Tool

Correct usage:
python3 main.py path/to/book.txt

Example:
python3 main.py books/frankenstein.txt

If invoked without a file path:
Usage: python3 main.py <path_to_book>

# Example Output

============ BOOKBOT ============

Analyzing book found at books/frankenstein.txt...

----------- Word Count ----------

Found 75767 total words

--------- Character Count -------

e: 44538

t: 29493

a: 25894

...

============= END ===============

# Technical Notes

- sys.argv is used for CLI argument parsing.
- Files are read using a dedicated helper (get_books_text).
- Alphabetical character filtering uses .isalpha() to ignore punctuation and whitespace.
- Sorting uses a custom key extractor (sort_on) to order by frequency.
- stats.py contains pure functions with no side effects, making the analysis layer testable and reusable.
- The repository deliberately excludes large text files to keep the repo lightweight and focused.

# Proposed Improvments

This section outlines reasonable extensions:

CLI Enhancements

- Support multiple input files in a single run
- Optional streaming mode for large texts

Engineering Improvements
- Add type hints and static analysis (mypy)
- Introduce unit tests (pytest)
- Provide structured error handling and logging
- Package as an installable module (pip install bookbot)

Optional Frontend Work
- Minimal web UI for visualization (Flask/FastAPI)
- Character-frequency charts
- File upload interface
