# > open series of text files
# > get timestamp
# >compare with start and end time
# >classify event type
#
# >create file

import os
import pandas as pd

Task1_folder = "./Task1/"
Timestamp_file = "metadata.xlsx"
columns_metadata = ['StartTime','EndTime','EventType']

columns_datafile = ['Timestamp','x','y','z','EventType']
# Output file for classified events
output_file = 'classified_events.xlsx'
worksheet_name = "Sheet1"
#timestamp format YYYY-DD-MM-DD-hh:mm:ss:fff
#metadata timestamp hh:mm:ss:fff

def get_metadata_rows(df):
    rows = df[columns_metadata].values.tolist()
    return rows
def load_metadata():
    return pd.read_excel(Task1_folder + Timestamp_file)

# Define the start and end time range for comparison
#start_time = datetime.strptime("2023-11-01 00:00:00", "%Y-%m-%d %H:%M:%S")
#end_time = datetime.strptime("2023-11-05 23:59:59", "%Y-%m-%d %H:%M:%S")

# def parse_timestamp(timestamp_str):
#     return datetime.strptime(timestamp_str, '%Y-%m-%d-%H:%M:%S:%f')
# def format_timestamp(parsed_dt):
#     return parsed_dt.strftime('%H:%M:%S:%f')



def classify_event(timestamp, metadata_rows):
    # if start_time <= timestamp <= end_time:
    #    return "Within Range Event"
    # else:
    #    return "Out of Range Event"


    for rows in metadata_rows: #row[0] start time, row[1] end time, row[2], event type
        if rows[0] <= timestamp <= rows[1]:
            return rows[2]  # Event type column
    return 0 #Not within time boundaries

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

def get_data_per_row(metadata_rows):
    filepath = []
    df_with_events = []
    for filename in os.listdir(Task1_folder):
        # Only process text files
        if filename.endswith('.txt'):
            df_to_process = pd.read_csv(Task1_folder + filename,delim_whitespace=True,names=columns_datafile)
            df_with_events.append(test_data_per_row(df_to_process,metadata_rows))
    return df_with_events

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
    # Load metadata
    df = load_metadata()

    #Get StartTime and EndTime from metadata
    metadata_rows = get_metadata_rows(df)

    #Get classified Data
    df_with_data = get_data_per_row(metadata_rows)

    #Save classified data to xlsx
    save_to_xlsx(df_with_data)

if __name__ == "__main__":
    main()