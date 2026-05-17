#!/usr/bin/env python3
"""
wifi_qr.py -- Generate WiFi QR codes for Android
Usage: python3 wifi_qr.py --ssid "Network" --password "pass" [--security WPA] [--output qr.png]
Android 10+ can scan these QR codes to auto-connect to WiFi
"""
import argparse, sys

try: import qrcode
except ImportError:
    print("pip install qrcode[pil]"); sys.exit(1)

def wifi_string(ssid, password, security="WPA", hidden=False):
    """Generate WiFi QR code string"""
    # Format: WIFI:T:<security>;S:<ssid>;P:<password>;H:<hidden>;;
    sec_map = {"WEP": "WEP", "WPA": "WPA", "WPA2": "WPA", "WPA3": "WPA", "open": "nopass"}
    t = sec_map.get(security, "WPA")
    
    # Escape special chars
    ssid_esc = ssid.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\"", "\\\"")
    pass_esc = password.replace("\\", "\\\\").replace(";", "\\;") if password else ""
    
    s = f"WIFI:T:{t};S:{ssid_esc};"
    if password:
        s += f"P:{pass_esc};"
    if hidden:
        s += "H:true;"
    s += ";;"
    return s

def nfc_tag(ssid, password, security="WPA"):
    """Generate NFC tag NDEF format"""
    wifi_str = wifi_string(ssid, password, security)
    # Simplified NDEF record format (actual NFC requires more complex encoding)
    return f"WIFI:{wifi_str}"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ssid", required=True, help="Network name")
    parser.add_argument("--password", default="", help="WiFi password (leave blank for open)")
    parser.add_argument("--security", default="WPA", choices=["WEP","WPA","WPA2","WPA3","open"])
    parser.add_argument("--hidden", action="store_true", help="Hidden network")
    parser.add_argument("--output", default="wifi.png", help="Output PNG file")
    parser.add_argument("--nfc", action="store_true", help="Show NFC tag format instead")
    args = parser.parse_args()

    if args.nfc:
        nfc = nfc_tag(args.ssid, args.password, args.security)
        print(f"NFC tag content:\n{nfc}")
        return

    # Generate QR code
    wifi_str = wifi_string(args.ssid, args.password, args.security, args.hidden)
    print(f"WiFi QR string:\n{wifi_str}\n")
    
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(wifi_str)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(args.output)
    print(f"✅ QR code saved to: {args.output}")
    print(f"Share: scan with Android device or AirDroid")

if __name__ == "__main__":
    main()
