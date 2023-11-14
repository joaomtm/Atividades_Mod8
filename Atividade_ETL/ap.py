from flask import Flask, render_template
from datetime import datetime

ap = Flask(__name__)

@ap.route('/')
def home():
    return render_template('index.html')

@ap.route('/etl')
def perform_etl():
    ingestion_date = datetime.utcnow()
    weather_type = "Sunny"
    temperature = 25
    usage = "Example Usage"

    return render_template('etl_result.html', ingestion_date=ingestion_date, weather_type=weather_type, temperature=temperature, usage=usage)

if __name__ == '__main__':
    ap.run(debug=True)
