
import os
import sys
import flask

SLIDES_DIR = '_slides'
PORT = 8888

app = flask.Flask(__name__)
# add static path
app.static_folder = 'static'


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
<html >

<head>
    <meta charset="utf-8">
    <!-- test search cdn -->
    <script src="https://cdn.jsdelivr.net/npm/fuse.js@6.6.2"></script>
    <!-- boostwrap cdn -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">
    <title>Select Slide</title>
    <link rel="apple-touch-icon" sizes="180x180" href="static/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="static/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="static/favicons/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
</head>

<body data-bs-theme="dark">
    <nav class="navbar justify-content-md-between px-4" style="background-color: rgba(255, 255, 255, 0.15);">
    <div>
        <img class="navbar-brand" src="static/images/logo.png" height="40px" style="padding:0;margin:0 0.75rem 0 0; border-radius:0.5rem;" >
        <a class="navbar-brand">Local Markdown Presentation</a>
    </div>
       
        
        <div class="form-inline" data-bs-theme="dark">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" onkeyup="search(event)" style="background-color:#272e34;" >
        </div>
    </nav>
    <div class="my-4" id="slideList" >

    </div>

    <div id="card-template" style="visibility: hidden; position:fixed;">
        <div class="card m-auto mb-3" style="background-color: #272e34; width: 30rem;">
            <div class="card-body">
                <div class="d-flex justify-content-between">
                    <div>
                        <h5 class="card-title mb-3">Demo 1</h5>
                        <div class="card-text" style="margin: 0 5rem 0.75rem 1rem; overflow: hidden; display: -webkit-box; -webkit-box-orient: vertical; -webkit-line-clamp: 3; white-space: pre-wrap;">Slide 1</div>
                        <pre class="card-name mb-0">Markdown.md</pre>
                    </div>
                    <div class="d-flex flex-column justify-content-center">
                        <a class="btn btn-primary" href="slide/name.md">Select</a>
                    </div>
                </div>
                
            </div>
        </div>
    </div>
    

    <script>
        // slideList
        var slideDataList = {slidesData};
    </script>
    <script>
        var options = {
            // shouldSort: true,
            // threshold: 0.6,
            // location: 0,
            // distance: 100,
            // maxPatternLength: 32,
            // minMatchCharLength: 1,
            keys: [
                "name",
                "title",
            ]
        };

        var fuse = new Fuse(slideDataList, options);
        var result = fuse.search("md");
        console.log(result);

        var slideList = document.getElementById("slideList");
        var cardTemplate = document.getElementById("card-template").children[0];

        console.log( "slideList", slideList )
        console.log( "cardTemplate", cardTemplate )
        for (let i = 0; i < result.length; i++) {
            slideList.appendChild( createCard( result[i].item.name , result[i].item.title , result[i].item.markdown_content ));
        }

        function createCard( name , title , markdown_content ){
            const clone = cardTemplate.cloneNode(true);
            clone.setAttribute("id", "");
            clone.querySelector(".card-title").innerHTML = title;
            clone.querySelector(".card-text").innerHTML = markdown_content;
            clone.querySelector(".card-name").innerHTML = name;
            clone.querySelector(".btn").setAttribute("href", "slide/" + name);
            return clone;
        }

        function search(event) {
            event.preventDefault();
            // clear slideList
            slideList.innerHTML = "";
            
            const searchValue = document.querySelector("input").value;
            console.log("searchValue" , searchValue );
            console.log(searchValue);
            const result = fuse.search(searchValue=="" ? "md": searchValue );
            console.log(result);

            for (let i = 0; i < result.length; i++) {
                slideList.appendChild( createCard( result[i].item.name , result[i].item.title , result[i].item.markdown_content ));
            }

        }
    </script>
</body>

</html>
'''

slideHtml = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Slide</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/css/theme/black.css">
    

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css">
    <!-- add other language support : pyhton3 , cpp , javascript  ,bash , json -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/cpp.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/javascript.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/bash.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/json.min.js"></script>

    <title>Slide</title>
    <link rel="apple-touch-icon" sizes="180x180" href="static/favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="static/favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="static/favicons/favicon-16x16.png">
    <link rel="manifest" href="/site.webmanifest">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="../markdown/{name} " data-separator="^\n---\n$" data-separator-vertical="^\n----\n$" data-notes="^Note:"></section>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/lib/js/head.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/js/reveal.min.js"></script>
    <script>
        document.addEventListener("readystatechange", function(event) {
            // initialize Reveal
            Reveal.initialize({
                width: '100%',
                height: '100%',
                controls: true,
                progress: true,
                slideNumber: true,
                keyboard: true,
                history: true,
                center: true,
                transition: 'slide',
                dependencies: [
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/lib/js/classList.js', condition: function () { return !document.body.classList; } },
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/markdown/marked.js', condition: function () { return !!document.querySelector('[data-markdown]'); } },
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/markdown/markdown.js', condition: function () { return !!document.querySelector('[data-markdown]'); } },
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/highlight/highlight.js', callback: function () { hljs.initHighlightingOnLoad(); } },
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/zoom-js/zoom.js' },
                    { src: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.6.0/plugin/notes/notes.js' }
                ]
            });
        });
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    # using selectSlideHtml
    slidesData = []
    for slide in all_slides:
        with open(os.path.join(slides_path, slide), 'r') as f:
            content = f.read()
            # title = first `#` appeared line
            title = ''
            markdown_content = ''
            for line in content.split('\n'):
                if title == '' and line.startswith('# '):
                    title = line[2:]
                if len(markdown_content) < 200 and len(line) > 2:
                    markdown_content += line.strip() + ' '
                
                if title != '' and len(markdown_content)> 200 :
                    break

            slidesData.append({
                "name": slide,
                "title": title,
                "markdown_content": markdown_content
            })
    return selectSlideHtml.replace('{slidesData}', str(slidesData))
    return selectSlideHtml % {'slides': '\n'.join('<li><a href="/slide/%s">%s</a></li>' % (s, s) for s in all_slides)}

# @app.route('/static/<path:path>')
# def getStaticFile(path):
#     return flask.send_from_directory('static', path)

@app.route('/markdown/<name>')
def getMarkdownContent(name):
    return flask.send_from_directory('_slides', name)

@app.route('/slide/<name>')
def showSlide(name):
    # using slideHtml
    return slideHtml.replace('{name}', name)


if __name__ == '__main__':
    app.run(debug=True,port=PORT)