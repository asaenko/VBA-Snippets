import sys
import webbrowser

query = ' '.join(sys.argv[1:])
webbrowser.open('https://www.google.ru/search?q=%22' + query + '%22')
