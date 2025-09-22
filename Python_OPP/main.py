# from animation import start_animation 


class IdolGioiTre:
    # inheritance : tinh ke thua 
    def __init__(self,name,age,appearance):
        self.name = name
        self.age = age
        self.__appearance = appearance # Set private variable 
    
    # Encapsulation
    def GetAppearance(self): # hàm dùng để gọi từ bên ngoài
        return self.__appearance
    
    def SetAppearance(self ,value): # chỉnh sửa attribute
        self.__appearance = value
        
class KhaBanh(IdolGioiTre):

    def __init__(self, name, age, appearance,location): # them para
        super().__init__(name, age, appearance)# giu lai para tren class
        self.location = location
    def Livestream(self):
        # start_animation()
        pass
    def SignatureQuote(self):
        print("Ao that day")
        
class TienBip(IdolGioiTre):
    def LiveStream(self):
        pass

    def SignatureQuote(self):
        print('Con cai nit')
        
KBanh = KhaBanh("Ngo Ba Kha", 39,"idol",'trong tu')
TBip = TienBip("vo tien",24,"idol")

print(KBanh.name)
KBanh.SignatureQuote()
# print(KBanh.__appearance) : như này sẽ bị lỗi vì attribute đã để ở private
print(KBanh.GetAppearance())
print(KBanh.Livestream())

print(TBip.name)
TBip.SignatureQuote()