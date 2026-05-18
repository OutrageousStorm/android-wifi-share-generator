# Dirty Flash Guide

How to update a custom ROM without losing data or apps.

## What is a dirty flash?

A **dirty flash** means flashing a new ROM version without wiping userdata — you keep your apps, settings, accounts. The alternative is a **clean flash** (wipe everything).

## When to dirty flash
- ✅ Updating to a minor version (e.g., 14.1 → 14.2)
- ✅ Same ROM, same device
- ❌ Major version jumps (Android 12 → 13) — usually requires clean flash
- ❌ Different ROM (Pixel Experience → LineageOS) — must be clean
- ❌ Migration between devices — must be clean

## Steps

### 1. Backup (important!)
```bash
# Via TWRP: Backup → System, Boot, Vendor, Data

# Or ADB
adb backup -apk -shared -all -f backup.ab
```

### 2. Boot to recovery
```bash
adb reboot recovery
```

### 3. Sideload new ROM
```bash
adb sideload rom.zip
# Or in recovery UI: Apply update → From ADB
```

### 4. Flash GApps (if using)
```bash
# Still in TWRP recovery
adb sideload gapps.zip
```

### 5. Reboot
```bash
adb reboot
```

## Troubleshooting

**Bootloop after dirty flash:**
- Boot to recovery, restore backup
- Or format data and clean flash

**Apps crashing after flash:**
- Clear app cache: Settings → Apps → [app] → Storage → Clear cache
- Or reinstall problematic apps

**Magisk lost:**
- Reflash Magisk via recovery

## When to clean flash instead
- Updating across major Android versions (12 → 13)
- Switching between completely different ROMs
- Experiencing persistent crashes or bootloops after dirty flash
- ROM dev recommends it in changelog
