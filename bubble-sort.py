import sys
import time

# Read standard input
words = sys.stdin.readlines()

# Remove new line character
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

# Start time
start_time = time.perf_counter()

# Counter of the number permutations done in one pass
nb_permutations = -1

# Counter for the number of passes
pass_nb = 0

# Loop until no permutations are done
while nb_permutations != 0:
    
    # Count number of passes
    pass_nb += 1
    
    # Reset number of permutations
    nb_permutations = 0
    
    # Review all words
    for i, _ in enumerate(words):
        
        # Should current word be put before previous word?
        if i > 0 and words[i-1] > words[i]:
            
            # Permute current word with previous one
            words[i - 1], words[i] = words[i], words[i - 1]

            # Count number of permutations
            nb_permutations += 1
            
    # Log progress
    if pass_nb % 100 == 0:
        sys.stderr.write(
                "Elasped time at pass %d, with %d permutations done: %f s\n" %
                (pass_nb, nb_permutations, time.perf_counter() - start_time))
    
# Print sorted words
print("\n".join(words))

# Print elapsed time
sys.stderr.write("Elasped time: %f s\n" %
        (time.perf_counter() - start_time))
