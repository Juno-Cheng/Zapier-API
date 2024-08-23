import requests
import os
import zipfile
import schedule
import time


# Define the webhook URL (provided by Zapier)
webhook_url = '....'

# Define the folder to upload
folder_path = '/Users/omega/Documents/Octoparse/ScrapedData'
zip_file_path = '/Users/omega/Documents/Octoparse/ScrapedData.zip'

# Function to zip the folder
def zip_folder(folder_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print(f'Folder {folder_path} has been zipped into {zip_file_path}')

# Function to upload file to Zapier webhook
def upload_to_zapier():
    with open(zip_file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post(webhook_url, files=files)
        if response.status_code == 200:
            print(f'Successfully uploaded {os.path.basename(zip_file_path)} to Zapier')
        else:
            print(f'Failed to upload file. Status code: {response.status_code}, Response: {response.text}')

def job():
    zip_folder(folder_path, zip_file_path)
    upload_to_zapier()

# Schedule the job to run every Monday at noon
schedule.every().monday.at("12:00").do(job)

# Keep the script running to check for scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
