|                                                    |
|--------------------------------------------------- |
| [Repository](https://github.com/AlbertoV5/tec-data) |


# [Topic Title](./01-excel/readme.md)

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
2.  Python
3.  Working with Python files
4.  Python Types
5.  Python Lists
6.  Python Tuples
7.  Python Dictionaries
8.  Decision Statements
9.  Loops
10. F-Strings and Printing
11. Footnotes


# [Topic Title](./04-dataframes/readme.md)

1.  Header
2.  Resources

---


# Site generation

<p>

The previous index is generated from the home directory using emacs&rsquo; org-mode and python.

```python
"""Get all folders of {name} in cwd. Returns org formatted string."""
from pathlib import Path
from orgparse import load


dir_ident = "-"
file_name = "readme.org"
titles, headings = [], []

def get_title(org_file):
    return org_file.get_body().split("\n")[0].replace("#+title:", "").strip()

def to_title(path, title):
    return f"* [[./{path}/{file_name}][{title}]]"

def to_heading(i, path, heading):
    return  f"{i}. {heading}"

def combine(title, headings):
    return f"{title}\n{headings}"

paths = [p for p in sorted(Path.cwd().iterdir())
        if dir_ident in p.name and p.is_dir()]

for path in paths:
    org_file = load(path/file_name)
    title = to_title(path.name, get_title(org_file))
    titles.append(title)
    heading = "\n".join(to_heading(i+1, path.name, d.get_heading())
                         for i, d in enumerate(org_file.children))
    headings.append(heading)

return "\n".join(combine(p, c) for p, c in zip(titles, headings))
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
