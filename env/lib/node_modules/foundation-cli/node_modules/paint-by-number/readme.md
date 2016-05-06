![Paint by Number](https://raw.githubusercontent.com/gakimball/paint-by-number/master/logo.png)

A small Node library for coloring ASCII art using color maps, which map a color to a character.

```bash
npm install paint-by-number
```

Let's say you have a string like this:

```
Rainbow!
```

Now you create a color map with a string of the same character length like this:

```
 0123456
```

Now you create a palette that maps [ANSI colors](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors) to the numbers.

```js
var palette = {
  0: 'red',
  1: 'yellow',
  2: 'green',
  3: 'cyan',
  4: 'blue',
  5: 'magenta',
  6: 'white'
}
```

Let's put it all together.

```js
var paint = require('paint-by-number');

var input  = 'Rainbow!';
var colors = ' 0123456';
var palette = {
  0: 'red',
  1: 'yellow',
  2: 'green',
  3: 'cyan',
  4: 'blue',
  5: 'magenta',
  6: 'white'
};

var output = paint(input, colors, palette);
process.stdout.write(output);
```

## paint(input, colors, palette)

Colors the characters of a string (or an array of strings) based on a color map and palette. Returns the same string or array, but colored.

### input

Type: `String` or `Array`

String or array of strings to be colored.

### colors

Type: `String` or `Array`

Color map to refer to when coloring the input string. The structure of `colors` should match that of `input`.

Every non-whitespace character in the color map is read and checked against the color palette. If a matching color is found, the character in the input string is colored. Use whitespace to indicate that a character should not be colored, which means it will use the user's command line default.

### palette

Type: `Object`

Color palette to use when reading the color map. The key is the character to use, and the value is the color to attach to that character. Any character can be a key, but a key must be a single character.

Characters are colored using [chalk](https://www.npmjs.com/package/chalk). Any function chalk has for coloring can be used as a palette color.

```js
var palette = {
  0: 'red',
  1: 'bgRed'
}
```

It's also possible to override the default color by adding a one-space key to the palette.

```js
var palette = {
  ' ': 'blue'
}
```
