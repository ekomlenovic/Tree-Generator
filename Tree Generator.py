import os
import tkinter as tk
from tkinter import filedialog, scrolledtext
from tkinter.ttk import Progressbar
import pyperclip
import threading

progress_bar = None
stop_event = threading.Event()

def generate_tree(start_path, indent='', root_path=None, progress=None, callback=None):
    if not os.path.exists(start_path) or stop_event.is_set():
        return

    if root_path is None:
        root_path = start_path

    files = os.listdir(start_path)
    files.sort()
    total_elements = len(files)

    for index, file in enumerate(files):
        if stop_event.is_set():
            break

        path = os.path.join(start_path, file)

        if ignore_dot_var.get() and file.startswith('.'):
            continue

        if index == total_elements - 1:
            marker = '└── '
            new_indent = indent + '    '
        else:
            marker = '├── '
            new_indent = indent + '│   '

        relative_path = os.path.relpath(path, root_path)
        print(indent + marker + relative_path)
        text_area.insert(tk.END, indent + marker + relative_path + '\n')

        if progress:
            progress.step(1)
            window.update_idletasks()

        if os.path.isdir(path):
            generate_tree(path, new_indent, root_path, progress)

    if callback:
        window.after(100, callback)

def tree_generation_complete():
    if progress_bar:
        progress_bar.destroy()
    window.grab_release()

    choose_button.config(state=tk.NORMAL)
    copy_button.config(state=tk.NORMAL)
    clear_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

    global stop_event
    stop_event.clear()

def choose_folder():
    global progress_bar 
    selected_folder = filedialog.askdirectory()
    if selected_folder:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, '│-' + get_parent_folder_name(selected_folder) + '\n')
        print('│-' + get_parent_folder_name(selected_folder))

        total_elements = count_files(selected_folder)

        progress_bar = Progressbar(window, mode='determinate', length=500, maximum=total_elements)
        progress_bar.pack(pady=5)

        window.grab_set()

        choose_button.config(state=tk.DISABLED)
        copy_button.config(state=tk.DISABLED)
        clear_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

        threading.Thread(target=generate_tree, args=(selected_folder, '', selected_folder, progress_bar, tree_generation_complete)).start()

def count_files(folder):
    count = 0
    for _, dirs, files in os.walk(folder):
        count += len(dirs) + len(files)
    return count

def copy_to_clipboard():
    content = text_area.get("1.0", tk.END)
    pyperclip.copy(content)

def clear_text():
    text_area.delete('1.0', tk.END)

def get_parent_folder_name(path):
    return os.path.basename(os.path.normpath(path))

def stop_generation():
    global stop_event
    stop_event.set()

def toggle_ignore_dot():
    return

window = tk.Tk()
window.title("Tree Generator")
window.resizable(False, False)

ignore_dot_var = tk.BooleanVar(value=True)

choose_button = tk.Button(window, text="Choose Folder", command=choose_folder)
choose_button.pack(pady=10)

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack(pady=10)

print('aaa')
ignore_dot_checkbox = tk.Checkbutton(window, text="Ignore Dot", variable=ignore_dot_var, command=toggle_ignore_dot)
ignore_dot_checkbox.pack(pady=5)

text_area = scrolledtext.ScrolledText(window, width=130, height=30, wrap=tk.WORD)
text_area.pack()

stop_button = tk.Button(window, text="Stop", command=stop_generation, state=tk.DISABLED)
stop_button.pack(pady=10)

window.mainloop()
