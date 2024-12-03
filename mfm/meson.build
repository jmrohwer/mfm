mymodule_dir = py.get_install_dir() / 'mwm'

py.install_sources([
    '__init__.py'
  ],
  subdir: 'mwm'
)

pure_subdirs = [
    'pymath',
    'tests'
]

foreach subdir: pure_subdirs
  install_subdir(subdir, install_dir: mymodule_dir, install_tag: 'python-runtime')
endforeach

subdir('fmath')
