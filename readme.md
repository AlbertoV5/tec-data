# [Excel for Data Analytics](./01-excel/readme.md)

1.  Header
2.  Resources


# [Visual Basic for Applications](./02-vba/readme.md)

1.  Introduction
2.  Reference
3.  Keywords and Operators
4.  Design Patterns
5.  Doing Research
6.  Developing a Macro
7.  Running Macros with Buttons
8.  Debugging and Timing Code
9.  Footnotes


# [Python Fundamentals](./03-python/readme.md)

1.  Introduction
2.  How to work with Python.
3.  VS Code and GitHub
4.  Working with Python

---


# Site generation

<p>

The previous index is generated from the home directory using emacs&rsquo; org-mode and python.

```python
"""Get all folders of {name} in cwd. Returns org formatted string."""
from pathlib import Path
from orgparse import load


name = "-"
file = "readme.org"
# header, title and final formatting
h1 = lambda ref, text: f"* [[./{ref}/{file}][{text}]]"
h2 = lambda i, text: f"{i}. {text}"
t1 = lambda b: (
    b.split("\n")[0]
    .replace("#+title:", "")
    .strip())
ff = lambda p, c: f"{p}\n{c}"

# Find directories
paths =     [p for p in sorted(Path.cwd().iterdir())
            if name in p.name and p.is_dir()]
# Find index.org files
files =     [load(p/file) for p in paths]
# Format titles and paths
titles =    [h1(p.name, t1(c.get_body()))
            for p, c in zip(paths, files)]
# Format headers as list
headers =   ["\n".join(h2(i+1, d.get_heading())
            for i, d in enumerate(c.children))
            for c in files]

return "\n".join(ff(p, c) for p, c in zip(titles, headers))
```

The HTML is rendered with org-mode&rsquo;s export dispatcher <sup><a id="fnr.1" class="footref" href="#fn.1" role="doc-backlink">1</a></sup> and a custom css setup inspired by Read the Docs and the Furo theme for sphinx.

I am using an org parser instead of an HTML one because I will also be exporting to markdown and text.

I am also using alpha2phi&rsquo;s guide <sup><a id="fnr.2" class="footref" href="#fn.2" role="doc-backlink">2</a></sup> as a referece, and spudlyo&rsquo;s video too <sup><a id="fnr.3" class="footref" href="#fn.3" role="doc-backlink">3</a></sup>.

</p>

<div style="width: 80px; padding-bottom: 20px">
<img src = "./resources/tec-logo.svg" alt="tec-logo"/>
</div>

## Footnotes

<sup><a id="fn.1" class="footnum" href="#fnr.1">1</a></sup> <https://orgmode.org/manual/The-Export-Dispatcher.html>

<sup><a id="fn.2" class="footnum" href="#fnr.2">2</a></sup> <https://alpha2phi.medium.com/writing-technical-documentation-with-emacs-276f13284e54>

<sup><a id="fn.3" class="footnum" href="#fnr.3">3</a></sup> <https://youtu.be/0g9BcZvQbXU>
