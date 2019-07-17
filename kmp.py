# Knuth Morris Pratt, Pattern Searching
# O(n) in worst case

def KMPPreprocessing(pat):
   matches = 0
   lps = [0]
   for i in range(1, len(pat)):
       if pat[i] == pat[i-1]:
           matches += 1
       else:
           matches = 0
       lps.append(matches)
   return lps

def KMP(text, pat):
    lps = KMPPreprocessing(pat)
    i = 0
    j = 0
    M = len(text)
    N = len(pat)
    while i < M:
        if text[i] == pat[j]:
            i += 1
            j += 1

        if j == N:
            print("Match found at index ", i-j)
            j = lps[j-1]

        elif i < M and pat[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

test = "BAAAATMAAAAAN"
pat = "AAA"

KMP(test, pat)
