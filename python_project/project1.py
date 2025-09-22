'''
THUẬT TOÁN CHUYỂN ĐỔI ĐỘ "C " THÀNH ĐỘ "F"
'''

def ConvertTemp():
    while True: # vòng lặp 
        cTemp = input("hãy nhập độ C vào")
        if cTemp:
            #print(type(cTemp))
        
            cTemp = float(cTemp) # gán type trước công thức
            fTemp = round(9*cTemp/5 +32,1)
            
            print(f"vậy nhiệt độ F là {fTemp}")
            break # nếu đúng thì dừng 
        
        else:
            print(f"bạn đã để trống nhiệt độ")
            continue # nếu sai thì tiếp tục vòng lặp
       
        

        
def main():
    ConvertTemp()

    
if __name__ == "__main__":
    ConvertTemp() # gọi trong hàm "main"  hoặc hàm phụ là "ConvertTemp" để cho funcion chạy