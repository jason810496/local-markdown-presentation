import os
from flask import Flask , make_response , render_template_string
from views.selectSlides import selectSlidesHtml
from views.showSlide import showSlideHtml
from config import *

app = Flask(__name__ )
app.static_folder = 'static'

all_slides = []
def getLocalSlides():
    global all_slides
    all_slides = []
    for root, dirs, files in os.walk(slides_path):
        for f in files:
            if f.endswith('.md'):
                all_slides.append(os.path.join(root, f)[len(slides_path)+1:])
    print(f'{GREEN}Available slides:{ENDC}\n' , all_slides)

slides_path = os.path.join(os.path.dirname(__file__), SLIDES_DIR)
print('Slides path:', slides_path)

getLocalSlides()

@app.before_request
def before_request():
    print(f'{BLUE}Update slide_list in before_request{ENDC}')
    # update slides list before all requests
    getLocalSlides()

@app.route('/')
def index():
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
        print(f'{RED}Slide not found:{ENDC}', name)
        return make_response('Not Found', 404)

    with open(os.path.join(slides_path, name), 'r') as f:
        content = f.read()
    
    print(f'{GREEN}GET{ENDC} {name} {GREEN}content{ENDC} ')
    return make_response(content , 200, {'Content-Type': 'text/plain'} )

@app.route('/slide/<name>')
def showSlide(name):
    # using slideHtml
    return render_template_string(showSlideHtml, name=name, SLIDE_THEME=SLIDE_THEME, SYNTAX_HIGHLIGHT_LANG=SYNTAX_HIGHLIGHT_LANG, SYNTAX_HIGHLIGHT_THEME=SYNTAX_HIGHLIGHT_THEME, VERTICAL_SLIDE_SEPARATOR=VERTICAL_SLIDE_SEPARATOR, HORIZON_SLIDE_SEPARATOR=HORIZON_SLIDE_SEPARATOR)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=False,port=PORT)
