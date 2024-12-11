def count_word_occurrences(input_string):

    words = input_string.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

input_string = "hello world hello python world"
word_occurrences = count_word_occurrences(input_string)

print(word_occurrences)