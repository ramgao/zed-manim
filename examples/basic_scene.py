from manim import *


class BasicScene(Scene):
    def construct(self):
        title = Text("Hello, Manim!", font_size=48)
        subtitle = Text("Rendered from a Zed project", font_size=28)
        subtitle.next_to(title, DOWN)

        group = VGroup(title, subtitle).move_to(ORIGIN)

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.play(group.animate.set_color_by_gradient(BLUE, GREEN))
        self.wait()
