import itertools

def solve_cryptarithm(words, result):
    # Get all unique characters involved in the puzzle
    unique_chars = set("".join(words) + result)
    if len(unique_chars) > 10:
        raise ValueError("Too many unique characters for digits (max 10).")

    # Create a list of digits from 0 to 9
    digits = range(10)

    # Create permutations of the digits with the length equal to the number of unique characters
    for perm in itertools.permutations(digits, len(unique_chars)):
        # Map each unique character to a digit
        char_digit_map = dict(zip(unique_chars, perm))
        
        # Check if the solution is valid (i.e., no leading zeros)
        if any(char_digit_map[word[0]] == 0 for word in words + [result]):
            continue
        
        # Convert the words and result into numbers based on the current mapping
        word_sum = sum(int("".join(str(char_digit_map[char]) for char in word)) for word in words)
        result_value = int("".join(str(char_digit_map[char]) for char in result))
        
        # Check if the sum of the words equals the result
        if word_sum == result_value:
            # Print the solution
            for word in words:
                print(f"{word}: {''.join(str(char_digit_map[char]) for char in word)}")
            print(f"{result}: {''.join(str(char_digit_map[char]) for char in result)}")
            return char_digit_map
    
    return None

# Example usage:
words = ["SEND", "MORE"]
result = "MONEY"

solution = solve_cryptarithm(words, result)
if solution:
    print("\nSolution found:")
    for char, digit in solution.items():
        print(f"{char} = {digit}")
else:
    print("No solution found.")
