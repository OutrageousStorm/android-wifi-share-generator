#!/bin/bash
# share_cli.sh -- CLI tool to share WiFi details
# Usage: ./share_cli.sh

read -p "WiFi network name (SSID): " ssid
read -sp "WiFi password: " pass
echo
read -p "Security type (WPA/WEP/nopass) [WPA]: " security
security=${security:-WPA}

python3 generate.py --ssid "$ssid" --pass "$pass" --security "$security" --output "wifi_${ssid}.png"
echo "📲 Scan this QR code to connect to $ssid"
