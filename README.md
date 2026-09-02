# Aspie Bootcamp Finance Manager

A simple command-line personal finance manager built in Python. It lets you record income and expenses with automatic timestamps, view your transaction history, and see a summary of your total income, expenses, and net balance.

## Requirements

- Python 3.12
- No external libraries required (uses only the standard library)

## How to Run

```bash
python finance_manager.py
```

## How to Use

When the program starts, you'll see a menu with the following options:

| Option | Action |
|--------|--------|
| `1` | Add an expense |
| `2` | Add an income |
| `3` | View finance report (all transactions) |
| `4` | View summary statistics |
| `5` | Modify a transaction |
| `6` | Delete a transaction |
| `q` | Quit the application |

**Adding a transaction (1 or 2):**
1. Enter the option number and press Enter.
2. Enter a name/description for the transaction (cannot be blank).
3. Enter the amount (must be a valid number greater than 0).
4. The time of entry is recorded automatically, and you're returned to the main menu.

Repeat this process for each transaction you want to log.

**Viewing your data:**
- Option `3` prints every recorded transaction, including its name, amount, and timestamp.
- Option `4` calculates and displays your total expenses, total income, and net balance.

**Refining your data**
- Option `5` allows the user to change their entries.
- Option `6` allows the user to delete unwanted entries.

## Features (Current — v0.3)

- Tracks income and expenses with an automatically recorded timestamp for each entry
- Input validation:
  - Names cannot be left blank
  - Amounts must be valid numbers greater than 0
- Transactions are stored as structured records (name, amount, and time), rather than plain text, making the data easier to process and extend
- View all transactions in a simple report
- View a summary of total income, total expenses, and net balance, formatted to two decimal places
- Modifies entries
- deletes entries

## Roadmap — Planned for a Future Update

The following features are planned but not yet implemented:

- **Add Category Totals** — Add an option to view the

## Version History

- **v0.1** — Initial release. Basic add/view/summary functionality using plain-text transaction strings.
- **v0.2** — Added input validation, switched to structured (dictionary-based) transaction records, and improved summary formatting.
- **v0.3** — Made Transaction summaries prettier, added the ability to delete entries and modify entries.
- **v0.4** — Added Categories in order to identify the aspects that the cash flow moves, or track the amount spent on certain accounts.

## Author

Ryan Sfiligoi
