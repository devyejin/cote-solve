modify = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for ch in modify:
    word = word.replace(ch,"*")
#없는 문자는 어차피 1글자짜리라 replace 고려 안해도 됨

print(len(word))