def can_reduce_to_one_element(t, test_cases):
    results = []
    for case in test_cases:
        n, a = case
        a.sort()
        possible = True
        for i in range(n - 1):
            if a[i + 1] - a[i] > 1:
                possible = False
                break
        if possible:
            results.append("YES")
        else:
            results.append("NO")
    return results

t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = can_reduce_to_one_element(t, test_cases)
print("\n".join(results))
