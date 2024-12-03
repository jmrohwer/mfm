fmath_wrappers = custom_target('fmathmodule.c',
  input : ['fmath.pyf'],
  output : ['fmathmodule.c', 'fmath-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
)

py.extension_module('fmath',
                     [
                         'fmath.f',
                         fmath_wrappers,
                         fortranobject_c
                     ],
                     include_directories: inc_np,
                     dependencies : [
                     py_dep,
                     # quadmath_dep,
                     ],
                     install : true,
                     subdir: 'mwm/fmath')

py.install_sources([
    '__init__.py'
  ],
  subdir: 'mwm/fmath'
)
