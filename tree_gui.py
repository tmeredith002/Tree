import tkinter as tk
import tkinter.messagebox
import math

MAX = 50

class PrintGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Print Tree')
        self.count = 0
        self.create_frames()
        self.create_intvars()
        self.create_radio_buttons()
        self.create_labels()
        self.create_entry()
        self.create_buttons()
        self.pack_widgets()
        self.pack_frames()

    def create_frames(self):
        self.top_frame = tk.Frame(self.main_window)
        self.middle_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.leaf_frame = tk.Frame(self.top_frame)
        self.trunk_frame = tk.Frame(self.top_frame)
        self.orn_frame = tk.Frame(self.top_frame)
        self.star_frame = tk.Frame(self.top_frame)

    def create_intvars(self):
        self.leaf_var = tk.IntVar()
        self.trunk_var = tk.IntVar()
        self.orn_var = tk.IntVar()
        self.star_var = tk.IntVar()
        self.leaf_var.set(1)
        self.trunk_var.set(1)
        self.orn_var.set(1)
        self.star_var.set(1)

    def create_radio_buttons(self):
        self.leaf_rb1 = tk.Radiobutton(self.leaf_frame, text='*', variable=self.leaf_var, value=1)
        self.leaf_rb2 = tk.Radiobutton(self.leaf_frame, text='^', variable=self.leaf_var, value=2)
        self.trunk_rb1 = tk.Radiobutton(self.trunk_frame, text='| |', variable=self.trunk_var, value=1)
        self.trunk_rb2 = tk.Radiobutton(self.trunk_frame, text='[ ]', variable=self.trunk_var, value=2)
        self.orn_rb1 = tk.Radiobutton(self.orn_frame, text='@', variable=self.orn_var, value=1)
        self.orn_rb2 = tk.Radiobutton(self.orn_frame, text='%', variable=self.orn_var, value=2)
        self.star_rb1 = tk.Radiobutton(self.star_frame, text='$', variable=self.star_var, value=1)
        self.star_rb2 = tk.Radiobutton(self.star_frame, text='&', variable=self.star_var, value=2)

    def create_labels(self):
        self.leaf_label = tk.Label(self.leaf_frame, text='Leaves')
        self.trunk_label = tk.Label(self.trunk_frame, text='Trunk')
        self.orn_label = tk.Label(self.orn_frame, text='Ornaments')
        self.star_label = tk.Label(self.star_frame, text='Star')

    def create_entry(self):
        self.height_label = tk.Label(self.middle_frame, text='Enter height: ')
        self.height_entry = tk.Entry(self.middle_frame, width=10)
        self.max_label = tk.Label(self.middle_frame, text='Max: ')
        self.max_value = tk.Label(self.middle_frame, text=str(MAX))

    def create_buttons(self):
        self.print_button = tk.Button(self.bottom_frame, text='Print', command=self.new_tree)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

    def pack_widgets(self):
        self.leaf_label.pack(side='top')
        self.leaf_rb1.pack(side='top')
        self.leaf_rb2.pack(side='top')
        self.trunk_label.pack(side='top')
        self.trunk_rb1.pack(side='top')
        self.trunk_rb2.pack(side='top')
        self.orn_label.pack(side='top')
        self.orn_rb1.pack(side='top')
        self.orn_rb2.pack(side='top')
        self.star_label.pack(side='top')
        self.star_rb1.pack(side='top')
        self.star_rb2.pack(side='top')
        self.height_label.pack(side='left')
        self.height_entry.pack(side='left')
        self.max_label.pack(side='left')
        self.max_value.pack(side='left')
        self.print_button.pack(side='left')
        self.quit_button.pack(side='left')

    def pack_frames(self):
        self.leaf_frame.pack(side='left')
        self.trunk_frame.pack(side='left')
        self.orn_frame.pack(side='left')
        self.star_frame.pack(side='left')
        self.top_frame.pack(side='top')
        self.middle_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

    # Open New Tree Window
    def new_tree(self):
        self.leaf = '*' if self.leaf_var.get() == 1 else '^'
        self.trunk = '| |' if self.trunk_var.get() == 1 else '[ ]'
        self.orn = '@' if self.orn_var.get() == 1 else '%'
        self.star = '$' if self.star_var.get() == 1 else '&'
        try:
            self.height = int(self.height_entry.get())
            if self.height > MAX: self.height = MAX
            if self.height <= 0:
                tk.messagebox.showerror("Input Error", "Please enter a positive integer for height.")
                return
        except ValueError:
            tk.messagebox.showerror("Input Error", "Please enter a valid integer for height.")
            return
        self.count += 1
        self.tree = TreeGUI(self.height, self.leaf, self.trunk, self.orn, self.star, self.count)

class TreeGUI:
    def __init__(self, height, leaf, trunk, orn, star, count):
        self.height = height
        self.leaf = leaf
        self.trunk = trunk
        self.orn = orn
        self.star = star
        self.count = count
        self.tree_window = tk.Toplevel()
        self.tree_window.title(f'Tree # {self.count}')
        self.tree_frame = tk.Frame(self.tree_window)
        self.tree_frame.pack()
        self.build_tree()

    def build_tree(self):
        # Print the star at the top
        self.add_label(' ' * (self.height - 1) + self.star + ' ' * (self.height - 1))
        # Print the top leaf
        self.add_label(' ' * (self.height - 1) + self.leaf + ' ' * (self.height - 1))
        # Print the middle part of the tree
        self.print_tree(2)
        # Print the trunk
        for _ in range(math.ceil(self.height / 10)):
            self.add_label(' ' * (self.height - 2) + self.trunk + ' ' * (self.height - 2))

    def print_tree(self, step):
        if step > self.height:
            return
        if step % 2 == 0: # Alternate ornaments on each side
            self.add_label((' ' * (self.height - step - 1)) + self.orn + \
                            self.leaf + (self.leaf * ((step - 1) * 2)) + \
                            ' ' * (self.height - step)) # Padding, Orn, Leaves, Padding
        else:
            self.add_label(' ' * (self.height - step + 1) + \
                            (self.leaf * ((step - 1) * 2)) + self.leaf + \
                            self.orn + (' ' * (self.height - step))) # Padding, Leaves, Orn, Padding
        self.print_tree(step + 1)

    def add_label(self, text):
        label = tk.Label(self.tree_frame, text=text, font=("Courier", 12))
        label.pack()

def main():
    print_gui = PrintGUI()
    tk.mainloop()

if __name__ == '__main__':
    main()