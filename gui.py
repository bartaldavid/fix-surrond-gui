import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showerror, showinfo
import ffmpeg
from pathlib import Path

root = tk.Tk()
root.title("AAC to AC3 converter")
root.geometry("500x200")

main_frame = ttk.Frame(root)
main_frame.pack(expand=True, padx=10, pady=10)

style = ttk.Style()
style.configure(".", font=("Helvetica", 12))

label = ttk.Label(main_frame, text="")
label.pack(padx=5, pady=5)


def select_file():
    filetypes = (
        ("Video Files", ".mp4 *.mkv"),
        ("all files", "*")
    )
    global fn
    fn = fd.askopenfilename(
        title="Select a file you want to convert", filetypes=filetypes, initialdir="/")
    global filepath
    if fn != "":
        filepath = Path(fn)
        label.config(text=f"Opened file: {filepath.name}")
        convertBtn.state(["!disabled"])
    else:
        label.config(text="Please open a valid file below")


def convert_file():
    if filepath.is_file():
        (
            ffmpeg
            .input(fn)
            .output(str(filepath.parent) + " - converted.mkv", acodec="ac3", vcodec="copy", scodec="copy")
            .run()
        )
        showinfo(title="Success!",
                 message=f"{filepath.name} converted successfully")
    else:
        showerror(title="Error", message="Selected file is not valid")


openfileBtn = ttk.Button(main_frame, text="Open file",
                         command=select_file)

convertBtn = ttk.Button(main_frame, text="Convert",
                        command=convert_file)


openfileBtn.pack()
convertBtn.pack()
convertBtn.state(["disabled"])

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
