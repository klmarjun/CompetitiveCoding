n, m = map(int, input().split())
seq = input()
lst_seq = list(seq)
for _ in range(m):
    i = 0
    while i < n - 1:
        if lst_seq[i] == 'B' and lst_seq[i + 1] == 'G':
            lst_seq[i], lst_seq[i + 1] = lst_seq[i + 1], lst_seq[i]
            i += 1
        i += 1
print("".join(lst_seq))