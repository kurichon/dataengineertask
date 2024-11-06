# > read xlsx file
# > check increment index
# > fault tolerance is set to 20
# > check time stamp (any timestamps that has less than 20 data points are considered to have missing data)
# > determine index, and number of missing data.
# > print data loss report
import os
import pandas as pd

Task2_folder = "./Task2/"
data_file = "data.xlsx"
columns_datafile = ['Index','Timestamp','Incremental_Index','Acceleration_X','Acceleration_Y','Acceleration_Z']

# threshold of the number of data to be considered as timestamps with missing data points
fault_tolerance = 20
#0-255 incremental index
incremental_index_max = 255

def load_data():
    return pd.read_excel(Task2_folder + data_file)


def find_missing_data(df_to_check):
    missing_data = [] #list to store missing data
    consecutive_timestamp_count = 1 #counter to count batch size based on timestamp


    for i in range(len(df_to_check) - 1):
        current_row = df_to_check.iloc[i]
        next_row = df_to_check.iloc[i+1]

        current_timestamp = current_row['Timestamp']
        next_timestamp = next_row['Timestamp']
        # Check if timestamps match

        if current_timestamp == next_timestamp:
            consecutive_timestamp_count += 1
        else:
            # If the timestamp doesn't match, check fault tolerance
            if consecutive_timestamp_count < fault_tolerance:
                #total_missing_data = batch_size - consecutive_timestamp_count
                print(f"Missing data detected from index {current_row['Index']}, Timestamp at {current_row['Timestamp']} only has :{consecutive_timestamp_count} data points.")
            #no missing data, reset
            consecutive_timestamp_count = 1


        #Incremental Index checking
        current_value = current_row['Incremental_Index']
        next_value = next_row['Incremental_Index']

        # Calculate the gap between current and next
        if next_value > current_value:
            gap = next_value - current_value - 1
        else:  # Account for wraparound from 255 to 0
            gap = (incremental_index_max - current_value) + next_value

        if gap !=0: # has missing data
            # Add missing values to the list
            missing_data.extend([(current_value + j + 1) % (incremental_index_max + 1) for j in range(gap)])
            print(f"Data loss found at index {current_row['Index']}, total data loss: {len(missing_data)}")
            missing_data = []


def main():
    # Load data
    df = load_data()
    find_missing_data(df)

if __name__ == "__main__":
    main()