import re

def resolve_pronouns(text, entities):
    # Find all highlighted pronouns in the text
    pronouns = re.findall(r'\*\*(.*?)\*\*', text)
    
    # Split the text into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Mapping of pronouns to entities
    pronoun_to_entity = []
    
    for pronoun in pronouns:
        resolved_entity = None
        closest_distance = float('inf')
        
        # Iterate through each sentence to find the pronoun and its closest entity
        for sentence in sentences:
            if f"**{pronoun}**" in sentence:
                # Get the position of the pronoun in the sentence
                pronoun_index = sentence.find(f"**{pronoun}**")
                
                # Check for the closest entity before the pronoun
                for entity in entities:
                    entity_index = sentence.find(entity)
                    if 0 <= entity_index < pronoun_index:
                        distance = pronoun_index - entity_index
                        if distance < closest_distance:
                            closest_distance = distance
                            resolved_entity = entity

        if not resolved_entity:
            # Fallback to search the entire text for the nearest entity if no match in the same sentence
            text_index = text.find(f"**{pronoun}**")
            for entity in entities:
                entity_index = text.find(entity)
                if 0 <= entity_index < text_index:
                    distance = text_index - entity_index
                    if distance < closest_distance:
                        closest_distance = distance
                        resolved_entity = entity
        
        pronoun_to_entity.append(resolved_entity)

    return pronoun_to_entity

def main():
    # Input reading
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N = int(data[0])  # Number of lines in the text
    text = " ".join(data[1:N + 1])  # Combine text lines
    entities = data[N + 1].split(";")  # List of entities
    
    # Resolve pronouns
    results = resolve_pronouns(text, entities)
    
    # Print results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
