# Newsletter Pipepline

This project is about creating a system of producing email newsletters from templates
and markdown using the make command. The intention is that it will be as simple as it
is to generate a static site like Pelican. It is based on the Foundation for Emails 2
 framework but will be optimized for python users (at least this is the intention). 
The following will most likely be used (the list may most likely change:
![71430af3-14f7-496c-ad80-d95829130b2f](https://cloud.githubusercontent.com/assets/1266505/14922618/99d761cc-0e06-11e6-90e5-1eaef7fb6490.png)

- [x] [Github](https://github.com/)  - for the repository
- [x] [Markdown](https://daringfireball.net/projects/markdown/) - creating content
- [x] [Python-markdown](https://pythonhosted.org/Markdown/) - used to handle and change the markdown into HTML
- [x] [Make](http://www.gnu.org/software/make/) - controls the generation of of the resulting newsletter emails
- [ ] [Fabfile](http://www.fabfile.org/) - to help with the generation (not necessary)
- [x] [Gulp](http://gulpjs.com/) - Provides the facility to call tasks including but not limited to inline CSS
- [x] [SASS](http://sass-lang.com/) - The CSS generator
- [ ] [Python-livereload](https://livereload.readthedocs.io/en/latest/) - Shows the effects of changes on the fly
- [ ] [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/) or [Scrapy](http://scrapy.org/) - required to extract stuff out of websites
- [ ] [Mailchimp](http://mailchimp.com/) or similar - for actually sending out the email
- [x] [Jinja2](http://jinja.pocoo.org/)- the templating framework
- [x] [Foundation For Emails 2](http://foundation.zurb.com/emails.html) - is the framework that we will use for building responsive emails
- [ ] [Image compression](#) - Not sure what tool will be used for this. may come from most likely from F4E 2

## Concept/Idea
The overall idea is that we are building a jekell or pelican for email newsletters, 
You start with a chunk or chunks of markdown, call `make` you have an email newsletter
ready to send out on mailchimp. The newsletter templates are based on [Foundation for
Emails 2 (F4E 2)](http://foundation.zurb.com/emails.html). Very similar to Pelican the
static site generator. This is tricky because of the way email clients work. You have
to consider how to handle images etc. The markup for emails is based on tables since 
the email clients have limited support for modern CSS. F4E 2 helps it is not that user
friendly to python users among other things. 

### Heplful Links
- [html2text] (https://github.com/aaronsw/html2text)
- [Jinja tutorial] (http://packetpushers.net/python-jinja2-tutorial/)
- [Jinja Primer] (https://realpython.com/blog/python/primer-on-jinja-templating/)
- [Pelican](http://docs.getpelican.com/en/3.6.3/) & [Pelicanthemes](http://www.pelicanthemes.com/)
- [Alexandre Deschamps] (http://cakedown.alexandredeschamps.ca/)
- [A Guide to CSS Inlining in Email](https://litmus.com/blog/a-guide-to-css-inlining-in-email)
- Testing - [Litmus](https://litmus.com/) and [Email on Acid](https://www.emailonacid.com/)

### Requirements
Python 2.7
virtualenv 


### Install Guide
- Clone repo  
`$ git clone https://github.com/kaguillera/newspipeline.git`

- Change directory to project  
`$ cd newspipeline`

- Once in directory create a virtualenv using the following command  
`$ make env`

- Install requirements using pip  
`$ make install`

- Run the porject  
`$ make start`

As with the original Foundation for email project once it has been successfully 
installed and run your browser will open with the index page that would have been 
created in the `dist` directory.


### Other make options
- Reset project by deleting the `env` and `dist` directory  
`$ make clean`

- Calls the npm gulp build script  
`$ make build`

- As expected does everything. Clean, env, install and start.  
`$ make all`


### Plan of Action
*(for my personal use)*
- Produce Template and verify the presentation.
- Read in the Markdown file and produce HTML snippets
- Insert the output snippets into the HTML Template newsletter file.
- Convert the resulting HTML newsletter file into an CSS inline email file
- Output/write the resulting HTML CSS inline newsletter email file.

##### Problems/Issues

- The author may want different parts of the content to go in different places (e.g. make two columns) How do we implement that.
- It should work if the markdown files are changed or the templates are changed. i.e. ensure decoupling of templates and markdown component.

##### Ultimately:
We need to take the current F4E add Makefile, remove Panini and Handlebars and replace it with Jinja2, finally replace BrowserSync with Python-livereload. i.e. Pythonize F4E2

__Initial Foundation Directory Structure__
![screen shot 2016-04-29 at 11 46 25 am](https://cloud.githubusercontent.com/assets/1266505/14922643/c8a4ad3e-0e06-11e6-935e-df4e76ebae06.png)

__Estimated Resulting Directory Structure__
![screen shot 2016-04-29 at 11 46 38 am](https://cloud.githubusercontent.com/assets/1266505/14922647/ccc90b08-0e06-11e6-9dc8-84634d645e8b.png)


#### Progress/TODO

- [x] Read Pelican Documentation
- [x] Make a virtualenv for the project
- [x] Install nodejs (pip install virtual-node)
- [x] Install foundation-cli using nom (npm install —global foundation-cli)
- [x] Create a new foundation email project
- [x] Play around with it by making templates and emails based on the knolly
- [x] Make it run with make
- [x] Remove Handlebars bit by bit and replace with Jinja2 bit by bit
- [x] Create a repo in Github
- [ ] Remove Browersync and replace with python-livereload

