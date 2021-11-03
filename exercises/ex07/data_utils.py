"""Utility functions."""

from csv import DictReader
__author__ = "730490041"

# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(a: dict[str, list[str]], b: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N forws of data for each column."""
    result: dict[str, list[str]] = {}

    for column in a:
        first_row: list[str] = []
        i: int = 0
        if b > len(a[column]):
            b = len(a[column])
        while i < b:
            first_row.append(a[column][i])
            i += 1
        result[column] = first_row    
        
    return result


def select(a: dict[str, list[str]], b: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for columns in b:
        result[columns] = a[columns]
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for columns in a:
        result[columns] = a[columns]
    for columns in b:
        if columns in result:
            result[columns].extend(b[columns])
        else:
            result[columns] = b[columns]

    return result


def count(a: list[str]) -> dict[str, int]:
    """Produce a dictionary with the each item of a list of strings being the key and the frequency being the value."""
    result: dict[str, int] = {}
    for i in a:
        if i in result.keys():
            result[i] += 1
        else: 
            result[i] = 1
    return result
