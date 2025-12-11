# combineMDpython
A simple Python tool that recursively gathers all Markdown files in a directory and merges them into a single combined document with separators and size confirmation.

# CombineMD

CombineMD is a lightweight Python utility that recursively scans a directory and merges all Markdown files into a single consolidated document, inserting separators between entries and confirming estimated size before generation.

## Features

1. Recursively detects all `.md` files under the current directory  
2. Generates a single `combined.md` file in sorted order  
3. Inserts a clear separator (`&& && && &&`) between merged files  
4. Estimates the final file size and prompts the user before writing  
5. Automatically ignores the output file if it already exists  
6. Requires no external dependencies

## Usage

1. Place the script (`combinemd.py`) in the directory whose Markdown files you want to merge.
2. Run the script from the terminal:

```bash
python combinemd.py
````

3. Review the estimated combined size and confirm to proceed.

## Output

A new file named `combined.md` will be created in the same directory. It will contain all Markdown files in sorted order with separators for easy navigation.

## Purpose

CombineMD is ideal for consolidating prompt notes, agent definitions, writing archives, documentation fragments, or any multi-file Markdown knowledge base into a single file for backup or review.

## Requirements

* Python 3.7 or later

## License

This project is licensed under the GNU Affero General Public License v3.0.
See the `LICENSE` file for full details.

