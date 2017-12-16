# Programmer:   Given
# Project:  Web Page Generator
# Date: 2017


class CascadingStyleSheet:

    def __init__(self, fileName='stylesheet.css'):
        self.fileName = fileName

    def textFormatting(self):
        textFormat = """

body {
    background-image: url('bg.jpg');
    opacity: 0.5px;
}
h1 {
    color: #f99c53;
    font: 35px Helvetica, sans-serif;
    text-align: center;
    text-transform: smallcaps;
    text-decoration: none;
}
.main-content {
    margin:0 auto;
    padding: 20px 15px;
    width: 95%;
    color: #c53;
    background-color: #ccc;
    border: 1px dashed carol;
    border-size: border-box;
}

.container {
    /*margin: 720px;*/
    padding-top: 15px;
    padding-bottom: 10px;
    padding-left: 5px;
    padding-right: 5px;
    width: 1005;
    /*color: #fff;*/
    overflow: hidden;
    text-align: center;
}

div .navigation {
    clear: both;
    background-color: #f99c53;
    font-weight: normal;
    font-size: 16px;
    line-height: 1.6em;
    height: 100px;
    line-height: 50px;
    border-radius: 25px;
}

nav #nav-bar {
    padding-left: 45px;
    font: Monospace, sans;
    color: #c53;
}
nav#nav-bar ul li {
    display: inline-block;
    text-decoration: none;
    padding-left: 45px;
    padding-right: 45px;
    padding-top: 25px;
    padding-bottom: 25px;
   /* background-color: darkgrey;*/
}
li:hover {
    background-color: grey;
    color:white;
    border-style: dashed;
    border-radius: 30px;
}
footer {
    background-color: #f4f4f4;
    border-radius: 15px;
    color: #c53;
    padding: 20px 15px;
    line-height: 1.4em;
    font: Arial, Helvetica, sans-serif;
}


        """

        def darkTheme(self):
            activate = input("Activate DARK theme[Y/N]:  ")
            monokaiTheme = """
body {
    background-image: url('monokai');
    padding-top: 15px;
    padding-right: 25px;
    padding-bottom: 10px;
    padding-left: 25px;
    margin: 0 auto;
    color: #fff;
}
h1, h2, h3, h4, h5, h6 {
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    text-decoration: none;
}

.main-content {
    margin:0 auto;
    padding: 20px 15px;
    width: 95%;
    color: #fff;
    background-color: #f3f3f3;
    border: 1px dashed carol;
    border-size: border-box;
}            

li:hover {          
    background-color: #cf333;
    color: #c53;
    border-radius: 30px;
    border-style: 2px dashed;
}
            
            """


        with open("stylesheet.css", "w") as file:
            file.write(textFormat)
            file.flush()
            file.close()


def main():
    prototype = CascadingStyleSheet()
    prototype.textFormatting()

if __name__ == '__main__':
    main()
