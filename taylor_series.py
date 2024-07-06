"""
taylor_series.py

This script uses the Manim library to create animations that visualize the Taylor series.
It contains multiple classes, each serving a specific purpose related to the Taylor series animations for the YouTube channel "Math Simplified."

Classes:
- CosExpansion: Visualizes the Taylor series expansion of cos(x) around x = 0.
- CosExpansion2: Visualizes the Taylor series expansion of cos(x) around a different point of expansion.
- SinExpansion: Visualizes the Taylor series expansion of sin(x).
- TaylorProofCos: Provides a step-by-step proof of the Taylor series for cos(x).
- GeneralProof: Provides a general proof framework for any function.
- Poly: Visualizes a general polynomial function.
- Taylor: Shows the Taylor series expansions for cos(x), sin(x), and e^x.
- eExpansion: Visualizes the Taylor series expansion of e^x.
- TaylorVsMaclaurine: Compares the Taylor series and Maclaurin series expansions.
- Thumbnail: Generates a thumbnail visual for the video.

Each class uses Manim to construct animations demonstrating various aspects of Taylor series video.

Functions:
- dcos(n, a): Defines the derivative of cos(x) used in the Taylor series expansions.
- maclaurine_exp(x): Computes the Maclaurin series expansion of cos(x) around x = 0.
- taylor_exp(x): Computes the Taylor series expansion of cos(x) around x = π.

Dependencies: Requires Manim and standard Python libraries (numpy, math).

"""

from manim import *
import numpy as np
import math as m

# Function definitions (dcos, maclaurine_exp, taylor_exp) are defined here.

def dcos(n,a):
   if(n%4==1):
      return -np.sin(a)
   elif(n%4==2):
      return -np.cos(a)
   elif(n%4==3):
      return np.sin(a)
   else:
      return np.cos(a)

epsilon = 0.001

def maclaurine_exp(x):
   sum = 0
   i=0
   while(abs(sum-np.cos(4))>epsilon):
    sum += dcos(i,0)*x**i/m.factorial(i)
    i+=1
   return sum,i

def taylor_exp(x):
 sum = 0
 i=0
 while(abs(sum-np.cos(4))>epsilon):
   sum += dcos(i,np.pi)*(x-np.pi)**i/m.factorial(i)
   i+=1
 return sum,i


class TaylorSeriesFormula(Scene):
    def construct(self):
        taylor_series = MathTex(
            "f(x) = ", "\\sum_{n=0}^{\infty}", "\\frac{f^{(n)}(a)}{n!}(x - a)^n"
        ).scale(1.5)
        self.play(Write(taylor_series))
        self.wait()
        
class Poly(Scene):
   def construct(self):
      self.play(Write(MathTex("p(x) = a_0 + a_1x + a_2x^2 + ............. + a_nx^n",color=BLUE).shift(3*UP)))
      self.wait()

class Taylor(Scene):
   def construct(self):
      tex1 = MathTex("cos(x) = ","1"," - \\frac{x^2}{2!}"," + \\frac{x^4}{4!}"," - \\frac{x^6}{6!}"," + \\frac{x^8}{8!} "," - \\frac{x^{10}}{10!} "," + \\frac{x^{12}}{12!} "," - \\frac{x^{14}}{14!} ","+ ............\infty",color=BLUE).scale(0.9).move_to(2*UP)
      tex2 =  MathTex("sin(x) = ","x"," - \\frac{x^3}{3!}"," + \\frac{x^5}{5!}"," - \\frac{x^7}{7!}"," + \\frac{x^9}{9!} "," - \\frac{x^{11}}{11!} "," + \\frac{x^{13}}{13!} "," - \\frac{x^{15}}{15!} ","+ ............\infty",color=RED).scale(0.9)
      tex3 = MathTex("e^x = ","1"," + \\frac{x}{1!}"," + \\frac{x^2}{2!}"," + \\frac{x^3}{3!}"," + \\frac{x^4}{4!} "," + \\frac{x^5}{5!} "," + \\frac{x^{6}}{6!} "," + \\frac{x^7}{7!} ","+ ............\infty",color=YELLOW).move_to(2*DOWN)
      self.play(Write(tex1),Write(tex2),Write(tex3))
      self.wait(2)


