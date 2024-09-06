# Chiropractor Office Check-In App
Welcome to the Chiropractor Office Check-In App! This application helps streamline the check-in process at a chiropractor’s office by allowing clients to check in via a user-friendly interface, timestamp their check-in time, and automatically log their information into a Google Sheet for easy tracking.

## Features
Client Check-In: Clients can input their name and check in through a simple, easy-to-use interface.
Automatic Timestamp: Each check-in is automatically timestamped to record the exact date and time of the visit.
Google Sheets Integration: The app records the client's name and check-in time directly into a Google Sheet, making it easy for office staff to manage and track client visits in real-time.
Minimalistic UI: A clean and responsive interface makes it easy for clients to check in without confusion.
Technologies Used
Python: Backend development, form handling, and Google Sheets API integration.
Flask: Used to create the web server that handles the client check-in requests.
Google Sheets API: Used to log the check-in information (client name and timestamp) into a Google Sheet.
HTML/CSS: Frontend interface design for a clean user experience.
Tkinter: Used in the server control app for starting and stopping the web server.
Installation and Setup

## Setup
### Clone the repository:

`git clone https://github.com/yourusername/chiropractor-checkin-app.git
cd chiropractor-checkin-app`


### Install dependencies: Make sure you have Python installed. Install the required packages by running:

`pip install -r requirements.txt`

### Set up Google Sheets API:

Go to the Google Developers Console, create a new project, and enable the Google Sheets API.
Create credentials and download the credentials.json file.
Place the credentials.json file in the root directory of your project.

**Create the Google Sheet:**
Create a Google Sheet to store client check-in data (e.g., columns: Name, Check-In Time).
Share the sheet with the service account email from your credentials.json.

### Run the Application: To start the server, run the following command:

`python myapp.py`

The server will start, and the app will be accessible via http://localhost:8080

Control the Server (Optional): You can control the server (start/stop) using the Server Control App built with Tkinter. Run the following to package the app:

`python -m PyInstaller --name=ServerControlApp --onefile --noconsole server_control.py`

## Usage

### Client Check-In:

Clients visit the app on an in-office device, enter their name in the form, and click "Check In."
A timestamp is generated, and the client's name along with the timestamp is saved to the Google Sheet.
Office Staff Management:

Office staff can view the Google Sheet in real-time to see when clients have checked in and manage the flow of appointments.

## Future Improvements
Client ID Integration: Adding unique client IDs for better tracking and integration with the office’s appointment system.
Notifications: Notify the staff when a client has checked in.
Advanced Analytics: Generate reports based on client check-in data for business insights.


### Contributing
If you want to contribute to this project, feel free to submit a pull request. Any ideas, feedback, or bug reports are greatly appreciated!

Thank you for using the Chiropractor Office Check-In App!
Feel free to reach out with any questions or issues!







