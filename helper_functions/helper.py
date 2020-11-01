#importing all the required modules/libraries

import requests
from bs4 import BeautifulSoup,Comment


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


def get_content_on_basis_of_tag_name(soup,tag_name):
 if tag_name==None:return None
 if tag_name=='':return None
 try:
  return soup.find_all(tag_name)
 except:
  return None


def get_content_on_basis_of_property_name(tag,property_name):
 if property_name==None or tag==None:return None
 if property_name=='':return None
 try:
  return tag.get(property_name)
 except:
  return None




def find_all_comments(soup):
   comments=None
   try:
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))
   except:
    print("Entry in log")
   return comments



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