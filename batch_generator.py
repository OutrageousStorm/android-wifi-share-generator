#!/usr/bin/env python3
"""
batch_generator.py -- Batch generate WiFi QR codes from a list
Usage: python3 batch_generator.py devices.csv --output qrcodes/
       python3 batch_generator.py networks.txt
"""
import subprocess, os, sys, argparse, csv
from pathlib import Path

def generate_qr(ssid, password, auth='WPA', output_file=None):
    """Generate single WiFi QR using wifi_qr.py"""
    result = subprocess.run(
        ['python3', 'wifi_qr.py', '--ssid', ssid, '--password', password, '--auth', auth] +
        (['--output', output_file] if output_file else []),
        capture_output=True, text=True
    )
    return result.returncode == 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='CSV or TXT file with networks (SSID,Password,Auth)')
    parser.add_argument('--output', default='./generated_qrcodes', help='Output directory')
    parser.add_argument('--auth', default='WPA', help='Default auth type (WPA, WEP, nopass)')
    args = parser.parse_args()

    out = Path(args.output)
    out.mkdir(exist_ok=True)

    with open(args.input_file) as f:
        lines = f.readlines()

    success, fail = 0, 0
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        parts = line.split(',')
        ssid = parts[0].strip()
        password = parts[1].strip() if len(parts) > 1 else ''
        auth = parts[2].strip() if len(parts) > 2 else args.auth

        output_file = out / f"{ssid.replace('/', '_')}.png"
        ok = generate_qr(ssid, password, auth, str(output_file))
        if ok:
            print(f"  ✓ {ssid}")
            success += 1
        else:
            print(f"  ✗ {ssid} — generation failed")
            fail += 1

    print(f"\n✅ Generated: {success}  ❌ Failed: {fail}")
    print(f"Output: {out.resolve()}")

if __name__ == "__main__":
    main()
