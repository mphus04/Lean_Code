class Kter:
    def __init__(self,ho,ten) :
        self.ho = ho 
        self.ten = ten
        #self.email =  self.ho + '-' + self.ten +'@email.com'
    @property # biến phương thức thành thuộc tính không cần phải () : gọi là getter
    def email(self):
        return self.ho + '-' + self.ten +'@email.com'
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho,self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self,ten_moi):
        ho_moi , ten_moi = ten_moi.split(' ')  
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print("da xoa")
kter_A = Kter("Nguyen","Phu")

kter_A.ho = 'phu'
kter_A.ten = 'nguyen'

print(kter_A.ten)
print(kter_A.ho)
print(kter_A.email)
print(kter_A.ho_va_ten)

#setter : gán lại họ tên 
kter_A.ho_va_ten = "Kha Banh"
print(kter_A.ho_va_ten)
print(kter_A.ho)

#deleter
del kter_A.ho_va_ten
print(kter_A.ho_va_ten)