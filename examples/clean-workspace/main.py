from manim import *


class CleanScene(Scene):
    def construct(self):
        title = Text("Clean Manim Workspace")
        equation = MathTex(r"a^2 + b^2 = c^2")
        axes = Axes(x_range=[-3, 3, 1], y_range=[-1, 9, 1])
        graph = axes.plot(lambda x: x**2, color=BLUE)

        title.to_edge(UP)
        equation.next_to(title, DOWN)

        self.play(Write(title))
        self.play(Write(equation))
        self.play(Create(axes), Create(graph))
        self.wait()


class CleanThreeDScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        self.play(Create(axes))
        self.wait()
