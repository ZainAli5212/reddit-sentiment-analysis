# text = "Here's a link to my site:\nhttps://example.com/\n\nAnd here's another one:\nwww.test-site.org"
import re

text = """
This is a link: https://example.com
Here's another one:
https://anotherexample.org
"""

# text_with_multiline = """
# Here is my websitess:
# https://example.com/blog-post-1.html
# Another link:
# www.anotherexample.com/
# """
cleaned_text = re.sub(r'http\S+|https\S+|www\S+', '', text)

print(cleaned_text)
