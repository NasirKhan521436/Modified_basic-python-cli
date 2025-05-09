import os
import sys
import argparse
from typing import Union

def get_file_size_in_mb(file_path: str, verbose: bool = False) -> int:
    """
    Return the size of a file in megabytes (MB).
    
    Args:
        file_path: Path to the file.
        verbose: If True, prints progress messages.
    
    Raises:
        FileNotFoundError: If file does not exist.
        ValueError: If path is a directory.
    """
    if verbose:
        print(f"Calculating size for {file_path}...")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    if not os.path.isfile(file_path):
        raise ValueError(f"Path is not a file: {file_path}")
    
    bytes_size = os.path.getsize(file_path)
    return bytes_size // (1024 ** 2)

def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="CLI tool to calculate file size in MB."
    )
    parser.add_argument(
        "file",
        help="Path to the file."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output."
    )
    return parser.parse_args()

def main() -> None:
    """Entry point for the CLI."""
    args = parse_args()
    try:
        mb_size = get_file_size_in_mb(args.file, args.verbose)
        print(f"{mb_size} MB")
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()