

tell application "System Events"
	repeat while exists (processes where name is "SecurityAgent")
		tell process "SecurityAgent"
			try
				click button "Always Allow" of window 0
			on error
			
				set value of text field 1 of window 0 to "your-username"
				set value of text field 2 of window 0 to "your-password"
				
				click button "Allow" of window 0
				
			end try
		end tell
		delay 0.3
	end repeat
end tell