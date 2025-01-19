import re

def count_articles_and_dates(text):
    # Patterns to detect articles
    a_pattern = r'\\ba\\b'
    an_pattern = r'\\ban\\b'
    the_pattern = r'\\bthe\\b'

    # Patterns to detect dates
    date_patterns = [
        # Dates like 15/11/2012 or 15/11/12
        r'\\b\\d{1,2}/\\d{1,2}/\\d{2,4}\\b',
        # Dates like 15th March 1999 or 15th March 99
        r'\\b\\d{1,2}(st|nd|rd|th)?\\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\\s+\\d{2,4}\\b',
        # Dates like 20th of March, 1999
        r'\\b\\d{1,2}(st|nd|rd|th)?\\s+of\\s+(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec),?\\s+\\d{2,4}\\b'
    ]

    # Count articles
    a_count = len(re.findall(a_pattern, text, re.IGNORECASE))
    an_count = len(re.findall(an_pattern, text, re.IGNORECASE))
    the_count = len(re.findall(the_pattern, text, re.IGNORECASE))

    # Count dates
    date_count = sum(len(re.findall(pattern, text, re.IGNORECASE)) for pattern in date_patterns)

    return a_count, an_count, the_count, date_count

def main():
    import sys
    input = sys.stdin.read().strip().splitlines()  # Properly split input into lines

    T = int(input[0])  # First line is the number of test cases
    results = []

    index = 1
    for _ in range(T):
        # Read text fragment
        text = input[index].strip()
        index += 2  # Skip the blank line after each fragment

        # Get counts
        a_count, an_count, the_count, date_count = count_articles_and_dates(text)

        # Store results
        results.extend([a_count, an_count, the_count, date_count])

    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
