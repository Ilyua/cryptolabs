import base64
from third import third_task
from second import string_xor

def autizm(a, b):
    length = len(b)
    for i in range(length, len(a)//2):
        b += b[i - length]
    b = ''.join([hex(ord(i))[2:] for i in b])
    d = string_xor(a, b)
    print(''.join([chr(int(d[i: i + 1], 16)) for i in range(0, len(d))]))



f = open('breakRepeatedKeyXor.txt')
c = ''
for s in f:
    c += '%s' % s[0: len(s) - 1]
print(c)
b = "".join(["{:08b}".format(x) for x in base64.b64decode(c)])
print(b)

a = hex(int(b, 2))[2:]



for k in range(29, 30):
    a = []
    for j in range(0, k):
        a.append('')
    for j in range(0, len(b), 8):
        a[(j // 8) % k] += b[j: j + 8]

    print(a, len(a))

    for j in range(0, len(a)):
        a[j] = third_task(hex(int(a[j], 2)))
    ans = ''
    print(a, len(a))
    for j in range(len(b) // 8):
        ans += a[j % k][0]
        a[j % k] = a[j % k][1:]
    print(ans)