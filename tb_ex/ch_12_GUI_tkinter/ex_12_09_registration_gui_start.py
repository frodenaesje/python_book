# file: ex_12_09_registration_gui_start.py
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Registration")

    # TODO: add three labels (Name, Email, Age) and three
    #   Entry widgets, each bound to a StringVar. Lay them
    #   out with grid().

    # TODO: add a Listbox that will show registered people.

    # TODO: write register() - read the three StringVars,
    #   skip if any is empty, insert a line into the Listbox
    #   (e.g. "Alice (32) - alice@x.no"), then clear the
    #   fields. Wire it to a Button with command=register.

    root.mainloop()


if __name__ == "__main__":
    main()
