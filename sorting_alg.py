class SelectionSort(Scene):
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
            language="Python",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).to_edge(DOWN)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Selection Sorting Algorithm", gradient=[BLUE, PURPLE]).move_to(2.6 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        selection_sort_code = """
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        """
        code_display = self.display_code(selection_sort_code)

        # Array setup
        nums = [4,1,3,2,0,5,7,8,9,6]
        array = VGroup(*[Square().scale(0.4) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        
        self.play(Create(array), Create(num_tex))
        
        n = len(nums)
        # Selection Sort Animation
        for i in range(n - 1):
            min_index = i
            # Highlight the starting point of the current position
            self.play(num_tex[i].animate.set_color(GREEN))
            
            # i Pointer
            i_pointer = self.create_pointer(num_tex[i].get_center(), "i")
            self.play(Create(i_pointer))

            for j in range(i + 1, n):
                # j Pointer
                j_pointer = self.create_pointer(num_tex[j].get_center(), "j")
                self.play(Create(j_pointer))

                # Highlight the element being compared
                self.play(num_tex[j].animate.set_color(YELLOW), run_time=0.3)
                
                if nums[j] < nums[min_index]:
                    # Deselect the old minimum and set the new minimum
                    self.play(num_tex[min_index].animate.set_color(WHITE), run_time=0.3)
                    min_index = j
                    self.play(num_tex[min_index].animate.set_color(RED), run_time=0.3)  # Mark as new min

                # Reset color if not the minimum
                else:
                    self.play(num_tex[j].animate.set_color(WHITE), run_time=0.3)
                
                # Remove the j pointer
                self.play(FadeOut(j_pointer))
            
            # Swap if a new minimum was found
            if min_index != i:
                self.play(Swap(num_tex[i], num_tex[min_index]))
                # Swap values in nums list
                nums[i], nums[min_index] = nums[min_index], nums[i]
                # Swap the positions in num_tex as well
                num_tex[i], num_tex[min_index] = num_tex[min_index], num_tex[i]
            
            # Finalize the sorted element
            self.play(num_tex[i].animate.set_color(GREEN), run_time=0.5)
            # Remove the i pointer
            self.play(FadeOut(i_pointer))
        
        # Final wait before ending the scene
        self.play(FadeOut(code_display))
        self.wait(1)

class BubbleSort(Scene):
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
            language="Python",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).to_edge(DOWN)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Bubble Sorting Algorithm", gradient=[BLUE, PURPLE]).move_to(2.6 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        bubble_sort_code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        """
        code_display = self.display_code(bubble_sort_code)

        # Array setup
        nums = [4, 1, 3, 2, 0, 5, 7, 8, 9, 6]
        array = VGroup(*[Square().scale(0.4) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        
        self.play(Create(array), Create(num_tex))
        
        n = len(nums)
        # Bubble Sort Animation
        for i in range(n - 1):
            # i Pointer
            i_pointer = self.create_pointer(num_tex[n - i - 1].get_center(), "i")
            self.play(Create(i_pointer))

            for j in range(n - i - 1):
                # j Pointer
                j_pointer = self.create_pointer(num_tex[j].get_center(), "j")
                self.play(Create(j_pointer))
                
                # Compare and swap if needed
                self.play(num_tex[j].animate.set_color(YELLOW), num_tex[j + 1].animate.set_color(YELLOW))
                
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    self.play(Swap(num_tex[j], num_tex[j + 1]))
                    num_tex[j], num_tex[j + 1] = num_tex[j + 1], num_tex[j]
                
                # Reset colors and remove the j pointer
                self.play(num_tex[j].animate.set_color(WHITE), num_tex[j + 1].animate.set_color(WHITE))
                self.play(FadeOut(j_pointer))
            
            # Finalize the sorted element and remove the i pointer
            self.play(num_tex[n - i - 1].animate.set_color(GREEN))
            self.play(FadeOut(i_pointer))
        
        # Final wait before ending the scene
        self.play(FadeOut(code_display))
        self.wait(1)

class InsertionSort(Scene):
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
            language="Python",
            font_size=18,
            insert_line_no=False,
            line_spacing=0.6
        ).to_edge(DOWN)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Insertion Sorting Algorithm", gradient=[BLUE, PURPLE]).move_to(2.6 * UP).scale(1.2)
        self.add(title)

        # Code snippet at the bottom
        insertion_sort_code = """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        """
        code_display = self.display_code(insertion_sort_code)

        # Array setup
        nums = [4, 1, 3, 2, 0, 5, 7, 8, 9, 6]
        array = VGroup(*[Square().scale(0.4) for _ in range(len(nums))]).arrange(RIGHT, buff=0.1).move_to(UP)
        num_tex = VGroup(*[MathTex(str(num)) for num in nums]).scale(1.5).arrange(RIGHT).scale(0.8)
        [num_tex[i].move_to(array[i].get_center()) for i in range(len(nums))]
        
        self.play(Create(array), Create(num_tex))

        n = len(nums)
        # Insertion Sort Animation
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            # Highlight the current key position
            self.play(num_tex[i].animate.set_color(YELLOW))
            
            # i Pointer
            i_pointer = self.create_pointer(num_tex[i].get_center(), "i")
            self.play(Create(i_pointer))
            
            while j >= 0 and nums[j] > key:
                # j Pointer
                j_pointer = self.create_pointer(num_tex[j].get_center(), "j")
                self.play(Create(j_pointer))
                
                # Shift element to the right
                nums[j + 1] = nums[j]
                self.play(num_tex[j].animate.set_color(YELLOW))
                num_tex[j + 1].become(MathTex(str(nums[j])).move_to(num_tex[j + 1].get_center()))

                self.play(FadeOut(j_pointer))
                j -= 1
            
            # Insert key into the correct position
            nums[j + 1] = key
            num_tex[j + 1].become(MathTex(str(key)).move_to(num_tex[j + 1].get_center()))
            self.play(num_tex[j + 1].animate.set_color(GREEN))
            
            # Remove i pointer
            self.play(FadeOut(i_pointer))
        
        # Final wait before ending the scene
        self.play(FadeOut(code_display))
        self.wait(1)


