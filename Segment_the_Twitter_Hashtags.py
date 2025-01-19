# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import zlib
import pickle

# Example dictionary (you should replace this with a comprehensive list of 5000+ words)
word_list = [
    "we", "are", "the", "people", "mention", "your", "faves", 
    "now", "playing", "the", "walking", "dead", "follow", "me"
]
word_set = set(word_list)

def segment_hashtag(hashtag, word_set):
    """
    Segments a single hashtag into its constituent words using a greedy approach.
    """
    n = len(hashtag)
    dp = [None] * (n + 1)
    dp[0] = []
    
    for i in range(1, n + 1):
        for j in range(0, i):
            word = hashtag[j:i]
            if word in word_set and dp[j] is not None:
                dp[i] = dp[j] + [word]
                break
    
    return " ".join(dp[-1]) if dp[-1] is not None else hashtag

def main():
    # Input processing
    N = int(input().strip())
    hashtags = [input().strip() for _ in range(N)]
    
    # Segment each hashtag
    for hashtag in hashtags:
        print(segment_hashtag(hashtag, word_set))

# Example usage
if __name__ == "__main__":
    main()
