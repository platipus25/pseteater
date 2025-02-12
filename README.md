
# Pset Eater

Take a pdf of a pset and output cropped svgs for each page

Relies on [PyMuPdf](https://pymupdf.readthedocs.io/en/latest/), the python wrapper for [mupdf](https://mupdf.com/) for pdf parsing.

## Usage

```
usage: pseteater [-h] [-o OUTPUT] filename

Take a pdf of a pset and output svgs for each problem

positional arguments:
  filename

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT
```