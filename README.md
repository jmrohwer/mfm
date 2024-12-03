# mfm
## Minimal Fortran module

A minimal Fortran extension module built using `f2py` and `meson-python`.
For testing and debugging the compilation with [Pyodide](https://pyodide.org/en/stable/index.html).
My first mixed Python and Fortran module, built with `mesonpy`. For compilation with Pyodide.

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
