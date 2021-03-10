
import subprocess
from tkinter import *

window = Tk()
window.title("pip packages installer")
window.configure(bg="gray")

result_text = StringVar()
result_color = StringVar()

result_color.set("white")


def install_button_callback():
    subprocess.Popen(f"pip install {package.get()}", shell=True, stdout=subprocess.PIPE)


instructions = Label(
    text = "Enter package name here:",
    fg = "white",
    bg = "gray",
    font = "fira-sans, 12"
)

results = Label(
        text = result_text.get(),
        fg = result_color.get(),
        font = "fira-sans, 8",
        bg = "gray"
    )

package = StringVar()
package_entry = Entry(
    textvariable = package,
    fg = "black",
    bg = "white",
    selectbackground = "blue",
    selectforeground = "white",
    width = 30
)

install_button = Button(
    bg = "white",
    width = 5,
    bd = 1,
    text = "install",
    command = install_button_callback
)


def enter(event):
    install_button.invoke()


instructions.grid(row=0, column=0, pady=(20,0), padx=15)
package_entry.grid(row=1, column=0, pady=(5, 10), padx=20)
install_button.grid(row=2, column=0, pady=(0, 10), padx=(200, 0))
results.grid(row=2, column=0, pady=(0, 40))

package_entry.focus()
window.resizable(False, False)
window.mainloop()
