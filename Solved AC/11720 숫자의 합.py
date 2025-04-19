n = int(input())
numlist = list(input()) #string받아서 indexing

#print(n, numlist)
sum = 0
for i in range(n): #for i in numlist:
    sum += int(numlist[i]) #sum += int(i)

print(sum)