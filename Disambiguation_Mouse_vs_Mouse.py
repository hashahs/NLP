# Enter your code here. Read input from STDIN. Print output to STDOUT
import zlib
import pickle

# Sample corpus for classification
CONTEXT_CORPUS = {
    "animal": [
        "genome", "tail", "fur", "postnatal", "development", "rodent", "habitat", "temperature", "nest"
    ],
    "computer-mouse": [
        "input", "device", "click", "cursor", "screen", "scroll", "pointer", "usb", "bluetooth"
    ]
}

# Serialize and compress the corpus for embedding
compressed_corpus = zlib.compress(pickle.dumps(CONTEXT_CORPUS))

# Function to decompress and load the corpus
def load_corpus():
    return pickle.loads(zlib.decompress(compressed_corpus))

# Function to classify the context of the word "mouse"
def classify_mouse(sentence, corpus):
    animal_keywords = corpus["animal"]
    computer_keywords = corpus["computer-mouse"]
    
    # Tokenize the sentence and convert to lowercase
    words = sentence.lower().split()
    
    # Check for keywords in the sentence
    for word in words:
        if word in animal_keywords:
            return "animal"
        if word in computer_keywords:
            return "computer-mouse"
    # Default to "animal" if no keywords are found
    return "animal"

# Input and output handling
def main():
    # Load the dictionary
    corpus = load_corpus()
    
    # Read input
    n = int(input())
    sentences = [input().strip() for _ in range(n)]
    
    # Classify each sentence
    results = [classify_mouse(sentence, corpus) for sentence in sentences]
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
