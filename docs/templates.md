# Project Templates

The `templates/` directory contains copyable Manim project starters for common workflows.

Each template includes:

- a renderable `main.py`
- `pyrightconfig.json` for clean basedpyright diagnostics
- `pyproject.toml` for Ruff wildcard-import lint configuration
- `.zed/tasks.json` with Manim render tasks
- a short template README

## Templates

| Template | Use it for |
| --- | --- |
| `clean-workspace` | A beginner-friendly Manim project with a simple scene and clean Zed diagnostics |
| `youtube-4k` | 3840x2160, 60 FPS intro or channel animation work |
| `math-education` | Lessons with `MathTex`, axes, graph plotting, and highlighted results |
| `3d-showcase` | `ThreeDScene`, surfaces, and camera movement experiments |

## Copy a Template

Copy a template directory into a new project location, then open that copied folder in Zed.

PowerShell example:

```powershell
Copy-Item -Recurse templates\clean-workspace C:\Users\you\my-manim-project
```

macOS or Linux example:

```sh
cp -R templates/clean-workspace ~/my-manim-project
```

Then create a virtual environment and install Manim:

```sh
python -m venv .venv
.venv/bin/python -m pip install manim
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install manim
```

Open the copied project folder in Zed. If Zed does not automatically select `.venv`, choose it from the Python toolchain selector.

## Render

Open `main.py`, run `task: spawn` from the Command Palette, and choose one of the Manim tasks.

The `-p` flag in the tasks opens the rendered video externally after rendering.

The `math-education` template uses `MathTex` when LaTeX is installed and falls back to plain `Text` otherwise, so the starter scene still renders in a fresh environment.

## Diagnostics

The templates suppress only wildcard-import false positives caused by common Manim style:

- basedpyright: `reportWildcardImportFromLibrary`
- Ruff: `F403` and `F405`

Real errors are not suppressed. Missing Manim imports, wrong Python environments, syntax errors, and genuine Manim API errors should still appear.
