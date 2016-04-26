var gulp  = require('gulp')
var shell = require('gulp-shell')


gulp.task('jinja',
    shell.task(['python convert.py src/pages/markdown.md -o dist/markdown3.html']))

gulp.task('echo', shell.task([
  'echo hello',
  'echo world'
]))

gulp.task('default',
  gulp.series('echo', 'jinja'));
