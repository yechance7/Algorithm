import sys

word = sys.stdin.readline().strip().upper()
word_dict = {}
for val in word:
    if val in word_dict:
        word_dict[val] += 1
    else:
        word_dict[val] = 1
        
max_count = max(word_dict.values())

max_val = []

for val, count in word_dict.items():
    if count == max_count:
        max_val.append(val)

if len(max_val) == 1:
    print(max_val[0])


else:
    print("?")