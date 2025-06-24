# 🛰️ ISS Overhead Notifier

This project tracks the International Space Station (ISS) and sends you an email notification **when the ISS is overhead your location** and it's currently dark (so it's visible in the sky). A perfect tool for space enthusiasts who want to spot the ISS in real time!

## Features

- Tracks the ISS position using open API.
- Detects whether it's night time at your location.
- Sends an email notification when:
  - The ISS is overhead (within a certain latitude/longitude range).
  - It's currently night time (so the ISS is visible).

## Requirements

- Python 3.6+
- `smtplib` (built-in)
- `requests`
- Email account (SMTP-enabled, e.g., Gmail)

Install dependencies:
```bash
pip install requests
