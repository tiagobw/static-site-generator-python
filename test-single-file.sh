#!/usr/bin/env sh

# Example usage: ./test-single-file.sh parentnode 
python3 -m unittest discover -s src -p "test_$1.py"