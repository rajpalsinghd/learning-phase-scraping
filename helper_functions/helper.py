#importing all the required modules/libraries

import requests
from bs4 import BeautifulSoup,Comment
from bs4.element import *





#newly added functions starts here

def retrieve(element):
 if type(element)!=Tag:return None
 cc=element.children
 return cc


def scrap_info(information_scrapped,element):
 parent=element.parent.name
 if parent in information_scrapped:
  information_scrapped[parent].append(element.string)
 else:
  information_scrapped[parent]=[element.string]

def scrap_info_img(information_scrapped,element):
 if 'img' in information_scrapped:
   information_scrapped['img'].append(element.get('src'))
 else:
   information_scrapped['img']=[element.get('src')]

def traversing(information_scrapped,elements):
 try:
  for element in elements:
   element_name=element.name
   if element_name==None:
    if element!='\n':
     scrap_info(information_scrapped,element) 
    continue
   x=retrieve(element)
   if x==None:
     print(element)
   else:
     if element.name=='img':scrap_info_img(information_scrapped,element)
     traversing(information_scrapped,x)
   
 except Exception as e:
   print(e)


#newly added function ends here




"""
 This helper function will return html content if fetched else will return None
 example:url="http://google.com"

"""

def get_html_content(url):
 response_content=None
 try:
  response=requests.get(url)
  if response.status_code==200:
   response_content=response.content
 except Exception as e:
  #Todo entry in logs
  return response_content
 return response_content


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

def get_title(soup):
 if soup==None:return None
 try:
  return soup.title.string
 except:
  #Todo entry in logs
  return None


#outdated we don't need this function

def get_content_on_basis_of_tag_name(soup,tag_name):
 if tag_name==None:return None
 if tag_name=='':return None
 try:
  return soup.find_all(tag_name)
 except:
  return None


#outdated can/ we will use this to extract links

def get_content_on_basis_of_property_name(tag,property_name):
 if property_name==None or tag==None:return None
 if property_name=='':return None
 try:
  return tag.get(property_name)
 except:
  return None


#If we need to add comments functionality also

def find_all_comments(soup):
   comments=None
   try:
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
   except:
    print("Entry in log")
   return comments


#To generate a valid url

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






