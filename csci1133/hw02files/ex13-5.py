def binary_strings(n, prefix):
    if n == 0:
        print(prefix)
        return
    binary_strings(n-1, prefix + '0')
    binary_strings(n - 1, prefix + '1')



binary_strings(11, '')


























