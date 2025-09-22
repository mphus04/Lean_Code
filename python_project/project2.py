'''
project : random password genarater
'''
#Password : abdlsadka-7281
import string
import random

LETTER = string.ascii_letters # mã asci từ a-z chữ in thường và in hoa
NUMBER = string.digits # random số 
PUNCTUATION = string.punctuation # random ký tự đặc biệt

def password_genagater(dai=8): 
    printable = f'{LETTER},{NUMBER},{PUNCTUATION}' # khai báo biến trong list
    printable =list(printable)
    random.shuffle(printable) # hàm trộn lẫn 
    ''' có thể dùng 1 trong 2 đoạn code này'''
    random_password = random.sample(printable, k=dai) # dùng hàm sample nếu muốn dùng nhiều item trong list , mật khẩu tạo ra sẽ không lặp lại
    random_password = [random.choice(printable) for _ in range (dai)] # dùng hàm choice có thể chọn cùng một mục nhiều lần, 
    # nên mật khẩu cuối cùng có thể chứa các ký tự lặp lại (và phải dùng thêm vòng lặp for)
    ''' sau đó thì gom lại các tự trong list'''
    random_password = ''.join(random_password) # cú pháp (''.join) để gộp lại các ký tự 
    return random_password  



def get_password():
    lenght_password = input('hãy nhập độ dài mật khẩu bạn muốn')
    return int(lenght_password)


def main():
    lenght_password = get_password() # cho hàm này chạy trước để lấy độ dài pass
    password = password_genagater(lenght_password) #bỏ biến của hàm độ dài vào tham số của hàm tạo mk 
    '''--> giá trị của  (length_password) sẽ bằng giá trị của (dai) hay bằng k'''
    print(password)

#print()
if __name__ == '__main__':
    main()
    