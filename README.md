### README for Traffic_data_analyser

---

# Traffic_data_analyser

TrafficFlow Analyzer is a Python-based application designed to process traffic data from CSV files, generate insightful statistics, and visualize vehicle frequency using histograms. This tool is particularly useful for analyzing traffic patterns at specific junctions and identifying key metrics such as speed violations, electric vehicle counts, and weather impacts.

---

## Features

- Processes CSV files containing traffic data.
- Calculates various traffic statistics:
  - Total vehicles, trucks, electric vehicles, and two-wheeled vehicles.
  - Percentage of trucks and scooters in the traffic data.
  - Speed limit violations.
  - Vehicles not turning and buses heading north.
  - Rain hours impacting traffic.
- Generates a histogram to visualize hourly traffic frequency for two junctions.
- Saves results to a text file for future reference.

---

## Requirements

- Python 3.x
- `graphics.py` module for graphical output

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/saugat2003/traffic_data_analyser.git
   cd traffic_data_analyser
   ```
2. Install Python dependencies (if applicable).

---

## Usage

1. Prepare a CSV file with the following columns:
   ```
   Junction Name, Date, Time, Travel In, Travel Out, Weather, Speed Limit, Vehicle Speed, Vehicle Type, Electric/Hybrid
   ```
2. Run the program:
   ```bash
   python trafficflow_analyzer.py
   ```
3. Enter the CSV file name when prompted.

4. View the results in the terminal, saved to `results.txt`, or as a histogram visualization.

---

## Example Output

### Terminal Results
```
Data file selected is traffic_data.csv
The total number of vehicles recorded for this date is 500
The total number of trucks recorded for this date is 120
...
The total number of hours of rain for this date is 3
```

### Histogram
A graphical window will display a bar chart comparing traffic volume at two junctions by the hour.

---

## File Structure

- `trafficflow_analyzer.py`: Main script.
- `results.txt`: File to store analysis results.
- Example CSV files: Provide sample traffic datasets (if included).

---

## Future Enhancements

- Add support for more junctions.
- Improve data visualization with advanced graphing libraries.
- Implement a web-based interface for easier file uploads and result viewing.

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.

---

## Contributions

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

--- 

Enjoy using TrafficFlow Analyzer! 🚦
