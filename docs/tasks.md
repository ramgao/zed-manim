# Manim Tasks in Zed

Zed tasks are the recommended way to run Manim render commands from inside Zed.

Zed extensions currently do not auto-install tasks for users. To use these examples, copy the task definitions into your own Manim project's project-local `.zed/tasks.json` file.

Manim must be installed separately:

```sh
pip install manim
```

These tasks use Zed's task variables:

- `$ZED_FILE` is the absolute path of the currently open file.
- `$ZED_WORKTREE_ROOT` is the root directory of the current Zed worktree.

The `-p` flag tells Manim to open the rendered video externally after rendering.

## Render the Current File

Copy this into `.zed/tasks.json` in your Manim project:

```json
[
  {
    "label": "Manim: Render Current File Low Quality",
    "command": "manim",
    "args": ["-pql", "$ZED_FILE"],
    "cwd": "$ZED_WORKTREE_ROOT",
    "use_new_terminal": false,
    "allow_concurrent_runs": false
  },
  {
    "label": "Manim: Render Current File High Quality",
    "command": "manim",
    "args": ["-pqh", "$ZED_FILE"],
    "cwd": "$ZED_WORKTREE_ROOT",
    "use_new_terminal": false,
    "allow_concurrent_runs": false
  }
]
```

## Render an Explicit Scene

If your file has multiple scenes, add the scene class name to the task arguments:

```json
[
  {
    "label": "Manim: Render BasicScene Low Quality",
    "command": "manim",
    "args": ["-pql", "$ZED_FILE", "BasicScene"],
    "cwd": "$ZED_WORKTREE_ROOT",
    "use_new_terminal": false,
    "allow_concurrent_runs": false
  }
]
```

Replace `BasicScene` with the scene class you want to render.
