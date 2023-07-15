showSlideHtml = '''
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