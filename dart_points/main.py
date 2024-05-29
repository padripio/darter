# dart points calculator
import datetime
import tkinter
from tkinter import messagebox
BACKGROUND_COLOR="#5e6b64"
import time

# clearing previous logs
# get time
time_now = datetime.datetime.now()
hour = time_now.hour
minute = time_now.minute
game_mode = 501

with open(file="game_logs.txt", mode="w") as file:
    file.write(f"{hour} : {minute}\n")

with open(file="player_names.txt", mode="r") as file:
    names = file.readline()

    name1 = names.split(sep=",")[0]
    name2 = names.split(sep=",")[1]


# adding a welcome screen
def main(round, game_mode, default_points, index):
    global round_count
    round_count = round
    global points1
    global points2
    points1 = default_points[index]
    points2 = default_points[index]

    def alt_game_mode(game_mode):
        for x in default_points:
            if x != game_mode:
                return x

    BG_COLOR = "#EEEEEE"
    FLASH_COLOR = "#F3CA52"
    round_count = 0

    window = tkinter.Tk()
    window.title("Dart points")
    window.minsize(width=300, height=300)
    window.config(bg=BACKGROUND_COLOR,)

    player1_name = name1
    player2_name = name2

    # set up the canvas
    title_text = tkinter.Label(bg=BACKGROUND_COLOR,text="Dart points", )
    game_mode_label = tkinter.Label(bg=BACKGROUND_COLOR,text=f"Game : {game_mode}", )
    player1_label = tkinter.Label(bg=BACKGROUND_COLOR,text=player1_name, )
    player2_label = tkinter.Label(bg=BACKGROUND_COLOR,text=player2_name, )

    # TODO fetch the game mode from welcome and bind here

    player1_points = tkinter.Label(bg=BACKGROUND_COLOR,text=points1,)
    player2_points = tkinter.Label(bg=BACKGROUND_COLOR,text=points2, )
    entry_text = tkinter.Label(bg=BACKGROUND_COLOR,text="enter points here")

    player1_entry = tkinter.Entry()
    player2_entry = tkinter.Entry()
    enter_button_1 = tkinter.Button(text="Submit")
    enter_button_2 = tkinter.Button(text="enter")
    new_game = tkinter.Button(text="Start new game", bg=BG_COLOR)
    change_game = tkinter.Button(text=f"Change game to {alt_game_mode(game_mode)}", bg=BG_COLOR)

    # packing the elements
    title_text.grid(row=0, column=1)
    game_mode_label.grid(row=0, column=2)

    space_text = tkinter.Label(text=" ", bg=BACKGROUND_COLOR,)
    space_text.grid(row=1, column=0)

    player1_label.grid(row=2, column=0)
    player2_label.grid(row=2, column=2)

    space_text = tkinter.Label(text=" ",bg=BACKGROUND_COLOR,)
    space_text.grid(row=3, column=0)

    player1_points.grid(row=4, column=0)
    player2_points.grid(row=4, column=2)

    space_text = tkinter.Label(text=" ",bg=BACKGROUND_COLOR,)
    space_text.grid(row=5, column=0)

    entry_text.grid(row=6, column=1, columnspan=1)

    space_text = tkinter.Label(bg=BACKGROUND_COLOR,text=" ", )
    space_text.grid(row=7, column=0)

    player1_entry.grid(row=8, column=0)
    player2_entry.grid(row=8, column=2)

    space_text = tkinter.Label(bg=BACKGROUND_COLOR,text=" ", )
    space_text.grid(row=9, column=0)

    enter_button_1.grid(row=10, column=1)
    # enter_button_2.grid(row=10,column=2)

    space_text = tkinter.Label(bg=BACKGROUND_COLOR,text=" ", )
    space_text.grid(row=11, column=0)

    new_game.grid(row=12, column=1, columnspan=1)

    space_text = tkinter.Label(text=" ", bg=BACKGROUND_COLOR,)
    space_text.grid(row=13, column=1)

    change_game.grid(row=14, column=1, columnspan=1)
    player1_entry.focus()

    def points_minus(points, current_points):
        current_points -= points
        return current_points

    def show_winner(winner):
        messagebox.showinfo(title="Hongera", message=f"{winner} wins !")

    def shift_focus(event):
        # move the focus to th p2 bar
        # check if p2 is empty
        # fetch the p2 entry
        p2_entry = player2_entry.get()
        if len(p2_entry) < 1:
            player2_entry.focus()
        else:
            fetcher()

    window.bind("<Return>", shift_focus)

    def fetcher():
        p1 = player1_entry.get()
        p2 = player2_entry.get()
        if len(p1) < 1 or len(p2) < 1:
            messagebox.showerror(title="empty fields", message="Please fill in all the fields")
        else:
            deductor(p1, p2)

    # todo fetch the game mode from welcome and bind here

    def deductor(p1, p2):
        global points1, points2

        # enter_button_1.config(bg=FLASH_COLOR)
        # time.sleep(1)
        # enter_button_2.config(bg=BG_COLOR)
        # empty_fields=0
        # p1 = player1_entry.get()
        # p2 = player2_entry.get()
        # if len(p1) or len(p2)<1:
        #    messagebox.showerror(title="empty fields" ,message="Please fill in all the fields")
        #

        try:
            p1 = int(p1)
            p2 = int(p2)

            # for player1

            new_point = points1
            new_point -= p1
            if new_point < 0:
                print("Miss")
            elif new_point == 0:
                show_winner(player1_name)

                points1 = new_point
            else:
                points1 = new_point

            # TODO for player2

            new_point = points2
            new_point -= p2
            if new_point < 0:
                print("Miss")
            elif new_point == 0:
                show_winner(player2_name)
                points2 = new_point
            else:
                points2 = new_point

            player1_points.config(text=points1)
            player2_points.config(text=points2)

            # clearing the fields
            player1_entry.delete(0, tkinter.END)
            player2_entry.delete(0, tkinter.END)

            global round_count
            round_count += 1
            print(f" Round count : {round_count}")
            player1_entry.focus()
            # TODO game logs
            with open(file="game_logs.txt", mode="a") as file:
                file.write(f"\nRound : {round_count} \n{player1_name}->{p1} , {player2_name}->{p2}\n")

        except ValueError:
            messagebox.showerror(title="Invalid input", message="Please enter only numbers")

    def start_new_game():
        global points2
        global points1
        popup = messagebox.askokcancel("Confirm", message="You are about to start a new game ")
        if popup:
            player1_entry.delete(0, tkinter.END)
            player2_entry.delete(0, tkinter.END)
            points2 = points1 = game_mode
            player2_points.config(text=points2)
            player1_points.config(text=points1)

    def change_game_mode():
        global round_count
        round_count = 0
        global game_mode
        popup = messagebox.askokcancel("Confirm",
                                       message=f"Change game mode to {alt_game_mode(game_mode)}? \n this will reset "
                                               f"all progress")
        if popup:
            # clear logs
            with open(file="game_logs.txt", mode="w") as file:
                file.write(f"{hour} : {minute}\n")

            global points2
            global points1
            for x in default_points:
                if x != game_mode:
                    game_mode = x
                    game_mode_label.config(text=game_mode)
                    player1_entry.delete(0, tkinter.END)
                    player2_entry.delete(0, tkinter.END)
                    points2 = points1 = game_mode
                    player2_points.config(text=points2)
                    player1_points.config(text=points1)
                    change_game.config(text=f"Change game to {alt_game_mode(game_mode)}")
                    return game_mode

    new_game.config(command=start_new_game)

    enter_button_1.config(command=fetcher)

    change_game.config(command=change_game_mode)

    window.mainloop()


if __name__ == "__main__":
    main(0, 501, [501,301], 0)
