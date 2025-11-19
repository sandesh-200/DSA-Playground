def pairFinder(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]+arr[j]==target):
                return True,f"There is a pair {arr[i]},{arr[j]} that makes the target sum of {target}"
    return False

        
print(pairFinder([11111,45,67,1,3],4))