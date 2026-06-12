# Clean Manim Workspace

This is a minimal Manim project layout for Zed.

It includes:

- `main.py` with beginner-friendly `Scene` and `ThreeDScene` examples
- `pyrightconfig.json` that keeps standard basedpyright diagnostics but disables the Manim wildcard import false positive
- `pyproject.toml` that disables only Ruff's wildcard-import false positives for Manim
- `.zed/tasks.json` with Manim render tasks

## Set Up

Create a virtual environment from this directory:

```sh
python -m venv .venv
```

Install Manim:

```sh
.venv/bin/python -m pip install manim
```

On Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install manim
```

Open this directory in Zed, then make sure Zed is using the `.venv` Python toolchain.

## Render

Open `main.py`, run `task: spawn` from the Command Palette, and choose one of the Manim tasks.

The tasks use `-p`, so Manim opens the rendered video externally after rendering.
