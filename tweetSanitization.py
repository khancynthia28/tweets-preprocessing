#!/usr/bin/python
#
import json
import time
#
fO = open("main_table.txt", "w")
with open('tweets_ds.json', 'r') as f:
    cnt=1
    for cnt, line in enumerate(f):
        tweet = json.loads(line) # load it as Python dict
    #print(json.dumps(tweet, indent=4)) # pretty-print
        try: 
            tweetCreated = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
        except:
            tweetCreated ='NULL'
        try:
            tweetID=str(tweet["id"])
        except:
            tweetID='0'
        try:
            tweetText = str(tweet["text"]).replace("\n","").replace("\r","").replace("\t","").replace(";","").strip()
        except:
            tweetText = 'NULL'
        try:
            display_text_range = str(tweet["display_text_range"]).strip()
        except: 
            display_text_range = 'NULL'
        try:
            source = str(tweet["source"])
        except: 
            source = 'NULL'
        try:
            truncated = str(tweet["truncated"])
        except: 
            truncated= 'NULL'
        try:
            in_reply_to_status_id = str(tweet["in_reply_to_status_id"])
        except: 
        	  in_reply_to_status_id= '0'
        try:
        	  in_reply_to_user_id = str(tweet["in_reply_to_user_id"])
        except: 
        	  in_reply_to_user_id= '0'
        try:
        	  in_reply_to_screen_name = str(tweet["in_reply_to_screen_name"]).strip()
        except: 
        	  in_reply_to_screen_name = 'NULL'
        try:
        	  tweetUser = str(tweet["user"]["id"])
        except: 
        	  tweetUser = '0'
        try:
        	 tweetGeoType = str(tweet["geo"]["type"]).strip()
        except: 
        	 tweetGeoType = 'NULL'
        try:
        	 tweetGeoCoord = str(tweet["geo"]["coordinates"]).strip()
        except: 
        	 tweetGeoCoord = 'NULL'
        try:
        	 tweetCoordType = str(tweet["coordinates"]["type"]).strip()
        except: 
        	 tweetCoordType = 'NULL'
        try:
        	 tweetCoord = str(tweet["coordinates"]["coordinates"]).strip()
        except: 
        	 tweetCoord = 'NULL'
        try:
        	 placeID = str(tweet["place"]["id"]).strip()
        except: 
        	 placeID = 'NULL'
        try:
        	 placeURL = str(tweet["place"]["url"]).strip()
        except: 
        	 placeURL = 'NULL'
        try:
        	 placeType = str(tweet["place"]["place_type"]).strip()
        except: 
        	 placeType = 'NULL'
        try:
        	 placeCountry = str(tweet["place"]["country"]).strip()
        except: 
        	 placeCountry = 'NULL'
        try: 
            tweetPFullName = str(tweet["place"]["full_name"]).strip()
        except:
            tweetPFullName = 'NULL'
        try: 
            tweetPCountryCode = str(tweet["place"]["country_code"]).strip()
        except:
            tweetPCountryCode ='NULL'
        try:
            tweetPname = str(tweet["place"]["name"]).strip()
        except:
            tweetPname = 'NULL'
        try:
            tweetPBBox1x= str(tweet["place"]["bounding_box"]["coordinates"][0][0][0])
        except:
            tweetPBBox1x='NULL'
        try:
            tweetPBBox1y= str(tweet["place"]["bounding_box"]["coordinates"][0][0][1])
        except:
            tweetPBBox1y='NULL'
        try:
            tweetPBBox2x= str(tweet["place"]["bounding_box"]["coordinates"][0][1][0])
        except:
            tweetPBBox2x='NULL'
        try:
            tweetPBBox2y= str(tweet["place"]["bounding_box"]["coordinates"][0][1][1])
        except:
            tweetPBBox2y='NULL'
        try:
            tweetPBBox3x= str(tweet["place"]["bounding_box"]["coordinates"][0][2][0])
        except:
            tweetPBBox3x='NULL'
        try:
            tweetPBBox3y= str(tweet["place"]["bounding_box"]["coordinates"][0][2][1])
        except:
            tweetPBBox3y='NULL'
        try:
            tweetPBBox4x= str(tweet["place"]["bounding_box"]["coordinates"][0][3][0])
        except:
            tweetPBBox4x='NULL'
        try:
            tweetPBBox4y= str(tweet["place"]["bounding_box"]["coordinates"][0][3][1])
        except:
            tweetPBBox4y='NULL'
        try:
        	  placeAttributes = str(tweet["place"]["attributes"]).strip()
        except: 
        	  placeAttributes = 'NULL'
        try:
        	  tweetContributors = str(tweet["place"]["contributors"]).strip()
        except: 
        	  tweetContributors = 'NULL'
        try:
        	  is_quote_status= str(tweet["is_quote_status"])
        except: 
        	  is_quote_status= 'NULL'
        try:
        	  retweetCount= str(tweet["retweet_count"])
        except: 
        	  retweetCount= '0'
        try:
        	  favoriteCount= str(tweet["favorite_count"])
        except: 
        	  favoriteCount= '0'
        try:
        	  entitiesID= str(tweet["entities"]["user_mentions"]["id"])
        except: 
        	  entitiesID = '0'
        try:
        	  entitiesMediaID= str(tweet["entities"]["media"]["id"])
        except: 
        	  entitiesMediaID = '0'
        try:
        	  extendedEntitiesID= str(tweet["extended_entities"]["media"]["id"])
        except: 
        	  extendedEntitiesID = '0'
        try:
        	  favoritedstr = (tweet["favorited"]).strip()
        except: 
        	  favorited = 'NULL'
        try:
        	  retweeted = (tweet["retweeted"]).strip()
        except: 
        	  retweeted = 'NULL'
        try:
        	  possibly_sensitive = (tweet["possibly_sensitive"]).strip()
        except: 
        	  possibly_sensitive = 'NULL'
        try:
        	  filter_level = (tweet["filter_level"]).strip()
        except: 
        	  filter_level = 'NULL'
        try:
        	  tweetLang = (tweet["lang"]).strip()
        except: 
        	  tweetLang = 'NULL'
        try:
        	  tweetTimestamp = (tweet["timestamp_ms"])
        except: 
        	  tweetTimestamp = '0'
        try:
        	  matchingRulesTag = (tweet["matching_rules"]["tag"]).strip()
        except: 
        	  matchingRulesTag = 'NULL'
        try:
        	  matchingRulesID = (tweet["matching_rules"]["id"])
        except: 
        	  matchingRulesID = '0'

        fO.write(tweetCreated + "\t" 
                 + tweetID + "\t" 
                 + tweetText + "\t"
                 + display_text_range + "\t"
                 + source + "\t"
                 + truncated + "\t"
                 + in_reply_to_status_id + "\t"
                 + in_reply_to_user_id + "\t"
                 + in_reply_to_screen_name + "\t"
                 + tweetUser + "\t"
                 + tweetGeoType + "\t"
                 + tweetGeoCoord + "\t"
                 + tweetCoordType + "\t"
                 + tweetCoord + "\t"
                 + placeID + "\t"
                 + placeURL + "\t"
                 + placeType + "\t"
                 + placeCountry + "\t"
                 + tweetPFullName + "\t" 
                 + tweetPCountryCode + "\t" 
                 + tweetPname + "\t" 
                 + tweetPBBox1x +"\t" 
                 + tweetPBBox1y  + "\t" 
                 + tweetPBBox2x + "\t" 
                 + tweetPBBox2y + "\t" 
                 + tweetPBBox3x + "\t" 
                 + tweetPBBox3y + "\t" 
                 + tweetPBBox4x + "\t" 
                 + tweetPBBox4y + "\t"
                 + placeAttributes + "\t"
                 + tweetContributors + "\t"
                 + is_quote_status + "\t"
                 + retweetCount + "\t"
                 + favoriteCount + "\t"
                 + entitiesID + "\t"
                 + entitiesMediaID + "\t"
                 + extendedEntitiesID + "\t"
                 + favorited + "\t"
                 + retweeted + "\t"
                 + possibly_sensitive + "\t"
                 + filter_level + "\t"
                 + tweetLang + "\t"
                 + tweetTimestamp + "\t"
                 + matchingRulesTag + "\t"
                 + matchingRulesID + "\n")
        
        cnt +=1