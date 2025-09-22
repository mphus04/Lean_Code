def plus_minus(chuoi):
    arr = {"am": 0,"duong": 0,"zero":0 }
    for x in chuoi: 
        if x > 0 and x < 100:
            arr["duong"] += 1
        elif x < 0 and x >-100:
            arr["am"] += 1
        elif x == 0 :
            arr["zero"] += 1 
    for y in arr.values():
        print("{:.5f}".format(y/len(chuoi)))
        
arr = [ 1,1,0,-1,-1]
plus_minus(arr)