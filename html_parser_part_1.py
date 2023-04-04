from html.parser import HTMLParser

# Create a subclass and override the handler methods.
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])


N = int(input())
snippet = "".join([input().strip() for _ in range(N)])

# Instantiate the parser and feed it some HTML.
parser = MyHTMLParser()
parser.feed(snippet)
