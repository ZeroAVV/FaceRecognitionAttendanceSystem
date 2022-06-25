import webbrowser
url = 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=GFrJzkbtFjpZTLPgLBpRXFmtlHgRzHGZRGhKpzqzDKPsxpvdFMsGNVWXQxRgBwQwkbrW'

# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

webbrowser.get(chrome_path).open(url)