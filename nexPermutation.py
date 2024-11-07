from manim import *

class NextPermutation(Scene):
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
        ).move_to(1.9 * DOWN).scale(0.8)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Next Permutation Algorithm", gradient=[GREEN, YELLOW]).move_to(3 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        next_permutation_code = """
    int last = nums.size() - 1;
    int pivot = last - 1;
    while (pivot >= 0 && nums[pivot] >= nums[pivot + 1]) {
        pivot--;
    }
    if (pivot >= 0) {
        int successor = last;
        while (nums[successor] <= nums[pivot]) {
            successor--;
        }
        swap(nums[pivot], nums[successor]);
    }
    reverse(nums.begin() + pivot + 1, nums.end());
        """
        code_display = self.display_code(next_permutation_code)

        # Array setup with larger array for a longer animation
        nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]
        array = VGroup(*[Square().scale(0.5) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(UP*1.5)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        
        self.play(Create(array), Create(num_tex))

        # Step 1: Find pivot
        pivot = len(nums) - 2
        pivot_pointer = self.create_pointer(num_tex[pivot].get_center(), "pivot")
        self.play(Create(pivot_pointer))

        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            self.play(num_tex[pivot].animate.set_color(RED))
            self.wait(0.5)
            self.play(num_tex[pivot].animate.set_color(WHITE))

            # Move the pointer left one step
            pivot -= 1
            if pivot >= 0:
                self.play(pivot_pointer.animate.next_to(num_tex[pivot].get_center(), DOWN))
        
        # Check if we found a valid pivot
        if pivot >= 0:
            self.play(num_tex[pivot].animate.set_color(GREEN))

            # Step 2: Find successor
            successor = len(nums) - 1
            successor_pointer = self.create_pointer(num_tex[successor].get_center(), "successor")
            self.play(Create(successor_pointer))

            while nums[successor] <= nums[pivot]:
                self.play(num_tex[successor].animate.set_color(YELLOW))
                self.wait(0.5)
                self.play(num_tex[successor].animate.set_color(WHITE))

                # Move the pointer left one step
                successor -= 1
                self.play(successor_pointer.animate.next_to(num_tex[successor].get_center(), DOWN))

            # Swap pivot and successor
            self.play(num_tex[pivot].animate.set_color(YELLOW))
            self.play(num_tex[successor].animate.set_color(YELLOW))
            self.play(
                num_tex[pivot].animate.move_to(num_tex[successor].get_center()),
                num_tex[successor].animate.move_to(num_tex[pivot].get_center())
            )
            num_tex[pivot], num_tex[successor] = num_tex[successor], num_tex[pivot]
            self.play(num_tex[pivot].animate.set_color(WHITE), num_tex[successor].animate.set_color(WHITE))
            self.play(FadeOut(pivot_pointer), FadeOut(successor_pointer))

        # Step 3: Reverse the subarray from pivot+1 to the end
        start = pivot + 1
        end = len(nums) - 1
        self.play(num_tex[start:end+1].animate.set_color(BLUE))
        while start < end:
            self.play(
                num_tex[start].animate.move_to(num_tex[end].get_center()),
                num_tex[end].animate.move_to(num_tex[start].get_center())
            )
            num_tex[start], num_tex[end] = num_tex[end], num_tex[start]
            start += 1
            end -= 1
        self.play(num_tex[start-1:end+2].animate.set_color(WHITE))

        # Final wait before ending the scene
        self.play(FadeOut(code_display))
        self.wait(1)
