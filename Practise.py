import os
import pdf2image
from PIL import Image
from pdf2image import convert_from_path


class Pic_Pdf(object):
    def __init__(self, file_path):
        self.file_path = file_path.split("\\")
        self.file_name = self.file_path[-1]
        self.file_ext = self.file_name.split(".")[-1]
        self.file_path = os.path.join(*self.file_path)

    def __repr__(self):
        return f"{self.file_name} converted...."

    def main(self):
        if self.file_ext == "pdf":
            pages = convert_from_path(self.file_path, 500)
            for page in pages:
                page.save(self.file_path.replace(f"{self.file_ext}", ".pdf"))


if __name__ == '__main__':
    print("Drag and drop file heere")
    file = input(r" >>")
    pdf_tool = Pic_Pdf(file)
    print((pdf_tool))
