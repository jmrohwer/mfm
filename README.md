# mfm
## Minimal Fortran module

A minimal Fortran extension module built using `f2py` and `meson-python`.
For testing and debugging the compilation with
[Pyodide](https://pyodide.org/en/stable/index.html).

The module defines 3 wrapped Fortran functions:

```python
mfm.fmath.hello()
    Simple hello world program, no arguments.
```
```python
mfm.fmath.fadd(x, y)
    Adds numbers `x` and `y`, casts result as float.
```
```python
mfm.fmath.fmult(x, y)
    Multiplies numbers `x` and `y`, casts result as float.
```

## Build instructions

1. Clone the repo:
   ```shell 
   $ git clone https://github.com/jmrohwer/mfm.git
   ```
2. Build / install:
   ```shell
   $ cd mfm
   $ python -m build .      or
   $ pip install .
   ```
3. Test (requires `pytest`):
   ```python
   import mfm
   mfm.test()
   ```
