class HTML_Generator:
    def __init__(self, file_name='index.html'):
        self.file_name = file_name

    def __str__(self):
        return self.file_name

    def meta_data_tags(self, keywords, content_description="Generator"):
        meta_data = [
            "<meta name='viewport' content='width=device-width, initial-scale=1'>",
            "<meta charset='utf-8'>",
            "<meta http-equiv='X-UA-Compatible' content='IE=edge'>",
            "<meta description='{}' content='{}'>"
        ]
        meta_data[3] = meta_data[3].format(keywords, content_description)
        return ''.join(meta_data)

    def dividers_tags(self, tag_type):
        data = input("Enter Information:    ")
        if not data:
            return "Data needed for a divider"
        
        if tag_type == 'div':
            return "\n\t<div> {} </div>\t\n".format(data)
        elif tag_type == 'section':
            return """
            <section>
                <div>
                    {}
                </div>
            </section>
            """.format(data)
        elif tag_type == 'aside':
            return """
            <div>
                <aside>
                    {}
                </aside>
            </div>
            """.format(data)
        elif tag_type == 'header':
            return """
                <header>
                    {}
                </header>
            """.format(data)
        elif tag_type == 'span':
            return """
            <div>
                <span>
                    {}
                </span>
            </div>
            """.format(data)
        else:
            return ""

    def paragraph_tag(self, data):
        return "<p> {} </p>".format(data)

    def image_tag(self, src=None, alt=None, height=450, width=720, border=None):
        if src and alt:
            if isinstance(height, int) and isinstance(width, int):
                return """
                <img src='{}' alt='{}' width='{}' height='{}'/><br/>
            """.format(src, alt, width, height)
        return "<img src='' alt='NO IMAGE FOUND'><br/>"

    def break_line_tag(self):
        return "<br/>"

    def video_tag(self, src=None, _type='video/mp4'):
        if src:
            return """
                <video loop controls autoplay preload>
                    <source src='{}' type='{}'>
                </video>
            """.format(src, _type)
        else:
            return ""

    def audio_tag(self, src=None, _type='video/mp4'):
        if src:
            return """
                <audio loop controls autoplay preload>
                    <source src='{}' type='{}'>
                </audio>
            """.format(src, _type)
        else:
            return ""

    def header_tags(self, _type=2, data="Heading"):
        if _type in range(1, 7):
            return "<h{}> {} </h{}>".format(_type, data, _type)
        else:
            return "Error: Header does not exist"

    def nav_links_tags(self, nav_links=('Home', 'Services', 'FAQ', 'Contact'), href=("#",) * 4):
        nav_sys = """
        <nav id='nav-bar'>
            <ul>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
            </ul>
        </nav>
        """.format(*href, *nav_links)
        return nav_sys

    def footer_tag(self, data):
        return """
        <footer>
            {}
        </footer>
        """.format(data)

    def horizontal_line_tag(self, border=2):
        return "<hr border='{}'/>".format(border)

    def text_formatting_tags(self, style, data, sub_data=None, sup_data=None):
        style = style.lower()
        if style == "b":
            return "<p><b>{}</b></p>".format(data)
        elif style == "big":
            return "<p><big>{}</big></p>".format(data)
        elif style == "small":
            return "<p><small>{}</small></p>".format(data)
        elif style in ("i", "italic"):
            return "<p><i>{}</i></p>".format(data)
        elif style == "sup":
            return "<p>{}<sup>{}</sup></p>".format(data, sup_data)
        elif style == "sub":
            return "<p>{}<sub>{}</sub></p>".format(data, sub_data)
        elif style in ("del", "deleted"):
            return "<p><del>{}</del></p>".format(data)
        elif style in ("ins", "inserted"):
            return "<p><ins>{}</ins></p>".format(data)
        elif style == "strong":
            return "<p><strong>{}</strong></p>".format(data)
        else:
            return "That text format has not yet been added or is unknown"


def main():
    generator = HTML_Generator()
    file = open('index.html', 'wb')
    opts = [
        '--metadata', '--dividers', '--paragraph', '--image',
        '--header', '--text-formatting', '--footer', '--line',
        '--comment', '--nav-links', '--video', '--audio', '--break-line'
    ]

    def display_information():
        nonlocal opts
        info = [
            'Provides metadata feature', 'Provides divider functionality',
            'Enables paragraph creation', 'Enables image creation',
            'Enables header creation', 'Enables text-formatting options',
            'Enables creation of footers', 'Enables creation of a <hr> tag',
            'Enables commenting', 'Creates navigation links',
            'Enables video tag creation', 'Enables audio tag creation',
            'Enables <br> tag'
        ]
        for i, opt in enumerate(opts, 1):
            print(i, "-", opt, ":", info[i - 1])

    _help = input("Do you need help (Y/N): ")
    if _help.lower() in ('y', 'yes'):
        return display_information()

    stop = False
    while not stop:
        input_tag = input("Enter tag (--metadata etc.): ")
        if input_tag == "--metadata":
            keywords = input("Enter keywords: ")
            content_description = input("Enter content description: ")
            if keywords:
                file.write(generator.meta_data_tags(keywords, content_description))
        elif input_tag == "--dividers":
            tag_type = input("Enter tag type (div, section, aside, header, span): ")
            file.write(generator.dividers_tags(tag_type))
        elif input_tag == "--paragraph":
            data = input("Enter paragraph data: ")
            if data:
                file.write(generator.paragraph_tag(data))
        elif input_tag == "--image":
            src = input("Enter image's path relative to the site's directory: ")
            alt = input("Enter alternative text, in case the image doesn't show: ")
            height = int(input("Enter image height: "))
            width = int(input("Enter image width: "))
            file.write(generator.image_tag(src, alt, height, width))
        elif input_tag == "--header":
            header_data = input("Enter header information: ")
            header_type = int(input("Enter header type (1-6): "))
            file.write(generator.header_tags(header_type, header_data))
        elif input_tag == "--comment":
            data = input("Enter comment data: ")
            if data:
                file.write(generator.comment(data))
        elif input_tag == "--nav-links":
            nav_links = input("Enter navigation links (separated by commas): ").split(",")
            href = input("Enter href values (separated by commas): ").split(",")
            file.write(generator.nav_links_tags(nav_links, href))
        elif input_tag == "--line":
            border = int(input("Enter border width: "))
            file.write(generator.horizontal_line_tag(border))
        elif input_tag == "--break-line":
            file.write(generator.break_line_tag())
        elif input_tag == "--video":
            src = input("Enter video source: ")
            file.write(generator.video_tag(src))
        elif input_tag == "--audio":
            src = input("Enter audio source: ")
            file.write(generator.audio_tag(src))
        else:
            stop = True

    file.close()


if __name__ == "__main__":
    main()
