# Image_Notifier_Script
This Python script is designed to automatically identify and move image files that haven't been accessed for a specified number of days (7 days in this case) from the user's current directory to a designated folder on the Desktop. The images are moved to a folder named Useless_images for easier management and potential deletion. The script also sends a notification through Windows ToastNotifier, alerting the user of the number of files moved.
Key Features:

    Identifies Old Image Files: The script scans the current directory for image files (.png, .jpg, .jpeg).
    Automatic Sorting: It identifies image files that haven't been accessed for more than 7 days.
    Moves Old Files: It moves these old image files to a folder on the Desktop (~/Desktop/Useless_images).
    Notifications: Sends a notification via the Windows ToastNotifier to inform the user about the files that have been moved.
    Cross-platform Compatibility: Handles file paths in a way that is compatible with both Windows and Unix-like systems (macOS, Linux).

Requirements:

    Python 3.x
    Required Python libraries:
        win10toast: For sending desktop notifications (Windows only)
        os: For file and directory handling
        shutil: For moving files
        datetime: For comparing file access times
        pathlib (optional for enhanced path handling)

You can install the necessary Python dependencies using pip:

pip install win10toast

Usage:

    Download the script to your local machine.

    Run the script:
        The script will scan your current directory (where the script is located).
        It checks each image file (.png, .jpg, .jpeg) and compares its last access time to the current date.
        If the image hasn't been accessed for over 7 days, it will be moved to the Useless_images folder on your Desktop.

    Run the script by executing:

    python move_old_images.py

    Check the notifications:
        Once the script completes, a toast notification will appear informing you how many images were moved.

Directory Structure:

    Source directory: The directory where the script is executed from.
    Destination directory: ~/Desktop/Useless_images (automatically created if it doesn't exist).

Example Workflow:

    If there are images in the current directory that haven't been accessed for more than 7 days, the script will move them to a folder called Useless_images located on the Desktop. The script will display a notification indicating the number of files moved.

Code Explanation:

    Directory creation: If the Useless_images folder does not exist, it is created with permissions set to 777 (full access).
    File iteration: The script uses os.walk() to iterate over all files in the current directory and subdirectories.
    File filtering: It checks whether the file is an image (.png, .jpg, .jpeg) and whether its last access time is older than 7 days.
    Moving files: Files that meet the criteria are moved to the Useless_images folder.
    Toast Notification: A notification is displayed showing the number of files moved.

Future Improvements:

    Error handling: More specific error messages for when moving files fails.
    Customizable time: Allow the user to configure the number of days to check before moving files.
    Cross-platform notifications: Modify the script to send notifications on non-Windows platforms as well.
    Logging: Add a logging system to track which files were moved and provide an audit trail.

License:

This project is open-source and licensed under the MIT License.
