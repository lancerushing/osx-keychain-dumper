
# Quick Key Chain Dumper

Tested on OS X El Capitan ver 10.11.6

## Setup 

Need to allow the "script editor" to access the user prompts.

1. Go to preferences
2. Open Security & Privacy
3. Click on the "Privacy" tab
4. Unlock the settings (bottom left)
5. Allow the "Script Editor.app" access
6. Lock the settings (bottom left)

## To Run 

1. Open "Script Editor"
2. paste in the [key-chain-dump-prompt.applescript](key-chain-dump-prompt.applescript)
3. click palay

Then:

1. Open "terminal"
2. Run the following:
````bash
	$ security dump-keychain -d > keychain_all.txt
````



# Notes to self

I used the Accessibility Inspector to determine the correct syntax for the apple script


## References

* https://developer.apple.com/legacy/library/documentation/Darwin/Reference/ManPages/man1/security.1.html
* https://gist.github.com/rmondello/b933231b1fcc83a7db0b
* https://stackoverflow.com/questions/16829450/how-to-enter-password-for-prompt-windows-using-applescript