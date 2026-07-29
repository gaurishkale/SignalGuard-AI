import tkinter as tk

from gui.app import SignalGuardApp


def main():

    root = tk.Tk()

    SignalGuardApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()
