# Decodificador

Decodes a secret message hidden in a Google Docs table.

The document holds a table where each row is a character and its position on a grid:

| x-coordinate | Character | y-coordinate |
|---|---|---|
| 0 | █ | 0 |
| 0 | █ | 1 |
| 1 | ▀ | 1 |
| ... | ... | ... |

The program reads the table and prints every character in its position, which draws the message in the terminal.

## Requirements

- Python 3
- pandas
- lxml (used by `pandas.read_html` to parse the page)

```
pip install pandas lxml
```

## Usage

Pass the published document URL as an argument:

```
python main.py "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
```

Output:

```
█▀▀▀
█▀▀
█
```

Keep the URL in quotes, since it contains special characters.

## How it works

1. `main` receives the URL through `sys.argv[1]`.
2. `pandas.read_html` reads the table from the document, and each column is stored in its own list: `x`, `caracteres` and `y`.
3. The grid is printed row by row, starting from the highest `y` (the top row) down to 0.
4. For each row, every column from 0 to the highest `x` is checked. If an entry's `x` and `y` match the current position, its character is printed; if not, a space is printed.
5. After all the columns of a row are checked, a line break is printed.

## Troubleshooting

If you get `UnicodeEncodeError: 'charmap' codec can't encode character`, your terminal is not using UTF-8. On Windows, run this before the script:

```
set PYTHONIOENCODING=utf-8
```

In PowerShell:

```
$env:PYTHONIOENCODING = "utf-8"
```