class CosExpansion(Scene):
    def construct(self):
        tex = MathTex(
            "f(x) = ", "1", " - \\frac{x^2}{2!}", " + \\frac{x^4}{4!}",
            " - \\frac{x^6}{6!}", " + \\frac{x^8}{8!} ", " - \\frac{x^{10}}{10!} ",
            " + \\frac{x^{12}}{12!} ", " - \\frac{x^{14}}{14!} ", "+ ............\\infty",
            color=BLUE
        )
        tex.move_to(2 * DOWN)
        ax = Axes((-6, 6), (-3, 3))
        labels = ax.get_axis_labels(x_label="x", y_label=MathTex(r"f(x)=cos(x)"))
        graph1 = ax.plot(lambda x: m.cos(x), color=PINK)

        graphs = [
            ax.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k) / m.factorial(2*k) for k in range(n+1)
            ), color=YELLOW_E) for n in range(10)
        ]

        recs = [
            SurroundingRectangle(VGroup(tex[0], tex[i]), color=WHITE) for i in range(1, 9)
        ]

        self.play(Create(ax), Create(graph1), Create(labels))
        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.wait()
        self.play(Create(recs[0]))
        self.wait()

        for i in range(1,8):
            self.play(ReplacementTransform(graphs[i-1], graphs[i]), Write(tex[i+1]),Transform(recs[0],recs[i]))
            self.wait()
        
        self.play(FadeOut(recs[0]))
        self.play(Write(tex[9]))
        self.wait()

class CosExpansion2(Scene):
    def construct(self):
        a = ValueTracker(0)

        tex = MathTex(
            "f(x) = ", "f(a)", " + f'(a)\\frac{(x-a)^1}{1!}", " + f''(a)\\frac{(x-a)^2}{2!}",
            " + f'''(a)\\frac{(x-a)^3}{3!}", " + f''''(a)\\frac{(x-a)^4}{4!}", "+ ............\\infty",
            color=BLUE
        ).scale(0.6)
        tex.move_to(2 * DOWN)

        ax = Axes((-6, 6), (-3, 3))
        labels = ax.get_axis_labels(x_label="x", y_label=MathTex("f(x)=cos(x)"))
        graph1 = ax.plot(lambda x: m.cos(x), color=PINK)

        dot = always_redraw(lambda: Dot().move_to(ax.c2p(a.get_value(), np.cos(a.get_value()))))
        self.add(ax, graph1, labels, dot)
        self.play(a.animate.set_value(2))

        graphs = [
            ax.plot(lambda x, n=n: sum(
                dcos(k, a.get_value()) * (x - a.get_value())**k / m.factorial(k) for k in range(n+1)
            ), color=YELLOW_E) for n in range(9)
        ]

        self.wait(2)
        self.play(Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.wait()

        for i in range(1, 6):
            self.play(ReplacementTransform(graphs[i-1], graphs[i]), Write(tex[i+1]))
            self.wait()

        self.wait()

class SinExpansion(Scene):
    def construct(self):

        tex = MathTex(
            "f(x) = ", "x", " - \\frac{x^3}{3!}", " + \\frac{x^5}{5!}",
            " - \\frac{x^7}{7!}", " + \\frac{x^9}{9!} ", " - \\frac{x^{11}}{11!} ",
            " + \\frac{x^{13}}{13!} ", " - \\frac{x^{15}}{15!} ", "+ ............\\infty"
        )
        tex.move_to(2 * DOWN)

        ax = Axes((-6, 6), (-3, 3))
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)=sin(x)")
        graph1 = ax.plot(lambda x: m.sin(x), color=RED)

        graphs = [
            ax.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k+1) / m.factorial(2*k+1) for k in range(n+1)
            ), color=YELLOW_E) for n in range(10)
        ]

        self.play(Create(ax), Create(graph1), Create(labels), Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))

        for i in range(1, 9):
            self.play(ReplacementTransform(graphs[i-1], graphs[i]), Write(tex[i+1]))
            self.wait()

        self.play(Write(tex[9]))
        self.wait()


