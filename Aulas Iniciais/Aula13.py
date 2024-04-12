a = 'AAAA'
b = 'BBBB'
c = 1.1

formato = 'a={}, b={}, c={:.2f}'.format(a, b, c)
formato2 = 'a={1}, b={0}, c={2:.2f}'.format(a, b, c)


print(formato)
print(formato2)