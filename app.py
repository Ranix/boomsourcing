import codecs
import csv
import io
from flask import Flask
from flask import request
from flask import make_response
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder

app = Flask(__name__)

@app.route('/locate_numbers', methods = ['GET','POST'])
def locate_numbers():
    if request.method == 'POST':
        numbers_file = request.files['numbers']
        return location_each_number(numbers_file)
    else:
        number = request.args.get('number')
        return closest_number(number)


def location_each_number(numbers_file):
    stream = codecs.iterdecode(numbers_file.stream, 'utf-8')
    data = [row[0] for row in csv.reader(stream, dialect=csv.excel)]
    data.pop(0) # Clean the header of the csv file.

    # Create the new CSV file using the phone numbers library
    si = io.StringIO()
    csv_output_file = csv.writer(si, dialect='excel')
    csv_output_file.writerow(['numbers', 'valid', 'location'])
    for row in data:
        phone_data = phonenumbers.parse(row, "US")
        valid = phonenumbers.is_valid_number(phone_data)
        time_zone = timezone.time_zones_for_number(phone_data)
        csv_output_file.writerow([phone_data.national_number, valid, time_zone[0]])

    # Make response
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=export.csv"
    output.headers["Content-type"] = "text/csv"
    return output
    

def closest_number(number):
    with open('numbers.csv') as csv_file:
        data = [row[0] for row in csv.reader(csv_file, dialect=csv.excel)]
        data.pop(0)
    phone_parse = phonenumbers.parse(number, "US")
    phone_number = phone_parse.national_number
    closest = min(data, key=lambda x:abs(phone_number-int(x[-1])))
    closest_parse = phonenumbers.parse(closest, "US")
    time_zone = geocoder.description_for_number(closest_parse, "US")
    return f"Result could be {closest}, since {phone_number} and {closest} are a {time_zone} phone number."


if __name__ == "__main__":
	app.run()