# 3Liz PyMarkdown

## Usage

Transform a markdown page to HTML webpage with 3Liz design.

```bash
docker run --rm -w /plugin -v $(pwd):/plugin 3liz/pymarkdown:latest docs/user_guide.md docs/user_guide.html
```

## Syntax

Some metadata are supported in the metadata section

* `Title` : Title of the page
* `Favicon` : Favicon to use, or it will be the 3Liz one by default
* `Up` : `True` or `False`, link to the parent folder (it should have a `index.html`)
* `Index` : `True` or `False`, link to the current folder (it should have a `index.html`)
