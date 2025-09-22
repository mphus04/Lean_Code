import math
muctieu = math.inf
khonggian = 20
kq_x , kq_y , kq_z = -1 , -1 ,-1
for x in range(khonggian):
    for y in range(khonggian):
        for z in range(khonggian):
            rangbuoc1 = (107*x + 500*y >=5000)
            rangbuoc2 = (107*x +500*y <= 50000)
            rangbuoc3 = (72*x +121*y +65*z >= 2000)
            rangbuoc4 = (72*x +121*y +65*z <= 2500)
            rb = rangbuoc1 and rangbuoc2 and rangbuoc3 and rangbuoc4 
            if rb :
                mt = 0.18*x + 0.23 * y + 0.05*z 
                if mt < muctieu:
                    kq_x = x
                    kq_y = y
                    kq_z = z
                    muctieu = mt
                    
print(kq_x,kq_y,kq_z,muctieu)