"""Test bootstrap.

Puts the project root on sys.path and stubs the heavy optional runtime
dependencies so the pure-logic tests run without installing or importing
pandas, paramiko, py7zr, fpdf, etc. The functions under test here do not use
those libraries at call time; they only need the module import to succeed.
"""
import importlib.abc
import importlib.machinery
import os
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Heavy / platform-specific deps replaced by permissive dummies.
_FAKE = {"pandas", "paramiko", "py7zr", "fpdf", "openpyxl", "tabulate",
         "questionary", "pexpect"}


class _AnyModule(types.ModuleType):
    def __getattr__(self, name):
        # Any attribute access returns a trivial class/callable.
        return type(name, (), {"__init__": lambda self, *a, **k: None})


class _StubFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, name, path, target=None):
        if name.split(".")[0] in _FAKE:
            return importlib.machinery.ModuleSpec(name, self)
        return None

    def create_module(self, spec):
        return _AnyModule(spec.name)

    def exec_module(self, module):
        pass


sys.meta_path.insert(0, _StubFinder())
