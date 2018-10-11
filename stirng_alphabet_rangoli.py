import string
def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    L = []
    for i in range(size):
        s = '-'.join(alpha[i:n])
        L.append((s[::-1] + s[1:]).center((2*n) -1 + 2*(n-1), '-'))
    print('\n'.join(L[::-1] + L[1:len(L)]))

if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)