
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

selectSlideHtml = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Slide</title>
</head>
<body>

    <h1>Available slides</h1>
    <ul>
        %(slides)s
    </ul>
</body>
</html>
'''


slideHtml = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Slide</title>
    <link rel="stylesheet" href="/static/css/reveal.css">
    <link rel="stylesheet" href="/static/css/theme/black.css">
    <link rel="stylesheet" href="/static/css/custom.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown data-separator="^\n\n\n" data-vertical="^\n\n" data-notes="^Note:">
                <textarea data-template>
                    %(slide)s
                </textarea>
            </section>
        </div>
    </div>
    <script src="/static/js/reveal.js"></script>
    <script>
        Reveal.initialize({
            controls: true,
            progress: true,
            history: true,
            center: true,
            transition: 'slide',
            dependencies: [
                { src: '/static/js/classList.js', condition: function() { return !document.body.classList; } },
                { src: '/static/js/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: '/static/js/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: '/static/js/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
                { src: '/static/js/zoom.js', async: true, condition: function() { return !!document.body.classList; } },
                { src: '/static/js/notes.js', async: true, condition: function() { return !!document.body.classList; } }
            ]
        });
    </script>
</body>
</html>
'''

slideHtmlWithCDN = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Slide</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/theme/black.css">
</head>
<body>
    <div class="reveal">
        <section data-markdown="../static/%(slide)s" data-separator="^\n\n\n" data-vertical="^\n\n" data-notes="^Note:">
        </section>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/lib/js/head.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/js/reveal.min.js"></script>
    <script>
        Reveal.initialize({
            controls: true,
            progress: true,
            history: true,
            center: true,
            transition: 'slide',
            dependencies: [
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/lib/js/classList.js', condition: function() { return !document.body.classList; } },
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/markdown/marked.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/markdown/markdown.js', condition: function() { return !!document.querySelector( '[data-markdown]' ); } },
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/highlight/highlight.js', callback: function() { hljs.initHighlightingOnLoad(); } },
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/zoom-js/zoom.js', condition: function() { return !!document.body.classList; } },
                { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/notes/notes.js', condition: function() { return !!document.body.classList; } }
            ]
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    # using selectSlideHtml
    return selectSlideHtml % {'slides': '\n'.join('<li><a href="/slide/%s">%s</a></li>' % (s, s) for s in all_slides)}

@app.route('/static/<path>')
def staticFiles(path):
    content = ''
    with open(os.path.join(slides_path, path), 'r') as f:
        content = f.read()
    
    return flask.make_response(content, 200, {'Content-Type': 'text/plain; charset=utf-8'})

@app.route('/slide/<path>')
def showSlide(path):
    # get content of slide
    # content = ''
    # with open(os.path.join(slides_path, path), 'r') as f:
    #     content = f.read()

    return slideHtmlWithCDN % {'slide': path}

if __name__ == '__main__':
    app.run(debug=True,port=PORT)