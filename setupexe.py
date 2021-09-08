import os
from distutils.core import setup
import py2exe

setup(
    windows=["gui.py"],
    options={
                "py2exe":{
                        "unbuffered": True,
                        "optimize": 2,
                        "includes": ["lxml._elementpath"],
                }
        }
)