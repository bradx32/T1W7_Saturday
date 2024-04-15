# http://leetcode.com/problems/concatenation-of-array/
# Please post your solution here, wrapped in triple backticks (`) and double vertical bars (|), for code and hiding it respectively.
# These formatting options can also be accessed when you highlight your text.


# Have tested it myself and below code should work (from Jairo)

def sentence_words(sentences):
    word_sentence = []

    for sentence in sentences: # loops through each item in sentences
        word_count = 1
        for character in sentence: # loop through each character in sentence
            if character == " ":
                word_count += 1
        word_sentence.append(word_count)

    word_sentence.sort(reverse=True)
    return(word_sentence[0])

max_words = sentence_words(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])

print(max_words)