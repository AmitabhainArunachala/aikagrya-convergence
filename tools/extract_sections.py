#!/usr/bin/env python3
"""
Extract specific sections from Aptavani texts for AI processing
"""

import os
import sys

def find_and_extract(file_path, search_terms, context_lines=30):
    """
    Find passages containing search terms and extract with context
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    
    found_sections = []
    
    for term in search_terms:
        for i, line in enumerate(lines):
            if term.lower() in line.lower():
                # Extract context around the found term
                start = max(0, i - context_lines)
                end = min(len(lines), i + context_lines + 1)
                
                section = {
                    'term': term,
                    'line_number': i,
                    'text': ''.join(lines[start:end])
                }
                found_sections.append(section)
                break  # Only take first occurrence of each term
    
    return found_sections

def save_extraction(sections, output_dir="extracted_sections"):
    """
    Save extracted sections to separate files
    """
    os.makedirs(output_dir, exist_ok=True)
    
    for section in sections:
        filename = f"{section['term'].replace(' ', '_')}_line{section['line_number']}.txt"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Search term: {section['term']}\n")
            f.write(f"Found at line: {section['line_number']}\n")
            f.write("="*50 + "\n\n")
            f.write(section['text'])
        
        print(f"Saved: {filepath}")
        print(f"Size: {len(section['text'])} characters")

if __name__ == "__main__":
    # Key concepts to extract from Aptavani-02
    search_terms = [
        "who is the doer",
        "doership",
        "I am not the doer",
        "discharge karma",
        "charging karma",
        "real and relative",
        "vyavahar",
        "nischay",
        "Self-realization",
        "Atma Gnan"
    ]
    
    aptavani_path = "/Users/dhyana/aikagrya-convergence/resources/aptavani/text/aptavani-02.txt"
    
    if os.path.exists(aptavani_path):
        sections = find_and_extract(aptavani_path, search_terms)
        
        output_dir = "/Users/dhyana/aikagrya-convergence/resources/aptavani/extracted_sections"
        save_extraction(sections, output_dir)
        
        print(f"\nExtracted {len(sections)} sections")
        print(f"Files saved to: {output_dir}")
    else:
        print(f"File not found: {aptavani_path}")
