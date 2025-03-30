import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
from tkinter import messagebox, Toplevel, Button, Entry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)

        # Create a label to display the message
        label = tk.Label(self, text=message, font=('Arial', 20, 'bold'), fg='black')
        label.pack(padx=10, pady=10)

        # Create a button to close the dialog
        button = tk.Button(self, text="OK", font=('Arial', 16, 'bold'), relief='raised', borderwidth=3, fg='white', bg='black', cursor='hand2', command=self.destroy)
        button.pack(pady=10)


def show_custom_dialog(parent, title, message):
    dialog = CustomDialog(parent, title, message)
    parent.wait_window(dialog)


instructions = ('Use this app to decipher encoded text.\n'
                'Decoding will be done based on relative frequencies.\n'
                'You will have to enter two messages: \n'
                '- The first message inputted will be in plain English text.\n'
                '- The second message inputted will be the enciphered text.\n'
                'You will be shown the graphs of the relative frequencies along with the mapping of the letters.\n'
                'The decoded message can be seen with the help of the Decoded message button.\n'
                'You can use the Exit button on the home page and the output section page to exit the app.\n')


class AnimatedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WISE Project, Team 1")
        self.mapping = {}

        # Load the animated GIF
        self.gif_path = "1_AGct0ZJuD8ZHV1jMnvJlIw.gif"
        self.gif = Image.open(self.gif_path)
        self.frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(self.gif)]
        self.frame_index = 0
        self.animation_running = False

        # Create a canvas for the animated background
        self.canvas = tk.Canvas(root, width=1920, height=1000)
        self.canvas.pack(fill="both", expand=True)

        # Display the first frame of the GIF
        self.gif_label = tk.Label(root)
        self.gif_label.place(relx=0.5, rely=0.5, anchor="center")

        # Title block
        self.title_label = tk.Label(root, text="The Code Breaker", font=("Georgia", 24, 'bold'), borderwidth=10, relief='raised', fg='white', bg='black')
        self.title_label.config(bg=self.title_label.cget("bg"))  # Set background to current color
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Start button
        self.start_button = tk.Button(root, text="Start", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='white', bg='black', command=self.input_section, cursor='hand2')
        self.start_button.place(relx=0.3, rely=0.5, anchor="center")

        # Help button
        self.help_button = tk.Button(root, text="Help", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='white', bg='black', command=self.show_help, cursor='hand2')
        self.help_button.place(relx=0.5, rely=0.5, anchor="center")

        # Info button
        self.info_button = tk.Button(root, text="Info", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='white', bg='black', command=self.show_info, cursor='hand2')
        self.info_button.place(relx=0.7, rely=0.5, anchor="center")

        # Exit button
        self.exit_button_output = tk.Button(self.root, text="Exit", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='white', bg='black', command=self.exit_app, cursor='hand2')
        self.exit_button_output.place(relx=0.5, rely=0.9, anchor="center")

        # Start the animation automatically when the window loads
        self.start_animation()

    def start_animation(self):
        self.animation_running = True
        # Schedule the first call to animate_gif
        self.animate_gif_callback()

    def exit_app(self):
        # Destroy all windows and exit the main loop
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    # Function which returns the relative frequencies of each letter in the string given
    def rel_freq(self, ls: list) -> dict:
        freq1 = {}
        for i in ls:
            if i.isalpha() and i != ' ':
                if i in freq1:
                    freq1[i] += 1
                else:
                    freq1[i] = 1
        for key in freq1:
            freq1[key] = freq1[key] / len(ls)
        return freq1

    def animate_gif_callback(self):
        if self.animation_running:
            frame = self.frames[self.frame_index]
            self.gif_label.config(image=frame)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            # Schedule the next call to animate_gif
            self.root.after(100, self.animate_gif_callback)

    def stop_animation(self):
        self.animation_running = False

    def input_section(self):
        self.withdraw_window()
        self.new_window = Toplevel(self.root)
        self.new_window.title("The input section")
        self.new_window.geometry("1920x1000")

        # Load background image
        self.bg_image = Image.open("DataBreach.png")
        self.bg_image = self.bg_image.resize((1920, 1000))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Create a canvas to place the background image
        canvas = tk.Canvas(self.new_window, width=1920, height=1000)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create and place labels and entry widgets in the middle of the window
        self.info1 = tk.Label(self.new_window, text="Enter the message in plain English text.", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='red', bg='white')
        self.info1.place(relx=0.5, rely=0.4, anchor="center")

        self.entry1 = tk.Entry(self.new_window, font=('Arial', 16))
        self.entry1.place(relx=0.5, rely=0.45, anchor="center")

        self.info2 = tk.Label(self.new_window, text="Enter the enciphered message.", font=("Arial", 20, 'bold'), borderwidth=5, relief='raised', fg='red', bg='white')
        self.info2.place(relx=0.5, rely=0.5, anchor="center")

        self.entry2 = tk.Entry(self.new_window, font=('Arial', 16))
        self.entry2.place(relx=0.5, rely=0.55, anchor="center")

        # Decipher button
        self.decipher_button = Button(self.new_window, text="Decipher", command=self.decipher, font=('calibri', 15, 'bold'), fg='white', bg='green', cursor='hand2')
        self.decipher_button.place(relx=0.5, rely=0.6, anchor="center")

        # Back button
        self.back_button = Button(self.new_window, text='Back', command=self.go_back, font=('calibri', 15, 'bold'), fg='white', bg='red', cursor='hand2')
        self.back_button.place(relx=0.5, rely=0.65, anchor='center')

    def go_back(self):
        self.new_window.destroy()
        self.root.deiconify()

    def output_section(self, data1, data2):
        self.new_window.withdraw()
        self.op_new_window = Toplevel(self.root)
        self.op_new_window.title("The output section")
        self.op_new_window.geometry("1920x1000")

        # Load background image
        self.op_bg_image = Image.open("op_bg.png")
        self.op_bg_image = self.op_bg_image.resize((1920, 1000))
        self.op_bg_photo = ImageTk.PhotoImage(self.op_bg_image)

        # Create a canvas to place the background image
        canvas = tk.Canvas(self.op_new_window, width=1920, height=1000)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.op_bg_photo, anchor="nw")

        # Create and place labels and pie charts
        self.plot_pie_chart(data1, "Chart 1: Plain Text Letter Frequency", 0.3, 0.3)
        self.plot_pie_chart(data2, "Chart 2: Enciphered Text Letter Frequency", 0.7, 0.3)

        self.show_pet = tk.Button(self.op_new_window, text='Show plain text', command=self.show_plain_txt, font=('Arial', 13, 'bold'), relief='raised', fg='white', bg='black', borderwidth=3, cursor='hand2')
        self.show_pet.place(relx=0.3, rely=0.57, anchor='center')

        self.show_enc = tk.Button(self.op_new_window, text='Show encoded text', command=self.show_enc, font=('Arial', 13, 'bold'), relief='raised', borderwidth=3, fg='white', bg='black', cursor='hand2')
        self.show_enc.place(relx=0.7, rely=0.57, anchor='center')

        # Back to input button
        self.back_to_input_button = Button(self.op_new_window, text='Back to Input', command=self.go_back_to_input, font=('calibri', 15, 'bold'), fg='white', bg='red', cursor='hand2')
        self.back_to_input_button.place(relx=0.5, rely=0.9, anchor='center')

        # Mapping button
        self.mapping_text = '{' + ', '.join(f"{key}: {value}" for key, value in (self.mapping).items()) + '}'
        print(self.mapping_text)
        mapping_button = tk.Button(self.op_new_window, text='Mapping', font=('Arial', 13, 'bold'), relief='raised', borderwidth=3, fg='white', bg='black', command=self.show_mapping, cursor='hand2')
        mapping_button.place(relx=0.5, rely=0.55, anchor='center')

        # Create Decoded message button
        decoded_label = tk.Button(self.op_new_window, text="Decoded message", font=("Arial", 16, 'bold'), fg='white', bg='black', relief='raised', command=self.show_decoded, cursor='hand2', borderwidth=3)
        decoded_label.place(relx=0.5, rely=0.7, anchor='center')

        # Exit button
        exit_completely = tk.Button(self.op_new_window, text='Exit the app', font=('Arial', 14, 'bold'), fg='white', bg='purple', relief='raised', borderwidth=4, command=self.exit_app, cursor='hand2')
        exit_completely.place(relx=0.5, rely=0.8, anchor='center')

    def show_plain_txt(self):
        show_custom_dialog(self.op_new_window, 'Plain English text', self.text1)

    def show_decoded(self):
        show_custom_dialog(self.op_new_window, 'Decoded message', self.decoded)

    def show_enc(self):
        show_custom_dialog(self.op_new_window, 'Encoded text', self.text2)

    def show_mapping(self):
        show_custom_dialog(self.op_new_window, 'Mapping', self.mapping_text)

    def animate_gif(self):
        if self.animation_running:
            frame = self.frames[self.frame_index]
            self.gif_label.config(image=frame)
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.root.after(100, self.animate_gif)  # Change frame every 100 ms

    def withdraw_window(self):
        self.root.withdraw()

    def show_help(self):
        show_custom_dialog(root,"Help", instructions)

    def decipher(self):
        self.text1 = self.entry1.get().upper()
        self.text2 = self.entry2.get().upper()

        # The dictionaries in descending order based on relative frequencies
        data1 = dict(sorted(self.rel_freq(list(self.text1)).items(), key=lambda item: item[1], reverse=True))
        data2 = dict(sorted(self.rel_freq(list(self.text2)).items(), key=lambda item: item[1], reverse=True))

        # Populate mapping dictionary
        self.mapping = {}
        for key1, key2 in zip(data2.keys(), data1.keys()):
            self.mapping[key1] = key2

        self.output_section(data1, data2)

        # Construct decoded message
        self.decoded = ''.join(self.mapping.get(char, char) for char in self.text2)

    def show_info(self):
        messagebox.showinfo("Info", "This app was made by Team 1, ECE A. \n We are\n23WH1A0401 - Keerthana\n23WH1A0402 - Tejaswani\n23WH1A0403 - Kavya\n23WH1A0404 - Priyanka")

    def plot_pie_chart(self, data, title, relx, rely):
        labels = data.keys()
        sizes = data.values()
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Embed the pie chart in the Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=self.op_new_window)
        canvas.draw()
        canvas.get_tk_widget().place(relx=relx, rely=rely, anchor='center')

        # Create a label above the pie chart
        label = tk.Label(self.op_new_window, text=title, font=("Arial", 16, 'bold'), fg='black', bg='white')
        label.place(relx=relx, rely=rely - 0.25, anchor='center')  # Adjust rely parameter to create separation

    def go_back_to_input(self):
        self.op_new_window.destroy()
        self.new_window.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimatedApp(root)
    root.mainloop()