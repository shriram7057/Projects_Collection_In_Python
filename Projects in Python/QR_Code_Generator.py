# qr_generator.py
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from datetime import datetime
import os

def generate_qr(data, filename=None):
    # Set a default filename with timestamp if none provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"QR_{timestamp}.png"

    # Create QR code with high error correction
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as {filename}")
    return filename

if __name__ == "__main__":
    while True:
        data = input("Enter data for QR code (or type 'exit' to quit): ")
        if data.lower() == "exit":
            print("👋 Goodbye!")
            break
        filename = input("Enter filename (leave blank for auto): ")
        filename = filename.strip() or None
        generate_qr(data, filename)
