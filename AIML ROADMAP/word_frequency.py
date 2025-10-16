def count_words(word_list):
    word_counts = {}
    for i in word_list:
        if i in word_counts:
            word_counts[i] += 1
        else:
            word_counts[i] = 1
data = ["apple","banana","apple","orange","apple"]
result = count_words(data)
print(result)