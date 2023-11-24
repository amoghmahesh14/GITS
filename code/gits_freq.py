import os
import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from datetime import datetime, timedelta
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_commit_stats(duration_months=12):
    git_log_output = subprocess.check_output(["git", "log", "--format=%ad", "--date=format:%Y-%m-%d"], universal_newlines=True).strip().split('\n')

    commit_stats = {}
    today = datetime.today()

    for date_str in git_log_output:
        commit_date = datetime.strptime(date_str[:10], "%Y-%m-%d")

        if today - commit_date <= timedelta(days=duration_months * 30):
            year_month = commit_date.strftime("%b")
            commit_stats[year_month] = commit_stats.get(year_month, 0) + 1

    start_date = today - timedelta(days=duration_months * 30)
    while start_date <= today:
        year_month = start_date.strftime("%b")
        commit_stats.setdefault(year_month, 0)
        start_date += timedelta(days=30)

    return commit_stats

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def display_commit_stats():
    root = tk.Tk()
    root.title("Commit Stats")

    style = ttk.Style()
    style.configure("Stats.TLabel", font=("Helvetica", 14), padding=(10, 5))

    main_frame = ttk.Frame(root, style="Stats.TFrame")
    main_frame.pack(padx=20, pady=20)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    icons_dir = os.path.join(script_dir, "..", "icons")

    commit_icon = resize_image(os.path.join(icons_dir, "commit_icon.png"), 50, 50)

    duration_label = ttk.Label(main_frame, text="Select Duration:")
    duration_label.grid(row=0, column=0, pady=(10, 0), padx=(10, 0), sticky="nsew")

    duration_var = tk.IntVar(value=12)
    duration_dropdown = ttk.Combobox(main_frame, values=[1, 3, 6, 12], textvariable=duration_var, state="readonly")
    duration_dropdown.grid(row=0, column=1, pady=(10, 0), padx=(10, 0), sticky="nsew")

    duration_dropdown.bind("<<ComboboxSelected>>", lambda event: update_graph(main_frame, commit_icon, 1, duration_var))

    update_graph(main_frame, commit_icon, 1, duration_var)

    root.mainloop()

def update_graph(main_frame, icon, row, duration_var):
    duration_months = duration_var.get()
    commit_stats = get_commit_stats(duration_months)

    fig = Figure(figsize=(8, 4), tight_layout=True)
    ax = fig.add_subplot(111)
    ax.plot(list(commit_stats.keys()), list(commit_stats.values()), marker='o', linestyle='-', color='b')
    ax.set_title(f"Commit Frequency for the Last {duration_months} Months")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Commits")
    ax.grid(True)

    for month, commits in commit_stats.items():
        ax.text(month, commits, str(commits), ha='center', va='bottom', fontsize=8)

    canvas = FigureCanvasTkAgg(fig, master=main_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=row, column=0, columnspan=2, pady=(10, 0), padx=(10, 0), sticky="nsew")

def gits_freq(args):
    display_commit_stats()
