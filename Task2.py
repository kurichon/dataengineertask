# > read xlsx file
# > check increment index
# > from data observation batch size is 40
# > check time stamp (check if there is  40 data per batch)
# > determine index, and number of missing data.
# > print data loss report
# > make a copy to file

import os
import pandas as pd

Task2_folder = "./Task2/"
data_file = "data.xlsx"
columns_datafile = ['Index','Timestamp','Incremental_Index','Acceleration_X','Acceleration_Y','Acceleration_Z']
# Output file for classified events
output_file = 'missing_data.csv'
worksheet_name = "Sheet1"
#timestamp format YYYY-DD-MM-DD-hh:mm:ss:fff
batch_size = 40
incremental_index_max = 255

#def get_metadata_rows(df):
#    rows = df[columns_datafile].values.tolist()
#    return rows

def load_data():
    return pd.read_excel(Task2_folder + data_file)




def find_missing_data(df_to_check):
    missing_data = []
    for i in range(len(df_to_check) - 1):
        current_row = df_to_check.iloc[i]
        next_row = df_to_check.iloc[i+1]

        current_value = current_row['Incremental_Index']
        next_value = next_row['Incremental_Index']

        current_timestamp = current_row['Timestamp']
        next_timestamp = next_row['Timestamp']

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

    # if start_time <= timestamp <= end_time:
    #    return "Within Range Event"
    # else:
    #    return "Out of Range Event"

    # check next row incremental index

    #count batch

def test_data_per_row(df_to_process,metadata_rows):
    #df_timestamp = pd.Dataframe()
    #print(df[0].iloc[:,0].apply(lambda x: format_timestamp(parse_timestamp(x))))

    df_timestamp = pd.DataFrame(columns=['Timestamp'])
    #Convert to date time (pd.to_datetime), then use dt.strftime to format to match metadata format, and x[:-3] to reduce floating point precision to 3 digits
    df_timestamp['Timestamp'] =df_to_process.iloc[:, 0].apply(lambda x: pd.to_datetime(x,format='%Y-%m-%d-%H:%M:%S:%f'))
    df_timestamp['Timestamp'] = df_timestamp['Timestamp'].dt.strftime('%H:%M:%S:%f').apply(lambda x: x[:-3])
    df_to_process['EventType'] = df_timestamp['Timestamp'].apply(lambda x:classify_event(x,metadata_rows))
    return df_to_process
    #print(df_timestamp)
    #df_to_process.to_excel(output_file,index=False)

#def get_data_per_row(metadata_rows):
#    filepath = []
#    df_with_events = []
#    for filename in os.listdir(Task1_folder):
#        # Only process text files
#        if filename.endswith('.txt'):
#            df_to_process = pd.read_csv(Task1_folder + filename,delim_whitespace=True,names=columns_datafile)
#            df_with_events.append(test_data_per_row(df_to_process,metadata_rows))
#    return df_with_events

def save_to_xlsx(df):
    # Save data
    for data in df:
        if os.path.exists(output_file):
            print(f"{output_file} exists. Appending data.")

            # Append data to the Excel file
            with pd.ExcelWriter(output_file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                data.to_excel(writer, index=False, header=False, sheet_name=worksheet_name,
                              startrow=writer.sheets[worksheet_name].max_row)

            print("Data appended successfully!")
        else:
            print(f"{output_file} does not exist. Creating new file.")
            data.to_excel(output_file, index=False)

def main():
    # Load data
    df = load_data()
    find_missing_data(df)
    #Get StartTime and EndTime from metadata
    #metadata_rows = get_metadata_rows(df)

    #Get classified Data
    #df_with_data = get_data_per_row(metadata_rows)

    #Save classified data to xlsx
    #save_to_xlsx(df_with_data)

if __name__ == "__main__":
    main()