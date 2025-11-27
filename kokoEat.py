from math import ceil
def kokoEat(arr, K):
    #code ere
    low = 1
    high = max(arr)
    while(low<=high):
        mid = (low+high)//2
        sum = 0
        for num in arr:
            sum+=ceil(num/mid)
        if(sum<=K):
            high = mid-1
        else:
            low = mid+1
    return low
arr=[3,6,7,11]
K=8
print(kokoEat(arr,K))

