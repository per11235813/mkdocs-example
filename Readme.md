## Example project to explore `mkdocs`


### Objective

This repo serves as an example of how to use mkdocs for technical writing in a python context, 
in particular it demonstrates:

* Use markdown files for documentation
* Include python snippets and outputs in the documentation
* Use jupyter notebooks for documentation
* Demonstrate the use the cross references in `mkdocs`
* Create diagrams using [squidfunk](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)

### Trying it

To try it out:

```powershell
py -3.10 -m venv venv
.\venv\scripts\Activate.ps1
py -m pip install -U pip
pip install -r requirements.txt

py makefile.py build
py makefile.py serve
```