from shutil import which

from manim import *


def math_mobject(tex, fallback):
    if which("latex") is not None:
        return MathTex(tex)
    return Text(fallback)


class MathEducationScene(Scene):
    def construct(self):
        title = Text("Quadratic Functions", font_size=42).to_edge(UP)
        equation = math_mobject(r"f(x) = x^2 - 1", "f(x) = x^2 - 1").next_to(title, DOWN)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 5, 1],
            tips=False,
        ).scale(0.8).to_edge(DOWN)
        graph = axes.plot(lambda x: x**2 - 1, color=BLUE)
        label = math_mobject(r"f(x)", "f(x)").move_to(axes.c2p(2.2, 3.4))

        roots = VGroup(
            Dot(axes.c2p(-1, 0), color=YELLOW),
            Dot(axes.c2p(1, 0), color=YELLOW),
        )
        root_label = math_mobject(r"x = \pm 1", "x = +/- 1").next_to(roots, UP)

        self.play(Write(title), Write(equation))
        self.play(Create(axes), Create(graph), Write(label))
        self.play(FadeIn(roots), Write(root_label))
        self.wait()
