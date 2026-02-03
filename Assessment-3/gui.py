import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2, os
from image_processor import ImageProcessor

class ImageEditorGUI:
    # Main GUI class for HIT137 Image Editor.
    # Handles menu, buttons, sliders, canvas, and status bar.
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("HIT137 Image Editor")
        self.root.geometry("1100x700")
        
        self.processor = ImageProcessor()
        self.tk_image = None
        self.image_path = None
        
        self.setup_menu()
        self.setup_ui()
        self.root.bind("<Configure>", self.redraw)
        
        # MENU
        def setup_menu(self):
            menubar = tk.Menu(self.root)
            file_menu = tk.Menu(menubar, tearoff = 0)
            file_menu.add_command(label="Open", command=self.open_image)
            file_menu.add_command(label="Save As", command=self.save_image)
            file_menu.add_separator()
            file_menu.add_command(label="Exit", command=self.root.quit)
            menubar.add_cascade(label="File", menu=file_menu)
            self.root.config(menu=menubar)
            
            # UI
            def setup_ui(self):
                # Canvas for displaying image
                self.canvas = tk.Canvas(self.root, bg="black")
                self.canvas = tk.pack(expand=True, fill=tk.BOTH)
                
                # Panel for buttons & sliders
                panel = tk.Frame(self.root)
                panel.pack(side=tk.BOTTOM, fill=tk.X)
                
                # Buttons
                tk.Button(panel, text="Grayscale", command=self.apply(self.processor.grayscale)).pack(side=tk.LEFT)
                tk.Button(panel, text="Edge", command=self.apply(self.processor.edge)).pack(side=tk.LEFT)
                tk.Button(panel, text="Rotate 90°", command=self.apply(lambda: self.processor.rotate(90))).pack(side=tk.LEFT)
                tk.Button(panel, text="Rotate 190°", command=self.apply(lambda: self.processor.rotate(180))).pack(side=tk.LEFT)
                tk.Button(panel, text="Rotate 270°", command=self.apply(lambda: self.processor.rotate(270))).pack(side=tk.LEFT)
                tk.Button(panel, text="Flip H", command=self.apply(lambda: self.processor.flip("horizontal"))).pack(side=tk.LEFT)
                tk.Button(panel, text="Flip V", command=self.apply(lambda: self.processor.flip("vertical"))).pack(side=tk.LEFT)
                tk.Button(panel, text="Undo", command=self.apply(self.processor.undo)).pack(side=tk.LEFT)
                tk.Button(panel, text="Redo", command=self.apply(self.processor.redo)).pack(side=tk.LEFT)
                
                
                
                

