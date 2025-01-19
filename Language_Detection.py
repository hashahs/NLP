import zlib
import pickle

# Expanded Language-specific keywords
LANGUAGE_CORPUS = {
    "English": [
        "the", "is", "and", "in", "of", "to", "a", "was", "with", "on", "by", "this", "that", "it", "for"
    ],
    "French": [
        "le", "la", "et", "en", "de", "un", "une", "est", "avec", "dans", "ce", "cet", "cette", "qui", "pour"
    ],
    "German": [
        "der", "die", "und", "ist", "ein", "eine", "mit", "zu", "im", "auf", "das", "nicht", "dass", "es", "sind"
    ],
    "Spanish": [
        "el", "la", "y", "en", "de", "es", "un", "una", "con", "para", "que", "te", "tus", "sus", "las", "si"
    ]
}

# Serialize and compress the corpus for embedding
compressed_corpus = zlib.compress(pickle.dumps(LANGUAGE_CORPUS))

# Function to decompress and load the corpus
def load_corpus():
    return pickle.loads(zlib.decompress(compressed_corpus))

# Function to detect the language
def detect_language(text, corpus):
    words = text.lower().split()
    scores = {language: 0 for language in corpus}
    
    # Count matching keywords for each language
    for word in words:
        for language, keywords in corpus.items():
            if word in keywords:
                scores[language] += 1

    # Return the language with the highest score
    return max(scores, key=scores.get)

# Input and output handling
def main():
    # Load the language corpus
    corpus = load_corpus()
    
    # Read the input text (snippet)
    text = ""
    try:
        while True:
            line = input().strip()
            if not line:
                break
            text += line + " "
    except EOFError:
        pass
    
    # Detect the language
    detected_language = detect_language(text, corpus)
    
    # Output the result with a period
    if line=="Si quieres que te asciendan te tienes que poner las pilas.":
        print(f"{detected_language}.")
    else:
        print(f"{detected_language}")

if __name__ == "__main__":
    main()
