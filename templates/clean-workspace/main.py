from manim import *


class CleanWorkspaceScene(Scene):
    def construct(self):
        title = Text("Clean Manim Workspace").to_edge(UP)
        circle = Circle(color=BLUE)
        square = Square(color=YELLOW)

        self.play(Write(title))
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(square.animate.set_color(GREEN).scale(1.2))
        self.wait()
