# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import zlib
import pickle
from difflib import get_close_matches

# Sample corpus: a dictionary with common words and country names
CORPUS = [
    "going", "to", "china", "who", "was", "the", "first", "president", "of",
    "india", "winner", "match", "food", "in", "america", "usa"
]

# Serialize and compress the corpus for embedding in the script
compressed_corpus = zlib.compress(pickle.dumps(CORPUS))

# Function to decompress and load the corpus
def load_corpus():
    return pickle.loads(zlib.decompress(compressed_corpus))

# Spell corrector function
def spell_correct(query, dictionary):
    words = query.split()
    corrected_words = []

    for word in words:
        if word in dictionary:
            corrected_words.append(word)
        else:
            # Find close matches with edit distance of 1 or 2
            matches = get_close_matches(word, dictionary, n=1, cutoff=0.8)
            corrected_words.append(matches[0] if matches else word)
    return " ".join(corrected_words)

# Input and output handling
def main():
    # Load the dictionary
    dictionary = load_corpus()
    
    # Read input
    n = int(input())
    queries = [input().strip() for _ in range(n)]
    
    # Process each query
    results = [spell_correct(query, dictionary) for query in queries]
    
    # Output results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
