# Programmer:   Given
# Project:  Web Page Generator
# Date: 2017


class CascadingStyleSheet:
    def __init__(self, fileName='stylesheet.css'):
        self.fileName = fileName
        self.textFormat = """
body {
    background-image: url('bg.jpg');
    opacity: 0.5;
}
h1 {
    color: #f99c53;
    font: 35px Helvetica, sans-serif;
    text-align: center;
    text-transform: uppercase;
    text-decoration: none;
}
.main-content {
    margin: 0 auto;
    padding: 20px 15px;
    width: 95%;
    color: #c53;
    background-color: #ccc;
    border: 1px dashed #c53;
    box-sizing: border-box;
}

.container {
    padding-top: 15px;
    padding-bottom: 10px;
    padding-left: 5px;
    padding-right: 5px;
    width: 1005px;
    overflow: hidden;
    text-align: center;
}

div.navigation {
    clear: both;
    background-color: #f99c53;
    font-weight: normal;
    font-size: 16px;
    height: 100px;
    line-height: 50px;
    border-radius: 25px;
}

nav #nav-bar {
    padding-left: 45px;
    font: Monospace, sans-serif;
    color: #c53;
}
nav#nav-bar ul li {
    display: inline-block;
    text-decoration: none;
    padding-left: 45px;
    padding-right: 45px;
    padding-top: 25px;
    padding-bottom: 25px;
}

li:hover {
    background-color: grey;
    color: white;
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

    def add_rule(self, selector, properties):
        self.textFormat += f"\n{selector} {{\n"
        for prop, value in properties.items():
            self.textFormat += f"    {prop}: {value};\n"
        self.textFormat += "}\n"

    def dark_theme(self):
        activate = input("Activate DARK theme [Y/N]: ").upper()
        if activate == "Y":
            dark_theme_format = """
body {
    background-image: url('monokai.jpg');
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
    margin: 0 auto;
    padding: 20px 15px;
    width: 95%;
    color: #fff;
    background-color: #f3f3f3;
    border: 1px dashed #c53;
    box-sizing: border-box;
}

li:hover {
    background-color: #cf333;
    color: #c53;
    border-radius: 30px;
    border: 2px dashed;
}
"""
            self.textFormat += dark_theme_format

    def save_to_file(self):
        with open(self.fileName, "w") as file:
            file.write(self.textFormat)

def main():
    style = CascadingStyleSheet()
    style.dark_theme()  # Toggle dark theme
    style.add_rule("h2", {"color": "#00FF00", "font-size": "24px"})  # Add a new CSS rule
    style.save_to_file()

if __name__ == '__main__':
    main()
