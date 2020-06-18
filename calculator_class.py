from tkinter as tk
from typing import List

class Calculator:
    def __init__(self, root: tk.Tk,
    label: tk.label,
    display: tk.Entry,
    buttons: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.buttons = buttons

