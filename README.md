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

Available snippet prefixes:

- `manim-scene`
- `manim-camera`
- `manim-text`
- `manim-math`
- `manim-axes`
- `manim-transform`
- `manim-vgroup`
- `manim-updater`

Use tab stops to rename scene classes, variables, text, colors, and other values.

## Run Manim from Zed Tasks

Zed extensions currently do not automatically install tasks. To render Manim scenes from inside Zed, copy `examples/tasks.json` into `.zed/tasks.json` in your own Manim project.

Then:

1. Open a `.py` Manim file.
2. Open the Command Palette.
3. Run `task: spawn`.
4. Choose one of the Manim tasks.

See `docs/tasks.md` for details and task examples.

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
Document Manim render tasks for Zed
```
