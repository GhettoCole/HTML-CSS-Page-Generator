# Programmer:   Given Lepita
# Project:  Web Page Generator
# Date: 2017


class HTMLStructure:

    htmlParagraphs = []
    navigationLinks = []
    footerTag = []
    metaData = [
        # meta characters
        "<meta charset='utf-8'>",
        # redirect to home in 1 second
        "<meta http-equiv='redirect(1) index.html'>",
        # description will be provided by user and formatted
        "<meta description='keyword' content='{}'>"
    ]

    def __init__(self, fileName='index.html'):
        self.fileName = fileName

    # incorporates a paragraph tag with a class --> content
    # for the purpose of style editing.
    def paragraphs(self, paragraph):
        self.htmlParagraphs.append("<p class='content'>{}</p>".format(paragraph))


    def navigationlinks(self, navLinks=('Home', 'Services', 'FAQ', 'Contact'), hyperlinkRef=['#' for x in range(4)]):
        '''
        # make a navigation system function.
        # set default links with no hyperlink ref
        # nav tag with nav-bar id for style editing
        '''

        if navLinks is not None and hyperlinkRef is not None:
            navLinks, hyperlinkRef = list(navLinks), list(hyperlinkRef)
        elif navLinks is None and hyperlinkRef is None:
            pass
        else:
            pass

        navSys = """
        <nav id='nav-bar'>
            <ul>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
            </ul>
        </nav>
        """.format(hyperlinkRef[0], navLinks[0],
                   hyperlinkRef[1], navLinks[1],
                   hyperlinkRef[2], navLinks[2],
                   hyperlinkRef[3], navLinks[3])

        self.navigationLinks.append(navSys)

    # def background(self, bgcolor):
    #     tag = """
    #         <style>
    #             body {
    #                 background-image: url('{}');
    #             }
    #         </style>
    #         """
    #     tag.format(bgcolor)
    #     self.styleTags.append(tag)
    def footer(self):
        owner = input("Enter Owner's name:  ")
        year = input("Year Created: ")
        copyright = input("Copyright business:  ")

        footerEle = """
<footer>
    <p class='owner'>
        Name:   {}<br/>
        Year:   {}<br/>
        Copyright:  &copy; {}
    </p>
</footer>
        """.format(owner, year, copyright)
        self.footerTag.append(footerEle)


    def basicHTML(self):
        title = input("Enter title for page:    ")
        h1 = input("Enter main heading:     ")
        stylesheet = "<link href='stylesheet.css' type='text/css' rel='stylesheet'>"
        content = ""
        for ptag in self.htmlParagraphs:
            if ptag is not None:
                content += ptag
            else:
                pass

        navSys = self.navigationLinks[0]
        code = """
<!DOCTYPE html>
    <head>
        <title>{}</title>
        {}
    </head>
    <body class='main-content'>
        <div class='container'>
            <div class='navigation'>
                {}
            </div>
            <section id='article-post'>
                <header>
                    <h1>{}</h1>
                </header>
                <article class='article-post'>
                    {}
                </artitle>
            </section>
            {}
        </div>
    </body>
</html>
        """.format(title, stylesheet, navSys, h1, content, self.footerTag[0])

        with open("index.html", "w") as file:
            file.write(code)
            file.flush()
            file.close()



def main():
    generator = HTMLStructure('index.html')
    keepAdding = True
    while keepAdding:
        keepGoing = input("Add another paragraph[Y/N]:")
        if keepGoing == "Y" or keepGoing == "y":
            par = input("Insert paragraph:    ")
            generator.paragraphs(par)
        elif keepGoing == "N" or keepGoing == "n":
            keepAdding = False
    # generator.background('#f4f4f4')
    generator.navigationlinks()
    generator.footer()
    generator.basicHTML()

if __name__ == '__main__':
    main()