class eExpansion(Scene):
    def construct(self):
        tex = MathTex(
            "e^x = ", "1", " + \\frac{x}{1!}", " + \\frac{x^2}{2!}", 
            " + \\frac{x^3}{3!}", " + \\frac{x^4}{4!}", " + \\frac{x^5}{5!}", 
            " + \\frac{x^6}{6!}", " + \\frac{x^7}{7!}", "+ ............\\infty",
            color=BLUE
        ).move_to(2 * DOWN)

        ax = Axes((-6, 6), (-3, 3))
        labels = ax.get_axis_labels(x_label="x", y_label=MathTex("f(x)=e^x"))
        graph1 = ax.plot(lambda x: m.e**x, color=PINK)

        def taylor_series_approx(n):
            return ax.plot(lambda x: sum(x**k / m.factorial(k) for k in range(n + 1)), color=YELLOW_E)

        graphs = [taylor_series_approx(n) for n in range(10)]

        self.play(Create(ax), Create(graph1), Create(labels))
        self.play(Create(tex[0]))
        self.play(Create(VGroup(graphs[0], tex[1])))
        self.wait()

        for i in range(1, 9):
            self.play(ReplacementTransform(graphs[i-1], graphs[i]), Write(tex[i+1]))
            self.wait()

        self.play(Write(tex[9]))
        self.wait()


