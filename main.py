def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Uncomment to see the file's contents if needed
    # print(file_contents)

    def wordcount(file_contents):
        words = file_contents.split()
        word_count = len(words)
        return word_count

    def charcount(file_contents):
        words_lower = file_contents.lower()
        
        char_count = {}
        for char in words_lower:
            if char.isalnum():  # Only count alphanumeric characters
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

        # Sort the dictionary items by key (character)
        sorted_chars = sorted(char_count.items())
        return sorted_chars

    # Call the functions and store their results
    word_count = wordcount(file_contents)
    sorted_chars = charcount(file_contents)

    # Generate the report
    print("-- Begin report of books/frankenstein.txt --")
    print(f"{word_count} words found in the document")
    for char, count in sorted_chars:
        print(f"The character '{char}' was found {count} times")

# Run the main function
main()
