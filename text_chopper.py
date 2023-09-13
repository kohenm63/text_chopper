import tkinter as tk
import pyperclip

def chop_text():
    text_to_chop = entry.get()
    if text_to_chop:
        text_parts = [text_to_chop[i:i + len(text_to_chop) // 8] for i in range(0, len(text_to_chop), len(text_to_chop) // 8)]
        create_result_frame(text_parts)
    else:
        clear_result_frame()

def copy_chunk(chunk):
    pyperclip.copy(chunk)

def create_result_frame(text_parts):
    clear_result_frame()
    global result_frame
    result_frame = tk.Frame(window)
    result_frame.pack()

    for i, chunk in enumerate(text_parts):
        chunk_label = tk.Label(result_frame, text=f"Chunk {i + 1}:", padx=10)
        chunk_label.grid(row=i, column=0, sticky="w")

        chunk_text = tk.Label(result_frame, text=chunk, padx=10, width=40)  
        chunk_text.grid(row=i, column=1, sticky="w")

        copy_button = tk.Button(result_frame, text="Copy", command=lambda ch=chunk: copy_chunk(ch), padx=5, pady=5)  # Adjusted padding
        copy_button.grid(row=i, column=2)

def clear_result_frame():
    if 'result_frame' in globals():
        result_frame.destroy()

# Create the main window
window = tk.Tk()
window.title("Text Chopper")

# Entry widget for input
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# Button to chop text
chop_button = tk.Button(window, text="Chop Text", command=chop_text)
chop_button.pack()

# Start the Tkinter main loop
window.mainloop()
