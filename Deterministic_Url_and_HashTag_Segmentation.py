import re

# Load words from "words.txt" into a set for quick lookup
def load_words():
    with open("words.txt", "r") as f:
        return set(word.strip().lower() for word in f)

WORDS = load_words()

# Check if a string is a valid word or a number
def is_valid_token(token):
    return token in WORDS or re.fullmatch(r'\d+(\.\d+)?', token)

# Recursive segmentation with memoization
def segment_string(s, memo):
    if s in memo:
        return memo[s]
    if not s:
        return []

    best_split = None
    for i in range(1, len(s) + 1):
        left = s[:i]
        if is_valid_token(left):
            right_split = segment_string(s[i:], memo)
            if right_split is not None:
                current_split = [left] + right_split
                if best_split is None or len(current_split) > len(best_split):
                    best_split = current_split

    memo[s] = best_split if best_split is not None else [s]
    return memo[s]

# Process domain names and hashtags, removing extensions
def process_input(input_str):
    input_str = input_str.lower()
    input_str = re.sub(r"^(www\.|#)|\.(com|net|org|gov|edu|ru|co\.uk|cn|mil|cz|us|in|io)$", "", input_str)
    segmented = segment_string(input_str, {})
    return ' '.join(segmented)

if __name__ == "__main__":
    n = int(input().strip())
    inputs = [input().strip() for _ in range(n)]

    for input_str in inputs:
        print(process_input(input_str).strip())