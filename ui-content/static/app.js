var url="";
var keywords=[]
var tags=[]
var keywords1=[]
    

function displayURL()
{
document.getElementById("url2").value=""
document.getElementById("url3").value=""
document.getElementById("allkeywords").value=""
document.getElementById("allkeywords1").value=""
document.getElementById("alltags").value=""
document.getElementById("showdata").style.display="none"
document.getElementById("displayURLKeywords").style.display="none"
document.getElementById("displayURLTags").style.display="none"
document.getElementById("displayKeywords").style.display="none"
document.getElementById("myContainer").style.display="block"
document.getElementById("displayURL").style.display="block"
}
 
function displayURLKeywords()
{
document.getElementById("displayURL").style.display="none"
document.getElementById("url1").value=""
document.getElementById("url3").value=""
document.getElementById("myContainer").style.display="block"
document.getElementById("allkeywords").value=""
document.getElementById("allkeywords1").value=""
document.getElementById("alltags").value=""
document.getElementById("showdata").style.display="none"
document.getElementById("displayURLTags").style.display="none"
document.getElementById("displayKeywords").style.display="none"
document.getElementById("displayURLKeywords").style.display="block"
} 

function displayURLTags()
{
document.getElementById("displayURL").style.display="none"
document.getElementById("showdata").style.display="none"
document.getElementById("url1").value=""
document.getElementById("url2").value=""
document.getElementById("myContainer").style.display="block"
document.getElementById("allkeywords").value=""
document.getElementById("allkeywords1").value=""
document.getElementById("alltags").value=""
document.getElementById("displayURLKeywords").style.display="none"
document.getElementById("displayURLTags").style.display="block"
document.getElementById("displayKeywords").style.display="none"
}
 
function displayKeywords()
{
document.getElementById("allkeywords").value=""
document.getElementById("allkeywords1").value=""
document.getElementById("alltags").value=""
document.getElementById("myContainer").style.display="block"
document.getElementById("showdata").style.display="none"
document.getElementById("displayURL").style.display="none"
document.getElementById("displayURLKeywords").style.display="none"
document.getElementById("displayURLTags").style.display="none"
document.getElementById("displayKeywords").style.display="block"
}






function keywordHandler()
{
keyword=document.getElementById("keyword")
data=keyword.value
if(data.length==0)return
keyword.value=""
keywords.push(data)
allkeywords=document.getElementById("allkeywords")
v=allkeywords.value
allkeywords.value=""
if(v==null)return
v=v+data+"\n"
allkeywords.value=v
}

function keywordHandler1()
{
keyword=document.getElementById("keyword1")
data=keyword.value
if(data.length==0)return
keyword.value=""
keywords1.push(data)
allkeywords1=document.getElementById("allkeywords1")
v=allkeywords1.value
allkeywords1.value=""
if(v==null)return
v=v+data+"\n"
allkeywords1.value=v
}



function tagHandler()
{
tag=document.getElementById("tag")
data=tag.value
if(tag.length==0)return
tag.value=""
tags.push(data)
alltags=document.getElementById("alltags")
v=alltags.value
alltags.value=""
if(v==null)return
v=v+data+"\n"
alltags.value=v
}




async function sendURLRequest()
{
processing=document.getElementById("processing")
processing.style.display="block"
myContainer=document.getElementById("myContainer")
myContainer.style.display="none"
url="http://localhost:5000/scrap"
myURL=document.getElementById("url1").value

data={
"url":myURL,
"tags":[],
"keywords":[]
}
try {

    const config = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }
    const response = await fetch(url, config)
    
    const json = await response.json()
     
    if (response.ok) {


//done done

allKeys=Object.keys(json)
t=""       
function dataExtractor(tt)
{
arr=json[tt]
e=0
f=arr.length
t=t+tt.bold()+"<br/>";
while(e<f)
{
t=t+arr[e]+"<br/>"
e=e+1
}
}

allKeys.map(dataExtractor)

document.getElementById("data").innerHTML=t;
processing.style.display="none"
document.getElementById("showdata").style.display="block"
        //return json;
        return response
    } else {
        //
    }
} catch (error) {
console.log(error)        //
}
}




