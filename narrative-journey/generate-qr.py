#!/usr/bin/env python3
"""
QR Code Generator for Narrative Journey Web App
Generates a QR code for easy mobile access
"""

import sys

def generate_qr_terminal(url):
    """Generate QR code in terminal (requires qrcode package)"""
    try:
        import qrcode
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make()
        qr.print_ascii(invert=True)
        print(f"\nQR Code for: {url}")
    except ImportError:
        print("Error: qrcode package not installed")
        print("Install it with: pip install qrcode[pil]")
        return False
    return True

def generate_qr_image(url, filename='qr-code.png'):
    """Generate QR code as image file (requires qrcode and PIL)"""
    try:
        import qrcode
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        print(f"QR code saved to: {filename}")
        return True
    except ImportError:
        print("Error: qrcode package not installed")
        print("Install it with: pip install qrcode[pil]")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-qr.py <URL> [output_filename]")
        print("\nExample:")
        print("  python generate-qr.py https://your-app.netlify.app")
        print("  python generate-qr.py http://192.168.1.5:8000 qr-local.png")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else 'qr-code.png'

    print("Generating QR Code...")
    print("=" * 50)

    # Generate terminal version
    print("\nTerminal QR Code:")
    generate_qr_terminal(url)

    # Generate image file
    print("\nImage File:")
    generate_qr_image(url, filename)

    print("\n" + "=" * 50)
    print("Done! Share this QR code with participants.")
    print("\nTips:")
    print("- Test by scanning with your phone")
    print("- Ensure phones are on same network (for local URLs)")
    print("- Print at least 2x2 inches for best scanning")

if __name__ == "__main__":
    main()
