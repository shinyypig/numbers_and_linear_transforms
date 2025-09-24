from manim import *
from utils import *


class WelcomeScene(Scene):
    def construct(self):

        title = Text("数理同契", font_size=80, color=WHITE)
        title.move_to(ORIGIN)

        logo_cn = VerticalText("矩阵之美", font_size=32, color=WHITE)
        logo = Logo()
        title_group = VGroup(logo_cn, logo)

        logo.next_to(logo_cn, RIGHT, aligned_edge=DOWN)
        title_group.to_edge(DR, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(title_group, shift=UP))
        self.play(FadeOut(logo_cn), FadeOut(title))
        self.wait(1)
