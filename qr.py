import json
import qrcode

def generate_qr(data, filename):
    """
    Generates a QR code for the given data and saves it to the specified file.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Read data from JSON file
with open('cartridges.json', 'r') as f:
    cartridges = json.load(f)

# Generate QR codes for each item in the file
for cartridge in cartridges:
    data = json.dumps(cartridge)
    filename = f"{cartridge['cartridge_id']}.png"
    generate_qr(data, filename)
