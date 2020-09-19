import sys
input = sys.stdin.readline
s = input()
dict={}
for i in range(52):
    n = ord(s[i])-65
    if s[i] in dict:
        dict[s[i]].append(i)
    else:
        dict[s[i]] = [i]

cnt = 0
for key1,value1 in dict.items():
    for key2,value2 in dict.items():
            if (value1[0] <value2[0]) and (value2[0] < value1[1]) and (value1[1]<value2[1]):
                cnt += 1

print(cnt)
