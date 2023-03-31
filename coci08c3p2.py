
encode_words = input()

encode_words_to_list = list(encode_words)

for i in range(len(encode_words_to_list)):
    if encode_words_to_list[i] in 'aeiou':
        encode_words_to_list[i+1] = '_'
        encode_words_to_list[i+2] = '_'
        i = i + 2

decode_words = ''.join(encode_words_to_list)
decode_words = decode_words.replace('_', '')

print(decode_words)