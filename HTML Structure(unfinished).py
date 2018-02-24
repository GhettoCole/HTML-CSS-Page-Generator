# Programmer: Given Lepita
# Project: Web Page Generator
# Date: 2018


class HTML_Generator:

    def __init__(self, file_name='index.html'):
        self.file_name = file_name

    def __str__(self):
        return repr(self.file_name)[1:-1]

    def meta_data_tags(self, keywords, content_description="Generator"):

        # meta data tags for the head section
        meta_data = [
            "<meta name='viewport' content='width=device-width, initial-scale=1'>",
            "<meta charset='utf-8'>",
            "<meta http-equiv='X-UA-Compatible' content='IE=edge'>",
            "<meta description='{}' content='{}'>"
        ]
        meta_data[3].format(keywords, content_description)
        return repr(meta_data)[1:-1]

    def dividers_tags(div=True, section=False, aside=False, header=False, span=False):
        data = input("Enter Information:    ")
        try:
            if data is not None or data != "":
                if div is True:
                    return "\n\t<div> {} </div>\t\n".format(data)
                elif section is True:
                    return """
                    <section>
                        <div>
                            {}
                        </div>
                    </section>
                    """.format(data)
                elif aside is True:
                    return """
                    <div>
                        <aside>
                            {}
                        <aside>
                    </div>
                    """.format(data)
                elif header is True:
                    return """
                        <header>
                            {}
                        </header>
                    """.format(data)
                elif span is True:
                    return """
                    <div>
                        <span>
                            {}
                        </span>
                    <div>
                    """.format(data)
                else:
                    return ""
            else:
                return "Data needed for a divider"
        except Exception as e:
            print("Error:  ", e)

    def paragraph_tag(self, data):
        return "<p> {} </p>".format(data)

    def image_tag(self, src=None, alt=None, height=450, width=720, border=None):
        if src is None and alt is None:
            return False
        if src is not None and (alt is None or alt is not None):
            if type(height) is not str and type(width) is not str:
                return """
                <img src={0} alt={1} width="{2}" height={3}/></br>
            """.format(src, alt, width, height)
        else:
            return "<img src='' alt='NO IMAGE FOUND'></br>"

    def break_line_tag(self):
        return "</br>"

    def video_tag(self, loop=True, controls=True, autoplay=True, src=None, _type='video/mp4'):
        if loop is True and controls is True and autoplay is True and src is not None:
            return """
                <video loop controls autoplay preload>
                    <source src={0} type={1}>
                </video>
            """.format(src, _type)
        else:
            return """
                <video controls preload>
                    <source src={0} type={}>
                </video>
            """.format(src, _type)

    def audio_tag(self, loop=True, controls=True, autoplay=True, src=None, _type='video/mp4'):
        if loop is True and controls is True and autoplay is True and src is not None:
            return """
                <audio loop controls autoplay preload>
                    <source src={0} type={1}>
                </audio>
            """.format(src, _type)
        else:
            return """
                <audio controls preload>
                    <source src={0} type={}>
                </audio>
            """.format(src, _type)

    def header_tags(self, _type=2, data="Heading"):
        if _type is not None:
            if _type == 1:
                return "<h1> {} </h1>".format(data)
            elif _type == 2:
                return "<h2> {} </h2>".format(data)
            elif _type == 3:
                return "<h3> {} </h3>".format(data)
            elif _type == 4:
                return "<h4> {} </h4>".format(data)
            elif _type == 5:
                return "<h5> {} </h5>".format(data)
            elif _type == 6:
                return "<h6> {} </h6>".format(data)
            elif _type > 6 or _type < 0:
                return "Error: Header does not exist"
            else:
                pass
        else:
            return "Error: Header not given"

    def nav_links_tags(self, navLinks=(
        'Home', 'Services', 'FAQ', 'Contact'),
        href=["#" for x in range(4)]):

        '''
        # make a navigation system function.
        # set default links with no hyperlink ref
        # nav tag with nav-bar id for style editing
        '''

        if navLinks is not None and href is not None:
            nav_links, href = list(navLinks), list(href)
        else:
            pass

        nav_sys = """
        <nav id='nav-bar'>
            <ul>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
                <li><a href='{}'>{}</a></li>
            </ul>
        </nav>
        """.format(
            href[0], nav_links[0],
            href[1], nav_links[1],
            href[2], nav_links[2],
            href[3], nav_links[3]
        )
        return nav_sys

    def back_ground(self, color='#f99c53', image='background.jpg'):
        content = None
        if color is None:
            if image is not None:
                content = """
                body {
                    background-image: url('images/background.jpg');
                }
                """
            if image is None:
                return False
        if color is not None:
            if image is None:
                content = """
                body {
                    background-color: #C44F13;
                }
                """
        try:
            file = open('stylesheet.css', 'a')
            if file:
                file.write(content)
                file.close()
            else:
                pass
        except FileNotFoundError:
            return "File Not Found"

    def form_section_tag(self, method='post', action='email.php', required=True, label="Name",
                        name='Name', email="ghettocole@gmail", tel='011-5953-232', subject='News', msg='MSG',
                    Company='ltd pty registered'):
        if required is True:
            required = "required"
        else:
            required = "N/A"
        content = """
        <form id="main-contact-form" class="contact-form" name="contact-form" method="{0}" action="{1}">
                    <div class="col-sm-5 col-sm-offset-1">
                        <div class="form-group">
                            <label>{3}</label>
                            <input type="text" name="name" class="form-control" required="{2}">
                        </div>
                        <div class="form-group">
                            <label>{3}</label>
                            <input type="email" name="email" class="form-control" required="{2}">
                        </div>
                        <div class="form-group">
                            <label>{3}</label>
                            <input type="number" class="form-control">
                        </div>
                        <div class="form-group">
                            <label>{3}</label>
                            <input type="text" class="form-control">
                        </div>
                    </div>
                    <div class="col-sm-5">
                        <div class="form-group">
                            <label>{3}</label>
                            <input type="text" name="subject" class="form-control" required="{2}">
                        </div>
                        <div class="form-group">
                            <label>{3}</label>
                            <textarea name="message" id="message" required="required" class="form-control" rows="8"></textarea>
                        </div>
                        <div class="form-group">
                            <button type="submit" name="submit" class="btn btn-primary btn-lg" required="{2}">Submit Message</button>
                        </div>
                    </div>
                </form>

        """.format(method, action, required)

    def link_tag(href="google.com", target='_blank'):
        return """
        <a href='{}' target='{}'></a>
        """.format(href, target)

    def ordered_list_tags(list_items=5, data=[1, 2, 3, 4, 5]):
        list_item = ""
        for x in range(list_items):
            list_item += "<li>{}</li>\n".format(data[x])
        list_tags = """
        <ol>
            {}
        </ol>
        """.format(list_item)

        return list_tags

    def unordered_list_tags(list_items=5, data=[1, 2, 3, 4, 5]):
        list_item = ""
        for x in range(list_items):
            list_item += "<li>{}</li>\n".format(data[x])
        list_tags = """
        <ul>
            {}
        </ul>
        """.format(list_item)

        return list_tags

    def article_tag(subsect=True, aside=True, asideData=None, sectData=None):
        if subsect is True and aside is True:
            content = """
            <article>
                <section>
                    <div id='article-section'>
                        {}
                    </div>
                <section>
                <section>
                    <div id='article-aside-section'>
                        <aside class='aside-section'>
                            {}
                        </aside>
                    </div>
                </section>
            </article>
            """
            if asideData is not None and sectData is not None:
                content.format(sectData, asideData)
            elif asideData is None and sectData is not None:
                content.format(sectData, '')
            elif asideData is not None and sectData is None:
                content.format('', asideData)
            elif asideData is None and sectData is None:
                return ""
            else:
                return False
        return content

    # Don't know why someone would use this but hey, what the heck.
    def comment(self, data):
        return "<!-- {} -->".format(data)

    # def table_tags(rows=2, td=6, border=1, data=[1, 2, 3, 4, 5, 6]):
    #     table = """
    #     <table>
    #         {}
    #     </table>
    #     """
    #     table_data = ""
    #     for x in range(rows):
    #         row = "<tr> {} </tr>\n"
    #         for i in range(td):
    #             td_info = "<td> {} </td>".format(data[i])
    #             row.format(td_info)
    #         table_data += row
    #     table.format(table_data)

    def horizontal_line_tag(self, border=2):
        return "<hr border='{}'/>".format(border)

    def footer_tag(self, data):
        return """
        <footer>
            {}
        </footer>
        """.format(data)

    def text_formatting_tags(style, data, subData=None, supData=None):
        style = style.lower()
        if style == "b":
            return """
            <p>
                <b>{}</b>
            </p>
            """.format(data)
        elif style == "big":
            return """
            <p>
                <big>{}</big>
            </p>
            """.format(data)
        elif style == "small":
            return """
            <p>
                <small>{}</small>
            </p>
            """.format(data)
        elif style in ("i", "italic"):
            return """
            <p>
                <i>{}</i>
            </p>
            """.format(data)

        elif style == "sup":
            return """
            <p>
                {}<sup>{}</sup>
            </p>
            """.format(data, supData)
        elif style == "sub":
            return """
            <p>
                {}<sub>{}</sub>
            </p>
            """.format(data, subData)
        elif style in ("del", "deleted"):
            return """
            <p>
                <del>{}</del>
            </p>
            """.format(data)
        elif style in ("ins", "inserted"):
            return """
            <p>
                <ins>{}</ins>
            </p>
            """.format(data)
        elif style == "strong":
            return """
            <p>
                <strong>{}</strong>
            </p>
            """.format(data)
        else:
            return "That text format has not yet been added or is unknown"


