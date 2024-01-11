import heapq

# Create an empty list
heap = []

# Insert elements into the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

# The heap now contains [1, 3, 2]

# Get the smallest element
smallest = heapq.heappop(heap)  # This removes and returns the smallest element
print(smallest)  # Output: 1

# The heap now contains [2, 3]

# You can also convert a regular list into a heap in-place
my_list = [5, 4, 6, 3, 7, 2]
heapq.heapify(my_list)  # Convert my_list into a heap
print(my_list)  # Output: [2, 3, 4, 5, 7, 6]

# Get the smallest element again
smallest = heapq.heappop(my_list)
print(smallest)  # Output: 2

# The heap (my_list) now contains [3, 5, 4, 6, 7]

# You can also find the smallest element without removing it
smallest = heapq.heappop(my_list)
print(smallest)  # Output: 3
print(my_list)  # Output: [4, 5, 7, 6]

# Other heap operations are available, such as heappushpop, heapreplace, and nlargest
