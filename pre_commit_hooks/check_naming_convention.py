from __future__ import annotations
import re

def check_naming_convention(files):
    for file_path in files:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line_num, line in enumerate(lines, start=1):
                identifiers = re.findall(r'\b[A-Za-z0-9_]+\b', line)
                for identifier in identifiers:
                    if not re.match(r'^[a-zA-Z0-9_]+_[a-zA-Z0-9_]+_[a-zA-Z0-9_]+_[a-zA-Z0-9_]+$', identifier):
                        print(f"ERROR: Invalid naming convention in {file_path}:{line_num}: {identifier}")

