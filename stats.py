def get_word_count(book_text):
    words = book_text.split()
    total_words = len(words)
    return total_words

def get_num_charac(book_text):
    charac_dict = {}
    for index in range(0, len(book_text)):
        character = book_text[index].lower()
        if character in charac_dict:
            charac_dict[character] += 1
        else:
            charac_dict[character] = 1
    return charac_dict

def sorted_list(charac_dict):
    list_of_dicts = []
    for key in charac_dict:
        dicts = {}
        dicts["char"] = key
        dicts["num"] = charac_dict[key]
        list_of_dicts.append(dicts)
    
    def sort_on(dicts):
        return dicts["num"]        
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts