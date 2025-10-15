"""
Coding Challenge 2: Word Frequency Counter
Problem:

Write a function named word_frequency that takes a string of text and returns a dictionary where:

Keys are the unique words found in the text.

Values are the counts (frequencies) of those words.

You'll need to handle a few things to make this robust:

Convert the entire text to lowercase.

Split the text into individual words.

Ignore simple punctuation (you don't need to get fancy; just focus on separating the words).
"""

def word_frequency(text):
    text = text.lower()
    text = text.split()
     