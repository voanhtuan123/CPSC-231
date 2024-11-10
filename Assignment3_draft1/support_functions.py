def get_greetings(name): #function1
    if name:
        return f"Greetings {name}! I am your virtual assistant Chat231."
    else:
        return " "


def full_word(sentence,word):     #function2

    ans = False
    # Convert both sentence and word to lowercase for case insensitivity and add " " to start and end of sentence
    SentenceLowercase = sentence.lower()
    WordLowercase = word.lower()
    SentenceLowercase = " " + SentenceLowercase + " "
    # if equal then return right away
    if SentenceLowercase == WordLowercase:
        return True
    WordLen = len(WordLowercase)
    SentLen = len(SentenceLowercase)

    # List of separators
    separators = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~", "`"]
    

    for i in range(1,SentLen):
        # Keep track of the char in sentence
        track = 0
        # If a char in sentence equals the first char in word and the previous char in sentence must be a separator
        if SentenceLowercase[i] == WordLowercase[0] and SentenceLowercase[i-1] in separators:
            # Checking for the index range
            if SentLen - i < WordLen:
                continue
            else:
                for j in range(WordLen):
                    # Checking if words by words is equal
                    if WordLowercase[j] == SentenceLowercase[j + i]:
                        track = j + i
                        ans = True
                    else:
                        print(ans)
                        continue
                # Checking for validity and if the next char is a separator
                if SentenceLowercase[track + 1] in separators and ans == True:
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
    

