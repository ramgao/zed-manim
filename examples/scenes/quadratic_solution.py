from manim import *

config.pixel_width = 3840
config.pixel_height = 2160
config.frame_rate = 60


class QuadraticFormulaDerivation(Scene):
    def construct(self):
        title = Text("Quadratic Formula", font_size=72)
        subtitle = Text("Derived by completing the square", font_size=36).next_to(
            title, DOWN
        )

        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=DOWN))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        example = MathTex(r"2x^2 + 7x - 4 = 0").scale(1.2)
        example_label = Text("Example problem", font_size=34).next_to(example, UP)

        self.play(FadeIn(example_label), Write(example))
        self.wait(1.5)

        general = MathTex(r"ax^2 + bx + c = 0").scale(1.2)
        general_label = Text("But let's solve the general case", font_size=34).next_to(
            general, UP
        )

        self.play(
            Transform(example, general),
            Transform(example_label, general_label),
        )
        self.wait(1.5)

        self.play(FadeOut(example_label))

        equations = [
            MathTex(r"ax^2 + bx + c = 0"),
            MathTex(r"ax^2 + bx = -c"),
            MathTex(r"x^2 + \frac{b}{a}x = -\frac{c}{a}"),
            MathTex(
                r"x^2 + \frac{b}{a}x + \left(\frac{b}{2a}\right)^2 = -\frac{c}{a} + \left(\frac{b}{2a}\right)^2"
            ),
            MathTex(
                r"\left(x + \frac{b}{2a}\right)^2 = -\frac{c}{a} + \frac{b^2}{4a^2}"
            ),
            MathTex(r"\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}"),
            MathTex(r"x + \frac{b}{2a} = \pm \frac{\sqrt{b^2 - 4ac}}{2a}"),
            MathTex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}"),
        ]

        for eq in equations:
            eq.scale(0.95)

        current = example
        notes = [
            "Move c to the other side",
            "Divide everything by a",
            "Add the magic square term",
            "Left side becomes a perfect square",
            "Combine the fractions",
            "Take the square root",
            "Isolate x",
        ]

        for i, next_eq in enumerate(equations[1:]):
            note = Text(notes[i], font_size=34).to_edge(DOWN)
            self.play(FadeIn(note, shift=UP))
            self.play(TransformMatchingTex(current, next_eq), run_time=1.7)
            current = next_eq

            pulse_box = SurroundingRectangle(current, color=YELLOW, buff=0.25)
            self.play(Create(pulse_box), run_time=0.4)
            self.play(FadeOut(pulse_box), run_time=0.4)
            self.play(FadeOut(note))
            self.wait(0.4)

        formula_box = SurroundingRectangle(current, color=GREEN, buff=0.3)
        formula_label = Text("The quadratic formula", font_size=38).next_to(
            formula_box, DOWN
        )

        self.play(Create(formula_box), FadeIn(formula_label))
        self.wait(2)

        self.play(
            current.animate.to_edge(UP),
            FadeOut(formula_box),
            FadeOut(formula_label),
        )

        section = Text("Now let's use it", font_size=48).next_to(
            current, DOWN, buff=0.8
        )
        self.play(Write(section))
        self.wait(1)
        self.play(FadeOut(section))

        problem = (
            MathTex(r"2x^2 + 7x - 4 = 0").scale(1.0).next_to(current, DOWN, buff=0.7)
        )
        values = (
            VGroup(
                MathTex(r"a=2"),
                MathTex(r"b=7"),
                MathTex(r"c=-4"),
            )
            .arrange(RIGHT, buff=0.8)
            .next_to(problem, DOWN)
        )

        self.play(Write(problem))
        self.play(LaggedStart(*[FadeIn(v, shift=UP) for v in values], lag_ratio=0.25))
        self.wait(1.5)

        substitutions = [
            MathTex(r"x = \frac{-7 \pm \sqrt{7^2 - 4(2)(-4)}}{2(2)}"),
            MathTex(r"x = \frac{-7 \pm \sqrt{49 + 32}}{4}"),
            MathTex(r"x = \frac{-7 \pm \sqrt{81}}{4}"),
            MathTex(r"x = \frac{-7 \pm 9}{4}"),
        ]

        for s in substitutions:
            s.scale(0.95).next_to(values, DOWN, buff=0.7)

        self.play(Write(substitutions[0]))
        active = substitutions[0]

        for nxt in substitutions[1:]:
            self.wait(0.8)
            self.play(TransformMatchingTex(active, nxt), run_time=1.4)
            active = nxt

        split = (
            VGroup(
                MathTex(r"x = \frac{-7 + 9}{4} = \frac{2}{4} = \frac{1}{2}"),
                MathTex(r"x = \frac{-7 - 9}{4} = \frac{-16}{4} = -4"),
            )
            .arrange(DOWN, buff=0.5)
            .next_to(active, DOWN, buff=0.7)
        )

        self.play(FadeIn(split, shift=DOWN))
        self.wait(1.5)

        final = MathTex(r"x = \frac{1}{2},\quad x = -4").scale(1.3)
        final_box = SurroundingRectangle(final, color=YELLOW, buff=0.35)

        self.play(
            FadeOut(current),
            FadeOut(problem),
            FadeOut(values),
            FadeOut(active),
            FadeOut(split),
        )

        fireworks = VGroup(
            Star(color=YELLOW).scale(0.25).shift(LEFT * 3 + UP),
            Star(color=BLUE).scale(0.25).shift(RIGHT * 3 + UP),
            Star(color=GREEN).scale(0.25).shift(LEFT * 2 + DOWN),
            Star(color=RED).scale(0.25).shift(RIGHT * 2 + DOWN),
        )

        self.play(Write(final))
        self.play(Create(final_box))
        animations: list = []

        for star in fireworks:
            animations.append(star.animate.scale(2).set_opacity(0))

        self.play(
            LaggedStart(
                *animations,
                lag_ratio=0.2,
            ),
            run_time=1.5,
        )

        done = Text("Solved.", font_size=52).next_to(final_box, DOWN)
        self.play(FadeIn(done))
        self.wait(3)
