import xml.etree.ElementTree as ET

class XMLReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None
    def doc_xmlxml(self):
        tree = ET.parse(self.file_path)
        self.data = tree.getroot()
    def display_data(self):
        if self.data:
            for product in self.data.findall('product'):
                name = product.find('name').text
                price = product.find('price').text
                quantity = product.find('quantity').text
                print(f"Product: {name}, Price: {price}, Quantity: {quantity}")
# Sử dụng lớp XMLReader
path='F:/Bài Tập Chương PYTHON/Bài tập chương 2/baitapchuong2/17A2DHKL/LAB 1/DATA/products.xml'
reader = XMLReader(path)
reader.doc_xmlxml()
reader.display_data()