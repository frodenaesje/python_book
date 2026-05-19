# filename: heapq_demo.py
# Demonstrerer bruk av heapq-modulen for å lage prioritetskøer

import heapq

# Minheap eksempel
minheap = []
data = [42, 5, 19, 73, 11, 2, 89, 34, 17, 60, 1, 28]
print("Original data:", data)
for element in data:
    heapq.heappush(minheap, element)

print("Minheap:", minheap)
#heapq.heappush(minheap, 2)
#print("Minheap etter å ha lagt til 2:", minheap)

heapq.heappop(minheap)
print("Minheap etter å ha fjernet minste element:", minheap)

while minheap:
    print("Minste element:", heapq.heappop(minheap))

# Maxheap eksempel (ved å bruke negative verdier)
maxheap = []
data = [42, 5, 19, 73, 11, 2, 89, 34, 17, 60, 1, 28]

for element in data:
    heapq.heappush(maxheap, -element)

print("Maxheap (lagret som negative verdier):", maxheap)

while maxheap:
    print("Største element:", -heapq.heappop(maxheap))

# bruk av heapify; konverterer en liste til en heap
data = [42, 5, 19, 73, 11, 2, 89, 34, 17, 60, 1, 28]
heapq.heapify(data)
print("Heapify:", data) # heapify jobber in-place
