class SieuNhan:
    sucmanh = 50
    def __init__(self,para_ten,para_vukhi,para_mausac):
        self.ten = "sieu nhan " + para_ten
        self.vukhi = para_vukhi
        self.mausac = para_mausac
    # cap nhat toan bo class 
    @classmethod
    def cap_nhat_suc_manh(cls,smanh):
        cls.sucmanh = smanh 
    @classmethod   
    def from_string(cls, s) : # thw những phương thức như thế này có tên là from
        lst = s.split('_')
        new_lst = [str.strip() for str in lst]
        ten,vu_khi,mau_sac = new_lst
        return cls(ten,vu_khi,mau_sac) 
        
    
sieu_nhan_A = SieuNhan("decade", "kiem","do")
sieu_nhan_A.sucmanh = 40 
sieu_nhan_b = SieuNhan("BUILD", "kiem","do/xanh")
sieu_nhan_b.sucmanh = 30 # cập nhật cho 1 đối tượng riêng  thôi 
# sieu_nhan_A.cap_nhat_suc_manh(40) # cập nhật cho toàn bộ class  
sieu_nhan_A = SieuNhan.from_string('decade _ kiem _ do')
print(sieu_nhan_A.ten)
print(sieu_nhan_A.sucmanh)

print(sieu_nhan_b.ten)
print(sieu_nhan_b.sucmanh)
# print(SieuNhan.sucmanh)

print(sieu_nhan_A.__dict__)