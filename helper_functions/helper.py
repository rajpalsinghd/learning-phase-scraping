#importing all the required modules/libraries
import requests
from bs4 import BeautifulSoup,Comment
from bs4.element import *
import shutil
import os
from error.WebScrapingError import *
import pathlib

"""
 This helper function extracts url,tags and keywords from client request if found
 else will raise WebScrapingError

"""
def extract_data(request):
  try: 
   #json data from user/client
   data=request.json
   #data object must have url,keyword and tags fields
   url=""
   tags=keywords=[]
   url=data["url"]
   tags=data["tags"]
   keywords=data["keywords"]
   return (tags,url,keywords)
  except Exception as e:
   raise WebScrapingError("tags,keywords or url missing")  


"""
 This function append http(s) with the given url to make it eligible for sending request
 if already http(s) is there in request then return the same url

"""
def generate_valid_url(url):
 try:
  x=url.find('http')
  if x!=-1:return url
  x=url.find('https')
  if x!=-1:return url
  url='http://'+url
  return url
 except:
  return None




"""
 This helper function will return html content if fetched else will return None

"""
def get_html_content(url):
 response_content=None
 try:
  headers = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
  response=requests.get(url,headers)
  if response.status_code==200:
   response_content=response.content
 except Exception as e:
    pass
    #entry in logs
    #done done
 return response_content




"""
 This function will fetch the html content taking help from other helper functions

"""
def process_request(url):
 try:
  url=generate_valid_url(url)
  html_content=get_html_content(url)
  if html_content==None:raise WebScrapingError(f"Invalid url, {url}")
  return html_content
 except WebScrapingError as e:
  raise WebScrapingError(e.value)   


"""
 This helper function scrap(s) information of children.

"""
def scrap_info(information_scrapped,element):
 parent=element.parent.name
 if parent in information_scrapped:
   information_scrapped[parent].append(element.string)
 else:
   information_scrapped[parent]=[element.string]

"""
 This helper function returns list of children of a node/element.  

"""
def retrieve(element):
 if type(element)!=Tag:return None
 cc=element.children
 return cc


"""
 This helper function will retrieve src from image
 along with this we are adding base_url if relative path is used for images in given url.

"""
def scrap_info_img(information_scrapped,element):
 src=element.get('src')
 if src.find("http")==-1:src=information_scrapped["base_url"]+src
 if 'img' in information_scrapped:
   information_scrapped['img'].append(src)
 else:
   information_scrapped['img']=[src]





"""
 This helper function does traversing/extraction(extraction of information) of complete DOM tree

"""
def complete_traversing(information_scrapped,elements):
 try:
  for element in elements:
   element_name=element.name
   if element_name==None:
    if element!='\n':
     scrap_info(information_scrapped,element) 
    continue
   x=retrieve(element)
   if x==None:
     pass
   else:
     if element.name=='img':scrap_info_img(information_scrapped,element)
     complete_traversing(information_scrapped,x)
 except Exception as e:
   pass


"""
 This helper function will return all the tags having the given tag name if found
 else will return None

"""
def get_tag_objects(soup,tag_name):
 if tag_name==None:return None
 if tag_name=='':return None
 try:
  return soup.find_all(tag_name)
 except:
  return None


"""
 This helper function will traverse/extract(information extraction) on basis of tag name if given by client
 
"""
def traversing_on_basis_of_tags(information_scrapped,soup,tags):
 for tag in tags:
  tag_objects=get_tag_objects(soup,tag) 
  for object in tag_objects:
    complete_traversing(information_scrapped,[object])
    

"""
 This helper function will scrap information on basis of keyword

"""
def scrap_info_on_basis_of_keyword(information_scrapped,element,keyword):
 parent=element.parent.name
 if keyword.upper()==element.string.upper():
    if parent in information_scrapped:
      if parent=='a':information_scrapped['a'].append(element.parent)
      else:information_scrapped[parent].append(element.string)
    else:
     if parent=='a':information_scrapped[parent]=[element.parent]
     else:information_scrapped[parent]=[element.string]
    


