from manim import *
import numpy as np

class ContainerWithMostWater(Scene):
    def create_pointer(self, position, label_text, color=BLUE):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=color).scale(0.1)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=22).next_to(pointer, DOWN * 0.2)
        return VGroup(pointer, label)
    
    def display_code(self, code_text):
        """Displays code snippet at the bottom."""
        code = Code(
            code=code_text,
            tab_width=4,
            background="window",
            language="C++",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).move_to(3.2*RIGHT + 0.5 * DOWN).scale(0.7)
        self.play(Create(code))
        return code


    def construct(self):
        # Title Text
        title = Text("Container with Most Water", gradient=[BLUE, PURPLE]).move_to(3 * UP)
        self.add(title)
        # Code snippet at the bottom
        container_with_most_water_code = """
        def max_area(height):
            left, right = 0, len(height) - 1
            max_area = 0
            
            while left < right:
                width = right - left
                min_height = min(height[left], height[right])
                area = width * min_height
                max_area = max(max_area, area)

                # Move the pointer corresponding to the shorter height
                if height[left] < height[right]:
                    left += 1
                else:
                    right -= 1
                    
            return max_area
        """

        code_display = self.display_code(container_with_most_water_code)
        # Heights of the vertical bars representing the container
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        
        # Scaling factor for bars and container
        scale_factor = 0.2

        # Create bars for each height and align bases
        bars = VGroup(*[
            Rectangle(width=0.2, height=h * scale_factor, color=RED, fill_opacity=1).align_to(ORIGIN, DOWN)
            for h in heights
        ]).arrange(RIGHT, buff=0.5, aligned_edge=DOWN).move_to( 3.8 * LEFT + 0.5* DOWN)

        # Labels for bar heights
        height_labels = VGroup(*[
            MathTex(str(h)).next_to(bar, UP).scale(0.8) for h, bar in zip(heights, bars)
        ])
        line = Line(start=bars[0].get_bottom(), end=bars[8].get_bottom(),color=RED)
        self.play(Create(bars), Create(height_labels),Create(line))

        

        # Initial pointers setup
        left, right = 0, len(heights) - 1
        max_area = 0

        # Create initial pointers
        left_pointer = self.create_pointer(bars[left].get_bottom(), "left", color=YELLOW)
        right_pointer = self.create_pointer(bars[right].get_bottom(), "right", color=GREEN)
        self.play(Create(left_pointer), Create(right_pointer))

        area_text = Tex("area = ", color=BLUE).move_to(4 * LEFT + 2 * UP).scale(0.6)
        max_area_text = Tex("max\_area = ",color = BLUE).next_to(area_text,DOWN).scale(0.6)
        self.play(Write(area_text), Write(max_area_text))
        
        # Container with Most Water animation
        while left < right:
            # Calculate the area
            width = bars[right].get_x() - bars[left].get_x()  # Directly calculate the distance between left and right bars
            current_height = min(heights[left], heights[right]) * scale_factor  # Height scaled with `scale_factor`
            area = (right - left) * min(heights[left], heights[right])  # Area calculation for display purposes
            max_area = max(max_area, area)
            
            # Highlight container area between pointers
            container = Rectangle(width=width, height=current_height, color=BLUE, fill_opacity=0.3)
            container.move_to((bars[left].get_center() + bars[right].get_center()) / 2)
            container.align_to(bars[left], DOWN)  # Align container base with bars
            # Display area calculation
            area_text1 = MathTex(f"{right - left} \\times {min(heights[left], heights[right])} = {area}").next_to(area_text, RIGHT, buff=0.3).scale(0.6)
            max_area_text1 = MathTex(f"{max_area}").next_to(max_area_text, RIGHT, buff=0.3).scale(0.6)
            self.play(Create(container), Write(area_text1), Write(max_area_text1))
            self.wait(2)

            # Move the pointer corresponding to the shorter bar
            if heights[left] < heights[right]:
                self.play(FadeOut(left_pointer), FadeOut(container), FadeOut(area_text1), FadeOut(max_area_text1))
                left += 1
                left_pointer = self.create_pointer(bars[left].get_bottom(), "left", color=YELLOW)
                self.play(Create(left_pointer))
            else:
                self.play(FadeOut(right_pointer), FadeOut(container), FadeOut(area_text1), FadeOut(max_area_text1))
                right -= 1
                right_pointer = self.create_pointer(bars[right].get_bottom(), "right", color=GREEN)
                self.play(Create(right_pointer))

        # Cleanup and wait
        self.play(FadeIn(Tex("49").next_to(area_text, RIGHT, buff=0.3).scale(0.6)), FadeIn(Tex("0").next_to(max_area_text, RIGHT, buff=0.3).scale(0.6)))

        self.wait(2)
