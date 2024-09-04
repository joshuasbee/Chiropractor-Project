from flask import Flask, request, redirect, url_for, render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from waitress import serve # For production server
app = Flask(__name__)

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Client Check-in Sheet").sheet1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/checkin', methods=['POST'])
def checkin():
    name = request.form['name']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Append the name and timestamp to the Google Sheet
    sheet.append_row([name, timestamp])

    return redirect(url_for('index'))

if __name__ == '__main__':
    # app.run(debug=True)
# to run the Production server, use 'python myapp.py' command
    serve(app, host='0.0.0.0', port=8080)