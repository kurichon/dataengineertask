# Task 1: Event Type Classification from Text Files

## Purpose

This script processes a series of text files containing timestamped data and classifies each event based on a metadata file that defines event types with start and end times. The classified event data is saved to an Excel file for further analysis.

## How to Use

### Prerequisites
1. Install the required libraries using `pip`:
    ```bash
    pip install pandas openpyxl
    ```

2. Place the following files in a directory called `./Task1/`:
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