class TaylorProofCos(Scene):
    def construct(self):
        # Taylor series representations
        series1 = MathTex("cos(x) = 1 - \\frac{1}{2}x^2","+ \\frac{1}{24}x^4 -","\\frac{1}{720}x^6 +","............", color=BLUE).move_to(DOWN)
        series2 = MathTex("cos(x) = 1 - \\frac{1}{2!}x^2","+ \\frac{1}{4!}x^4 -","\\frac{1}{6!}x^6 +","............", color=BLUE).move_to(DOWN)
        series3 = MathTex("cos(-x) = 1 - \\frac{1}{2!}(-x)^2","+ \\frac{1}{4!}(-x)^4 -","\\frac{1}{6!}(-x)^6 +","............", color=BLUE).move_to(DOWN)
        series4 = MathTex("cos(x) = 1 - \\frac{1}{2!}x^2","+ \\frac{1}{4!}x^4 -","\\frac{1}{6!}x^6 +","............", color=BLUE).move_to(DOWN)

        # Definitions and expressions
        tex1 = MathTex("f(","x",")","=","cos(","x",")", color=BLUE).move_to(3 * UP + 4.5 * LEFT)
        tex1_1 = MathTex("f(","0",")","=","cos(","0",")").next_to(tex1, DOWN, buff=0.8)
        tex1_2 = MathTex("f'(","x",")","=","-sin(","x",")").next_to(tex1_1, DOWN, buff=0.8)
        tex1_2_1 = MathTex("f'(","0",")","=","-sin(","0",")").next_to(tex1_1, DOWN, buff=0.8)
        tex1_3 = MathTex("f''(","x",")","=","-cos(","x",")").next_to(tex1_2, DOWN, buff=0.8)
        tex1_3_1 = MathTex("f''(","0",")","=","-cos(","0",")").next_to(tex1_2, DOWN, buff=0.8)
        tex1_3_2 = MathTex("f'''(0) = 0").next_to(tex1_3_1[2], DOWN, buff=0.8)
        tex1_3_3 = MathTex("f''''(0) = 1").next_to(tex1_3_1[2], DOWN, buff=0.8)

        # Polynomial approximation
        tex2 = MathTex("p(x) = ","a_0"," + ","a_1","x"," + ","a_2","x^2"," + ","a_3","x^3","+","a_4","x^4","..........", color=BLUE).next_to(tex1, RIGHT, buff=0.8)
        tex2_0 = MathTex("p(x) = ","1"," + ","0","x"," - ","\\frac{1}{2}","x^2"," + ","0","x^3","+","\\frac{1}{24}","x^4","+..........", color=BLUE).next_to(tex1, RIGHT, buff=0.8)
        
        for i in range(3, len(tex2_0)): 
            tex2_0[i].move_to(tex2[i].get_center() + 0.05 * DOWN)

        tex2_1 = MathTex("p(","0",")","=","a_0"," + ","a_1","0"," + ","a_2","0^2"," + ","a_3","0^3","+","a_4","0^4","+..........").next_to(tex2, DOWN, buff=0.8)
        tex2_2 = MathTex("p'(x)","=","a_1"," + " ,"2a_2","x"," + ","3a_3","x^2"," + ","4a_4","x^3","............").next_to(tex2_1, DOWN, buff=0.8)
        tex2_2_1 = MathTex("p'(0)","=","a_1"," + " ,"2a_2","0"," + ","3a_3","0^2"," + ","4a_4","0^3","............").next_to(tex2_1, DOWN, buff=0.8)

        tex3 = MathTex("p''(x)","=","2a_2"," + ","3.2a_3","x"," + ","4.3a_4","x^2",".............").next_to(tex2_2, DOWN, buff=0.8)
        tex3_1 = MathTex("p''(0)","=","2a_2"," + ","3.2a_3","0"," + ","4.3a_4","0^2",".............").next_to(tex2_2, DOWN, buff=0.8)
        tex3_2 = MathTex("\\frac{-1}{2}=a_2").move_to(tex3_1[1].get_center())
        tex3_3 = MathTex("0 = a_3").next_to(tex3_1[1], DOWN, buff=0.8)
        tex3_4 = MathTex("\\frac{1}{24} = a_4").next_to(tex3_1[1], DOWN, buff=0.8)

        tex2_0[3].move_to(tex2[3].get_center() + 0.1 * UP)

        cos_vals = [
            MathTex("1", "1").move_to(tex1_1[3]),
            MathTex("0", "0").move_to(tex1_2_1[3]),
            MathTex("-1", "-1").move_to(tex1_3_1[3]),
            MathTex("0", "0").move_to(tex1_3_2)
        ]

        # Axes and graphs
        ax = Axes(x_range=(-3.14, 3.14), x_length=10, y_range=[-2, 2], y_length=5).move_to(4 * RIGHT + UP).scale(0.6)
        graph1 = ax.plot(lambda x: m.cos(x), color=PINK)
        graph2 = ax.plot(lambda x: 1, color=YELLOW_E)
        graph3 = ax.plot(lambda x: 1 - x**2 / m.factorial(2), color=YELLOW_E)
        graph4 = ax.plot(lambda x: 1 - x**2 / m.factorial(2) + x**4 / m.factorial(4), color=YELLOW_E)

        line = Line(start=[-2.5, 3, 0], end=[-2.5, -3, 0])

        # Animations
        self.play(Create(tex1), Create(tex2), Create(line), Create(VGroup(ax, graph1)))
        self.wait(2)
        self.play(Create(tex1_1), Create(tex2_1))
        self.wait()
        self.play(FadeOut(tex2_1[5:]))
        self.wait()
        self.play(ReplacementTransform(tex1_1[4:7], cos_vals[0][0]))
        self.wait()
        self.play(ReplacementTransform(tex2_1[0:3], cos_vals[0][1]))
        self.wait()
        self.play(ReplacementTransform(tex2[1], tex2_0[1]), Create(graph2))
        self.wait()
        self.play(Create(tex1_2), Create(tex2_2))
        self.wait()
        self.play(ReplacementTransform(tex1_2, tex1_2_1), ReplacementTransform(tex2_2, tex2_2_1))
        self.play(FadeOut(tex2_2_1[3:]))
        self.play(ReplacementTransform(tex1_2_1[4:7], cos_vals[1][0]), ReplacementTransform(tex2_2_1[0], cos_vals[1][1]))
        self.wait()
        self.play(ReplacementTransform(tex2[3], tex2_0[3]))
        self.wait()
        self.play(Write(tex1_3), Write(tex3))
        self.wait()
        self.play(ReplacementTransform(tex1_3, tex1_3_1), ReplacementTransform(tex3, tex3_1))
        self.wait()
        self.play(FadeOut(tex3_1[3:]))
        self.play(ReplacementTransform(tex1_3_1[4:7], cos_vals[2][0]))
        self.play(Transform(tex3_1[0], cos_vals[2][1]))
        self.play(ReplacementTransform(tex3_1[0:3], tex3_2))
        self.wait()
        self.play(ReplacementTransform(tex2[5:7], tex2_0[5:7]), ReplacementTransform(graph2, graph3))
        self.wait()
        self.play(Write(tex1_3_2), Write(tex3_3))
        self.wait()
        self.play(ReplacementTransform(tex2[9], tex2_0[9]))
        self.wait()
        self.play(ReplacementTransform(tex1_3_2, tex1_3_3), ReplacementTransform(tex3_3, tex3_4))
        self.wait()
        self.play(ReplacementTransform(tex2[12], tex2_0[12]), ReplacementTransform(graph3, graph4))
        self.wait()
        self.play(FadeOut(VGroup(line, tex1_3_3, tex3_3, tex1, tex1_1[0:4], tex1_2_1[0:4], tex1_3_1[0:4], *cos_vals, tex3_4, tex3_2, tex2_1[3:5], tex2_2_1[1:3])))
        self.wait()
        self.play(ReplacementTransform(tex2, series1), FadeOut(VGroup(tex2_0[5:7], tex2_0[9], tex2_0[12])))
        self.wait(2)
        self.play(ReplacementTransform(series1, series2))
        self.wait(2)
        self.play(ReplacementTransform(series2, series3))
        self.wait()
        self.play(ReplacementTransform(series3, series4))
        self.play(Create(SurroundingRectangle(series2, color=YELLOW)))
        self.wait()


