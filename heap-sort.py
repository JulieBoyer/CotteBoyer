import sys
import time
    
def heapify(a, heap_size, i):
    """Converts a sub-array into a max-heap."""
    
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    i_max = i # Index of the max between numbers

    # Left child exists
    if left_child < heap_size:
        
        # Left child is bigger than current parent
        if a[left_child] > a[i_max]:
            i_max = left_child
            
        # Right child exists and is bigger
        if right_child < heap_size and a[right_child] > a[i_max]:
            i_max = right_child
            
        # Parent is not the max ==> swap
        if i_max != i:
            
            # Swap
            a[i], a[i_max] = a[i_max], a[i]
            
            # Update child subtree (child number has changed)
            heapify(a, heap_size, i_max)

# Read standard input
words = sys.stdin.readlines()

# Remove new line characters
words = [w.rstrip() for w in words]

# Remove empty words
words = list(filter(lambda s: s != '', words))

start_time = time.perf_counter()

# Build max-heap (initialization)
for i in range(len(words) // 2, -1, -1):
    heapify(words, len(words), i)

# Sort: move max to end of list and run max-heap on first part of array
heap_size = len(words)
for i in range(heap_size - 1, 0, -1):
    words[0], words[i] = words[i], words[0]
    heap_size -= 1
    heapify(words, heap_size, 0)

print("\n".join(words))

sys.stderr.write("Elasped time: %f s\n" % (time.perf_counter() - start_time))
