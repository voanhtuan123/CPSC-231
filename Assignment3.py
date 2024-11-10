# NGUYEN HOANG KHOI


def get_greetings(name):
    # return user's name if exists
    return "Greetings " + name + "! I am your virtual assistant Chat231."


def full_word(sentence,word):
    # Use a boolean to keep track
    ans = False
    # Convert both sentence and word to lowercase for case insensitivity and add " " to start and end of sentence
    new_sen = sentence.lower()
    new_word = word.lower()
    new_sen = " " + new_sen + " "
    # if equal then return right away
    if new_sen == new_word:
        return True
    word_len = len(new_word)
    sen_len = len(new_sen)

    # List of separators
    separators = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",
                  ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~", "`"]
    for i in range(sen_len):
        # Keep track of the char in sentence
        track = 0
        # If a char in sentence equals the first char in word and the previous char in sentence must be a separator
        if new_sen[i] == new_word[0] and new_sen[i-1] in separators:
            # Checking for the index range
            if sen_len - i < word_len:
                continue
            else:
                for j in range(word_len):
                    # Checking if words by words is equal
                    if new_word[j] == new_sen[j + i]:
                        track = j + i
                        ans = True
                    else:
                        ans = False
                        continue
                # Checking for validity and if the next char is a separator
                if new_sen[track+1] in separators and ans == True:
                    return True
    return False


def get_answer(database, sentence):
    # Check for keyword in
    for key in database:
        if full_word(sentence,key):
            # If exists then return the key value
            return(database[key])
    else:
        return "Sorry, I do not understand your question."