selectSlidesHtml = '''
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
        var slideDataList = {slidesDataList};
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