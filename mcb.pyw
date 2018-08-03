# Multiclipboard
# Saves and loads pieces of text to the clipboard.

# Usage: 
# py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords and value pair to clipboard.
# py.exe mcb.pyw deleteall - Deletes all keywords from shelf.

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3:
	if sys.argv[1].lower() == 'save':
		mcbShelf[sys.argv[2]] = pyperclip.paste()
	elif sys.argv[1].lower() == 'delete':
		del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(zip(mcbShelf.keys(),mcbShelf.values()))))
	elif sys.argv[1].lower() == 'deleteall':
		mcbShelf.clear()
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
	else:
		print('Invalid argument')
else:
	print('Please provide some arguments')

mcbShelf.close()
