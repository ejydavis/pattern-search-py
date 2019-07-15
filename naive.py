import time

with open('tale.txt', 'r') as file:
   book = file.read().replace('\n', '')
   print(len(book))

pat = "The"


def naive_ps(pattern, text):
   plen = len(pattern)
   tlen = len(text)
   matches = 0
   patterns = 0

   for i in range(0, tlen):
       if text[i] == pattern[0]:
           pi = 1
           ti = i+1
           matches += 1
           while ti < tlen and pi < plen and pattern[pi] == text[ti]:
               matches += 1
               pi += 1
               ti += 1
           if matches > 1:
               #print("Pattern found at index ", i)
               patterns += 1
           matches = 0
   print("Total patterns found ", patterns)


def naive_ps_v2(pattern, text):
   plen = len(pattern)
   tlen = len(text)
   patterns = 0

   # loop to slide pattern
   for i in range(tlen - plen + 1):
       j = 0

       # For curr index i, check for pattern match
       for j in range(0, plen):
           if (text[i+j] != pattern[j]):
               break
       if j == plen - 1:
           #print("Pattern found at index ", i)
           patterns += 1
   print("Total patterns found ", patterns)


start_time = time.time()
naive_ps(pat, book)
print("-- Execution time: %s seconds --" % (time.time() - start_time))

start_time = time.time()
naive_ps_v2(pat, book)
print("-- Execution time: %s seconds --" % (time.time() - start_time))


def naivePatternSearch(pattern, text):
   plen = len(pattern)
   tlen = len(text)
   matches = 0

   # loop through text
   for i in range(0, tlen-1):
       if pattern[0] == text[i]:
           j = i
           k = 0

           while text[j] == pattern[k] and k < plen-1 and j < tlen-1 :
               matches += 1
               j += 1
               k += 1
           if k == plen-1:
               print("Pattern found at index ", i)
       matches = 0



txt = "THIS IS A TEST TEXT"
ptat = "TEST"
naivePatternSearch(ptat, txt)

# Remember:
# Naive pattern searching has a worst case complexity of
# O(m(n-m+1))
