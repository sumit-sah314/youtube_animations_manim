"""
newton_raphson.py

This script contains the implementation of the Newton-Raphson method
visualized using the Manim library. It demonstrates how computers can
compute square roots using the Newton-Raphson iterative method.

Author: Sumit Sah

Classes:
    - Newton: A Manim scene that illustrates the Newton-Raphson method.
    - YThumbnail1: A Manim scene designed for creating a YouTube thumbnail.
    - Sqrt:

Description:
    The Newton-Raphson method is an iterative process to find successively better 
    approximations to the roots (or zeroes) of a real-valued function. This script 
    visually explains how the method works using an animation created with Manim.
"""

from manim import *

#Graphical Visualisation
class Newton(Scene):
    def construct(self):
        x0 = 4.3
        a = 2  # The 'a' value in the function f(x) = 0.3x^2 - a
        ax = Axes(x_range=(-1, 6), y_range=(-3, 3), axis_config={"include_tip": False})
        curve = ax.plot(lambda x: 0.3 * x**2 - a, color=BLUE)
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)=x^2-a")
        VGroup(ax, curve, labels).shift(3 * LEFT + DOWN).scale(0.8)
        self.play(Create(VGroup(ax, curve, labels)))

        dot1 = Dot().move_to(ax.c2p(x0, 0))
        dot2 = Dot().move_to(ax.c2p(x0, curve.underlying_function(x0)))
        tangent = ax.get_secant_slope_group(x=x0, graph=curve, dx=0.01, secant_line_color=GREEN)
        line = DashedLine(start=ax.c2p(x0, 0), end=ax.c2p(x0, curve.underlying_function(x0)))
        self.play(Create(VGroup(dot1, dot2, line, tangent)))
        self.play(
            Write(MathTex("x_0").scale(0.8).next_to(dot1, DOWN)),
            Write(MathTex("f(x_0)").scale(0.8).next_to(dot2, 0.1 * UL))
        )

        # Newton-Raphson iteration
        x1 = x0 - (0.3 * x0**2 - a) / (0.6 * x0)
        dot3 = Dot().move_to(ax.c2p(x1, 0))
        dot4 = Dot().move_to(ax.c2p(x1, curve.underlying_function(x1)))
        tangent1 = ax.get_secant_slope_group(x=x1, graph=curve, dx=0.01, secant_line_color=ORANGE, secant_line_length=5)
        line1 = DashedLine(start=ax.c2p(x1, 0), end=ax.c2p(x1, curve.underlying_function(x1)))
        self.play(Write(MathTex("x_1").scale(0.8).next_to(dot3, DOWN)), Write(dot3))
        self.wait(2)

        brace1 = Brace(VGroup(dot1, dot3), DOWN, color=YELLOW_D)
        brace2 = Brace(line, RIGHT, color=YELLOW_D)
        self.play(Create(brace1), Write(MathTex("\\Delta x = x_0-x_1").scale(0.8).next_to(brace1, DOWN)))
        self.play(Create(brace2), Write(MathTex("\\Delta y = f(x_0)").scale(0.8).next_to(brace2, RIGHT)))
        self.wait()

        tex1 = MathTex("f'(x_0) = \\frac{f(x_0)}{x_0-x_1}").scale(0.8).move_to(5 * RIGHT + 3 * UP)
        self.play(Write(tex1))
        self.wait()

        tex2 = MathTex("x_1 = x_0 -", "\\frac{f(x_0)}{f'(x_0)}").scale(0.8).next_to(tex1, DOWN)
        tex3 = MathTex("x_1 = x_0 -", " \\frac{x_0^2-a}{2x_0}").scale(0.8).next_to(tex1, DOWN)
        tex4 = MathTex("x_1 = \\frac{1}{2}(x_0 + \\frac{a}{x_0})").scale(0.8).next_to(tex1, DOWN)
        self.play(Write(tex2))
        self.wait()
        self.play(ReplacementTransform(tex2, tex3))
        self.wait()
        self.play(ReplacementTransform(tex3, tex4))
        self.wait()
        self.play(Create(SurroundingRectangle(tex4)))
        self.wait()
        self.play(Create(VGroup(dot3, line1, dot4, tangent1)))

        x2 = x1 - (0.3 * x1**2 - a) / (0.6 * x1)
        dot5 = Dot().move_to(ax.c2p(x2, 0))
        self.play(Create(dot5))
        tex5 = MathTex("x_2 = \\frac{1}{2}(x_1 + \\frac{a}{x_1})").scale(0.8).next_to(tex4, DOWN)
        tex6 = MathTex("x_{n+1} = \\frac{1}{2}(x_n + \\frac{a}{x_n})").scale(0.8).next_to(tex5, DOWN, buff=1.2)
        dotted = DashedLine(start=tex5.get_bottom(), end=tex6.get_top())
        self.play(Write(MathTex("x_2").scale(0.8).next_to(dot5, DOWN)))
        self.play(Write(tex5))
        self.play(Create(dotted))
        self.play(Write(tex6))
        self.play(Write(SurroundingRectangle(tex6)))
        self.wait()

