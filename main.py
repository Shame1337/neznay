#!/usr/bin/env python3

"""
Entry point script.

Run this file directly to execute the application. Extend the `main` function
with your actual program logic as needed.
"""

import sys
from typing import List


def main(command_line_arguments: List[str]) -> int:
    """Main entry point for the application.

    Args:
        command_line_arguments: Command-line arguments excluding the program name.

    Returns:
        Process exit code where 0 indicates success.
    """
    print("Hello from main.py 👋")
    if command_line_arguments:
        print("Arguments:", command_line_arguments)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

