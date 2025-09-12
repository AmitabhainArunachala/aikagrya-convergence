#!/usr/bin/env python3

# Extract a section from Aptavani-02
file_path = "/Users/dhyana/aikagrya-convergence/resources/aptavani/text/aptavani-02.txt"

with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    # Read file and look for section about fundamental concepts
    lines = f.readlines()
    
# Find sections with key terms
key_terms = ['Self', 'Atma', 'doer', 'knower', 'seer', 'karma', 'liberation']
relevant_sections = []
current_section = []

for i, line in enumerate(lines):
    if any(term in line for term in key_terms):
        # Capture context around this line
        start = max(0, i-10)
        end = min(len(lines), i+20)
        section = ''.join(lines[start:end])
        print(f"Found section at line {i}:")
        print("="*50)
        print(section)
        print("="*50)
        if len(section) > 1000:
            break
