import numpy as np
from manim import *


class ThreeDShowcaseScene(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: axes.c2p(u, v, 0.4 * np.sin(u) * np.cos(v)),
            u_range=(-3, 3),
            v_range=(-3, 3),
            resolution=(24, 24),
        )
        surface.set_style(fill_opacity=0.7, stroke_color=BLUE)
        surface.set_fill_by_checkerboard(BLUE, GREEN, opacity=0.6)

        title = Text("3D Surface", font_size=36).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        self.set_camera_orientation(phi=65 * DEGREES, theta=35 * DEGREES)
        self.play(Write(title), Create(axes))
        self.play(Create(surface), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(3)
        self.stop_ambient_camera_rotation()
