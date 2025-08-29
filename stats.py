def get_book_words(book):
    with open(book, 'r') as file:
        contents = file.read()
        words = contents.split()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {len(words)} total words")

def get_book_chars(book):
    with open(book, 'r') as file:
        contents = file.read().lower()
        keys = ['key1', 'key2', 'key3']
    character_dict = {char: 0 for char in contents}
    for char in contents:
        character_dict[char] += 1
    return character_dict

def sort_book_chars(character_dict):
    sorted_character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))
    print("--------- Character Count -------")
    for char in sorted_character_dict:
        if char.isalpha():
            print(f"{char}: {character_dict[char]}")
    print("============= END ===============")
