from distutils.core import setup
import py2exe
import sys

includes = ["encodings", "encoding.*"]
sys.argv.append("py2exe")
options = {"py2exe" : {"bundle_files": 1,
                       "dll_excludes": ["MSVCP90.dll","w9xpopen.exe"]}}

setup(
    windows=[{"script":'frame.py', "icon_resources": [(1, "title.ico")]}],
    options=options,
    zipfile=None
)