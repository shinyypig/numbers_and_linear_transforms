from manim import *
from utils import *
import numpy as np


class DiagScene(Scene):
    def construct(self):
        def jordan_block_2x2(lmbd):
            return np.array([[lmbd, 0], [0, 1]])

        logo = Logo()
        self.add(logo)

        title = Text("情形2：可对角化", font_size=38, color=WHITE)
        title.to_edge(UL, buff=0.2)
        self.play(Write(title))
        self.wait(0.3)

        # --- 2D Jordan block section ---
        matrix_2d_1 = MathTex(
            r"\mathbf{D} = ",
            font_size=40,
            color=WHITE,
        )
        matrix_2d_2 = MathTex(
            r"\begin{bmatrix} \lambda & 0 \\ 0 & 1 \end{bmatrix}",
            font_size=40,
            color=WHITE,
        )
        matrix_2d_2.next_to(matrix_2d_1, RIGHT, buff=0.3)
        matrix_2d = VGroup(matrix_2d_1, matrix_2d_2)

        matrix_2d.to_edge(LEFT, buff=1.0).shift(UP * 0.8)

        self.play(FadeIn(matrix_2d, shift=RIGHT))
        self.wait(0.4)

        # 添加一个框将矩阵括起来
        box = SurroundingRectangle(matrix_2d_2, buff=0.2, color=c1)
        self.play(FadeIn(box, shift=UP))

        axes = (
            NumberPlane(
                x_range=[-3, 3],
                y_range=[-3, 3],
                x_length=6,
                y_length=6,
            )
            .add_coordinates()
            .shift(RIGHT * 1.5)
        )
        self.play(FadeIn(axes))

        square = Square(side_length=1, color=c1, fill_opacity=0.4)
        square.move_to(axes.c2p(0.5, 0.5))  # 放在第一象限
        self.play(FadeIn(square))

        lambda_tracker_2d = ValueTracker(2.0)
        lambda_label_2d = MathTex(r"\lambda =", font_size=32, color=WHITE)
        lambda_value_2d = DecimalNumber(
            lambda_tracker_2d.get_value(),
            num_decimal_places=2,
            font_size=32,
            color=WHITE,
        )
        lambda_value_2d.add_updater(
            lambda dec: dec.set_value(lambda_tracker_2d.get_value())
        )
        lambda_group_2d = VGroup(lambda_label_2d, lambda_value_2d).arrange(
            RIGHT, buff=0.2
        )
        lambda_group_2d.next_to(matrix_2d, DOWN, buff=0.6, aligned_edge=LEFT)
        self.play(Write(lambda_group_2d))

        lambda_number_line = NumberLine(
            x_range=[-2, 2, 1],
            length=4,
            include_numbers=True,
            include_tip=False,
            font_size=24,
            color=WHITE,
        )
        lambda_number_line.next_to(
            lambda_group_2d, DOWN, buff=0.5, aligned_edge=LEFT
        ).shift(LEFT * 0.4)
        self.play(Create(lambda_number_line))

        lambda_dot = Dot(color=c1, radius=0.06)
        lambda_dot.add_updater(
            lambda dot: dot.move_to(
                lambda_number_line.n2p(lambda_tracker_2d.get_value()) + UP * 0.18
            )
        )
        self.play(FadeIn(lambda_dot))

        square_trans = always_redraw(
            lambda: square.copy()
            .set_color(c2)
            .apply_matrix(
                jordan_block_2x2(lambda_tracker_2d.get_value()),
                about_point=axes.c2p(0, 0),
            )
        )

        self.play(FadeIn(square_trans))
        self.play(lambda_tracker_2d.animate.set_value(-2), run_time=8, rate_func=linear)

        self.wait(0.3)

        label1 = Text("缩放", font_size=28, color=WHITE)
        label2 = Text("投影", font_size=28, color=WHITE)
        label3 = Text("反射", font_size=28, color=WHITE)

        vgroup = VGroup(label3, label2, label1).arrange(
            RIGHT, aligned_edge=LEFT, buff=1
        )

        vgroup.next_to(lambda_number_line, DOWN, buff=1.0)

        self.play(Write(label1))
        self.play(Write(label2))
        self.play(Write(label3))

        # clear page
        self.play(
            FadeOut(vgroup),
            FadeOut(square),
            FadeOut(axes),
            FadeOut(lambda_dot),
            FadeOut(lambda_number_line),
            FadeOut(lambda_group_2d),
            FadeOut(box),
            FadeOut(matrix_2d),
            FadeOut(square_trans),
        )

        self.wait(0.3)

        # rotation (complex eigenvalue) section
        matrix_2d_1 = MathTex(
            r"\mathbf{D} = ",
            font_size=40,
            color=WHITE,
        )
        matrix_2d_2 = MathTex(
            r"\begin{bmatrix} \lambda & 0 \\ 0 & \overline{\lambda} \end{bmatrix}",
            font_size=40,
            color=WHITE,
        )
        matrix_2d_2.next_to(matrix_2d_1, RIGHT, buff=0.3)
        matrix_2d = VGroup(matrix_2d_1, matrix_2d_2)

        matrix_2d.to_edge(LEFT, buff=1.0).shift(UP * 0.8)

        self.play(FadeIn(matrix_2d, shift=RIGHT))
        self.wait(0.4)
