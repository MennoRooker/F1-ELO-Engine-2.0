"""
Imports the data from books.csv into the newly created 'books' table in the database.
"""

import csv
import os

from flask import Flask
from models import *

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("data/drivers.csv")
    reader = csv.reader(f)

    # Skip the first line
    next(reader)

    # Parse the csv data
    for row in reader:
        driver = Driver(
            id=int(row[0]), 
            name=f"{row[4]} {row[5]}", 
            number=int(row[2]) if row[2] != "\\N" else None, 
            code=row[3], 
            dob=row[6], 
            nationality=row[7]
        )
        db.session.add(driver)

        # Commit the changes to the database
        db.session.commit()
        print(f"Added {driver.name} to 'drivers'")



# Run script to add the data
if __name__ == "__main__":
    with app.app_context():
        main()