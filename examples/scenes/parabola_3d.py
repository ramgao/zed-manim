from manim import *

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 60


class Parabola3D(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()

        paraboloid = Surface(
            lambda u, v: axes.c2p(u, v, 0.35 * (u**2 + v**2)),
            u_range=(-3, 3),
            v_range=(-3, 3),
            resolution=(24, 24),
        )

        paraboloid.set_style(
            fill_opacity=0.75,
            stroke_color=BLUE,
            stroke_width=0.5,
        )
        paraboloid.set_fill_by_checkerboard(BLUE_D, BLUE_E)

        self.set_camera_orientation(
            phi=65 * DEGREES,
            theta=35 * DEGREES,
            zoom=0.75,
        )

        title = Text("3D Paraboloid").scale(0.7).to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)

        self.play(Write(title))
        self.play(Create(axes))
        self.play(Create(paraboloid), run_time=3)

        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(8)
        self.stop_ambient_camera_rotation()