class GeneralProof(Scene):
    def construct(self):
       tex1 =  MathTex("f(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + a_4x^4 +.............."," = \sum_{n=0}^{\infty}a_nx^n").move_to(2*UP)
       tex2 = MathTex("a_n","??").scale(2)
       tex3 = MathTex("f^n(","x",")"," = ","n(n-1)(n-2)...2.1","a_n"," + (terms)x")

       tex4 = MathTex("0","0","a","0","0")
       tex4[0].move_to(tex3[1].get_center())
       tex4[1].move_to(tex3[6].get_center())
       
       tex5 = MathTex("f^n(0) = n!a_n")
       tex7 = MathTex("a_n = \\frac{f^n(0)}{n!}")
       
       self.play(Write(tex1[0]))
       self.wait(2)
       self.play(Write(tex1[1]))
       self.play(ShowCreationThenFadeOut(tex2))
       self.play(Write(tex3))
       self.play(Transform(tex3[1],tex4[0]),Transform(tex3[6],tex4[1]))
       self.play(tex3[0:6].animate.move_to(ORIGIN), FadeOut(tex3[6]))
       self.wait()
       
       brace = Brace(tex3[4],DOWN,color=YELLOW)
       tex6 = MathTex("n!").next_to(brace,DOWN)
       
       self.play(Create(brace),Write(tex6))
       self.wait()
       self.play(FadeOut(VGroup(brace,tex6)),ReplacementTransform(tex3[0:7],tex5))
       self.wait()
       self.play(ReplacementTransform(VGroup(tex3[0:4],tex3[5],tex5),tex7))
       self.wait()
       self.play(ShowCreationThenFadeOut(SurroundingRectangle(tex7),color=YELLOW))
       
       tex8 = MathTex("f(x) = \sum_{n=0}^{\infty}","\\frac{f^n(0)}{n!}","x^n").move_to(2*UP+3*LEFT)
       tex8_1 = Tex("Maclaurin Series").next_to(tex8,UP,buff=0.5)
       self.play(ReplacementTransform(VGroup(tex1,tex7),tex8))
       self.wait()
       tex9 = MathTex("f(x) = \sum_{n=0}^{\infty}","\\frac{f^n(a)}{n!}","(x-a)^n").next_to(tex8,RIGHT,buff=1)
       tex9_1 = Tex("Taylor Series").next_to(tex9,UP,buff=0.5)
       
       self.play(Write(tex9),Write(tex9_1))
       self.wait(2)
       self.play(ReplacementTransform(tex9[1].copy(),tex8[1]),ReplacementTransform(tex9[2].copy(),tex8[2]))
       self.wait()
       self.play(Write(tex8_1))
      #  self.play(VGroup(tex8,tex9,tex8_1,tex9_1).animate.scale(0.8).move_to(3*UP))
       self.wait(2)
      
       k = ValueTracker(0)
       
       ax = Axes((-6,6),(-3,3)).move_to(DOWN)
      #  labels = ax.get_axis_labels(x_label="x",y_label=MathTex(r"f(x)=cos(x)"))
       
       graph = ax.plot(lambda x: np.cos(x))
       graphs = [
            ax.plot(lambda x, n=n: sum(
                (-1)**k * x**(2*k) / m.factorial(2*k) for k in range(n+1)
            ), color=YELLOW_E) for n in range(5)
        ]
      
       dot = always_redraw(lambda: Dot().move_to(ax.c2p(k.get_value(),np.cos(k.get_value()),0)))
       line = always_redraw(lambda: DashedLine(start=ax.c2p(k.get_value(),0,0), end=ax.c2p(k.get_value(), graph.underlying_function(k.get_value()),0)))
       brace = always_redraw(lambda: Brace(line,RIGHT))
       tex0 = always_redraw(lambda: Tex(f"a = {round(k.get_value(),2)}").next_to(ax.c2p(k.get_value(),0,0),UP).scale(0.5))
       tex0_1 = always_redraw(lambda: Tex(f"f(a)").next_to(brace,RIGHT,buff=0.1).scale(0.5))
       
       self.play(Create(ax),Create(graph),Create(dot), Write(tex0),Write(tex0_1),Write(brace),Create(line))
       self.play(Create(graphs[0]))
       for i in range(1,5):
        self.play(ReplacementTransform(graphs[i-1],graphs[i]))
       self.play(FadeOut(graphs[4]))
       
       tex = MathTex("f(x) = ","f(a)"," + f'(a)\\frac{(x-a)^1}{1!}"," + f''(a)\\frac{(x-a)^2}{2!}"," + f'''(a)\\frac{(x-a)^3}{3!}"," + f''''(a)\\frac{(x-a)^4}{4!}","+ ............\infty",color=BLUE).scale(0.6)
       tex.move_to(2.5*DOWN)
      
       self.play(k.animate.set_value(3))
       
       
       a = 3

       Graphs = [
            ax.plot(lambda x, n=n: sum(
                dcos(k, a) * (x - a)**k / m.factorial(k) for k in range(n+1)
            ), color=YELLOW_E) for n in range(5)
        ]
       
       Graph9 = always_redraw(lambda: ax.plot(lambda x: np.cos(k.get_value())+ dcos(1,k.get_value())*(x-k.get_value())/m.factorial(1)+ dcos(2,k.get_value())*(x-k.get_value())**2/m.factorial(2)+ 
                                              dcos(3,k.get_value())*(x-k.get_value())**3/m.factorial(3)+ dcos(4,k.get_value())*(x-k.get_value())**4/m.factorial(4)+ dcos(5,k.get_value())*(x-k.get_value())**5/m.factorial(5)+ 
                                              dcos(6,k.get_value())*(x-k.get_value())**6/m.factorial(6)+ dcos(7,k.get_value())*(x-k.get_value())**7/m.factorial(7),color=YELLOW_E))
       
       self.play(Create(tex[0]))
       self.play(Create(VGroup(Graphs[0],tex[1])))
       for i in range(1,5):
        self.play(ReplacementTransform(Graphs[i-1],Graphs[i]),Write(tex[i+1]))
       
       self.play(ReplacementTransform(Graphs[4],Graph9))
       self.wait(2)
       self.play(k.animate.set_value(-1),run_time=2)
       self.wait()


