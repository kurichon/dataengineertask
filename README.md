
# Prerequisites
1. Install the required libraries using `pip`:
    ```bash
    pip install pandas openpyxl
    ```
# Task 1: Event Type Classification from Text Files

## Purpose

This script processes a series of text files containing timestamped data and classifies each event based on a metadata file that defines event types with start and end times. The classified event data is saved to an Excel file for further analysis.


1. Place the following files in a directory called `./Task1/`:
    - `metadata.xlsx`: Contains the metadata that defines the start and end times for events.
    - Multiple `.txt` files: Contain timestamped data that will be classified based on the metadata.

### Script Flow
1. The script loads the metadata from the `metadata.xlsx` file. The metadata includes:
    - `StartTime`: The start time of the event.
    - `EndTime`: The end time of the event.
    - `EventType`: The event classification.
    
2. It processes each `.txt` file in the `./Task1/` folder and reads the data, which should include a `Timestamp` column and other columns representing data for that event.

3. The script compares the timestamp of each row with the start and end times from the metadata to classify the event type.

4. The classified data is then saved into an Excel file `classified_events.xlsx`.

## How to Test

### Data Setup
1. Place your metadata in the `metadata.xlsx` file in the `./Task1/` folder. The metadata should be structured with columns:
   - `StartTime`: The event start time.
   - `EndTime`: The event end time.
   - `EventType`: The classification for that event.

2. Place your `.txt` files in the `./Task1/` folder. The data in these files should have the following structure:
    - `Timestamp`: The timestamp in the format `YYYY-DD-MM-DD-hh:mm:ss:fff`.
    - Other columns such as `x`, `y`, and `z` which will be processed for event classification.

### Testing Process
1. Ensure the necessary packages (`pandas`, `openpyxl`) are installed.
2. Run the script to classify the data and save it in an Excel file.

```bash
python Task1.py
```

# Task 2: Data Integrity Check and Missing Data Detection
1. 
2. Load Data
- The dataset is expected to be in the `./Task2/` folder with the filename `data.xlsx`. The dataset should contain columns named:
  - `Index`
  - `Timestamp`
  - `Incremental_Index`
  - `Acceleration_X`
  - `Acceleration_Y`
  - `Acceleration_Z`
## Purpose
This script processes a dataset to check for missing data points based on timestamps and incremental index values. The key objectives are to:
- **Identify timestamps** with fewer data points than the specified fault tolerance.
- **Detect gaps in the incremental index** (0-255) sequence.
- **Generate a report** detailing missing data points for each identified timestamp.
## Parameters
- **Fault Tolerance**: Defined by fault_tolerance (default: 20). Any timestamp with fewer data points than this threshold is flagged for missing data.
- **Incremental Index Range**: Set from 0 to 255. The script checks for gaps in this range and flags missing index values.
## Run the Script
Execute the script by running:

 ```bash
 python Task2.py
 ```
## Output
The script will print reports detailing:

- Timestamps with missing data (if consecutive data points fall below the fault tolerance threshold).
- Gaps in the incremental index sequence, indicating data loss.
## Example Output
```bash
Missing data detected from index 105, Timestamp at 2023-11-06 12:45:10 only has 18 data points.
Data loss found at index 210, total data loss: 4
```
