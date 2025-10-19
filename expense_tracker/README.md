# Expense Tracker

A minimal, file-based expense tracker written in Python. It stores expenses in `expenses.json` in the same directory and provides simple CLI commands to add and view expenses.

## Files

- `expense_tracker.py` - Main script (CLI).
- `expenses.json` - Data file created automatically after the first expense is added. A sample structure is shown below.

## Requirements

- Python 3.7+ (tested on 3.8+)

## Quick start (PowerShell)

1. Open PowerShell and change to the project directory:

```powershell
cd C:\Users\Kunal\Desktop\expense_tracker
```

2. Run the script:

```powershell
python .\expense_tracker.py
```

3. Use the menu to add or view expenses.

## Data format (`expenses.json`)

The file is a JSON array of expense objects. Each object has the following keys:

- `amount` (number) - expense amount in USD
- `category` (string) - category name, e.g. `food`, `travel`
- `note` (string) - optional note
- `date` (string) - ISO date (YYYY-MM-DD)

Example `expenses.json` content:

```json
[
    {
        "amount": 12.5,
        "category": "food",
        "note": "Lunch",
        "date": "2025-10-19"
    },
    {
        "amount": 35,
        "category": "travel",
        "note": "Bus fare",
        "date": "2025-10-18"
    }
]
```

## Troubleshooting

- If `expenses.json` becomes corrupted, you can remove or rename it; the script will recreate an empty list on next run.
- Ensure you run the script from the directory containing `expense_tracker.py` so it can find `expenses.json`.

## Next steps (optional)

- Add filtering by date or category.
- Add CSV export or import.
- Add tests and input validation.

---

If you'd like, I can also add a sample `expenses.json` file or enhance `expense_tracker.py` with argument parsing. Which would you prefer next?