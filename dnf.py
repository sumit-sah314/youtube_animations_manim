class DNFAlgorithm(Scene):
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
        ).move_to(3.5 * RIGHT + 0.5 * DOWN).scale(0.7)
        self.play(Create(code))
        return code

    def construct(self):
        # Title Text
        title = Text("Dutch National Flag Algorithm", gradient=[BLUE, PURPLE]).move_to(3 * UP)
        self.add(title)

        # Code snippet for DNF algorithm
        dnf_code = """
        void sortColors(vector<int>& nums) {
            
            int low = 0, mid = 0, high = nums.size()-1;
            while(mid <= high) {
                if(nums[mid] == 0) {
                    swap(nums[mid], nums[low]);
                    mid++; low++;
                } else if(nums[mid] == 1) {
                    mid++;
                } else {
                    swap(nums[mid], nums[high]);
                    high--;
                }
            }
        }
        """
        
        code_display = self.display_code(dnf_code)

        # Example array to sort (0s, 1s, and 2s) - Increased size
        nums = [0, 1, 2, 0, 1, 2, 1, 0, 2, 1, 0, 2, 0, 1, 1]
        
        # Create rectangles for each number and labels
        bars = VGroup(*[
            Rectangle(width=0.5, height=1, color=self.get_color(num), fill_opacity=1).scale(0.5)
            for num in nums
        ]).arrange(RIGHT, buff=0.2).move_to(3 * LEFT)

        labels = VGroup(*[
            Text(str(num), font_size=22).move_to(bars[i].get_top() + UP * 0.2)
            for i, num in enumerate(nums)
        ])

        # Create initial pointers
        low = 0
        mid = 0
        high = len(nums) - 1

        # Add bars and labels to the scene
        self.play(Create(bars), Create(labels))

        # Create pointers
        low_pointer = self.create_pointer(bars[low].get_bottom(), "low", color=YELLOW)
        mid_pointer = self.create_pointer(bars[mid].get_bottom(), "mid", color=GREEN)
        high_pointer = self.create_pointer(bars[high].get_bottom(), "high", color=RED)
        self.play(Create(low_pointer), Create(mid_pointer), Create(high_pointer)) 

        # DNF algorithm animation
        while mid <= high:
            # Highlight current state
            self.play(low_pointer.animate.next_to(bars[low].get_bottom(), DOWN),
                      mid_pointer.animate.next_to(bars[mid].get_bottom(), DOWN),
                      high_pointer.animate.next_to(bars[high].get_bottom(), DOWN))

            if nums[mid] == 0:
                # Swap low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                self.update_bars(bars, labels, nums)
                low += 1 
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                # Swap mid and high
                nums[mid], nums[high] = nums[high], nums[mid]
                self.update_bars(bars, labels, nums)
                high -= 1

            # Wait for clarity
            self.wait(1)

        # End scene
        self.wait(2)

    def get_color(self, num):
        """Returns color based on the number."""
        if num == 0:
            return RED
        elif num == 1:
            return WHITE
        else:  # num == 2
            return BLUE

    def update_bars(self, bars, labels, nums):
        """Updates the bars based on the new values in nums."""
        for i, (bar, num) in enumerate(zip(bars, nums)):
            bar.set_color(self.get_color(num))
            labels[i].become(Text(str(num), font_size=22).move_to(bar.get_top() + UP * 0.2))
