import heapq

# Example of a min heap
min_heap = [3, 1, 4, 1, 5, 9, 2, 6]

# Convert the list into a heap
heapq.heapify(min_heap)
print("Min Heap:", min_heap)

# Push an element into the heap
heapq.heappush(min_heap, 0)
heapq.heappush(min_heap, 28)
print("Heap after pushing 0:", min_heap)

# Pop and print the smallest element
min_element = heapq.heappop(min_heap)
print("Smallest element popped:", min_element)
print("Heap after popping the smallest element:", min_heap)
