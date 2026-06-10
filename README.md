# Manim for Zed

Manim for Zed is a small extension that adds helpful Manim snippets for Python files.

Manim is a Python library, not a separate programming language, so this extension does not add a new grammar or Tree-sitter language. It focuses on making common Manim scene patterns faster to write in Zed.

## Current Features

- Python snippets for common Manim scenes and animations
- A basic renderable example scene
- Lightweight extension metadata for Zed's Extensions panel

## Requirements

Install Manim separately before rendering scenes:

```sh
pip install manim
```

## Install as a Dev Extension

1. Clone this repository:

   ```sh
   git clone https://github.com/ramgao/zed-manim.git
   ```

2. Open Zed.
3. Open the command palette.
4. Run `zed: install dev extension`.
5. Select the cloned `zed-manim` directory.
6. Open the Extensions panel and look for `Manim`.

## Use Snippets

Open a Python file and type one of the snippet prefixes, then accept the completion.

Use tab stops to rename scene classes, variables, text, colors, and other values.

## Snippet Library

| Prefix | What it does |
| --- | --- |
| `manim-scene` | Creates a basic `Scene` with text animation |
| `manim-camera` | Creates a `MovingCameraScene` example |
| `manim-text` | Adds a text animation inside a scene |
| `manim-math` | Adds a `MathTex` equation animation |
| `manim-axes` | Creates axes and plots a graph |
| `manim-transform` | Transforms a square into a circle |
| `manim-vgroup` | Creates and animates a `VGroup` layout |
| `manim-updater` | Adds a `ValueTracker` updater example |
| `manim-3d` | Creates a basic `ThreeDScene` |
| `manim-plane` | Creates a `NumberPlane` with coordinates |
| `manim-function` | Plots a function with `Axes` |
| `manim-parametric` | Creates a parametric curve |
| `manim-barchart` | Creates a bar chart |
| `manim-table` | Creates a table |
| `manim-matrix` | Creates a matrix with a label |
| `manim-code` | Creates an animated code block |
| `manim-brace` | Adds a brace with a label |
| `manim-vector` | Creates a coordinate plane and vector |
| `manim-unit-circle` | Starts a unit circle scene |
| `manim-derivative` | Starts a derivative/tangent line scene |
| `manim-integral` | Starts an area under curve scene |

## Run Manim from Zed Tasks

Zed extensions currently do not automatically install tasks. To render Manim scenes from inside Zed, copy `examples/tasks.json` into `.zed/tasks.json` in your own Manim project.

Then:

1. Open a `.py` Manim file.
2. Open the Command Palette.
3. Run `task: spawn`.
4. Choose one of the Manim tasks.

See `docs/tasks.md` for details and task examples.

## Python Diagnostics

Zed uses basedpyright for Python diagnostics. In Manim projects, `from manim import *` can produce a wildcard import warning even though that style is common in Manim tutorials.

Do not suppress missing import errors. If Zed reports that `manim` cannot be resolved, fix the project virtual environment or selected Python toolchain and make sure Manim is installed.

The wildcard import warning can be disabled for Manim projects by copying [`examples/pyrightconfig.json`](examples/pyrightconfig.json) into your own project as `pyrightconfig.json`.

See [`docs/python-diagnostics.md`](docs/python-diagnostics.md) for details.

## Render the Example

From the repository root, run:

```sh
manim -pqh examples/basic_scene.py BasicScene
```

The `-pqh` flags preview the output at high quality.

## Roadmap

- Add more snippets for common animation patterns
- Add snippets for 3D scenes and camera helpers
- Add project setup examples for typical Manim workflows
- Improve documentation based on user feedback

## Contributing

Contributions are welcome. Keep this extension simple and focused on Python-based Manim workflows.

Please avoid generated media files, Python cache files, unnecessary dependencies, or complex build tooling.

Suggested commit message:

```text
Improve Manim Python diagnostics guidance
```

# About the crators

## Hi, I'm Yohad Navon.

### I'm learning software engineering through open-source contributions.

### Current Interests

* Linux *(I'm still very new to it, but it has quickly become one of my *biggest obsession.*)*
* Rust
* Zed Editor
* Developer Tools
* Manim
* Cybersecurity *(especially Red Hat technologies)*
* Open Source *(MUST BE OPEN SOURCE)*

### **Current Project**

* **zed-manim**

My goal is to become a strong contributor by understanding how large codebases work, investigating issues carefully, and sharing what I learn along the way while having fun.

If you have feedback, ideas, opportunities, questions, or just want to talk about a project, please reach out. I genuinely mean it—I'm always happy to connect, learn from others, and help where I can.

### Life Interests

* I love playing the drums.
* I'm a passionate gamer.
* I'm training to complete an Ironman.
* I love playing tennis.

