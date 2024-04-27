import os
#import wget

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
#url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'
#file_name = "data_raw.csv"
#wget.download(url, file_name)

import requests

# Download the zipped dataset
url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'

# Define the local file path where the data will be saved
local_file_path = "data_raw.csv"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the content to the local file
        with open(local_file_path, 'wb') as file:
            file.write(response.content)
        print("Data downloaded and saved successfully.")
    else:
        print(f"Failed to download data. HTTP Status Code: {response.status_code}")

except requests.RequestException as e:
    print(f"An error occurred while fetching data: {e}")