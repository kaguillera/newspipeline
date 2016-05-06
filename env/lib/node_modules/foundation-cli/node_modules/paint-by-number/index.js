var chalk = require('chalk');

module.exports = paint;

function paint(input, colors, palette) {
  var string = typeof input === 'string'
  var output = [];
  var defaultColor = palette[' '] || null;
  
  if (string) {
    input = [input];
    colors = [colors];
  }

  // Iterate through each line of the input
  for (var l in input) {
    var line = input[l];
    var newLine = '';

    // Iterate through each character of the line
    for (var ch = 0; ch < line.length; ch++) {
      // Find the color on the map that matches the character
      var newChar = line[ch];
      var color = colors[l] && palette[colors[l][ch] || defaultColor];

      if (color && chalk[color]) {
        newChar = chalk[color](line[ch]);
      }

      newLine += newChar;
    }

    output.push(newLine);
  }

  if (string) {
    return output[0];
  }
  return output;
}
