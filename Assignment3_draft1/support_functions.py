def get_greetings(name): #function1
    if name:
        return f"Greetings {name}! I am your virtual assistant Chat231." #return a name inside sentence
    else:
        return " "


def full_word(sentence,word):     #function2
    SentenceLowercase = sentence.lower() #convert all letters in sentence to lowercase
    WordLowercase = word.lower()  #convert all letters in word to lowercase
    SentenceLowercase = " " + SentenceLowercase + " " #add blank at the start and at the end of the sentence

    # List of separators
    separators = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/",":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "{", "|", "}", "~", "`"]

    # sentence is the same with word, return true 
    if SentenceLowercase == WordLowercase:
        return True

    for i in range(len(SentenceLowercase)):
        if SentenceLowercase[i] == WordLowercase[0] and SentenceLowercase[i-1] in separators: #add condition when first letter in word is the same with any letter in sentence and the letter before is seperator
                for x in range(len(WordLowercase)):
                    if WordLowercase[x] == SentenceLowercase[x + i]: #check the rest of letter in word if it the same with the next letter in sentence
                        ans = True
                    else: #if one of the rest isn't same, then return false
                        print(False)
                        continue
                if SentenceLowercase[x + i + 1] in separators and ans == True:   #if all the letter is the same, then check the letter next to the final letter is seperator
                    return True
    return False



def get_answer(database, sentence):
    for i in database: 
        if full_word(sentence,i): #check for existing keyword in database, and return the corresponding answer
            return(database[i])
    else:
        return "Sorry, I do not understand your question."
    

