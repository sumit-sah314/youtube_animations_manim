from manim import *
import numpy as np

class KadanesAlgorithm(Scene):
    def create_pointer(self, position, label_text):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=RED).scale(0.2)
        pointer.next_to(position, DOWN)
        label = Text(label_text, font_size=24).next_to(pointer, DOWN * 0.2)
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
        ).move_to(1.5 * DOWN)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Kadane's Algorithm", gradient=[BLUE, PURPLE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        kadanes_code = """
int maxSubArray(vector<int>& nums) {
    int sum = 0, max_sum = INT_MIN;
    for(int val : nums){
        sum += val;
        max_sum = max(sum, max_sum);
        if(sum < 0){
            sum = 0;
        }
    }
    return max_sum;
}
        """
        code_display = self.display_code(kadanes_code)

        # Array setup
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        array = VGroup(*[Square().scale(0.5) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(1.5 * UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        
        self.play(Create(array), Create(num_tex))
        
        # Initial sum and max_sum values
        sum_text = Tex("sum = ", "0")
        max_sum_text = Tex("max\\_sum =", "$-\\infty$")
        VGroup(sum_text, max_sum_text).arrange(DOWN, aligned_edge=LEFT, buff=1).shift(5 * LEFT)
        self.play(Write(sum_text), Write(max_sum_text))

        # Kadane's Algorithm Animation
        current_sum = 0
        max_sum = float('-inf')
        start_index = 0
        end_index = 0
        temp_start_index = 0

        for i in range(len(nums)):
            # i Pointer
            i_pointer = self.create_pointer(num_tex[i].get_center(), "i")
            self.play(Create(i_pointer))
            
            # Update current_sum and display change
            current_sum += nums[i]
            new_sum_text = Tex(f"{current_sum}").move_to(sum_text[1].get_center())
            self.play(Transform(sum_text[1], new_sum_text))
            
            # Update max_sum and start/end indices if current_sum exceeds max_sum
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = temp_start_index
                end_index = i
                new_max_sum_text = Tex(f"{max_sum}").move_to(max_sum_text[1].get_center())
                self.play(Transform(max_sum_text[1], new_max_sum_text))

                # Update the brace to highlight the current max subarray
                if hasattr(self, 'brace'):
                    self.play(FadeOut(self.brace))
                self.brace = Brace(VGroup(*num_tex[start_index:end_index + 1]), UP, color=YELLOW)
                self.play(Create(self.brace))

            # Reset current_sum and temp_start_index if current_sum drops below zero
            if current_sum < 0:
                current_sum = 0
                temp_start_index = i + 1  # New start for potential subarray
                reset_sum_text = Tex("0").move_to(sum_text[1].get_center())
                self.play(Transform(sum_text[1], reset_sum_text))

            # Highlighting the current value being considered
            self.play(num_tex[i].animate.set_color(YELLOW))
            self.wait(0.5)
            self.play(num_tex[i].animate.set_color(WHITE))
            self.play(FadeOut(i_pointer))

        # Final wait before ending the scene
        self.play(FadeOut(code_display), FadeOut(sum_text), FadeOut(max_sum_text))
        self.wait(1)