#function
class Sqrt(Scene):
   def construct(self):
       tex = MathTex("\sqrt{a}").scale(1.5)
       ques = MathTex("??").next_to(tex,DOWN)
       self.play(Write(tex))
       self.wait(2)
       self.play(FadeOut(ques))
       self.play(tex.animate.shift(UP))
       self.wait()
       tex1 = MathTex("f(x) = x^2-a")
       tex2 = MathTex("f(x) = (\sqrt{a})^2-a"," = 0").next_to(tex1,DOWN)
       self.play(Write(tex1))
       self.wait()
       self.play(Write(tex2[0]))
       self.wait()
       self.play(Write(tex2[1]))
       self.wait()
       self.play(FadeOut(tex2))
       self.play(Create(SurroundingRectangle(tex1)))
       self.wait()
       self.play(FadeOut(VGroup(tex,tex1)))


#Video Thumbnail
class YThumbnail(Scene):
    def construct(self):
        # Titles
        title3 = Text("How do Computers Compute", gradient=[TEAL, GREEN]).move_to(3.2 * UP).scale(1.5)
        title2 = Text("Square Roots?", gradient=[GREEN, TEAL]).next_to(title3, DOWN, buff=0.5).scale(1.5)
        method = Tex("Newton-Raphson Method").move_to(3.1 * DOWN).scale(2)
        
        # Axes and curve
        ax = Axes(x_range=(-1, 5), y_range=(-3, 3), axis_config={"include_tip": False})
        curve = ax.plot(lambda x: 0.3 * x**2 - 2, color=PINK)
        VGroup(ax, curve).shift(3 * LEFT + 2 * DOWN).scale(0.8)
        self.add(ax, curve, title3, title2, method)
        
        # Initial points and lines
        x0 = 4.3
        dot1 = Dot().move_to(ax.c2p(x0, 0))
        dot2 = Dot().move_to(ax.c2p(x0, curve.underlying_function(x0)))
        tangent = ax.get_secant_slope_group(x=x0, graph=curve, dx=0.01, secant_line_color=GREEN)
        line = DashedLine(start=ax.c2p(x0, 0), end=ax.c2p(x0, curve.underlying_function(x0)))
        self.add(dot1, dot2, line, tangent)
        self.add(MathTex("x_0").scale(0.8).next_to(dot1, DOWN))
        
        # First iteration
        x1 = x0 - (0.3 * x0**2 - 2) / (0.6 * x0)
        dot3 = Dot().move_to(ax.c2p(x1, 0))
        dot4 = Dot().move_to(ax.c2p(x1, curve.underlying_function(x1)))
        tangent1 = ax.get_secant_slope_group(x=x1, graph=curve, dx=0.01, secant_line_color=ORANGE, secant_line_length=5)
        line1 = DashedLine(start=ax.c2p(x1, 0), end=ax.c2p(x1, curve.underlying_function(x1)))
        self.add(MathTex("x_1").scale(0.8).next_to(dot3, DOWN), dot3)
        self.add(dot3, line1, dot4, tangent1)
        
        # Second iteration
        x2 = x1 - (0.3 * x1**2 - 2) / (0.6 * x1)
        dot5 = Dot().move_to(ax.c2p(x2, 0))
        self.add(MathTex("x_2").scale(0.8).next_to(dot5, DOWN), dot5)
        
        # Final text and arrow
        tex = MathTex("x_{n+1} = \\frac{1}{2}(x_n + \\frac{a}{x_n})").shift(4.3 * RIGHT)
        tex1 = Tex("sqrt()??").scale(1.5).move_to(3 * LEFT)
        arrow = Arrow(start=dot5.get_top(), end=tex1.get_bottom(), color=YELLOW_E)
        self.add(tex, tex1, arrow, SurroundingRectangle(tex))      