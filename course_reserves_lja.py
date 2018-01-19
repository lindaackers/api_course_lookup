#-------------------------------------------------------------------------------
# Name:        CourseReserves.py
# Purpose:     Create files from course reserves API
#
# Author:      Linda Ackers
#
# Created:     1/18/2018
#-------------------------------------------------------------------------------
from urllib.request import urlopen
from pprint import pprint
import simplejson
import json
import re

def createfiles (offsetnum):
  try:
    offset=str(offsetnum) 
    apikey= '[apikey]' #remove key for GitHub copy
    url = 'https://api-na.hosted.exlibrisgroup.com/almaws/v1/courses?apikey='+apikey+'&limit=100&offset='+offset+'&format=json'
    temp_file='crjson_temp'+offset+'.json'
    clean_file='crjson'+offset
    u = urlopen(url)
    resp = json.loads(u.read().decode('utf-8')) #Get JSON data
 
    #pprint(resp) #debug 
    #is_dic=type(resp) //check to see if it's  dictionary
    #print(is_dic)
    #for key in resp.keys(): # only keys are course & total_record_count
      #print (key)    
  
    jsondata = simplejson.dumps(resp, indent=4, skipkeys=True, sort_keys=True)
    
    with open(temp_file, 'w') as json_file:    
      json_file.write(jsondata)

    #print ('this file has been created: '+temp_file) #debug
    
    with open(temp_file) as data_file:  #open file
      with open(clean_file, 'w') as new_file:
        mycount=1
        for line in data_file:
          if 'primary_id' in line:            
            #print (mycount)
            #print ('do find/replace')
            is_stripped = re.sub(r'L[\d][\d][\d][\d][\d][\d][\d][\d]', 'stripped', line) #strip L number
            new_file.write(is_stripped)
            mycount=mycount+1 
          else:
            new_file.write(line)
    print ('this file has been created: '+clean_file)
    
  except:
    print ('there was a problem getting data')

if __name__ == '__main__':
  i=0
  while (i<500):
    createfiles(i);    
    i+=100 #increment offset in batches of 100