from manim import *
from utils import *


class JordanFormScene(Scene):
    def construct(self):
        logo = Logo()
        self.add(logo)

        title = Text("若尔当标准型", font_size=38, color=WHITE)
        title.to_edge(UL, buff=0.2)
        self.play(Write(title))
        self.wait(0.3)

        jordan_general = MathTex(
            r"\mathbf{J} = \begin{bmatrix} J_{\lambda_1} & & 0 \\ & \ddots & \\ 0 & & J_{\lambda_k} \end{bmatrix}",
            font_size=44,
            color=WHITE,
        )
        jordan_general.to_edge(UL, buff=1.2)

        self.play(FadeIn(jordan_general, shift=UP))
        self.wait(0.4)

        jordan_block = MathTex(
            r"\mathbf{J}_{\lambda_i} = \begin{bmatrix} \lambda_i & 1 & 0 & 0 \\ 0 & \lambda_i & 1 & 0 \\ 0 & 0 & \lambda_i & 1 \\ 0 & 0 & 0 & \lambda_i \end{bmatrix}",
            font_size=38,
            color=WHITE,
        )
        jordan_block.next_to(jordan_general, DOWN, buff=1.1)
        jordan_block.align_to(jordan_general, LEFT)

        self.play(FadeIn(jordan_block, shift=UP))
        self.wait(0.6)

        formula = MathTex(
            r"\mathbf{T} = \mathbf{P}\,\mathbf{J}\,\mathbf{P}^{-1}",
            font_size=44,
            color=WHITE,
        )
        formula.to_edge(UP, buff=1).shift(RIGHT * 2.5)
        self.play(FadeIn(formula, shift=DOWN))

        one_by_one = MathTex(
            r"J_{\lambda_i} = [\lambda_i], i=1,2,\cdots,k",
            font_size=36,
            color=WHITE,
        )
        one_by_one.next_to(formula, DOWN, buff=0.5)
        self.play(FadeIn(one_by_one, shift=UP))
        self.wait(0.4)

        formula2 = MathTex(
            r"\mathbf{T} = \mathbf{P}\,\mathbf{D}\,\mathbf{P}^{-1}",
            font_size=44,
            color=WHITE,
        )
        formula2.next_to(one_by_one, DOWN, buff=0.8)
        self.play(FadeIn(formula2, shift=DOWN))

        diagonal = MathTex(
            r"\mathbf{D} = \begin{bmatrix} \lambda_1 & & 0 \\ & \ddots & \\ 0 & & \lambda_k \end{bmatrix}",
            font_size=38,
            color=WHITE,
        )
        diagonal.next_to(formula2, DOWN, buff=0.5)
        self.play(FadeIn(diagonal, shift=UP))
        self.wait(0.4)
