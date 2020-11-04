from flask import *
from helper_functions import helper 
from error.WebScrapingError import *
import logging
import logs.log_initializer

app=Flask(__name__)


"""
 This is our main end point

"""
@app.route("/scrap",methods=["POST"])
def do_scraping():
 try:
  information_scrapped=helper.helper_scraper(request)
  return jsonify(information_scrapped) 
 except WebScrapingError as e:
  return jsonify({"error":e.value})  
 




app.run()