def generate_keyword(file_path): 
    keywords = []
    # Assuming both the script and the text file are in the same directory
    # Open the text file for reading
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            # Process the line (e.g., print it)
            keywords.append(line.strip().lower())

    # The file is automatically closed when the 'with' block is exited
    return keywords