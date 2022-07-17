string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
x = 3
res = [string[y - x:y] for y in range(x, len(string) + x, x)]
print(res)