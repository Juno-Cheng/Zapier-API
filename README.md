# Zapier Automation for File Upload

This script automates the process of zipping a directory of extracted files and uploading the zipped file to Zapier via a webhook. It is designed to run weekly, zipping the specified folder and triggering the Zapier workflow.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.0+
- Required Python libraries: `requests`, `zipfile`, `schedule`

## Installation

### Step 1: Install Required Python Libraries

To install the necessary libraries, open your terminal and run the following command:

```bash
pip3 install requests schedule
```

### Step 2: Adjust Script Configuration

1. **Webhook URL:**
   - Update the `webhook_url` variable in the script to your Zapier webhook URL.

   ```python
   webhook_url = 'https://hooks.zapier.com/hooks/catch/your-webhook-id/'
   ```

2. **File Paths:**
   - Ensure the `folder_path` and `zip_file_path` variables are set to the correct directories where your extracted files are stored and where the zipped file will be saved.

   ```python
   folder_path = '/path/to/your/extracted/files'
   zip_file_path = '/path/to/your/zip/ScrapedData.zip'
   ```

### Step 3: Placement of Script

This script must be placed in the same directory as the folder containing your extracted files to ensure the paths are correctly resolved, or ensure the `folder_path` is correctly pointing to the extracted files.

## Usage

### Running the Script

The script is designed to run continuously, checking every minute if it’s time to execute the weekly task (every Monday at noon). To start the script, simply run:

```bash
python3 Upload.py
```

### Keeping the Script Running

- **Leave the Script Running:** For the script to function properly, it needs to be running continuously. It is recommended to run this on a server or a machine that remains on for extended periods.
- **Automating Startup (Optional):** You can set up your operating system to run this script automatically on startup using tools like `cron` (on Linux/macOS) or Task Scheduler (on Windows). Refer to your OS documentation for instructions.

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

