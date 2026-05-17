# 📡 Android WiFi Share Generator

Generate QR codes and NFC tag content to easily share WiFi networks.

## Usage

```bash
# Web version
open index.html

# CLI version
python3 wifi_qr.py --ssid "MyNetwork" --password "pass123" --security WPA --output wifi.png
```

## Features

- ✅ Generate WiFi QR codes (scanned by Android 10+)
- ✅ NFC tag format (pre-formatted for NFC writer apps)
- ✅ WEP, WPA, WPA2, WPA3 support
- ✅ Hidden SSID support
