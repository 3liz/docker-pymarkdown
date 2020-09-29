## Usage

Transform a markdown page to HTML webpage with 3Liz design.

```bash
docker run --rm -w /plugin -v $(pwd):/plugin 3liz/pymarkdown:latest docs/user_guide/qgis-lizsync-plugin.md docs/user_guide/qgis-lizsync-plugin.html
```

## Syntax

Some metadata are supported in the metadata section

* `title` : Title of the page
* `favicon` : Favicon to use or it will be the 3Liz one by default
* `up` : Link to the parent folder (it should have a `index.html`)
* `index` : Link to the current folder (it should have a `index.html`)
