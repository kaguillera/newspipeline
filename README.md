This project is about creating a system of producing email newsletters from templates and markdown using the make command. The intention is that it will be as simple as it is to generate a static site like Pelican. It will be a Foundation for Emails 2 for python users. The following technologies/components/frameworks/languages will be used:

[x] Github - for the repository

[x] Markdown - creating content

[x] Python-markdown - used to handle and change the markdown into HTML

[ ] Make - controls the generation of of the resulting newsletter emails

[ ] Fabfile - to help with the generation (not necessary)

[ ] Gulp - Provides the facility to call tasks including but not limited to inline CSS

[x] SASS - The CSS generator

[ ] Python-livereload - Shows the effects of changes on the fly

[ ] Beautifulsoup or scrapy - required to extract stuff out of websites

[ ] Mailchimp or similar - for actually sending out the email

[x] Jinja2- the templating framework

[x] Foundation For Emails 2 - is the framework that we will use for building responsive emails

[ ] Image compression - Not sure what tool will be used for this. may come from most likely from F4E 2

The overall level we are building a jekell or pelican for email newsletters, You start with a chunk or chunks of markdown button and bam you have an email newsletter ready to send out on mailchimp.
The newsletter templates are based on http://foundation.zurb.com/emails/email-templates.html . Foundation for Emails 2 (F4E 2). Very similar to Pelican the static site generator. This is a lot tricker than you think because of the way email clients work. You have to consider how we are going to handle images etc. The markup for emails is based on tables since the email clients have limited support for modern CSS. F4E 2 helps but how do we render markdown to the Foundation Ink CSS. Well F4E 2 does a lot of the heavy lifting but how to take a generic markup format and turn it into the correct  Html and CSS that works with the various email clients.

Immediate Task

[x] Learn Foundation Ink (http://foundation.zurb.com/emails.html)

[x] Learn Markdown (https://daringfireball.net/projects/markdown/)

[x] Review html2text (https://github.com/aaronsw/html2text)

[x] Review Python-Markdown (http://pythonhosted.org/Markdown/index.html) - Progres: Python-Markdown Extra

[x] Learn Jinga2 (http://jinja.pocoo.org/docs/dev/templates/)

[x] Some tutorial (http://packetpushers.net/python-jinja2-tutorial/)

[x] Some tutorial (https://realpython.com/blog/python/primer-on-jinja-templating/)

[x] Look at Pelican & Pelicanthemes (http://docs.getpelican.com/en/3.6.3/) & (http://www.pelicanthemes.com/)

[x] Learn to convert from markdown to HTML/Foundation Ink

[ ] Learn Mailchimp API

NB:

- Write in markdown which is converted automatically into a responsive email Foundation for Emails (Ink) template by Alexandre Deschamps (http://cakedown.alexandredeschamps.ca/)

    - He created his own HTML-ish tags to simplify conversion from Markdown to HTML.
- jgallen23/grunt-inline-css - grunt-inline-css - Grunt task for turning an html file with linked css to inline css. Great for emails.
- A Guide to CSS Inlining in Email - Litmus Blog
- Testing - Litmus and Email on Acid

Note
Need to build the css and html from the markdown text depending in the template.??
Do we want to build the email directly from scratch using the markdown or just insert the markup content in a foundation ink template?
No need to change the css unless we want certain color scheme and such.

Considerations

- Make extensions for Markdown for special user defined HTML-like tags to allow less generic templates (see first bullet in NB above)

Constraints
Points to Note

- To send an HTML email just define the MIME type in the content/context head as part of the Meta data.
- The CSS and style must be inline and not internal or External. (i.e. <h1 style=“color:blue;”>)
- We will be using Gulp-inline for the inlining of the CSS
- Currently looking at Foundation for emails 2 (http://foundation.zurb.com/emails/docs/)

Input files

- Markdown file with the content of the newsletter
- HTML “template” file with the Foundation Ink CSS internal to the file with the basic format of the resulting output newsletter format. This file would contain header, footer, navbar etc. in it.

Ideas
Steps

- Produce Template and verify the presentation.
- Read in the Markdown file and produce HTML snippets
- Insert the output snippets into the HTML Template newsletter file.
- Convert the resulting HTML newsletter file into an CSS inline email file
- Output/write the resulting HTML CSS inline newsletter email file.

Problems/Issues

- The author may want different parts of the content to go in different places (e.g. make two columns) How do we implement that.
- It should work if the markdown files are changed or the templates are changed. i.e. ensure decoupling of templates and markdown component.

Ultimately:
We need to take the current F4E add Makefile, remove Panini and Handlebars and replace it with Jinja2, finally replace BrowserSync with Python-livereload. i.e. Pythonize F4E2

Approach

[x] Read Pelican Documentation

[x] Make a virtualenv for the project

[x] Install nodejs (pip install virtual-node)

[x] Install foundation-cli using nom (npm install —global foundation-cli)

[x] Create a new foundation email project

[x] Play around with it by making templates and emails based on the knolly

[ ] Make it run with make

[ ] Remove Handlebars bit by bit and replace with Jinja2 bit by bit

[ ] Create a repo in Github

[ ] Remove Browersync and replace with python-livereload

Initial Foundation Directory Structure

src
├── assets
│   ├── img
│   └── scss
│       ├── _settings.scss
│       └── app.scss
├── helpers
│   └── raw.js
├── layouts
│   └── default.html
├── pages
│   └── index.html
└── partials
 dist
├── css
│   └── app.css
└── index.html

Estimated Resulting Directory Structure

src
├── assets
│   ├── img
│   └── scss
│       ├── _settings.scss
│       └── app.scss
├── helpers
│   └── raw.js
├── templates
│   └── default.html
├── emails
       └── index.html

Self notes

- Gulp is the task runner. I need to see what tasks Gulp is calling and argument this with Makefile so that I can either circumvent the call to Panini and Handlebars or make it call Jinja2.
- Depending on if I can call Jinja2 with Gulp then I will know how I need to use Make. Why? Because if I can call Jinja 2 to to do what Panini and Handlebars are doing then I can just replace that code in the gulp call if not then I have to remove the call in Gulp and call Jinja 2 directly in the make file.
- npm start workflow - This command runs the script specified in package.js. In the case of this project that is `gulp` which can be instructions are found on the `gulpfile.babel.js`. This file does the requirement importing and then runs the necessary tasks. So I have three options:
    - Let make call Jinja
    - Let npm call Jinja
    - Let gulp call Jinja
- I intend to let Gulp call Jinja if not then npm (which I think is impossible) if not then finally let make call Jinja which I know for sure can be done.
- I figured out how to run an external script using gulp and NPM. The next step I am going to try is to set up Jinja 2 and run it using gulp/npm
    - Install Jinja in project
    - then set it up
    - Run it with gulp
    - I was successfully able to run a script that imported Jinja and ran a template rendering. The next step is to make it do this with files. i.e. template and markup.
- Stepping back a little.

    - [x] I am going to makeup a markdown file and let the vanilla F4E2 produce the resulting HTML for it. The Markdown was placed in the  following tags
        - <container> {{#markdown}} /* markdown content*/  {{/markdown}} </container>

    - [x] Then I am going to write a python script using Jinja to convert the same markdown and a template hoping that it creates similar results. I installed python-markdown by using $ pip install markdown

    - [ ] Need to us an external template and consider how to get all files in a directory like required.

    - [ ] Finally let Gulp call the python script possible placing that call in the gulpfile.babel.js file.

