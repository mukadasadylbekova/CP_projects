def edit_distance(a, b):
    n, m = len(a), len(b)
    
   
    prev = list(range(m + 1))
    curr = [0] * (m + 1)
    
    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(
                    prev[j],    # delete
                    curr[j - 1],# insert
                    prev[j - 1] # replace
                )
        prev, curr = curr, prev  # swap rows for next iteration

    return prev[m]

# Input reading
a = input().strip()
b = input().strip()
print(edit_distance(a, b))
