import tkinter as tk




class myapps:
    def __init__(self,root:tk.Tk):
        self.root=root
        self.root.title("arc")
        self.root.geometry("640x480")
        self.root.configure(background="black")
        self.canvas=tk.Canvas(background="black",width=640,height=480)
        self.canvas.pack(padx=0,pady=0)
        c=self.canvas
        for a in range(0,360,20):
            c.create_arc(a,a,640-a,480-a,start=0,extent=a, outline="white")
       
    

    




root=tk.Tk()
apps=myapps(root)
root.mainloop()