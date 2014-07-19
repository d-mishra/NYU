# -*- coding: utf-8 -*-
"""
Practical Data Science

E-Commerce Group Project

Team:
1. Cindy Dishmey
2. Rafeal Guimaraes
3. Diptimaya Mishra
4. Kannan Sridharan
5. Jamie Weaver

https://www.etsy.com/developers/documentation/getting_started/api_basics
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import urllib2
import json 
import pprint  #Use pprint "pretty print" for outputting complex data sets



capacityNotReached  = True
etsyCorpus = []
etsyResults = []
pageOffset = 0
capacity = 500


#Etsy only allows 100 items per call. Use 5,000 in final run
while capacityNotReached :
    etsyJSON = urllib2.urlopen('https://openapi.etsy.com/v2/private/shops?api_key=qg7ajp0cxlqjmubu9j2tfxr1&limit=100&offset='+ str(pageOffset)).read()
    etsyDict = json.loads(etsyJSON) #the whole file is a dictionary with 5 key:value pairs
    
    for item in etsyDict["results"]:
        ## Attributes for Text Similarity : Announcement, Title, Seller info, Welcome
        ## Concatenate all field into one string & add to a list
        ## List will have the same indices as estyResults       
       
       
     
        m = ""     
        """  
        #Words in the shop attribue do not repeat often and are not useful for TF
        if item["announcement"] is not None:
            m = m + str(item["announcement"].encode("utf-8") ) +" "
        
        if item["title"] is not None:
            m = m + str(item["title"].encode("utf-8") ) +" "
        
        if item["policy_seller_info"] is not None:
            m = m + str(item["policy_seller_info"].encode("utf-8") ) +" "
        
        if item["policy_welcome"] is not None:
            m = m + str(item["policy_welcome"].encode("utf-8") ) +" "

        """
        #Get listings - Pull the first 10 listing titles to document. Puling all available listings would more precise 
        for lt in json.loads(urllib2.urlopen('https://openapi.etsy.com/v2/private/shops/'+ str(item["shop_id"] )  +'/listings/active?api_key=qg7ajp0cxlqjmubu9j2tfxr1&limit=10').read())['results']:
             m = m + (lt['title'])




        if len(m) > 100:
            #Ignore small or blank documents
            etsyCorpus.append(m.lower())      
            etsyResults.append(item) #Result is a list of shops. 1 shop is a data dictionary

    
    
    if(len(etsyResults) > capacity):    
        capacityNotReached  = False
    else:
        pageOffset = pageOffset + 100


print("Number of shops loaded")
pprint.pprint(len(etsyResults)) # Number of Shops
print("Sample shop attributes")
pprint.pprint(etsyResults[0]) # names of shop attributes    

for sliceStart in range(0,len(etsyCorpus),1):
    #Vectorize and TF-IDF corpus. Rempve stop words
    tfidf = TfidfVectorizer(stop_words='english').fit_transform(etsyCorpus)
    
    #Slice matrix and compare with entire corpus
    cosine_similarities = linear_kernel(tfidf[sliceStart:(sliceStart+1)], tfidf).flatten()
    #pprint.pprint(cosine_similarities)
    
    #Indices of the documents most related to the slice. self is first
    related_docs_indices = cosine_similarities.argsort()[:-7:-1]
    #related_docs_indices
    #cosine_similarities[related_docs_indices]
    
    #Output similarities
    print(str(sliceStart)+" "+etsyResults[sliceStart]["shop_name"]+": "+str(related_docs_indices[1])+" "+etsyResults[related_docs_indices[1]]["shop_name"]+", "+str(related_docs_indices[2])+" "+etsyResults[related_docs_indices[2]]["shop_name"]+", "+str(related_docs_indices[3])+" "+etsyResults[related_docs_indices[3]]["shop_name"]+", "+str(related_docs_indices[4])+" "+etsyResults[related_docs_indices[4]]["shop_name"]+", "+str(related_docs_indices[5])+" "+etsyResults[related_docs_indices[5]]["shop_name"])
    
    
    








