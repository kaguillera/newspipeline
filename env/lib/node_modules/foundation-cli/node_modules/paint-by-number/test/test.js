var assert = require('assert');
var paint = require('../index');

describe('Paint', function() {
  it('colors a string, given a color map and palette', function() {
    var input  = 'Hello!';
    var colors = ' 01234';
    var palette = {
      ' ': 'default',
      0: 'red',
      1: 'yellow',
      2: 'green',
      3: 'blue',
      4: 'cyan'
    }

    var output = paint(input, colors, palette);
    console.log(output);
  });

  it('colors an array of strings, given a color map and palette', function() {
    var input  = ['John&', 'Paul&', 'Ringo&', 'George'];
    var colors = ['00000', '11111', '222222', '333333'];
    var palette = {
      0: 'bgBlue',
      1: 'bgRed',
      2: 'bgCyan',
      3: 'bgGreen'
    }

    var output = paint(input, colors, palette);
    console.log(output.join('\n'));
  });
});