"""
 This helper function does traversing/extraction(extraction of information) of complete DOM tree basis of keyword

"""
def complete_traversing_on_basis_of_keyword(information_scrapped,elements,keyword):
 try:
  for element in elements:
   element_name=element.name
   if element_name==None:
    if element!='\n':
     scrap_info_on_basis_of_keyword(information_scrapped,element,keyword) 
    continue
   x=retrieve(element)
   if x==None:
     pass
   else:
     if element.name=='img':scrap_info_img(information_scrapped,element)
     complete_traversing_on_basis_of_keyword(information_scrapped,x,keyword)
 except Exception as e:
   pass

"""
 This function is responsible for collecting information from anchor

"""

def collect_from_anchor(anchor):
  url=generate_valid_url(anchor)
  html_content=get_html_content(url)
  if html_content==None:return None
  soup=get_soup_object(html_content)
  if soup==None:return None  
  body=soup.body
  if body==None:return None
  info_from_link=dict()
  complete_traversing(info_from_link,[body])
  return info_from_link

"""
 This helper function will traverse/extract(information extraction) on basis of keyword if given by client
 
"""
def traversing_on_basis_of_keyword(information_scrapped,elements,keywords):
 for keyword in keywords: 
  complete_traversing_on_basis_of_keyword(information_scrapped,elements,keyword)
 anchors=information_scrapped['a']
 for anchor in anchors:
   i=collect_from_anchor(anchor.get('href'))
   information_scrapped[anchor.get('href')]=i
 del information_scrapped['a']
 return information_scrapped  



"""
 This helper function is for responsible for taking actions on basis of tags and keywords

"""
def scraping(soup,tags,url,keywords):
 body=soup.body
 information_scrapped=dict()
 information_scrapped["base_url"]=url
 
 len_tags=len(tags)
 len_keywords=len(keywords)

 #complete scraping of given url
 if len_keywords==0 and len_tags==0:
  title=get_title(soup)
  information_scrapped['title']=[title]
  complete_traversing(information_scrapped,[body])
 
 #on basis of keywords
 elif (len_tags==0 and len_keywords!=0):
  traversing_on_basis_of_keyword(information_scrapped,soup,keywords)

 #on basis of tags
 elif (len_tags!=0 and len_keywords==0):
  traversing_on_basis_of_tags(information_scrapped,[body],tags)
  
 del information_scrapped["base_url"]
 return information_scrapped


"""
 This helper function will return title from soup object

"""
def get_title(soup):
 if soup==None:return None
 try:
  return soup.title.string
 except:
  return None


"""
 This helper function will create a soup object which is basically a tree structure(DOM) of given html
 else will return None if some problem exists.

"""
def get_soup_object(html_content,parser='html.parser'):
 if html_content==None:return None
 soup=None
 try:
  soup=BeautifulSoup(html_content,parser) 
 except:
  #Todo entry in logs
  return soup 
 return soup

"""
 This function is responsible for creating a directory

"""
def create_directory():
  _here=os.path.dirname(os.path.abspath('app.py'))+pathlib.os.sep+"images"+pathlib.os.sep
  f=open(_here+"count.txt","r")
  number=int(f.read())
  f.close()
  directory = "new_request"+str(number)
  number=number+1
  f=open(_here+"count.txt","w")
  f.write(str(number))
  path = os.path.join(_here, directory) 
  os.mkdir(path)
  return path


"""
 This function is responsible for dumping images

"""
def dump_images(images):
 try:
  folder=create_directory()  
  for image_url in images:  
   filename = image_url.split("/")[-1]
   r = requests.get(image_url, stream = True)
   if r.status_code == 200:
     r.raw.decode_content = True
     filename=folder+pathlib.os.sep+filename
     #will delete this print after testing to make sure about this functionality(to keep it or not)
     print(filename)
     with open(filename,'wb') as f:
         shutil.copyfileobj(r.raw, f)

   
 except Exception as e:
  print(e)


"""
 This helper function is main function which being called from flask application/endpoint

"""
def helper_scraper(request):
 try:
  data=extract_data(request)
  tags,url,keywords=data  
  html_content=process_request(url)
  #get soup object which is basically a DOM tree created using html5parser
  soup=get_soup_object(html_content)
  if soup==None:raise WebScrapingError("HTML is not parsable, unable to create tree(DOM)") 
  #do scraping
  information_scrapped=scraping(soup,tags,url,keywords)
  if "img" in information_scrapped: 
   dump_images(information_scrapped["img"])
  return information_scrapped  
  
 except WebScrapingError as e:
  raise WebScrapingError(e.value) 