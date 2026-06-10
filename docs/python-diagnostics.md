# Python Diagnostics in Manim Projects

Zed uses basedpyright for Python diagnostics. In Manim projects, basedpyright can report both real setup errors and Manim-style false positives.

This extension does not install Python packages, configure your virtual environment, or suppress real errors automatically. Use the guidance below in your own Manim project.

## Real Errors vs Manim-Style False Positives

A real diagnostic points to code or environment setup that should be fixed. For example, if basedpyright cannot resolve `manim`, Zed is probably using the wrong Python interpreter or Manim is not installed in the selected environment.

A Manim-style false positive is a warning caused by a common Manim pattern that still works in normal Manim code. The main example is `from manim import *`.

## Wildcard Import Warning

You may see this warning:

```text
Wildcard import from a library not allowed
```

This comes from basedpyright's `reportWildcardImportFromLibrary` rule.

Manim tutorials commonly use:

```py
from manim import *
```

That import style is common because Manim scenes usually use many classes and constants such as `Scene`, `Text`, `Write`, `Circle`, `UP`, `DOWN`, `BLUE`, and `PI`. Importing them one by one can make beginner examples harder to read.

For Manim projects, it is reasonable to disable only this warning.

## Missing Manim Import

You may see this error:

```text
Import "manim" could not be resolved
```

Do not suppress this error. It usually means one of these is true:

- Manim is not installed.
- Zed is using the wrong Python interpreter.
- Your virtual environment was not selected or detected.

Fix the environment instead of hiding the diagnostic.

## Create a Virtual Environment

From your Manim project root:

```sh
python -m venv .venv
```

Then install Manim.

On macOS or Linux:

```sh
.venv/bin/python -m pip install manim
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install manim
```

After creating the environment, make sure Zed is using the `.venv` interpreter for the project.

## Recommended basedpyright Config

Copy `examples/pyrightconfig.json` from this repository into your own Manim project as:

```text
pyrightconfig.json
```

The example config uses standard type checking and disables only the wildcard import warning:

```json
{
  "typeCheckingMode": "standard",
  "reportWildcardImportFromLibrary": false
}
```

This keeps real errors visible, including missing imports and genuine API mistakes.
