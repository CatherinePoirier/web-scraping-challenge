from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Set route
@app.route('/')
def index():
    data_from_mongo=mongo.db.collection.find_one()
    return render_template('index.html', data_from_flask=data_from_mongo)

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape_info()
    mongo.db.collection.update({}, mars_data, upsert=True)
    #Call the scrape_pars.py, which will return a dictionary of re
    #store the dictionalry of results to mongo
    #client.mars_db.mars.insert(, upsert=True)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
