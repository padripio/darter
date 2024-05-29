import tkinter
from main import main_caller

FONT = ("Helvetica", "12",)
FONT_NAME = "Courier"
HIGHLIGHT_COLOR = "#f2dcc9"

welcome = tkinter.Tk()
welcome.config(background="#5e6b64")
welcome.title("Darter")

canvas = tkinter.Canvas(width=300, height=80)
canvas.config(background="#5e6b64", highlightthickness=0)

game_type_label = tkinter.Label(background="#5e6b64", text="Game type")

button_501 = tkinter.Button(text="501 Game", background=HIGHLIGHT_COLOR)
button_301 = tkinter.Button(text="301 Game")

game_mode = 0

# loading the icon
img = tkinter.PhotoImage(file="arrow.ppm")
# canvas.create_image(150, 10, image=img)
darter_heading = canvas.create_text(150,40,text="DARTER", font=(FONT_NAME, 40, "bold"))

# setting the default game state
with open(file="game_mode.txt",mode="w") as file:
    file.write(str(501))


# binding the start button
def activator():
    main_caller()


# creating a game mode file

def game_mode_501():
    # set the highlight
    button_301.config(background="white", activebackground="white")
    button_501.config(background=HIGHLIGHT_COLOR, fg="#000000", activebackground=HIGHLIGHT_COLOR,
                      activeforeground="#000000")
    global game_mode
    game_mode = 501
    with open(file="game_mode.txt", mode="w") as file:
        game_mode = str(game_mode)
        file.write(game_mode)

    return game_mode


def game_mode_301():
    button_301.config(background=HIGHLIGHT_COLOR, fg="#000000", activebackground=HIGHLIGHT_COLOR,
                      activeforeground="#000000")
    button_501.config(background="white", activebackground="white")
    global game_mode
    game_mode = 301
    with open(file="game_mode.txt", mode="w") as file:
        game_mode = str(game_mode)
        file.write(game_mode)
    return game_mode


button_301.config(command=game_mode_301)
button_501.config(command=game_mode_501)

name1_label = tkinter.Label(background="#5e6b64", text="Player 1 ", font=FONT)
name2_label = tkinter.Label(background="#5e6b64", text="Player 2 ", font=FONT)
name1_entry = tkinter.Entry()
name2_entry = tkinter.Entry()
name1_entry.focus()


# shifting the focus


# clean the name logs
def clean_logs():
    with open(file="player_names.txt", mode="w") as file:
        file.close()


clean_logs()


def write_names():
    name1_string = name1_entry.get()
    name2_string = name2_entry.get()
    names_string = name1_string + "," + name2_string
    print(names_string)
    with open(file="player_names.txt", mode="w") as file:
        file.write(names_string)
    # close the window
    welcome.destroy()
    activator()


def shift_focus(event):
    # check if name2 is already populated
    text = name2_entry.get()
    if len(text) < 1:
        pop = 0
    else:
        pop = 1
    if pop == 0:
        name2_entry.focus()
    else:
        # todo bind the start function here
        write_names()


welcome.bind("<Return>", shift_focus)

# or_label = tkinter.Label(text="Or ")

# default_name_button = tkinter.Button(text="Use default names")

start_button = tkinter.Button(text="Start", command=write_names)

# packing the elements
canvas.grid(row=0, column=0, columnspan=2)

# game_type_label.grid(row=1, column=0, padx=10, pady=10)

button_501.grid(row=2, column=0, padx=5, pady=10)
button_301.grid(row=3, column=0, padx=5, pady=10)

name1_label.grid(row=4, column=0, padx=20, pady=10)
name1_entry.grid(row=5, column=0, padx=20, pady=10)

name2_label.grid(row=4, column=1, padx=20, pady=10)
name2_entry.grid(row=5, column=1, padx=20, pady=10)

# prefill the entries
try:
    with open(file="player_names.txt", mode="r") as file:
        names = file.readline()

        name1 = names.split(sep=",")[0]
        name2 = names.split(sep=",")[1]

        name1_entry.insert(0, name1)
        name2_entry.insert(0, name2)

except:
    pass

# or_label.grid(row=6,column=1,padx=0,pady=10,sticky="w")
# default_name_button.grid(row=7,column=0,padx=10,pady=10)

start_button.grid(row=8, column=0, padx=20, pady=20)

welcome.mainloop()
