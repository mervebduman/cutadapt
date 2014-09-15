from __future__ import print_function
import sys

__version__ = '1.6dev'

def check_importability():
	try:
		import cutadapt._align
	except ImportError as e:
		if 'undefined symbol' in str(e):
			print("""
ERROR: A required extension module could not be imported because it is
incompatible with your system. A quick fix is to recompile the extension
modules with the following command:

    {} setup.py build_ext -i

See the documentation for alternative ways of installing the program.

The original error message follows.
""".format(sys.executable))
		raise
