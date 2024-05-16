from barcode import Code128
from barcode.writer import ImageWriter

def pambcgen(infos, fish):
    code128 = Code128(infos, writer=ImageWriter())
    thepath = f"{fish}"
    code128.save(thepath)