def main():
    Generator = HTML_Generator()
    file = open('index.html', 'wb')
    opts = [
        '--metadata', '--dividers', '--paragraph', '--image',
        '--header', '--text-formatting', '--footer', '--line',
        '--comment', '--article', '--ordered-list', 'unordered-list',
        '--audio', '--video', '--break-line', '--link', '--form',

    ]

    def information():
        nonlocal opts
        info = (
            'Provides metadata feature', 'Provides divider functionality',
            'Enables paragraph creation', 'Enables image creation',
            'Enables header creation', 'Enables Text-formatting options',
            'Enables creation of footers', 'Enables creation of a <hr> tag',
            'Enables commenting', 'Creates article tags(aside, article etc.)',
            'Creation of ordered lists', 'Creation of unordered lists',
            'Enables audio tag creation', 'Enables video tag creation',
            'Enables <br> tag', 'Enables link tags', 'Enables a form',
            )
        i = 1
        for opt in zip(opts, info):
            print(i, " - ", repr(opt)[1:-1])
            i += 1
    _help = input("Do you need help(Y/N):   ")
    if _help in ('Y', 'y', 'Yes', 'YES', 'yes'):
        return information()
    else:
        pass

    # tag = None
    stop = False
    while not stop:
        input_tag = input("Enter tag(--metadata etc.):  ")
        if input_tag == "--metadata":
            keywords = input("Enter keywords:  ")
            print()
            content_discription = input("Enter content description:   ")
            # check if both exist
            if keywords and content_discription:
                file.write(Generator.meta_data_tags(keywords, content_description))
            elif keywords and not content_discription:
                file.write(Generator.meta_data_tags(keywords))
            elif not keywords and not content_discription:
                pass
        elif input_tag == "--dividers":
            tag_type == ['div', 'section', 'aside', 'header', 'span']
            x = 1
            print('----------- Choose tag type ------------')
            for i in range(len(tag_type)):
                print("[{}]\t".format(i), tag_type[i], end='\n')
                i += 1
            choice = int(input("Choose tag type:  "))
            if choice == 1:
                file.write(Generator.dividers_tags())
            elif choice == 2:
                file.write(Generator.dividers_tags(False, True, False, False, False))
            elif choice == 3:
                file.write(Generator.dividers_tags(False, False, True, False, False))
            elif choice == 4:
                file.write(Generator.dividers_tags(False, False, False, True, False))
            elif choice == 5:
                file.write(Generator.dividers_tags(False, False, False, False, True))
            elif choice is None:
                file.write(Generator.dividers_tags())
            else:
                pass
        elif input_tag == "--paragraph":
            data = input("Enter paragraph data:   ")
            if data is not None or data != '':
                file.write(Generator.paragraph_tag(data))
            else:
                pass
        elif input_tag == "--image":
            src = input("Enter image's path relative to the site's directory:  ")
            alt = input("Enter alternative text, incase image doesn't show:  ")
            h = int(input("Enter image height:  "))
            w = int(input("Enter image width:  "))
            if src and alt:
                if h is None and w is None:
                    file.write(Generator.image_tag(src, alt))
                elif h is not None and w is None:
                    file.write(Generator.image_tag(src, alt, h))
                else:
                    pass
            else:
                pass
        elif input_tag == "--header":
            types = [x for x in range(1, 7)]
            type_description = [
                            "Biggest", "Bigger", "Big",
                            "Smaller", "Small", "Smallest"
                            ]
            help_ = input("Do you need help:  ")
            if help_ in ("Yes", "y", "YES", "Y"):
                for x in zip(types, type_description):
                    print(repr(x[1:-1]), end=" ")
            elif help_ in ("No", "N", "n", "no"):
                pass
            else:
                print("Option Error")
            header_data = input("Enter header information:   ")
            header_type = int(input())
            if header_type == 1:
                file.write(Generator.header_tags(header_type, header_data))
            elif header_type == 2:
                file.write(Generator.header_tags(header_type, header_data))
            elif header_type == 3:
                file.write(Generator.header_tags(header_type, header_data))
            elif header_type == 4:
                file.write(Generator.header_tags(header_type, header_data))
            elif header_type == 5:
                file.write(Generator.header_tags(header_type, header_data))
            elif header_type == 6:
                file.write(Generator.header_tags(header_type, header_data))
            else:
                pass
        elif input_tag == "--comment":
            data = input("Enter comment data:   ")
            if not data:
                print("Error: Comment cannot be empty")
            else:
                file.write(Generator.comment(data))
        elif input_tag == "--link":
            href = input("Enter the hyperlink reference of the link:  ")
            target = input("Enter target type(_blank, _parent etc.):   ")
            if href and target:
                if href.startswith("https://") or href.startswith("https://"):
                    file.write(Generator.link_tag(href, target))
                else:
                    pass
            elif href and not target:
                if href.startswith("https://") or href.startswith("https://"):
                    file.write(Generator.link_tag(href))
                else:
                    pass
            else:
                pass
        elif input_tag == "--line":
            border = int(input("Enter border-width:  "))
            if border:
                file.write(Generator.horizontal_line_tag(border))
            file.write(Generator.horizontal_line_tag())
        elif input_tag == "--break-line":
            file.write(Generator.break_line_tag())
        elif input_tag == "--video":


if __name__ == "__main__":
    main()
