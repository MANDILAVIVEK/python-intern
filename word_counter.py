# Word Counter Program

def count_words(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The input text to count words from.
    
    Returns:
        int: The number of words in the input text.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input and display output.
    """
    print("Welcome to the Word Counter Program!")
    
    # Prompt user for input
    user_input = input("Please enter a sentence or paragraph: ")
    
    # Check for empty input
    if not user_input:
        print("Error: Please enter some text.")
        return
    
    # Count words and display output
    word_count = count_words(user_input)
    print(f"The input text contains {word_count} words.")

if __name__ == "__main__":
    main()