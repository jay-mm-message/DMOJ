head_words = 'A long time ago in a galaxy '
tail_words = 'far away...'

new_hope_count = int(input())
new_hope_words = head_words
for i in range(new_hope_count-1)  :
    new_hope_words = new_hope_words + 'far, '
new_hope_words = new_hope_words + tail_words

print(new_hope_words)
