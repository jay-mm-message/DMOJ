head_word = 'sp'
tail_word = 'ky'

frightening_count = int(input())

frightening_word = head_word
for i in range(frightening_count):
    frightening_word = frightening_word + 'o'
frightening_word = frightening_word + tail_word

print(frightening_word)