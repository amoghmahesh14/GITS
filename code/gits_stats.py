import os
import subprocess
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def get_git_stats():
    # Run git commands to get statistics
    commit_count = subprocess.check_output(["git", "rev-list", "--all", "--count"], universal_newlines=True).strip()
    author_count = subprocess.check_output(["git", "shortlog", "-s", "-n"], universal_newlines=True).strip().split('\n')
    line_count = subprocess.check_output(["git", "ls-files", "|", "xargs", "wc", "-l"], shell=True, universal_newlines=True).strip().split()[-2]

    # Get the major contributor
    major_contributor = author_count[0].split('\t')[1]

    return commit_count, len(author_count), line_count, major_contributor

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

def display_git_stats():
    # Get Git stats
    commit_count, author_count, line_count, major_contributor = get_git_stats()

    # Create and configure Tkinter window
    root = tk.Tk()
    root.title("Git Stats")

    # Create a style for the labels
    style = ttk.Style()
    style.configure("Stats.TLabel", font=("Helvetica", 14), padding=(10, 5))

    # Create and configure frames
    main_frame = ttk.Frame(root, style="Stats.TFrame")
    main_frame.pack(padx=20, pady=20)

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the images directory
    icons_dir = os.path.join(script_dir, "..", "icons")

    # Load and resize icons
    commit_icon = resize_image(os.path.join(icons_dir, "commit_icon.png"), 50, 50)
    author_icon = resize_image(os.path.join(icons_dir, "author_icon.png"), 50, 50)
    lines_icon = resize_image(os.path.join(icons_dir, "lines_icon.png"), 50, 50)
    contributor_icon = resize_image(os.path.join(icons_dir, "contributor_icon.png"), 50, 50)

    # Create and configure labels with icons to display Git stats in a grid
    create_stat_label(main_frame, commit_icon, f"Total Commits: {commit_count}", 0, 0)
    create_stat_label(main_frame, author_icon, f"Total Authors: {author_count}", 0, 1)
    create_stat_label(main_frame, lines_icon, f"Total Lines of Code: {line_count}", 1, 0)
    create_stat_label(main_frame, contributor_icon, f"Major Contributor: {major_contributor}", 1, 1)

    # Run Tkinter main loop
    root.mainloop()

def create_stat_label(frame, icon, text, row, column):
    # Create a frame for each box with a border
    box_frame = ttk.Frame(frame, style="Stats.TFrame", borderwidth=2, relief="solid")
    box_frame.grid(row=row, column=column, pady=(10, 0), padx=(10, 0), sticky="nsew")

    # Place the icon on top of the label
    icon_label = ttk.Label(box_frame, image=icon, style="Stats.TLabel", anchor="center")
    icon_label.grid(row=0, column=0, pady=(0, 5), padx=(0, 5), sticky="nsew")

    # Configure column weight to ensure proper alignment
    box_frame.grid_columnconfigure(0, weight=1)

    # Center the image horizontally
    box_frame.grid_rowconfigure(0, weight=1)

    # Create and configure label with text
    stat_label = ttk.Label(box_frame, text=text, style="Stats.TLabel", anchor="center")
    stat_label.grid(row=1, column=0, pady=(5, 0), padx=(0, 5), sticky="nsew")

def gits_stats(args):
    display_git_stats()
