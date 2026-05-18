#!/usr/bin/env python3
"""
generate.py -- Generate WiFi QR codes and share strings
Usage: python3 generate.py --ssid "MyNetwork" --pass "password123" [--security WPA]
"""
import argparse, sys

try:
    import qrcode
except ImportError:
    print("Install: pip install qrcode[pil]")
    sys.exit(1)

def wifi_string(ssid, password, security="WPA", hidden=False):
    """Generate WiFi share string (Android format)"""
    # WIFI:T:WPA;S:SSID;P:PASSWORD;H:hidden;;
    h = "true" if hidden else "false"
    return f"WIFI:T:{security};S:{ssid};P:{password};H:{h};;"

def generate_qr(text, output_file=None):
    """Generate QR code from WiFi string"""
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    
    if output_file:
        img.save(output_file)
        print(f"✓ Saved to {output_file}")
    else:
        img.show()
    return img

def main():
    parser = argparse.ArgumentParser(description="Generate WiFi QR codes")
    parser.add_argument("--ssid", required=True, help="WiFi network name")
    parser.add_argument("--pass", dest="password", required=True, help="WiFi password")
    parser.add_argument("--security", default="WPA", choices=["WPA", "WEP", "nopass"])
    parser.add_argument("--hidden", action="store_true", help="Hidden SSID")
    parser.add_argument("--output", help="Save QR code to file (PNG)")
    args = parser.parse_args()

    wifi_str = wifi_string(args.ssid, args.password, args.security, args.hidden)
    print(f"\n📱 WiFi Share String:\n{wifi_str}\n")

    if args.output:
        generate_qr(wifi_str, args.output)
    else:
        print("(Pass --output to save QR code to file)")
        # Show string so it can be scanned by phone camera
        print(f"Share this with anyone who can scan QR codes!")

if __name__ == "__main__":
    main()
