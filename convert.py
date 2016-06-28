#!/usr/bin/env python

import argparse
import sys

import jinja2
import markdown

from os import listdir, makedirs
from os.path import isfile, join, exists

reload(sys)
sys.setdefaultencoding('utf-8')

def main(args=None):
    src_path = 'src/pages'
    dist_path = 'dist'

    with open('src/layouts/template.html', 'r') as f:
        template = f.read() 
    
    if not exists(dist_path):
        makedirs(dist_path)
    
    onlyfiles = [f for f in listdir(src_path) if isfile(join(src_path, f))]
    for file in onlyfiles:
        name, ext = file.split('.')
        if ext == 'md':
            infile = join(src_path, file)
            outfile = '{}/{}.{}'.format(dist_path, name, 'html')
            title = "Markdown to HTML from {}".format(name)  
            
            with open(infile, 'r') as f:
                md = f.read() 
            html = markdown.markdown(md, output_format='html5')
            doc = jinja2.Template(template).render(body=html, subject=title)
            
            out = open(outfile, 'w')
            out.write(doc)
            out.close()

if __name__ == '__main__':
    sys.exit(main())
