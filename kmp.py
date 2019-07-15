# Knuth Morris Pratt, Pattern Searchingk
# O(n) in worst case

def KMPProprocessing(pat):
   matches = 0
   lps = [0]
   for i in range(1, len(pat)):
       if pat[i] == pat[i-1]:
           matches += 1
       else:
           matches = 0
       lps.append(matches)
   return lps

prep = "AAAAA"
print(KMPProprocessing(prep))

prompt = "AABAACAABAA"
print(KMPProprocessing(prompt))
