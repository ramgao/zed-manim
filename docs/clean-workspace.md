# Clean Manim Workspace

This guide describes the cleanest practical Manim setup in Zed while preserving real Python diagnostics.

## What Clean Means

A clean Manim workspace should have:

- Manim installed in the project virtual environment
- Zed using the correct Python toolchain
- basedpyright able to resolve `manim`
- autocomplete for Manim classes such as `Scene`, `Text`, `MathTex`, `Axes`, and `ThreeDScene`
- no `from manim import *` false-positive warning
- no Ruff wildcard-import false positives
- real errors, such as missing imports, still visible
- project-local Manim render tasks

See `examples/clean-workspace/` for a complete starter layout. Open that folder itself in Zed, or copy its files into the root of your own Manim project, so `pyrightconfig.json` and `pyproject.toml` are at the project root.

## Create a Virtual Environment

From your Manim project root:

```sh
python -m venv .venv
```

Install Manim.

On macOS or Linux:

```sh
.venv/bin/python -m pip install manim
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install manim
```

## Select the Python Toolchain in Zed

Zed discovers Python environments as toolchains. For most projects, Zed selects the right one automatically.

If `manim` cannot be resolved, use Zed's toolchain selector and choose the `.venv` interpreter for your project. Once the correct toolchain is selected, Zed's built-in Python language servers can resolve dependencies from that environment.

## basedpyright Configuration

Use this project-local `pyrightconfig.json`:

```json
{
  "typeCheckingMode": "standard",
  "reportWildcardImportFromLibrary": false
}
```

This suppresses only the Manim wildcard import false positive. It does not suppress missing import errors.

## Ruff Configuration

If Ruff is enabled in Zed, Manim's common wildcard import style can produce these lint diagnostics:

- `F403`: `from manim import *` used; unable to detect undefined names
- `F405`: name may be undefined or defined from star imports

Use this project-local `pyproject.toml`:

```toml
[tool.ruff.lint]
ignore = ["F403", "F405"]
```

basedpyright diagnostics are handled by `pyrightconfig.json`. Ruff lint warnings are handled by `pyproject.toml`.

This suppresses only wildcard-import related Ruff warnings. It does not suppress real Python errors or other useful Ruff diagnostics.

## Common Diagnostics

| Diagnostic | Category | What to do |
| --- | --- | --- |
| `Wildcard import from a library not allowed` | False positive for Manim beginner code | Suppress with `reportWildcardImportFromLibrary: false` |
| `F403` from Ruff | False positive for Manim beginner code | Suppress with `ignore = ["F403", "F405"]` |
| `F405` from Ruff | False positive caused by Manim star imports | Suppress with `ignore = ["F403", "F405"]` |
| `Import "manim" could not be resolved` | Environment/setup issue | Install Manim in `.venv` and select the correct Zed toolchain |
| `"Scene" is not defined` | Usually cascading from missing Manim import | Fix the environment; do not suppress it |
| `"Text" is not defined` | Usually cascading from missing Manim import | Fix the environment; do not suppress it |
| Genuine bad arguments or missing attributes | Real error | Fix the Python or Manim API usage |

## Render Tasks

Use project-local Zed tasks in `.zed/tasks.json`.

Example:

```json
[
  {
    "label": "Manim: Render Current Scene Low Quality",
    "command": "manim",
    "args": ["-pql", "$ZED_FILE", "CleanScene"],
    "cwd": "$ZED_WORKTREE_ROOT",
    "use_new_terminal": false,
    "allow_concurrent_runs": false
  }
]
```

Run tasks from the Command Palette with `task: spawn`.

## Investigation Summary

In a fresh Manim project with Manim installed and no project config, basedpyright reported the wildcard import warning for `from manim import *`. In stricter basedpyright CLI defaults, it also reported style/typing warnings such as implicit override and partially unknown members. Zed's documented default for basedpyright is standard mode, and the recommended config keeps that mode explicit.

After adding the recommended `pyrightconfig.json`, a starter file using `from manim import *`, `Scene`, `Text`, `MathTex`, `Axes`, and `ThreeDScene` produced no basedpyright diagnostics.

After adding the recommended `pyproject.toml`, Ruff no longer reports `F403` on `from manim import *` or false `F405` undefined-name warnings for names imported through Manim's wildcard import.

With the same config but without Manim installed, basedpyright still reported `Import "manim" could not be resolved` and related undefined-name errors. Those errors are intentionally preserved.

## Warnings Removed

- `Wildcard import from a library not allowed` is removed because `from manim import *` is common, beginner-friendly Manim style.
- Ruff `F403` and `F405` are removed because they are caused by the same Manim wildcard import style.
- Stricter non-Zed basedpyright CLI style warnings are avoided by keeping `typeCheckingMode` at Zed's documented `standard` mode.

## Warnings Preserved

- `Import "manim" could not be resolved` remains visible when Manim is missing or Zed is using the wrong interpreter.
- Undefined names such as `Scene`, `Text`, or `Write` remain visible when they cascade from a missing Manim import.
- Genuine Python, Ruff, basedpyright, and Manim API errors remain visible.

## Remaining Limitations

- Zed extensions do not install Python packages or create virtual environments.
- The user still needs to select the correct Python toolchain if Zed picks the wrong interpreter.
- Manim rendering requires system dependencies such as LaTeX for some `MathTex` scenes.
- The `.zed/tasks.json` example is project-local; extensions do not automatically install these tasks into user projects.
