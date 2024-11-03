from manim import *
import numpy as np

class BinarySearch(Scene):
    def create_pointer(self, position, label_text, color=BLUE):
        """Creates a pointer with a label below the given position."""
        pointer = Triangle(fill_opacity=1, color=color)
        pointer.next_to(position, DOWN).scale(0.1)
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
        ).move_to(1.5 * DOWN)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Binary Search", gradient=[GREEN, BLUE]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        binary_search_code = """
int binarySearch(vector<int>& nums, int target) {
    int left = 0, right = nums.size() - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] == target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
        """
        code_display = self.display_code(binary_search_code)

        # Array setup
        nums = list(range(1, 21))  # Array of sorted numbers from 1 to 20
        array = VGroup(*[Square().scale(0.3) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(1.5 * UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.2).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]

        self.play(Create(array), Create(num_tex))

        # Initialize pointers for left, right, and mid
        left, right = 0, len(nums) - 1
        target = 9  # Target value to search for
        found = False

        # Display target value
        target_text = Tex("Target = ", str(target), color=YELLOW).move_to(5 * LEFT + 2.5 * UP)
        self.play(Write(target_text))

        # Initialize pointers outside the loop
        left_pointer = self.create_pointer(num_tex[left].get_center(), "left", color=RED)
        right_pointer = self.create_pointer(num_tex[right].get_center(), "right", color=GREEN)
        self.play(Create(left_pointer), Create(right_pointer))

        # Binary Search Animation
        while left <= right and not found:
            # Update positions of left and right pointers
            self.play(left_pointer.animate.move_to(num_tex[left].get_center() + 0.5 * DOWN))
            self.play(right_pointer.animate.move_to(num_tex[right].get_center() + 0.5 * DOWN))

            # Create midpoint pointer
            mid = left + (right - left) // 2
            mid_pointer = self.create_pointer(num_tex[mid].get_center(), "mid", color=YELLOW)
            self.play(Create(mid_pointer))

            # Highlight current midpoint
            self.play(num_tex[mid].animate.set_color(YELLOW))
            self.wait(0.5)

            # Check if mid is the target
            if nums[mid] == target:
                found = True
                # Indicate the target is found
                self.play(num_tex[mid].animate.set_color(PURPLE))
                result_text = Tex(f"Found {target} at index {mid}!").move_to(3 * DOWN)
                self.play(Write(result_text))
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

            # Reset midpoint color and remove mid pointer
            self.play(num_tex[mid].animate.set_color(WHITE))
            self.play(FadeOut(mid_pointer))

        # If target not found
        if not found:
            result_text = Tex(f"{target} not found in the array.").move_to(3 * DOWN)
            self.play(Write(result_text))

        # Final cleanup
        self.play(FadeOut(left_pointer), FadeOut(right_pointer), FadeOut(code_display), FadeOut(target_text))
        self.wait(1)
