For api implementation:

1) Make sure you have both git and python (3.7) installed locally, or that you are able to run both on your PC.
2) Download the code in this repo locally. Make sure that all files (FollowerId, api) are in the api folder
3) Start the api by going to the appropriate page:

Homepage: http://127.0.0.1:5000/

Followers page: http://127.0.0.1:5000/api/v1/resources/followers?id=NAME&maxFollowers=NUMBER , replacing NAME with the username of the GitHub user searched for, and NUMBER with the max number of followers for the user you want returned (maximum is no more than 5 per user).
  Full example: http://127.0.0.1:5000/api/v1/resources/followers?id=jskeet&maxFollowers=2
  
  Note that maxFollowers will be capped at 5 to prevent timeouts on the PC (each call will increase the base by a power of 5. It will get large quickly).
  







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