class TaylorVsMaclaurine(Scene):
    def construct(self):
        k = ValueTracker(0)
        
        # Setup axes
        ax = Axes(x_range=(-1, 5), y_range=(-2, 2), axis_config={"include_numbers": True})
        
        # Define graphs for cosine and its Taylor/Maclaurin series approximations
        graphs = [
            ax.plot(lambda x: m.cos(x), color=PINK),
            ax.plot(lambda x: 1, color=YELLOW_E),
            ax.plot(lambda x: 1 - x**2 / m.factorial(2), color=YELLOW_E),
            ax.plot(lambda x: 1 - x**2 / m.factorial(2) + x**4 / m.factorial(4), color=YELLOW_E),
            ax.plot(lambda x: 1 - x**2 / m.factorial(2) + x**4 / m.factorial(4) - x**6 / m.factorial(6), color=YELLOW_E)
        ]

        # Important points and their labels
        dots = [
            Dot().move_to(ax.c2p(4, np.cos(4), 0)),
            Dot().move_to(ax.c2p(np.pi, np.cos(np.pi), 0)),
            Dot().move_to(ax.c2p(0, 1, 0))
        ]
        labels = [
            MathTex("a = \pi").next_to(dots[1], DOWN),
            MathTex("a = 0").next_to(dots[2], UP)
        ]

        # Additional elements
        line = DashedLine(start=ax.c2p(4, 0, 0), end=ax.c2p(4, np.cos(4), 0))
        brace = Brace(line, RIGHT)
        tex0 = Tex("x = 4").next_to(ax.c2p(4, 0, 0), UP).scale(0.5)
        tex0_1 = Tex("f(4)").next_to(brace, RIGHT, buff=0.1).scale(0.5)
        title = Tex("Maclaurine vs. Taylor").scale(1.5).move_to(3 * UP)

        # Play initial animations
        self.play(Create(ax), Create(graphs[0]), Create(VGroup(*dots)), Write(VGroup(tex0, tex0_1, *labels, title)), Write(brace), Create(line))

        a = np.pi

        # Define Taylor series centered at a
        taylor_graphs = [
            ax.plot(lambda x: np.cos(a), color=RED_E),
            ax.plot(lambda x: np.cos(a) + (x-a)**2 / m.factorial(2), color=RED_E),
            ax.plot(lambda x: np.cos(a) + (x-a)**2 / m.factorial(2) - (x-a)**4 / m.factorial(4), color=RED_E),
            ax.plot(lambda x: np.cos(a) + (x-a)**2 / m.factorial(2) - (x-a)**4 / m.factorial(4) + (x-a)**6 / m.factorial(6), color=RED_E)
        ]

        # Redraw Taylor series graph based on tracker value
        def taylor_series_func(x):
            a = k.get_value()
            return np.cos(a) + sum(dcos(n, a) * (x-a)**n / m.factorial(n) for n in range(1, 7))

        dynamic_taylor_graph = always_redraw(lambda: ax.plot(taylor_series_func, color=YELLOW_E))

        # Play graph transformations
        self.play(Create(taylor_graphs[0]), Create(graphs[1]))
        for i in range(1, len(taylor_graphs)):
            self.play(ReplacementTransform(taylor_graphs[i-1], taylor_graphs[i]), ReplacementTransform(graphs[i], graphs[i+1]))
        
        self.play(ReplacementTransform(taylor_graphs[-1], dynamic_taylor_graph))
        self.wait()


