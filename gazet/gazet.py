from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('feedback.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Check if the CSV file exists; if not, create a new one with headers
    csv_file_path = 'feedback.csv'
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Email', 'Feedback'])

    # Append the feedback data to the CSV file
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, message])

    return "Thank you for your feedback!"

if __name__ == '__main__':
    app.run()
