# Tropical Cyclone Daily Monitor

A Python script that automatically monitors and logs active tropical storms using data from the Joint Typhoon Warning Center (JTWC) via the Tropycal package. The script generates daily reports with detailed information about active tropical cyclones, including their location, intensity, and characteristics.

## Features

- Automatically fetches real-time tropical cyclone data from JTWC
- Generates detailed daily reports with storm information including:
  - Storm name and ID
  - Storm status and category
  - Maximum sustained winds
  - Minimum pressure
  - Current location (latitude/longitude)
- Implements rotating log files for system monitoring
- Creates organized daily data files
- Handles errors gracefully with comprehensive logging

## Project Structure

```
tropycal_daily_tc_monitoring/
├── tropycal_daily_tc_check.py
├── data/                        # Storm data reports
│   └── storm_data_YYYY-MM-DD.txt
└── logs/                       # Rotating log files
    └── storm_monitor.log
```

## Prerequisites

- Python 3.x
- Tropycal package
- Unix-like operating system for crontab scheduling (optional)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/estamos/tropycal-daily.git
cd tropycal-daily
```

2. Install the required package:
```bash
pip install tropycal
```

3. Configure the base directory in the script:
Update the `base_dir` variable in `main()` to match your installation path:
```python
base_dir = "/path/to/your/tropycal_daily_tc_monitoring"
```

## Usage

### Manual Execution

Run the script manually:
```bash
python3 tropycal_daily_tc_check.py
```

### Automated Scheduling with Crontab

To run the script automatically every day at 9:00 AM:

1. Open your crontab configuration:
```bash
crontab -e
```

2. Add the following line (adjust paths according to your setup):
```bash
0 9 * * * /path/to/your/python3 /path/to/your/tropycal_daily_tc_check.py
```

Example configuration:
```bash
0 9 * * * /Users/evangelos/Desktop/my-pyenv/bin/python3 /Users/evangelos/Documents/tropycal_daily_tc_monitoring/tropycal_daily_tc_check.py
```

## Output Format

### Data Files
The script generates daily report files in the `data` directory with the following format:
```
Tropical Storm Report - YYYY-MM-DD
==================================================

Number of active storms: X

Active storms details:
========================================
Storm ID: AL012024
Name: Storm_Name
Status: TROPICAL_STORM
Category: Category_Value
Maximum Sustained Winds (knots): XXX
Minimum Pressure (hPa): XXXX
Location: Lat XX.X°N, Lon XX.X°E
```

### Logging
The script maintains rotating log files in the `logs` directory, with:
- Maximum file size: 1MB
- Backup count: 5 files
- Log format: `timestamp - log_level - message`

## Error Handling

The script includes comprehensive error handling for:
- Network connectivity issues
- Data parsing errors
- File system operations
- Individual storm data retrieval

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Tropycal](https://tropycal.github.io/tropycal/) for providing the tropical weather data interface
- JTWC for the tropical cyclone data

## Support

If you encounter any issues or have questions:
1. Check the log files in the `logs` directory
2. Ensure you have proper internet connectivity
3. Verify your Python environment and dependencies
4. Open an issue in this repository with the relevant log information
