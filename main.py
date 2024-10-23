def main(): 
   book_path = "./books/frankenstein.txt"

   text = get_book_text(book_path)
   num_words = get_word_count(text)
   char_dict = get_all_chars(text)

   sorted_char_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))

   print(f"--- Begin report of ${book_path} ---")
   print(f"{num_words} words were found in the document")

   for key in sorted_char_dict.keys():
       if type(key) == str:
           if key.isalpha():
               print(f"The '{key}' character was found {char_dict[key]} times ")
    
   print("--- End of report ---")


def get_book_text(path: str):
    with open(path) as f:
        return f.read()
    
def get_word_count(text: str):
    words = text.split()
    return len(words)

def get_count_for_char(text: str, char: str):
    lowerCaseChar = char.lower()
    return text.count(lowerCaseChar)

def get_all_chars(text: str):
    char_dict = {}

    for c in text:
        lowered = c.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    
    return char_dict

def sort_char_dict(dict):
    return sorted(dict)



if __name__ == "__main__":
    main()