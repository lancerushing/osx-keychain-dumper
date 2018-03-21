
# OSX Key Chain Dumper

Tested on OS X El Capitan ver 10.11.6

Use case: You need to get your wifi passwords out for backup, or migration to another OS.

This process requires two parts: 

1. Running the 'security' command line tool.
2. An AppleScript to keep clicking "allow" and/or enter the admin password.

## Setup 

First, you need to allow the "script editor" access the security prompts.

1. Go to preferences
2. Open Security & Privacy
3. Click on the "Privacy" tab
4. Unlock the settings (bottom left)
5. Allow the "Script Editor.app" access
6. Lock the settings (bottom left)

## To Run 

1. Open "Script Editor"
2. paste in the [key-chain-dump-prompt.applescript](key-chain-dump-prompt.applescript)
3. Change your-username and your-password accordingly
4. click the "play" button

Then:

1. Open "terminal"
2. Run the following:
````bash
	$ security dump-keychain -d > keychain_all.txt
````

## Extract Wifi Credentials From Dump File

To extract the wifi ssids and passwords from the dump file, run the provided [extract-wifi.py](extract-wifi.py) python script.

````bash
        $ python extract-wifi.py  
````


# Notes to self

I used the Accessibility Inspector to determine the correct syntax for the apple script.


## References

* https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/security.1.html
* https://gist.github.com/rmondello/b933231b1fcc83a7db0b
* https://stackoverflow.com/questions/16829450/how-to-enter-password-for-prompt-windows-using-applescript
