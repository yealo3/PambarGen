
from barcode import Code128 # type: ignore
from barcode.writer import ImageWriter # type: ignore

def pambcgen(data, fish):
    code128 = Code128(data, writer=ImageWriter())
    filexten = f"{fish}"
    code128.save(filexten)

if __name__ == "__main__":
    fac_num = "2708"    
    lot = "ebi233"      
    exp_date = "0124" 
    price = "2343248"  
    Bc_data = fac_num + lot + exp_date + price
    fish = "med_barcode3"
    pambcgen(Bc_data, fish)

    print(f"Barcode generated successfully: {fish}")
