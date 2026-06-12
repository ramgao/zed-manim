from manim import *

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 60


class YouTubeIntro4K(Scene):
    def construct(self):
        title = Text("Your Channel", font_size=96, weight=BOLD)
        subtitle = Text("High quality Manim visuals", font_size=44)
        subtitle.next_to(title, DOWN, buff=0.45)

        logo = Circle(radius=1.2, color=BLUE).set_fill(BLUE, opacity=0.2)
        logo.next_to(VGroup(title, subtitle), UP, buff=0.7)

        group = VGroup(logo, title, subtitle).move_to(ORIGIN)

        self.play(FadeIn(logo, scale=0.8), run_time=0.8)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.25))
        self.play(group.animate.scale(0.92))
        self.wait(1)
