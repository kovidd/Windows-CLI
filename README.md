# Windows-CLI
Windows vs Linux (how windows complicates everything)


## Context

Being able to ingest, validate and alter data is an important part of Data Engineering. We aim to write a small [CLI tool](https://en.wikipedia.org/wiki/Command-line_interface) that works as described below. Python is used, but only the core SDK/standard libraries provided by the language.

## Input

The program should expect valid JSON representing a two dimensional matrix (i.e. a list of lists) as a single string argument to the [CLI tool](https://en.wikipedia.org/wiki/Command-line_interface) as demonstrated below.

It will be in one of the following two formats:

**A**) **a list of lists**

The expected format is `[ [column names], [first row], [second row], ... ]`. An example invocation of your program using this format would be:

```
python3 map_csv.py '[ ["a","b","c"], [1,2,null], [2,3,4], [5,null,6] ]'
```

**B**) **a list of objects**

JSON objects are simply unordered collections of key:value pairs.

Each row is represented by an object containing the variables set for that row.

Accordingly, this form of input is convenient for sparse data sets. An example invocation of your program using this format would be:

```
python3 map_csv.py '[ { "a":1, "b":2 }, { "a": 2, "b":3, "c":4 }, { "c":6, "a":5 } ]'
```

## Output

The program should transform the input into a CSV file, mapping each column name to a column and each value to the appropriate row and column.

For input type (A), we expect the following output:

|a|b|c|
|---|---|---|
|1|2||
|2|3|4|
|5||6|

For input type (B), any variables that are missing in a row should be represented by an empty cell in the CSV.

The order of the values in each variable's list should be the same as the order of the rows, and we expect the following output:

|a|b|c|
|---|---|---|
|1|2||
|2|3|4|
|5||6|

## Usage 
python3 map_csv.py '[ { "a":1, "b":2 }, { "a": 2, "b":3, "c":4 }, { "c":6, "a":5 } ]'
python3 map_csv.py '[ ["a","b","c"], [1,2,null], [2,3,4], [5,null,6] ]'
