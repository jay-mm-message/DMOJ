
def is_america_words(words):
    return words[-2:] == 'or' 

def is_vowel(words):
    return words[-3] not in 'aeiouy'

while True:
    
    words = input()
    if words == 'quit!':
        break
    
    if len(words) > 4 and is_america_words(words) and is_vowel(words):
        words = words[:-2] + 'our'
    print(words)