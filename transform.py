#!/usr/bin/env python

import re
import sys

import markdown

from markdown.extensions.toc import TocExtension
from markdown.extensions.fenced_code import FencedCodeExtension

liz_domain = 'https://docs.3liz.org'

mkin = open(sys.argv[1])
md = markdown.Markdown(
    extensions=[
        TocExtension(
            title='Table of content',
        ),
        FencedCodeExtension(),
        'meta',
        'mdx_linkify',
        'tables',
    ],
    output_format="html5")
gen_html = md.convert(mkin.read())
md_meta = md.Meta
doc_title = md_meta.get('title')[0]
favicon = md_meta.get('favicon')
if favicon:
    favicon = favicon[0]
else:
    favicon = '{}/favicon.png'.format(liz_domain)


def parse_bool(text):
    if isinstance(text, list):
        text = text[0]
    if text in ['True', True]:
        return True
    else:
        return False


link_parent_folder = parse_bool(md_meta.get('up'))
link_current_folder = parse_bool(md_meta.get('index')) or parse_bool(md_meta.get('sibling'))

output = list()
output.append("""
<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/styles/github.min.css" rel="stylesheet"/>
  <link href="{domain}/remarkable.css" rel="stylesheet"/>
  <link href="{favicon}" rel="icon" type="image/png" >
 </head>
 <body>
 <header class="header-container" style="">
    <h1>{title}</h1>
 </header>
 <article>
""".format(title=doc_title, favicon=favicon, domain=liz_domain))

if link_parent_folder:
    output.append("""<p><a href="./../">Up</a></p>""")

if link_current_folder:
    output.append("""<p><a href="./">Index</a></p>""")

regex_link = r'<a href="(.*).md">'
result = re.sub(regex_link, r'<a href="\1.html">', gen_html)
output.append(result)

output.append("""
  </article>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/8.1/highlight.min.js">
  </script>
  <script>
   hljs.initHighlightingOnLoad();
  </script>
  <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript">
  </script>
  <script type="text/javascript">
   MathJax.Hub.Config({"showProcessingMessages" : false,"messageStyle" : "none","tex2jax": { inlineMath: [ [ "$", "$" ] ] }});
  </script>
 </body>
</html>
""")

outfile = open(sys.argv[2], 'w')
outfile.write(''.join(output))
outfile.close()
