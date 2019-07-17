# The Rabin-Karp Algorithm for Pattern Searching
# uses hashing to find patterns in text
# It is O(nm)

# ascii values go up to 255, so use 256 as a large prime number
d = 256

def rk(text, pat, q):
    # q is a prime number for hashing
    M = len(pat)
    N = len(text)
    i = 0
    j = 0

    pHash = 0
    tHash = 0

    hash = 1

    for i in range(0, M-1):
        hash = (hash*d)%q

    # calculate the hash value of the pattern
    # and the window
    for i in range(0, M):
        pHash = (d*pHash + ord(pat[i]))%q
        tHash = (d*tHash + ord(text[i]))%q

    # slide the pattern over text one by one
    for i in range(0, N-M+1):
        # check the hash values of current window of text and pattern
        # if hash values match, the check characters one by one
        if pHash == tHash:
            # check for characters one by one
            for j in range(0, M):
                if text[i+j] != pat[j]:
                    break

            j += 1

            if j == M:
                print("Pattern found at index ", i)

        # Calculate the hash value for the next window
        # Remove leading and trailing digit
        if i < N-M:
            tHash = (d*(tHash-ord(text[i])*hash) + ord(text[i+M]))%q

            if tHash < 0:
                tHash = tHash + q

text = "TEEST AND TEEEST AND TEEEEST"
pat = "EE"
num = 101
rk(text, pat, num)
