import tkinter as tk
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.array_label = tk.Label(root, text="Enter numbers separated by space:")
        self.array_label.pack()

        self.array_entry = tk.Entry(root)
        self.array_entry.pack()

        self.sort_button = tk.Button(root, text="Sort", command=self.start_sorting)
        self.sort_button.pack()

        self.algorithm_var = tk.StringVar(root)
        self.algorithm_var.set("Bubble Sort")
        self.algorithm_menu = tk.OptionMenu(root, self.algorithm_var, "Bubble Sort", "Selection Sort", "Insertion Sort")
        self.algorithm_menu.pack()

        self.canvas_width = 800
        self.canvas_height = 400
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.sorting_history = []

    def draw_array(self, array):
        self.canvas.delete("all")
        bar_width = self.canvas_width / len(array)
        max_value = max(array)

        for i, value in enumerate(array):
            bar_height = (value / max_value) * self.canvas_height
            self.canvas.create_rectangle(
                i * bar_width,
                self.canvas_height,
                (i + 1) * bar_width,
                self.canvas_height - bar_height,
                fill="blue",
            )
            self.canvas.create_text(
                (i + 0.5) * bar_width,
                self.canvas_height - bar_height - 10,
                text=str(value),
                fill="black",  # Change the text color to black
                font=("Helvetica", 10),
            )

        self.root.update()
        time.sleep(1)

    def bubble_sort(self, array):
        n = len(array)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    self.sorting_history.append(array.copy())

    def selection_sort(self, array):
        n = len(array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            self.sorting_history.append(array.copy())

    def insertion_sort(self, array):
        n = len(array)
        for i in range(1, n):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
            self.sorting_history.append(array.copy())

    def start_sorting(self):
        input_array = self.array_entry.get().split()
        try:
            array = [int(x) for x in input_array]
        except ValueError:
            self.array_label.config(text="Invalid input. Please enter numbers separated by space.")
            return

        self.array_label.config(text="Enter numbers separated by space:")

        selected_algorithm = self.algorithm_var.get()

        if selected_algorithm == "Bubble Sort":
            self.bubble_sort(array.copy())
        elif selected_algorithm == "Selection Sort":
            self.selection_sort(array.copy())
        elif selected_algorithm == "Insertion Sort":
            self.insertion_sort(array.copy())

        for step in self.sorting_history:
            self.draw_array(step)

def main():
    root = tk.Tk()
    visualizer = SortingVisualizer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
