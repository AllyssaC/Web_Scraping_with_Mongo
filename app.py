from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from Scrape_Mars2 import scrape
import time
# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"]="mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

@app.route('/')
def index():
   
    mars_data = mongo.db.mars.find_one()

    if mars_data is None:
        return scraper()
    else:
        return render_template('index.html',mars_data=mars_data)

# Route to render index.html template using data from Mongo
@app.route('/scrape')
def scraper():
   
    mars = mongo.db.mars
    mars_data = scrape()

 # Update the Mongo database using update and upsert=True
    mars.update({}, mars_data, upsert=True)
    time.sleep(5)
# Return template and data
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(debug=True)
