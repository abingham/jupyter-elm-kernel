This kernel adds support for Elm to [Jupyter](http://jupyter.org/) notebooks.

While basic functionality is in place, this is still very much a work in
progress. I'm still figuring it all out. Any help, ideas, etc. would be great.

# Installation

Install the package from source:
```
pip install -e .
```

Then install the kernel spec:
```
python -m elm_kernel.install
```

# Usage

Run `jupyter notebook` and select the Elm kernel for a new notebook.

# Examples

The `examples` directory contains a few examples of how to use this kernel. Just
go to that directory and run `jupyter notebook` to see them.
