a = int(input())
l = int(input())
p = int(input())
h = int(input())
x = (l + p + (abs(l - p))) // 2
y = (x + a + (abs(x - a)))// 2
z = y * h
print(f'{z}')