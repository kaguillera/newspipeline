#!/Users/kaguillera/Sandbox/virtualenvs/newspipeline/env/bin/python2.7
from livereload import Server, shell
server = Server()
server.watch('dist/*.html')
server.serve(root='dist')
