
import os
import sys
import flask

SLIDES_DIR = '_slides'
PORT = 8888

app = flask.Flask(__name__)
slides_path = os.path.join(os.path.dirname(__file__), SLIDES_DIR)

all_slides = []
for root, dirs, files in os.walk(slides_path):
    for f in files:
        if f.endswith('.md'):
            all_slides.append(os.path.join(root, f)[len(slides_path)+1:])

print('Slides path:', slides_path)
print('Available slides:' , all_slides)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/<path:path>')
def showSlide(path):
    if not path.endswith('.html'):
        path += '.html'
    return flask.render_template(path)

if __name__ == '__main__':
    app.run(debug=True,port=PORT)