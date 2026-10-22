from flask import Flask, request, redirect, url_for, render_template
import gspread
import re
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from waitress import serve  # For production server

app = Flask(__name__)
# Google Sheets setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name("secret.json", scope)
client = gspread.authorize(creds)


# Open the Google Sheet

sheet = client.open("Client Check-in Sheet").sheet1


# Allowed values for the patient type field

PATIENT_TYPES = ("New Patient", "Returning Patient")


# Highlight color for new patients (RGB values 0-1). Currently a light yellow.

NEW_PATIENT_COLOR = {"red": 1.0, "green": 0.95, "blue": 0.4}


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/checkin", methods=["POST"])
def checkin():

    name = request.form["name"]

    patient_type = request.form.get("patient_type", "")

    if patient_type not in PATIENT_TYPES:

        patient_type = ""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append the name, timestamp and patient type to the Google Sheet

    # Columns: A = Name, B = Check-In Time, C = Patient Type

    result = sheet.append_row([name, timestamp, patient_type])

    # Highlight the patient type cell for new patients

    if patient_type == "New Patient":

        try:

            # updatedRange looks like "Sheet1!A5:C5" - pull out the row number

            updated_range = result["updates"]["updatedRange"]

            row = int(re.search(r"(\d+)(?!.*\d)", updated_range).group(1))

            sheet.format(f"C{row}", {"backgroundColor": NEW_PATIENT_COLOR})

        except Exception as e:

            # Never block a check-in just because the highlighting failed

            print(f"Could not highlight new patient cell: {e}")

    return redirect(url_for("index"))


if __name__ == "__main__":

    # app.run(debug=True)

    # to run the Production server, use 'python myapp.py' command

    serve(app, host="0.0.0.0", port=8080)
