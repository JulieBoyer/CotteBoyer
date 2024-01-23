import sys
import time
    
def insert_word(words, i, j):

    # Store word to move
    w = words[i]
    
    # Switch all words from j to i - 1 position to the right
    for k in range(i, j, -1):
        words[k] = words[k-1]
        
    # Put word to move at position j
    words[j] = w
    
# Read standard input
words = sys.stdin.readlines()

# Remove new line characters
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

# Record start time
start_time = time.perf_counter()

# Loop on all words
for i in range(1, len(words)):

    # Find right place of insertion for current word
    j = i - 1
    while words[j] > words[i] and j >= 0:
        j -= 1

    # Move current word to the right place, shifting all words in between to the
    # right
    if j + 1 != i:
        insert_word(words, i, j + 1)

# Print sorted words
print("\n".join(words))

# Print elapsed time
sys.stderr.write("Elasped time: %f s\n" % (time.perf_counter() - start_time))
