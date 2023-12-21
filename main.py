import tkinter as tk
from tkinter import ttk
import time

class TimerApp:
    all_timers = []

    def __init__(self, window, timer_name, starting_time):
        self.window = window
        self.window.title("De slimste klinker van Schilde")

        self.timer_name = timer_name
        self.starting_time = starting_time

        self.timer_name_label = ttk.Label(window, text=self.timer_name, font=("Helvetica", 18))
        self.timer_name_label.pack()

        self.time_var = tk.StringVar()
        self.time_var.set("{:02d}".format(starting_time))

        self.label = ttk.Label(window, textvariable=self.time_var, font=("Helvetica", 48))
        self.label.pack(pady=10)

        self.start_pause_button = ttk.Button(window, text="Start", command=self.toggle_timer)
        self.start_pause_button.pack(pady=10)

        self.add_time_buttons = ttk.Frame(window)
        self.add_time_buttons.pack(pady=10)

        add_10_button = ttk.Button(self.add_time_buttons, text="+10s", command=lambda: self.add_time(10))
        add_20_button = ttk.Button(self.add_time_buttons, text="+20s", command=lambda: self.add_time(20))
        add_30_button = ttk.Button(self.add_time_buttons, text="+30s", command=lambda: self.add_time(30))
        add_40_button = ttk.Button(self.add_time_buttons, text="+40s", command=lambda: self.add_time(40))
        add_50_button = ttk.Button(self.add_time_buttons, text="+50s", command=lambda: self.add_time(50))

        add_10_button.grid(row=0, column=0, padx=5)
        add_20_button.grid(row=0, column=1, padx=5)
        add_30_button.grid(row=0, column=2, padx=5)
        add_40_button.grid(row=0, column=3, padx=5)
        add_50_button.grid(row=0, column=4, padx=5)

        self.is_running = False
        self.start_time = 0
        self.remaining_time = starting_time

        TimerApp.all_timers.append(self)
        self.update_display()

    def toggle_timer(self):
        if not self.is_running:
            self.start_timer()
            self.pause_other_timers()
            self.start_pause_button["text"] = "Pause"
        else:
            self.pause_timer()
            self.start_pause_button["text"] = "Resume"

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - (self.starting_time - self.remaining_time)
            self.update_timer()

    def pause_timer(self):
        if self.is_running:
            self.is_running = False
            self.start_pause_button["text"] = "Resume"
            self.update_display()

    def pause_other_timers(self):
        for timer in TimerApp.all_timers:
            if timer != self:
                timer.pause_timer()

    def update_timer(self):
        if self.is_running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            self.remaining_time = max(0, int(self.starting_time - elapsed_time))
            self.update_display()
            if self.remaining_time > 0:
                self.window.after(1000, self.update_timer)
            else:
                self.is_running = False
                self.start_pause_button["text"] = "Start"

    def add_time(self, seconds):
        self.start_time += seconds
        self.remaining_time += seconds
        self.update_display()

    def update_display(self):
        self.time_var.set("{:02d}".format(self.remaining_time))


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("500x800")

    timer1 = TimerApp(window, "Amandine", 60)  # Timer 1 with 60 seconds
    timer2 = TimerApp(window, "Evelyne", 60)  # Timer 2 with 120 seconds
    timer2 = TimerApp(window, "Anthony", 60)  # Timer 2 with 120 seconds

    window.mainloop()
