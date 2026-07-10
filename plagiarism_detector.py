import re

def normalize_and_tokenize(file_content):
    """
    Cleans the source code by removing comments, extra whitespaces, 
    and breaking it down into a unique set of structural tokens.
    """
    # Remove single-line comments (Python style # and JS style //)
    clean_content = re.sub(r'(#|//).*', '', file_content)
    
    # Convert text to lowercase and extract alphanumeric words/tokens
    tokens = re.findall(r'\b\w+\b', clean_content.lower())
    
    # Return as a mathematical set to store only unique structural elements
    return set(tokens)

def calculate_similarity(file1_path, file2_path):
    print(f"[PROCESSING] Analysing file structures...")
    print("-" * 60)
    
    try:
        with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
    except FileNotFoundError as e:
        print(f"[ERROR] Could not read files: {e.filename}")
        return

    # Transform raw text into unique token sets
    tokens1 = normalize_and_tokenize(content1)
    tokens2 = normalize_and_tokenize(content2)

    # ⚡ INTERVIEW FLEX: Jaccard Similarity Coefficient Calculation
    intersection = tokens1.intersection(tokens2) # Shared unique elements
    union = tokens1.union(tokens2)               # Total combined unique elements

    if not union:
        similarity_score = 0.0
    else:
        similarity_score = (len(intersection) / len(union)) * 100

    print(f"File 1 Unique Tokens: {len(tokens1)}")
    print(f"File 2 Unique Tokens: {len(tokens2)}")
    print(f"Shared Unique Tokens: {len(intersection)}")
    print("-" * 60)
    print(f"[RESULT] Structural Similarity Score: {similarity_score:.2f}%")
    
    if similarity_score >= 70.0:
        print("[WARNING] High similarity index detected. Potential code duplication.")
    else:
        print("[INFO] Similarity index within normal structural bounds.")

if __name__ == "__main__":
    # Create mock inline code files to test the execution immediately
    with open("student_a.py", "w") as f:
        f.write("def calculate_total(price, tax):\n    return price + (price * tax)\nprint(calculate_total(100, 0.05))")
        
    with open("student_b.py", "w") as f:
        f.write("def get_sum(val, fee):\n    # Copied logic with changed names\n    res = val + (val * fee)\n    return res\nprint(get_sum(100, 0.05))")

    # Run the detector against the mock files
    calculate_similarity("student_a.py", "student_b.py")