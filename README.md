# Framer

## Required Downloads

### JSTalk

[JSTalk][jstalk] is required to automate Acorn. You can download it from the JSTalk website.

Note: Be sure that the <pre>jstalk</pre> application is in your path. I put
mine in /usr/local/bin/

[jstalk]:http://jstalk.org/

## Usage

<code>
  python framer.py DIRECTORY
</code>

This will parse all of the .png images in the directory you pass and frame
them. The framed images will be placed in an output folder titled <em>framed</em>.

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


