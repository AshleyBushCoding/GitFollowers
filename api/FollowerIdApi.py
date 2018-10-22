#Requirements: 
# API endpoint that accepts a GitHub ID and returns Follower ID (Up to 5 total)
# Retrieve data 3 levels deep, 5 followers each
# data should be in JSON (JavaScript Object Notation) format
# code checked into public github
# readme should be included and checked into github with instructions on 
# how to execute and test the api

#bonus credit--the api endpoint is publically accessible and fully functional, 
# so that team members can execute and test your API at any time.

#done by Ashley Bush under MIT liscense--have fun!


import requests #for the API calls
import sys #for command line argument
import json #for making sure json stays as such!

def get_followers(githubId, maxNumFollowers = 5):
    
    #DO: check and see if name is valid
    #add a payload and see if you can get it to work
    #payload = {'key': 'value}

    #per github v3 API, per_page allows for making a limit on 
    # returned items (up to 100). Without it, returns every follower 
    githubApiLink = "https://api.github.com/users/" + githubId + "/followers" \
        + "?per_page=" + str(maxNumFollowers)

    response = requests.get(githubApiLink)
    #DO: confirm response was ok before proceeding further
    # example: (response.status_code == requests.code.ok)
    return response.json()

def query_followers(githubId, maxNumFollowers = 5):
    #note, recursion won't work here because you need to break it at level 3
    #all variables will eventually be stored in response
    #unauthenticated apps can only so may queries per minute and hour 
    # (might be as low as 60 queries per hour). at 3 levels of calls, 
    # 5 each, we're at 5^3, or 125 calls at min. 
    finalList = []
    level1 = get_followers(githubId, maxNumFollowers)
    queryIndex = 0 #search start point for next round

    finalList.extend(level1) #level1 is a list    
    stopIndex = len(finalList)
    #DO: CONFIRM Response is not empty before going further!!!!!!!
    #or that it's response is not "exceeded access allowed"

    # get second level of followers
    for dictionary in finalList[queryIndex : stopIndex]:
         #DO: confirm that it returns a good value
         #DO: check that the "dictionary" here isn't a string that says "limit exceeded"
        if(type(dictionary) is dict):
            queryIndex += 1
            userId = dictionary.get('login')
            if(userId is not None):
                level2 = get_followers(userId, maxNumFollowers)
                finalList.extend(level2)

    #get third level of followers
    stopIndex = len(finalList)
    for dictionary in finalList[queryIndex : stopIndex]:
        #DO: confirm that it returns a good value
        #DO: check that the "dictionary" here isn't a string that says "limit exceeded"
        if(type(dictionary) is dict):
            queryIndex += 1      
            userId = dictionary.get('login')
            if(userId is not None):
                level3 = get_followers(userId, maxNumFollowers)
                finalList.extend(level3)

    return finalList

def validAlphaNumOrHyphen(userId):
    for character in userId:
        if(not character.isalnum() and character is not "-"):
            return False
    #else it's good to go
    return True


if __name__ == '__main__':
    print("Please use the api to access this code.\n \
    Please enter userId of the GitHub member you are finding the \n \
    followers of at the end of the website. You can also optionally add in \n \
    the number of followers per person referenced (up to 5). \n \
    Ex: http://127.0.0.1:5000/api/v1/resources/followers?id=jskeet&maxNumFollowers=2")

      