async function sendURLKeywordRequest()
{
processing=document.getElementById("processing")
processing.style.display="block"
myContainer=document.getElementById("myContainer")
myContainer.style.display="none"
url="http://localhost:5000/scrap"
myURL=document.getElementById("url2").value
data={
"url":myURL,
"tags":[],
"keywords":keywords
}
try {

    const config = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }
    const response = await fetch(url, config)
    
    const json = await response.json()
     
    if (response.ok) {

allKeys=Object.keys(json)
t=""       




function dataExtractor1(j,tt)
{
arr=j[tt]
if(arr instanceof Array)
{
e=0
f=arr.length
t=t+tt.bold()+"<br/>";
while(e<f)
{
t=t+arr[e]+"<br/>"
e=e+1
}
}
}





function dataExtractor(tt)
{
arr=json[tt]
if(arr instanceof Array)
{
e=0
f=arr.length
t=t+tt.bold()+"<br/>";
while(e<f)
{
t=t+arr[e]+"<br/>"
e=e+1
}
}
else
{
if(arr instanceof Object)
{
o=Object.keys(arr)
lf=o.length
le=0
dataToPass=arr
while(le<lf)
{
dataExtractor1(dataToPass,o[le])
le=le+1
}
}
}
}






allKeys.map(dataExtractor)



document.getElementById("data").innerHTML=t;
processing.style.display="none"
document.getElementById("showdata").style.display="block"
        //return json;
        return response
    } else {
        //
    }
} catch (error) {
console.log(error)        //
}
}




async function sendURLTagRequest()
{
processing=document.getElementById("processing")
processing.style.display="block"
myContainer=document.getElementById("myContainer")
myContainer.style.display="none"
url="http://localhost:5000/scrap"
myURL=document.getElementById("url3").value
data={
"url":myURL,
"tags":tags,
"keywords":[]
}
try {

    const config = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }
    const response = await fetch(url, config)
    
    const json = await response.json()
     
    if (response.ok) {

       

allKeys=Object.keys(json)
t=""       
function dataExtractor(tt)
{
arr=json[tt]
e=0
f=arr.length
t=t+tt.bold()+"<br/>";
while(e<f)
{
t=t+arr[e]+"<br/>"
e=e+1
}
}
allKeys.map(dataExtractor)
document.getElementById("data").innerHTML=t;
processing.style.display="none"
document.getElementById("showdata").style.display="block"
        //return json;
        return response
    } else {
        //
    }
} catch (error) {
console.log(error)        //
}
}







async function sendKeywordRequest()
{
processing=document.getElementById("processing")
processing.style.display="block"
myContainer=document.getElementById("myContainer")
myContainer.style.display="none"
url="http://localhost:5000/scrap"

data={
"url":"",
"tags":[],
"keywords":keywords1
}
try {

    const config = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    }
    const response = await fetch(url, config)
    
    const json = await response.json()
     
    if (response.ok) {

 




t=""



function dataExtractor(dataObject,number)
{
console.log("exc",dataObject)
t=t+"<h2>Site "+number+":</h2><hr>"
k=Object.keys(dataObject)
start=0
end=k.length
while(start<end)
{
arr=dataObject[k[start]]
ee=0
ff=arr.length
t=t+k[start].bold()+"<br/>";
while(ee<ff)
{
t=t+arr[ee]+"<br/>"
ee=ee+1
}
start=start+1
}
}
      


console.log(json)
allKeys=Object.keys(json)
console.log(allKeys)
e=0
f=allKeys.length
console.log(f)
while(e<f)
{
current_key=allKeys[e]
data=json[current_key]
console.log("data",data)
objKeys=Object.keys(data)
eee=0
fff=objKeys.length
console.log(fff)
console.log(objKeys)
while(eee<fff)
{
curr_data=data[objKeys[eee]]
console.log(curr_data)
dataExtractor(curr_data,eee)
eee=eee+1
}
e=e+1
}

document.getElementById("data").innerHTML=t;
processing.style.display="none"
document.getElementById("showdata").style.display="block"
        //return json;
        return response
    } else {
        //
    }
} catch (error) {
console.log(error)        //
}
}


