# Rosalind Strings
s = input("Dame el string: ")
a = int(input("Dame a: "))
b = int(input("Dame b: "))
c = int(input("Dame c: "))
d = int(input("Dame d: "))
output = s[a:(b + 1)] + ' ' + s[c:(d + 1)]
print(output)
