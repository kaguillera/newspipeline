#!/usr/bin/env python

import argparse
import sys

import jinja2
import markdown

from os import listdir
from os.path import isfile, join

reload(sys)
sys.setdefaultencoding('utf-8')

def parse_args(args=None):
    d = 'Make a complete, styled HTML document from a Markdown file.'
    parser = argparse.ArgumentParser(description=d)
    parser.add_argument('mdfile', type=argparse.FileType('r'), nargs='?',
                        default=sys.stdin,
                        help='File to convert. Defaults to stdin.')
    parser.add_argument('-o', '--out', type=argparse.FileType('w'),
                        default=sys.stdout,
                        help='Output file name. Defaults to stdout.')
    return parser.parse_args(args)


def main(args=None):
    src_path = 'src/pages'
    dist_path = 'dist'
    with open('src/layouts/template.html', 'r') as f:
        template = f.read() 
    
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
            
            with open(outfile, 'w') as out :
                 out.write(doc)


if __name__ == '__main__':
    sys.exit(main())
