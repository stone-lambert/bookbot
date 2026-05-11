
import re 

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(book_text):
    return len(book_text.split())

def get_characters(book_text):
    full_text = re.split(r"(\s+)", book_text)
    character_dict = {}
    for word in full_text:
        word = word.lower()
        for character in word:
            
            if character not in character_dict:
                character_dict[character] = 1
            else:
                character_dict[character] += 1
    return character_dict

def print_report(file_name):
    book_text = get_book_text(file_name)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")

    character_dict = get_characters(book_text)
    character_array = {k: v for k, v in sorted(character_dict.items(),key=lambda item: item[1], reverse=True)}

    for key, value in character_array.items():
        print(f"{key}: {value}")

    print("============= END ===============")




