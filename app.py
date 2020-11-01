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
  #collecting data/doing scraping
  title=helper.get_title(soup)
  #creating response further we will store this information in our database for analytical purpose
  information_scrapped=dict()
  information_scrapped['title']=title
  anchors=helper.get_content_on_basis_of_tag_name(soup,'a')
  paragraphs=helper.get_content_on_basis_of_tag_name(soup,'p')
  tds=helper.get_content_on_basis_of_tag_name(soup,'td')
  
  information_scrapped['paragraphs']=[]
  for paragraph in paragraphs:
   information_scrapped['paragraphs'].append(paragraph.get_text())
  information_scrapped['anchors']=[]
  for anchor in anchors:
   l=[anchor.get_text(),helper.get_content_on_basis_of_property_name(anchor,'href')]
   information_scrapped['anchors'].append(l) 
    
  information_scrapped['tds']=[]
  for td in tds:
   information_scrapped['tds'].append(td.get_text())
  return render_template("output.html",information_scrapped=information_scrapped)
 except Exception as e:
  print(e)



app.run()