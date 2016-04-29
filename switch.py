from os import rename
import sys

usage = """
usage: switch.py [version]

Back up one version and change to another version

only version options:
  --to-orig         Back the Jinja script files and activate original scripts
  --to-jinja        Back the original script files and activate Jinja scripts
"""

if __name__ == '__main__':
    
    if len(sys.argv) == 1:
        print usage
    elif sys.argv[1] == "--to-orig":
        try:
            print "Backing up Jinja scripts..."
            rename('gulpfile.js','gulpfile.js.jinja')
            rename('package.json','package.json.jinja')
            print "Activating original scripts..."
            rename('gulpfile.babel.js.orig','gulpfile.babel.js')
            rename('package.json.orig','package.json')
        except:
            print "Already in original state!!"
    elif sys.argv[1] == "--to-jinja":
        try:
            print "Backing up original scripts..."
            rename('gulpfile.babel.js','gulpfile.babel.js.orig')
            rename('package.json','package.json.orig')
            print "Activating Jinja scripts..."
            rename('gulpfile.js.jinja','gulpfile.js')
            rename('package.json.jinja','package.json')
        except:
            print "Already in Jinja state!!"
    else:
        print usage
    
        
