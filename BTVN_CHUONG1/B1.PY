class hinh_chu_nhat :
    def __init__(self, chieu_dai =0, chieu_rong = 0):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    def dien_tich(self):
        return ( self.chieu_dai * self.chieu_rong)
    def nhap_du_lieu(self):
        self.chieu_dai = float(input("Nhập chiều dài :"))
        self.chieu_rong = float(input("Nhập chiều rộng :"))
    def thong_tin(self):
        CHU_VI = self.chu_vi()
        DIEN_TICH = self.dien_tich()
        print(f"Hình chữ nhật có chiều dài: {self.chieu_dai}, chiều rộng: {self.chieu_rong}")
        print(f"Chu vi: {CHU_VI}")
        print(f"Diện tích: {DIEN_TICH}")

hcn = hinh_chu_nhat()
hcn.nhap_du_lieu()
hcn.thong_tin()
