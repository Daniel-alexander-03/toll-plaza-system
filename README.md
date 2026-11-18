# Toll Plaza Management System

A basic command-line Python project that simulates a toll plaza. It records vehicles passing through the toll, calculates the toll fee based on vehicle type, and keeps a running total of collections.

## Features

- Register vehicles passing through the toll plaza
- Calculate toll fees based on vehicle type
- Display a summary of vehicles and total collection
- Simple text-based menu for interaction

## Requirements

- Python 3.8 or higher
- No external libraries required

## Getting Started

1. Clone or download the project folder.
2. Open a terminal in the project folder.
3. Run the program:

```bash
python toll_plaza.py
```

## Usage

When the program starts, you will see a menu:

```
1. Record a vehicle
2. View toll rates
3. View collection summary
4. Exit
```

- **Record a vehicle:** Enter the vehicle number and select its type. The program calculates and displays the toll fee.
- **View toll rates:** Shows the fee for each vehicle type.
- **View collection summary:** Shows the number of vehicles processed and the total amount collected.
- **Exit:** Closes the program.

## Toll Rates

| Vehicle Type | Fee (₹) |
|--------------|---------|
| Car / Jeep   | 50      |
| Bus / Truck  | 150     |
| Two-wheeler  | 20      |

> Update these values in the source code to match your local rates.

## Project Structure

```
toll-plaza/
├── toll_plaza.py   # Main program
└── README.md       # Project documentation
```

## How It Works

- Vehicle records are stored in a list while the program runs.
- Each fee is looked up from a dictionary that maps vehicle types to rates.
- The total collection is updated every time a vehicle is recorded.

> Data is not saved between runs. Adding file storage (for example, a CSV file) is a good next step.

## Possible Improvements

- Save records to a file or database
- Add input validation for vehicle numbers
- Add monthly or daily reports
- Add a discount for frequent users or passes

## Author

Aatif Vakas Khatri

## License

This project is for educational purposes.
