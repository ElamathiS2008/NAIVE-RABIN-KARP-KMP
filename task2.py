
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0

        while j < m:
            comparisons += 1

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            matches.append(i)

    return matches, comparisons

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)

    lps = compute_lps(pattern)

    matches = []
    comparisons = 0

    i = 0
    j = 0

    while i < n:

        comparisons += 1

        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            matches.append(i - j)
            j = lps[j - 1]

        elif i < n and text[i] != pattern[j]:

            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return matches, comparisons

def rabin_karp(text, pattern):
    d = 256
    q = 101

    n = len(text)
    m = len(pattern)

    matches = []
    comparisons = 0

    p_hash = 0
    t_hash = 0

    h = pow(d, m - 1, q)

    # Calculate initial hash values
    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % q
        t_hash = (d * t_hash + ord(text[i])) % q

    # Slide the pattern over the text
    for s in range(n - m + 1):

        if p_hash == t_hash:

            match = True

            for k in range(m):
                comparisons += 1

                if text[s + k] != pattern[k]:
                    match = False
                    break

            if match:
                matches.append(s)

        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % q

            if t_hash < 0:
                t_hash += q

    return matches, comparisons

print("===============================================")
print(" STRING MATCHING ALGORITHMS COMPARISON ")
print(" Naive | KMP | Rabin-Karp")
print("===============================================")

text = input("\nEnter the Text    : ")
pattern = input("Enter the Pattern : ")

if len(pattern) == 0:
    print("\nPattern cannot be empty.")

elif len(pattern) > len(text):
    print("\nPattern length should not exceed Text length.")

else:

    naive_match, naive_comp = naive_search(text, pattern)
    kmp_match, kmp_comp = kmp_search(text, pattern)
    rk_match, rk_comp = rabin_karp(text, pattern)

    print("\n===============================================")
    print("RESULT")
    print("===============================================")

    print("\nNaive Algorithm")
    print("----------------")
    print("Match Positions :", naive_match)
    print("Comparisons     :", naive_comp)

    print("\nKMP Algorithm")
    print("--------------")
    print("Match Positions :", kmp_match)
    print("Comparisons     :", kmp_comp)

    print("\nRabin-Karp Algorithm")
    print("--------------------")
    print("Match Positions :", rk_match)
    print("Comparisons     :", rk_comp)

    print("\n===============================================")
    print("Comparison Summary")
    print("===============================================")
    print("{:<15}{:<15}".format("Algorithm", "Comparisons"))
    print("-" * 30)
    print("{:<15}{:<15}".format("Naive", naive_comp))
    print("{:<15}{:<15}".format("KMP", kmp_comp))
    print("{:<15}{:<15}".format("Rabin-Karp", rk_comp))