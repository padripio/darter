import tkinter

welcome = tkinter.Tk()
welcome.config(background="#5e6b64")
welcome.title("Darter")

canvas = tkinter.Canvas(width=300, height=50)
canvas.config(background="#5e6b64", highlightthickness=0)

game_type_label = tkinter.Label(background="#5e6b64", text="Game type")

button_501 = tkinter.Button(text="501 Game", background="#f2dcc9")
button_301 = tkinter.Button(text="301 Game")

name1_label = tkinter.Label(background="#5e6b64", text="Player 1 name ")
name2_label = tkinter.Label(background="#5e6b64", text="Player 2 name ")
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

game_type_label.grid(row=1, column=0, padx=10, pady=10)

button_501.grid(row=2, column=0, padx=5, pady=5)
button_301.grid(row=3, column=0, padx=5, pady=5)

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
