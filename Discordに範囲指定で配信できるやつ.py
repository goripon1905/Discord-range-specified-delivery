import tkinter as tk
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap('C:/Users/goripon/Desktop/python/アイコン.ico')
        self.title("Discordに範囲指定で配信できるやつ")
        self.geometry("500x300")
        self.config(bg="white")
        self.attributes("-transparentcolor", "white")
        self.attributes("-topmost", True)
        
if __name__ == "__main__":
    application = Application()
    application.mainloop()
