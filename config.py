# Setting variables
SLIDES_DIR = '_slides'
PORT = 8887
SLIDE_THEME = 'black' # https://revealjs.com/themes/
SYNTAX_HIGHLIGHT_LANG = ['python', 'javascript', 'html', 'css', 'bash' , 'json' ] # search https://cdnjs.com/libraries/highlight.js for all languages
SYNTAX_HIGHLIGHT_THEME = 'atom-one-dark' # search https://cdnjs.com/libraries/highlight.js for all themes
VERTICAL_SLIDE_SEPARATOR = '^\n----\n$' # https://github.com/hakimel/reveal.js/issues/929#issuecomment-80734215 for more info
HORIZON_SLIDE_SEPARATOR = '^\n---\n$'

# Colors for logging messages
GREEN = '\033[92m'
BLUE = '\033[94m'
RED = '\033[91m'
ENDC = '\033[0m'