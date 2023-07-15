# Local Markdown Presentation

This is a markdown presentation tool for local usage.

Features :
- Present markdown file from local server
- Search markdown file by keywords with [fuse.js](https://www.fusejs.io/)
- Present markdown file with [reveal.js](https://revealjs.com/)

## Demo

https://github.com/jason810496/local-markdown-presentation/assets/68415893/2ba99ca1-017b-4574-b21b-d12c3f0e48fe

## Usage
```bash
git clone https://github.com/jason810496/local-presentation.git
# installation : see below
``` 

Replace your markdown file in `_slides` folder and run the server.
```bash
python3 app.py
```

Open your browser and go to `http://localhost:8888/` to select your presentation markdown file. <br>
Search your markdown file by keywords in the right top corner.

## Installation
### Docker
```
docker build -t local-markdown-presentation .
docker run -d -p 8888:8888 -v $(pwd)/_slides:/app/_slides --name presentation local-markdown-presentation
```

### Poetry
```
poetry install
poetry shell
```

### Manual (pip venv)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Dependencies
- Python version >= 3.6.0
- Python Packages
    - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
- Js lib from CDN
    - [reveal.js](https://revealjs.com/)
    - [fuse.js](https://www.fusejs.io/)

## Customization
All the configuration is in `config.py` file.

```python
# Setting variables
SLIDES_DIR = '_slides'
PORT = 8888
SLIDE_THEME = 'black' # https://revealjs.com/themes/
SYNTAX_HIGHLIGHT_LANG = ['python', 'javascript', 'html', 'css', 'bash' , 'json' ] # search https://cdnjs.com/libraries/highlight.js for all languages
SYNTAX_HIGHLIGHT_THEME = 'atom-one-dark' # search https://cdnjs.com/libraries/highlight.js for all themes
VERTICAL_SLIDE_SEPARATOR = '^\n----\n$'
HORIZON_SLIDE_SEPARATOR = '^\n---\n$'
```
( in `config.py` )

### Markdown file directory
Replace `_slides`with your markdown file folder for `SLIDES_DIR`.

Note : 
- if using `docker`, change the volume path in `docker run` command.
- `docker run ... -v $(pwd)/SLIDES_DIR:/app/_slides ...`
### Server port
Replace `8888` with your port number for `PORT`.

Note : 
- if using `docker`, change the expose mapping in `docker run` command.
- `docker run ... -p PORT:8888 ...`
### Other presentation themes
Replace `black` with your theme name for `SLIDE_THEME`.

All the themes can be found in [reveal.js theme](https://revealjs.com/themes/).
### Markdown page separator
- Replace `^\n---\n$` with your separator for `HORIZON_SLIDE_SEPARATOR`.
- Replace `^\n----\n$` with your separator for `VERTICAL_SLIDE_SEPARATOR`.

Note :
- The separator is a regular expression.
- The default separator is `^\n---\n$` for horizontal slide and `^\n----\n$` for vertical slide.
- Check this [reveal.js Markdown example](https://github.com/hakimel/reveal.js/blob/master/examples/markdown.html) and [this github issue](https://github.com/hakimel/reveal.js/issues/929#issuecomment-80734215) for more information.
- CND link : https://cdnjs.com/libraries/reveal.js
### Other languages syntax highlight
- Replace `['python', 'javascript', 'html', 'css', 'bash' , 'json' ]` with your languages for `SYNTAX_HIGHLIGHT_LANG`.

Note :
- The languages can be found in [highlight.js](https://cdnjs.com/libraries/highlight.js).
- CND link : https://cdnjs.com/libraries/highlight.js

## Inspiration
This project is inspired by [hackmd.io](https://hackmd.io/) and [marp-cli](https://github.com/marp-team/marp-cli).<br>
I want to present markdown file in local with a simple tool like marp-cli but with UI presentation like hackmd.io .

## License  

> MIT License
