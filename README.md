# Local Markdown Presentation

This is a markdown presentation tool for local usage.

Features :
- Present markdown file in local
- Search markdown file by keywords with [fuse.js](https://www.fusejs.io/)
- Present markdown file with [reveal.js](https://revealjs.com/)

## Demo 

## Usage

## Installation
### Docker
```
docker rm -f presentation
docker rmi local-markdown-presentation
docker build -t local-markdown-presentation .
docker run -d -p 8888:8888 -v $(pwd)/_slides:/app/_slides --name presentation local-markdown-presentation

docker exec -it local-markdown-presentation-image sh

docker run -d -p 8765:8888 --name test local-markdown-presentation-image 

docker run -d -p 8384:8888 -v $(pwd)/_slides:/app/_slides --name presentation local-markdown-presentation
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

## Options

## Inspiration
This project is inspired by [hackmd.io](https://hackmd.io/) and [marp-cli](https://github.com/marp-team/marp-cli).<br>
I want to present markdown file in local with a simple tool like marp-cli but with UI presentation like hackmd.io .

## License  

[MIT]()
