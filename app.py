from flask import *
from helper_functions import helper 


app=Flask(__name__)


@app.route("/")
def main_endpoint():
 return render_template("index.html")


@app.route("/scrap",methods=["POST"])
def do_scraping():
 try:
  
  url=request.form['url']
  url=helper.generate_valid_url(url)
  
  #validating URL
  html_content=helper.get_html_content(url)
  if html_content==None:return render_template("index.html",url_status=f"{url} is invalid url!!")
  
  #requesting soup's(a html5lib based parser)object
  soup=helper.get_soup_object(html_content)
  if soup==None:return render_template("error_page.html",error='HTML is not parsable, unable to create tree(DOM)') 
  
  #title
  title=helper.get_title(soup)
  
  #To store information/ we will use db after this.

  information_scrapped=dict()
  information_scrapped['title']=[title]
  
  #main target is body
  body=soup.body
  
  helper.traversing(information_scrapped,[body])
  return render_template('output.html',information_scrapped=information_scrapped)      
 except Exception as e:
  print(e)
  return "Some Error:)"


app.run()