def Geedy(ds,n):
    count = 0 
    for i in range(len(ds)):
        while n>=ds[i] :
            count += 1 
            n = n - ds[i]
    return count
    
ds = [25,10,5,1]
print(Geedy(ds,67))
#output = 6
