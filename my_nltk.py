import nltk
from nltk.tokenize import word_tokenize

    
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

keywords_pendidikan = generate_keyword("kementrianPendidikan.txt")
keywords_komunikasi = generate_keyword("kementrianKomunikasi.txt")

def classify_text(text):
    # Tokenisasi teks menjadi kata-kata
    words = word_tokenize(text.lower())

    # Cek aturan untuk mengklasifikasikan teks
    if any(word in words for word in keywords_pendidikan):
        return "Pendidikan"
    elif any(word in words for word in keywords_komunikasi):
        return "Teknologi"
    else:
        return "Tidak diketahui"
    
text_to_classify = "Komunikasi adalah hewan yang imut dan suka bermain."
category = classify_text(text_to_classify)
print(f"Kategori teks: {category}")
print(keywords_pendidikan)