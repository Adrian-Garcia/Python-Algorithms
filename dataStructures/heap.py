import heapq 

li = [5, 7, 9, 1, 3] 

heapq.heapify(li)

print ("The created heap is : ",end="") # [1, 3, 9, 7, 5]
print (list(li)) 

heapq._heapify_max(li)
print ("The reversed heap is : ",end="") # [9, 7, 1, 3, 5]
print (list(li))

heapq.heapify(li) # return as min_heap
heapq.heappush(li,4) 

print ("The modified heap after push is : ",end="") # [1, 3, 4, 7, 5, 9]
print (list(li)) 

print ("The popped and smallest element is : ",end="") # 1
print (heapq.heappop(li)) # delete 1 