GitFollowers is an api endpoint designed to grab the followers of a given userId (up to 5 followers). 
It takes those followers and finds their followers (again, up to five followers)
It takes those followers and finds their followers (again, up to five followers per person).

For api implementation:

1) Make sure you have both git and python (3.7) installed locally, or that you are able to run both on your PC.

2) Download the code in this repo locally. Make sure that all files (FollowerId, api) are in the api folder

3) Start the api by running the api script on the command line (after navigating to the folder with the api from the command line, use "python api.py", without quotes. This may be slightly different depending on your python version and OS. This was done in Windows 10 in the terminal.)
Navigation tips: can do "cd" to change the directory (no quotes), and if you use quote marks around the file path, you don't have to
use escape characters on spaces in the file name. Ex: cd "C:\Downloads\VMTest\GitFollowers\api" , and then you can start the program.

4) Navigate the api by going to the appropriate page:

Homepage: http://127.0.0.1:5000/

Followers page: http://127.0.0.1:5000/api/v1/resources/followers?id=NAME&maxFollowers=NUMBER , replacing NAME with the username of the GitHub user searched for, and NUMBER with the max number of followers for the user you want returned (maximum is no more than 5 per user).
  Full example URL: http://127.0.0.1:5000/api/v1/resources/followers?id=jskeet&maxFollowers=2
  
  Note that:
  1) maxFollowers is an OPTIONAL parameter. It has a default of 5 followers. It can be omitted from the query without issue.
  2) maxFollowers will be capped at 5 to prevent timeouts on the PC (each call will increase the base by a power of 5. It will get large quickly).
 

Finally, this is an unauthenticated application. As such, there can only be so many requests from the same IP per hour before the user is prevented from using the website. 

From https://developer.github.com/v3/#rate-limiting:

"For unauthenticated requests, the rate limit allows for up to 60 requests per hour. Unauthenticated requests are associated with the originating IP address, and not the user making requests."


Testing and ways to test (if server is running from api.py script, clicking these links will produce the result described):

The easiest way to test this project is to just enter some data in the address bar. For example:

A user that doesn't exist: http://127.0.0.1:5000/api/v1/resources/followers?id=animeInaction
  - Produces error page.
  - Should produce the error message page.

A user that will have a very small (less than 5) result tree: http://127.0.0.1:5000/api/v1/resources/followers?id=DuilioAquino
  - Shows the small list of results (currently 3)
  - Shows code can handle small results with lots of dead ends

A user with no followers:http://127.0.0.1:5000/api/v1/resources/followers?id=AshleyBushCoding
  - Produces error page.
  - Shows code handles that exception appropriately

No user name: http://127.0.0.1:5000/api/v1/resources/followers
  - Produces error page.
  - Shows code will properly deal with missing entries
  
No user name but max followers:  http://127.0.0.1:5000/api/v1/resources/followers?maxFollowers=5 
  - Produces error page.
  - Shows code will properly deal with missing entries.
  
A user name with improper symbols: http://127.0.0.1:5000/api/v1/resources/followers?id=j^skeet
  - Produces error page.
  - Shows code will properly deal with invalid entries
  
A user that will return a full list regardless of follower size: http://127.0.0.1:5000/api/v1/resources/followers?id=jskeet&maxFollowers=5
  - Will produce the full tree, shows code can handle it

Repeated calls to trigger the IP block: http://127.0.0.1:5000/api/v1/resources/followers?id=jskeet&maxFollowers=5 done 2-3 times
  -Will display error message 
  -NOTE tester will be prevented from testing at this point for ~ 1 hr!!!


#####################################################################################################################################

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/AshleyBushCoding/GitFollowers/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/AshleyBushCoding/GitFollowers/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
