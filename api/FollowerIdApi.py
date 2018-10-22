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

def get_followers(githubId, maxNumFollowers = 5):

    #per github v3 API, per_page allows for making a limit on 
    # returned items (up to 100). Without it, returns every follower 
    githubApiLink = "https://api.github.com/users/" + githubId + "/followers" \
        + "?per_page=" + str(maxNumFollowers)

    response = requests.get(githubApiLink)
    #Note: JSON response returned may be an error. Valid, but less useful.
    return response.json()

def query_followers(githubId, maxNumFollowers = 5):
    # Note, recursion won't work here because you need to break it at level 3
    # all variables will eventually be stored in response
    # 
    # Note: unauthenticated apps can only so may queries per minute and hour 
    # (might be as low as 60 queries per hour). at 3 levels of calls, 
    # 5 each, we're at 5^2 (first level is 5^0), or 25 calls a min.
    # To do more, app will need to be authenticated.
     
    finalList = []
    level1 = get_followers(githubId, maxNumFollowers)
    queryIndex = 0 #search start point for next round
    errMessage = [{"FollowerErrorMessage" : 
        "An unexpected error occurred. The data may or may not be truncated.\n \
         If you see this message repeatedly, it's likely your IP has been blocked \n \
         on the server. See https://developer.github.com/v3/#rate-limiting."}]

    # make sure before adding anything to the final list
    # that it's legit data.
    for dictionary in level1:
        if(type(dictionary) is dict):
            continue
        else: #not dictionary, may be error
            finalList.extend(errMessage)
            return finalList            

    finalList.extend(level1) #level1 is a list    
    stopIndex = len(finalList)

    # get second level of followers
    for dictionary in finalList[queryIndex : stopIndex]:
        if(type(dictionary) is dict):
            queryIndex += 1
            userId = dictionary.get('login')
            if(userId is not None):
                level2 = get_followers(userId, maxNumFollowers)
                finalList.extend(level2)
        else: #not dictionary, may be error
            finalList.extend(errMessage)
            return finalList

    #get third level of followers
    stopIndex = len(finalList)
    for dictionary in finalList[queryIndex : stopIndex]:
        if(type(dictionary) is dict):
            queryIndex += 1      
            userId = dictionary.get('login')
            if(userId is not None):
                level3 = get_followers(userId, maxNumFollowers)
                finalList.extend(level3)
        else: #not dictionary, may be error
            finalList.extend(errMessage)
            return finalList

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

      