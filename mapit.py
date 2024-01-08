import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = "".join(sys.argv[1:])
    print(sys.argv[1:] )
    print(address)
else:
    # Get address from clipboard.
    address = pyperclip.paste()
#hfehjfj
webbrowser.open('https://www.google.com/maps/place/' + address)

print(" let us check if this is working")

#Checking the the pull request of the code 