class Thumbnail(Scene):
   def construct(self):
      k= ValueTracker(2.5)
      ax = Axes((-6,6),(-2,2),y_length=4).move_to(1.8*DOWN)
      tex9 = MathTex("f(x) = \sum_{n=0}^{\infty}","\\frac{f^n(a)}{n!}","(x-a)^n").move_to(0.6*UP).scale(1.3)
      tex9_1 = Tex("A Polynomial Approximation of a ").scale(1.5).move_to(3.5*UP)
      # tex9_1[0].set_color(BLUE)
      tex10 = Tex("Non-Polynomial Function").next_to(tex9_1,DOWN,buff=0.5).scale(1.5)
      tex = MathTex("f(x) = ","f(a)"," + f'(a)\\frac{(x-a)^1}{1!}"," + f''(a)\\frac{(x-a)^2}{2!}"," + f'''(a)\\frac{(x-a)^3}{3!}"," + f''''(a)\\frac{(x-a)^4}{4!}","+ ............\infty",color=BLUE).scale(0.6)
      tex.move_to(3.5*DOWN)
      arrow = Arrow(start=ax.c2p(0,1,0),end= ax.c2p(0.8,1.8,0),color=YELLOW_E)
      #  labels = ax.get_axis_labels(x_label="x",y_label=MathTex(r"f(x)=cos(x)"))
       
      graph1 = ax.plot(lambda x: m.cos(x),color=PINK)
      Graph9 = always_redraw(lambda: ax.plot(lambda x: np.cos(k.get_value())+ dcos(1,k.get_value())*(x-k.get_value())/m.factorial(1)+ dcos(2,k.get_value())*(x-k.get_value())**2/m.factorial(2)+ dcos(3,k.get_value())*(x-k.get_value())**3/m.factorial(3)+ dcos(4,k.get_value())*(x-k.get_value())**4/m.factorial(4)+ dcos(5,k.get_value())*(x-k.get_value())**5/m.factorial(5)+ dcos(6,k.get_value())*(x-k.get_value())**6/m.factorial(6)+ dcos(7,k.get_value())*(x-k.get_value())**7/m.factorial(7),color=YELLOW_E))
      dot = always_redraw(lambda: Dot().move_to(ax.c2p(k.get_value(),np.cos(k.get_value()),0)))
      line = always_redraw(lambda: DashedLine(start=ax.c2p(k.get_value(),0,0), end=ax.c2p(k.get_value(), graph1.underlying_function(k.get_value()),0)))
      brace = always_redraw(lambda: Brace(line,RIGHT))
      tex0 = always_redraw(lambda: Tex(f"a = {round(k.get_value(),2)}").next_to(ax.c2p(k.get_value(),0,0),UP).scale(0.5))
      tex0_1 = always_redraw(lambda: Tex(f"f(a)").next_to(brace,RIGHT,buff=0.1).scale(0.5))

      self.add(ax,tex9,tex9_1,tex,graph1,Graph9,dot,line,brace,tex0,tex0_1,tex10)
      self.add(SurroundingRectangle(tex9,color=RED))
       