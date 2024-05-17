from barcode import Code128 # type: ignore
from barcode.writer import ImageWriter # type: ignore

def pambcgen(infos, fish):
    code128 = Code128(infos, writer=ImageWriter())
    thepath = f"{fish}"
    code128.save(thepath)
