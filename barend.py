import barcode
from barcode import Code128
from barcode.writer import ImageWriter

def generate_barcode(data, filename):
    # Generate Code 128 barcode
    code128 = Code128(data, writer=ImageWriter())

    # Save the barcode image
    filename_with_extension = f"{filename}"
    code128.save(filename_with_extension)

if __name__ == "__main__":
    # Define variables
    fac_num = "1608"    # Facture number (4 digits)
    lot = "ebi233"      # Lot number (6 characters)
    exp_date = "0124"   # Expiry date (4 digits)
    price = "2343248"  # Price (6 digits)

    # Concatenate variables into a single string
    barcode_data = fac_num + lot + exp_date + price

    # Generate barcode image
    filename = "product_barcode3"
    generate_barcode(barcode_data, filename)

    print(f"Barcode generated successfully: {filename}")
