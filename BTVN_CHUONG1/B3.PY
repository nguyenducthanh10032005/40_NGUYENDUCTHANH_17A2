class PS :
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra(self) :
            if (int(tu_so) == tu_so) and (int(mau_so) == mau_so) and (mau_so != 0):


                print('Phân số : {}/{}'.format(int(self.tu_so),int(self.mau_so)))
            else:
                print('Phân số không hợp lệ')

tu_so = int(input("NHập tử số  :"))
mau_so = int(input("Nhập mẫu số :"))
obj = PS(tu_so,mau_so)
obj.kiem_tra()
