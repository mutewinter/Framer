# Framer

![It's life-changing!](https://github.com/mutewinter/Framer/raw/master/screenshots/framer_info.jpg)

## Description

For a detailed description of the creation and purpose of Framer, see [my blog post][blog].

[blog]:http://pileofturtles.com/2011/04/framer-an-ios-screenshot-creator/

## Required Downloads

### Acorn

You'll need [Acorn][acorn] to run this script. It's worth every penny. Seriously, buy it right now.

[acorn]:http://flyingmeat.com/acorn/

### JSTalk

[JSTalk][jstalk] is required to automate Acorn. You can download it from the JSTalk website.

Note: Be sure that the <code>jstalk</code> application is in your path. I put
mine in <code>/usr/local/bin/</code>

[jstalk]:http://jstalk.org/

## Usage

<code>
  python framer.py DIRECTORY
</code>

This will parse all of the .png images in the directory you pass and frame
them. The framed images will be placed in an output folder titled
<code>framed</code> (if it doesn't exist it will be created).

## Apple Resources Note

Make sure you go to the Apple [marketing site][marketing] and complete the [App Marketing
License Agreement][license].

[marketing]:http://developer.apple.com/appstore/resources/marketing/
[license]:https://developer.apple.com/appstore/AppStoreMarketingLicense.pdf

## Special Thanks To

Max Di Capua - [iPad 2 PSD][max]
[max]:http://maxdicapua.tumblr.com/post/3619140813

teehan+lax - [iPhone 4 PSD][tl]
[tl]:http://www.teehanlax.com/blog/2010/06/14/iphone-gui-psd-v4/

## Bugs

Quality can not be scripted for web export currently. Instead the quality will
be set to whatever the quality was last set to in Acorn. Open Web Export in
Acorn through File -> Web Export to change your quality settings. The creator
of Acorn is aware of this and has [notified me][notified] it will be fixed in Acorn 3.0.1.

[notified]:http://twitter.com/#!/ccgus/status/59799046776299521


## License

The MIT License

Copyright (c) 2011 Jeremy Mack, Pile of Turtles, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


