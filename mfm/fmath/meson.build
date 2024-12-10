#fmath_wrappers = custom_target('fmath_wrappers',
#  input : ['fmath.pyf'],
#  output : ['fmathmodule.c', 'fmath-f2pywrappers.f'],
#  command : [py, '-m', 'numpy.f2py', '@INPUT@', '--build-dir', '@OUTDIR@']
#)

fmath_lib = static_library('fmath_lib',
  'fmath.f',
  fortran_args: [fortran_ignore_warnings],
  override_options: ['b_lto=false'],
  gnu_symbol_visibility: 'hidden',
)

py.extension_module('fmath',
                     'fmathmodule.c',
                     link_with: [fmath_lib],
                     c_args: [Wno_unused_variable],
                     dependencies: [py_dep, fortranobject_dep],
                     install: true,
                     link_language: 'fortran',
                     include_directories: inc_np,
                     subdir: 'mfm/fmath')

py.install_sources([
    '__init__.py'
  ],
  subdir: 'mfm/fmath'
)
