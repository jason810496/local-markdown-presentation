import os
from flask import Flask , make_response
from views.selectSlides import selectSlidesHtml
from views.showSlide import showSlideHtml

SLIDES_DIR = '_slides'
PORT = 8888

app = Flask(__name__ )
app.static_folder = 'static'

print( 'Current path:', os.path.dirname(__file__) )

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
    print('index' , selectSlidesHtml)
    # using selectSlideHtml
    slidesDataList = []
    for slide in all_slides:
        with open(os.path.join(slides_path, slide), 'r') as f:
            content = f.read()
            title = ''
            markdown_content = ''
            for line in content.split('\n'):
                if title == '' and line.startswith('# '):
                    title = line[2:]
                if len(markdown_content) < 200 and len(line) > 2:
                    markdown_content += line.strip() + ' '
                
                if title != '' and len(markdown_content)> 200 :
                    break

            slidesDataList.append({
                "name": slide,
                "title": title,
                "markdown_content": markdown_content
            })

    return selectSlidesHtml.replace('{slidesDataList}', str(slidesDataList) )

@app.route('/markdown/<name>')
def getMarkdownContent(name):
    if name not in all_slides:
        return make_response('Not Found', 404)

    with open(os.path.join(slides_path, name), 'r') as f:
        content = f.read()
    
    return make_response(content , 200, {'Content-Type': 'text/plain'} )

@app.route('/slide/<name>')
def showSlide(name):
    # using slideHtml
    return showSlideHtml.replace('{name}', name)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=False,port=PORT)