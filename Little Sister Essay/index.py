"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    
    return title.title()


def check_sentence_ending(sentence):
    
    if sentence.endswith('.'):
        return True
    else:
        return False


def clean_up_spacing(sentence):
    
    return sentence.strip('dnue ')
    

    pass


def replace_word_choice(sentence, old_word, new_word):
   
    return sentence.replace(old_word, new_word)
