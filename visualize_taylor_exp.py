from manim import *
import math as m

class TaylorSeriesExpansion(Scene):
    def construct(self):
        self.camera.background_color = "#1e1e1e"  # Dark gray background

        functions = [
            {
                "label": r"f(x) = sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1}",
                "func": lambda x: m.sin(x),
                "expansion": [
                    r"x", r" - \frac{x^3}{3!}", r" + \frac{x^5}{5!}", r" - \frac{x^7}{7!}", 
                    r" + \frac{x^9}{9!}", r" - \frac{x^{11}}{11!}", r" + \frac{x^{13}}{13!}", 
                    r" - \frac{x^{15}}{15!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((-1)**k * x**(2*k+1) / m.factorial(2*k+1) for k in range(n+1)),
                "x_range": (-6, 6),
                "y_range": (-3, 3)
            },
            {
                "label": r"f(x) = cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n}",
                "func": lambda x: m.cos(x),
                "expansion": [
                    r"1", r" - \frac{x^2}{2!}", r" + \frac{x^4}{4!}", r" - \frac{x^6}{6!}", 
                    r" + \frac{x^8}{8!}", r" - \frac{x^{10}}{10!}", r" + \frac{x^{12}}{12!}", 
                    r" - \frac{x^{14}}{14!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((-1)**k * x**(2*k) / m.factorial(2*k) for k in range(n+1)),
                "x_range": (-6, 6),
                "y_range": (-3, 3)
            },
            {
                "label": r"f(x) = \tan(x)",
                "func": lambda x: m.tan(x),
                "expansion": [
                    r"x", r" + \frac{x^3}{3}", r" + \frac{2x^5}{15}", r" + \frac{17x^7}{315}",
                    r" + \frac{62x^9}{2835}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((x**(2*k+1)) / (2*k+1) for k in range(n+1)),
                "x_range": (-1, 1),
                "y_range": (-2, 2)
            },
            {
                "label": r"f(x) = \sinh(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{(2n+1)!}",
                "func": lambda x: m.sinh(x),
                "expansion": [
                    r"x", r" + \frac{x^3}{3!}", r" + \frac{x^5}{5!}", r" + \frac{x^7}{7!}",
                    r" + \frac{x^9}{9!}", r" + \frac{x^{11}}{11!}", r" + \frac{x^{13}}{13!}",
                    r" + \frac{x^{15}}{15!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((x**(2*k+1)) / m.factorial(2*k+1) for k in range(n+1)),
                "x_range": (-3, 3),
                "y_range": (-10, 10)
            },
            {
                "label": r"f(x) = \cosh(x) = \sum_{n=0}^{\infty} \frac{x^{2n}}{(2n)!}",
                "func": lambda x: m.cosh(x),
                "expansion": [
                    r"1", r" + \frac{x^2}{2!}", r" + \frac{x^4}{4!}", r" + \frac{x^6}{6!}",
                    r" + \frac{x^8}{8!}", r" + \frac{x^{10}}{10!}", r" + \frac{x^{12}}{12!}",
                    r" + \frac{x^{14}}{14!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((x**(2*k)) / m.factorial(2*k) for k in range(n+1)),
                "x_range": (-3, 3),
                "y_range": (-10, 10)
            },
            {
                "label": r"f(x) = \arcsin(x) = \sum_{n=0}^{\infty} \frac{(2n)!}{4^n (n!)^2 (2n+1)} x^{2n+1}",
                "func": lambda x: m.asin(x),
                "expansion": [
                    r"x", r" + \frac{x^3}{6}", r" + \frac{3x^5}{40}", r" + \frac{5x^7}{112}",
                    r" + \frac{35x^9}{1152}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((m.factorial(2*k) / (4**k * (m.factorial(k)**2) * (2*k+1))) * x**(2*k+1) for k in range(n+1)),
                "x_range": (-1, 1),
                "y_range": (-2, 2)
            },
                    
                    
            {
            "label": r"f(x) = \operatorname{arcsinh}(x) = \sum_{n=0}^{\infty} \frac{(-1)^n (2n)!}{4^n (n!)^2 (2n+1)} x^{2n+1}",
            "func": lambda x: m.asinh(x),
            "expansion": [
                r"x", r" - \frac{x^3}{6}", r" + \frac{3x^5}{40}", r" - \frac{5x^7}{112}",
                r"+ ............\infty"
            ],
            "taylor_terms": lambda x, n: sum(((-1)**k * m.factorial(2*k)) / (4**k * (m.factorial(k)**2) * (2*k+1)) * x**(2*k+1) for k in range(n+1)),
            "x_range": (-3, 3),
            "y_range": (-5, 5)
        },
        
        {
            "label": r"f(x) = \operatorname{arctanh}(x) = \sum_{n=0}^{\infty} \frac{x^{2n+1}}{2n+1}",
            "func": lambda x: m.atanh(x),
            "expansion": [
                r"x", r" + \frac{x^3}{3}", r" + \frac{x^5}{5}", r" + \frac{x^7}{7}",
                r"+ ............\infty"
            ],
            "taylor_terms": lambda x, n: sum((x**(2*k+1)) / (2*k+1) for k in range(n+1)),
            "x_range": (-0.9, 0.9),
            "y_range": (-2, 2)
        },

            {
                "label": r"f(x) = \ln(1+x) = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} x^n",
                "func": lambda x: m.log(1+x),
                "expansion": [
                    r"x", r" - \frac{x^2}{2}", r" + \frac{x^3}{3}", r" - \frac{x^4}{4}", 
                    r" + \frac{x^5}{5}", r" - \frac{x^6}{6}", r" + \frac{x^7}{7}", 
                    r" - \frac{x^8}{8}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((-1)**(k-1) * x**k / k for k in range(1, n+2)),
                "x_range": (-0.9, 2),
                "y_range": (-2, 3)
            },
            {
                "label": r"f(x) = e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}",
                "func": lambda x: m.exp(x),
                "expansion": [
                    r"1", r" + x", r" + \frac{x^2}{2!}", r" + \frac{x^3}{3!}", 
                    r" + \frac{x^4}{4!}", r" + \frac{x^5}{5!}", r" + \frac{x^6}{6!}", 
                    r" + \frac{x^7}{7!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum(x**k / m.factorial(k) for k in range(n+1)),
                "x_range": (-6, 6),
                "y_range": (-3, 7)
            },
            {
                "label": r"f(x) = e^{x^2} = \sum_{n=0}^{\infty} \frac{x^{2n}}{n!}",
                "func": lambda x: m.exp(x**2),
                "expansion": [
                    r"1", r" + x^2", r" + \frac{x^4}{2!}", r" + \frac{x^6}{3!}",
                    r" + \frac{x^8}{4!}", r" + \frac{x^{10}}{5!}", r" + \frac{x^{12}}{6!}",
                    r" + \frac{x^{14}}{7!}", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum((x**2)**k / m.factorial(k) for k in range(n+1)),
                "x_range": (-2, 2),
                "y_range": (-1, 10)
            },
            {
                "label": r"f(x) = \frac{1}{(1-x)} = \sum_{n=0}^{\infty} x^n",
                "func": lambda x: 1/(1-x),
                "expansion": [
                    r"1", r" + x", r" + x^2", r" + x^3", 
                    r" + x^4", r" + x^5", r" + x^6", 
                    r" + x^7", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum(x**k for k in range(n+1)),
                "x_range": (-0.9, 0.9),
                "y_range": (-3, 3)
            },
            {
                "label": r"f(x) = \frac{1}{1+x} = \sum_{n=0}^{\infty} (-1)^n x^n",
                "func": lambda x: 1 / (1 + x),
                "expansion": [
                    r"1", r" - x", r" + x^2", r" - x^3", r" + x^4",
                    r" - x^5", r" + x^6", r" - x^7", r"+ ............\infty"
                ],
                "taylor_terms": lambda x, n: sum(((-1)**k * x**k) for k in range(n+1)),
                "x_range": (-0.9, 0.9),
                "y_range": (-2, 2)
            }
        ]

        for function in functions:
            self.display_taylor_series(function)

    def display_taylor_series(self, function):
        # Create the MathTex for the expansion terms
        tex = MathTex(r"f(x) =", *function["expansion"])
        tex.move_to(2 * DOWN)

        # Create the axes for plotting
        ax = Axes(
            x_range=function["x_range"], 
            y_range=function["y_range"], 
            axis_config={"color": WHITE}
        )
        labels = ax.get_axis_labels(x_label="x", y_label=function["label"])
        
        # Plot the actual function
        graph1 = ax.plot(lambda x: function["func"](x), color=RED, stroke_width=8)

        # Create the Taylor series approximation graphs
        graphs = []
        num_terms = min(len(function["expansion"]), 10)  # Ensure we're not accessing more terms than available
        for n in range(num_terms):
            graph = ax.plot(lambda x, n=n: function["taylor_terms"](x, n), color=YELLOW_E, stroke_width=6)
            graphs.append(graph)

        # Display the initial function graph and label
        self.play(Create(ax), Create(graph1), Create(labels), Create(tex[0]))
        
        # Animate the Taylor series expansion terms one by one
        for i in range(1, num_terms):
            # Ensure we do not exceed the number of tex terms or graphs
            if i < len(tex) and i < len(graphs):
                self.play(ReplacementTransform(graphs[i-1], graphs[i]), Write(tex[i]))
                self.play(FadeOut(graphs[i-1]))

        self.wait()

        # Clear the scene for the next function, fade out all graphs and Taylor formula
        self.play(FadeOut(ax), FadeOut(labels), FadeOut(graph1), FadeOut(VGroup(*tex)), FadeOut(graphs[-1]))

# This block will automatically render the scene when the script is run
if __name__ == "__main__":
    config.pixel_height = 1080  # Set height for 1080p
    config.pixel_width = 1920   # Set width for 1080p
    config.frame_rate = 60      # Set 60 FPS
    config.quality = "high_quality"
    
    scene = TaylorSeriesExpansion()
    scene.render()
