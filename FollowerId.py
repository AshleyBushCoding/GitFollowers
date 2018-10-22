#Requirements: 
# API endpoint that accepts a GitHub ID and returns Follower ID (Up to 5 total)
# Retrieve data 3 levels deep, 5 followers each
# data should be in JSON (JavaScript Object Notation) format
# code checked into public github
# readme should be included and checked into github with instructions on 
# how to execute and test the api

#bonus credit--the api enpoint is publically accessible and fully functional, 
# so that team members can execute and test your API at any time.

#done by Ashley Bush under MIT liscense--have fun!
#file is made in GitHub, not uploaded. Upload file is currently failing.


import requests #for the API calls
import sys #for command line argument
import json #for making sure json stays as such!

def get_followers(githubId, maxFollowers = 5):
    #DO: note--github only allows alphanumeric characters in name, and hyphens.
    #DO: check and see if name is valid
    #add a payload and see if you can get it to work
    #payload = {'key': 'value}

    #per github v3 API, per_page allows for making a limit on 
    # returned items (up to 100). Without it, returns every follower 
    githubApiLink = "https://api.github.com/users/" + githubId + "/followers" + "?per_page=" + str(maxFollowers)
    response = requests.get(githubApiLink)
    #DO: confirm response was ok before proceeding further
    # example: (response.status_code == requests.code.ok)
    return response.json()

def query_followers(githubId, maxFollowers = 5):
    #note, recursion won't work here because you need to break it at level 3
    #all variables will eventually be stored in response
    #unauthenticated apps can only so may queries per minute and hour 
    # (might be as low as 60 queries per hour). at 3 levels of calls, 
    # 5 each, we're at 5^3, or 125 calls at min. 
    finalList = []
    level1 = get_followers(githubId, maxFollowers)
    queryIndex = 0 #search start point for next round

    finalList.extend(level1) #level1 is a list    
    stopIndex = len(finalList)
    #DO: CONFIRM Response is not empty before going further!!!!!!!
    #or that it's response is not "exceeded access allowed"
    testlist = []
    level2testList = []
    level3testList = []

    # get second level of followers
    for dictionary in finalList[queryIndex : stopIndex]:
         #DO: confirm that it returns a good value
         #DO: check that the "dictionary" here isn't a string that says "limit exceeded"
        if(type(dictionary) is dict):
            queryIndex += 1
            userId = dictionary.get('login')
            if(userId is not None):
                testlist.append(userId)
                level2 = get_followers(userId, maxFollowers)
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
                level2testList.append(userId)
                level3 = get_followers(userId, maxFollowers)
                finalList.extend(level3)


    #Testing only--not used in final program
    stopIndex = len(finalList)
    #for testing, not needed later
    for dictionary in finalList[queryIndex : stopIndex]:
        #DO: confirm that it returns a good value
        #DO: check that the "dictionary" here isn't a string that says "limit exceeded"
        if(type(dictionary) is dict):
            queryIndex += 1      
            userId = dictionary.get('login')
            if(userId is not None):
                level3testList.append(userId)


    print("userIds: " + str(testlist))
    print("Level 2 userIds: " + str(level2testList))
    print("Level 3 userIds: " + str(level3testList))

    print ("Full list of users from finalList: ")

    for dictionary in finalList:
        print(dictionary.get('login'))

    return json.dumps(finalList)

if __name__ == '__main__':
   # argument needs to be one argument (or 2). Otherwise can't call function
    #DO: need to validate data and reject if bad
    if(len(sys.argv) > 2):
        query_followers(sys.argv[1], sys.argv[2])
    else:
        query_followers(sys.argv[1])
