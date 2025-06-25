# Workout Logger Proxy

A simple Flask-based web proxy to forward workout data to a Google Apps Script webhook for logging into Google Sheets.

## Usage

POST workout JSON data to `/log-workout` to have it forwarded to your Google Sheet.

## Example

```json
[
  {
    "date": "2025-06-25",
    "exercise": "Bench Press",
    "set": 1,
    "reps": 10,
    "weight": 60,
    "notes": "Felt strong"
  }
]
