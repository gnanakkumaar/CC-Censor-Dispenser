# These are the emails you will be censoring. The open() function is opening
#the text file that the emails are contained in and the .read() method is
#allowing us to save their contexts to the following variables:

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

###############################################################
## function converting one target word into censor string
###############################################################

def censor_one_word(word):
    censored = ''
    i = 0
    while i < len(word):
        #converting censor word in censoring character / in this case *
        if word[i] == ' ':
            censored += word[i]
        else:
            censored += '*'
        i += 1
    return censored

###############################################################
## first email censoring / based on input censor
###############################################################

def first_email(text, target):

    first_email_censored = text.replace(target, censor_one_word(target))

    return first_email_censored

#test of first email function
#print(first_email(email_one, 'learning algorithms'))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

###############################################################
## function to convert a list of words into a list of censored words, preserving word length
###############################################################

def words_to_censored(censor_list):

    targets_converted = []
    adding_target = ''

    for target in censor_list:
        #converting censor words in censoring shapes, while maintaining word length
        for counter in range(0,len(target)):
            if target[counter] == ' ':
                adding_target += target[counter]
            else:
                adding_target += '*'
        targets_converted.append(adding_target)
        adding_target = ''

    return targets_converted

###############################################################
## second email censoring based on list of items
###############################################################

def second_email(text, list_of_targets):

    targets_censored = words_to_censored(proprietary_terms)

    result = text.lower() #making sure every word is counted

    for counter in range(len(list_of_targets)):
        result = result.replace(list_of_targets[counter], targets_censored[counter])

    return result

#test of second email function
#print(second_email(email_two, proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

###############################################################
## third email censoring based on times word from list occured
###############################################################

def third_email(text, list_of_targets, double_targets):

    text = second_email(email_three, proprietary_terms)
    text = text.lower()
    text_to_words = text.split(' '); #making a list of words so that program can count how many times certain word occured

    words_to_replace = []
    counter = 0

    for record in double_targets:
        #loop for counting matched words, if more than 1, word is getting added to new list of words that are eligible for censoring
        for word in text_to_words:
            if record in word:
                counter += 1

            if counter > 1:
                words_to_replace.append(record)
                counter = 0 #after word occured more than once and gets appended, counter has to set on default value
        counter = 0 #making sure counter is back on default value when switching to next word

    censored_words = words_to_censored(words_to_replace)

    result = text_to_words
    result = ' '.join(result) #arranging string back again

    #notice that i used 'in' in next loop, so i dont have to use strip, therefore when I join the string, it gets same formatting
    for index in range(0,len(words_to_replace)):
        result = result.replace(words_to_replace[index], censored_words[index])

    return result

#testing for third email function
#print(third_email(email_three,proprietary_terms, negative_words))

###############################################################
## fourth email censoring with additional censoring of word from each side of target censor word
###############################################################

def fourth_email(text, list_of_targets, double_targets):

    #making list from email text, and also replacing new lines with ' * ', so that later i can join new line again
    text = text.lower()
    text = text.replace('\n', ' * ')
    text_to_words = text.split(' ');

    #concatenating all words that have to be censored
    all_censoring_words = proprietary_terms + negative_words
    words_for_censor = []

    #this is the main part. here, program is going through list of words that have to be censored_words
    #and matching it with every word from email text list
    for record in range(0, len(all_censoring_words)):
        for count in range(0, len(text_to_words)):
            if all_censoring_words[record] in text_to_words[count]:
                #when it founds a match, we use function censor_one_word to make '****' out of word and automatically
                #changing that into the list of email words, and doing same with one word from each side
                before = count - 1
                after = count + 1

                censoring_word = censor_one_word(all_censoring_words[record])
                text_to_words[count] = text_to_words[count].replace(text_to_words[count], censoring_word)

                censoring_word_before = censor_one_word(text_to_words[before])
                text_to_words[before] = text_to_words[count].replace(text_to_words[before], censoring_word_before)

                censoring_word_after = censor_one_word(text_to_words[after])
                text_to_words[after] = text_to_words[count].replace(text_to_words[after], censoring_word_after)

    #here text gets together, and also, im replacing my special string ' * ' with new line, so text returs with same formatting
    result = text_to_words
    result = ' '.join(result)
    result = result.replace(' * ', '\n')

    return result

#testing the fourth email function
#print(fourth_email(email_four, proprietary_terms, negative_words))
