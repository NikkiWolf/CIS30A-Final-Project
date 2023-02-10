#CIS30A Final Project Costa Rica (Tkinter) New

#Tkinter import
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import Image
import time
 
#Making a new window
window = tk.Tk()


#function to open image when click
#if and elif used to open buttons based on the user input
def show_image(buttonpressed):
    global buttonLabel
    if buttonpressed == "La Fortuna":
        image = ImageTk.PhotoImage(file="La Fortuna Pics Final.png")
        imagebox.config(image=image)
        imagebox.image = image
        buttonLabel["text"]= "This beautiful town welcomes you with local hot springs, along with a good view of Volcan Arenal!\n The star of La Fortuna is visiting Volcan Arenal for a hike, seeing different species of wildlife while\n surrounded by the volcano’s lush plant life. A few animals that can be seen on this hike include\n Howler Monkeys, yellow Vipers, and a rare chance of a sloth."
        buttonLabel.config(fg = "black", bg = "white", font="Oswald 10 bold")
    elif buttonpressed == "Monteverde":
        image = ImageTk.PhotoImage(file="Monteverde Pics Final.png")
        imagebox.config(image=image)
        imagebox.image = image
        buttonLabel["text"]= "Arriving in this lively town, it is worth stopping by a coffee shop to grab a quick latte as Monteverde is also known for\n its coffee. Monteverde is a great place to go ziplining, having the longest zipline in Latin America! Another\n attraction that many visit in monteverde is the cloud forest, which is soon to be closed to the public."
        buttonLabel.config(fg = "black", bg = "white", font="Oswald 10 bold")
    elif buttonpressed == "Palo Verde":
        image = ImageTk.PhotoImage(file="Palo_Verde_Pictures.png")
        imagebox.config(image=image)
        imagebox.image = image
        buttonLabel["text"]= "This is the home to the endangered bird species, the magnificent bird Jabiru.\n Here one can spend the night in the middle of all of the swamp nature. Strayed\n from civilization, you can reconnect to nature as you’re surrounded by iguanas,\n howler monkeys, and many different bird species. Fifty percent of the park is a\n flooded forest, hence giving the park the category of a wetland."
        buttonLabel.config(fg = "black", bg = "white", font="Oswald 10 bold")
    elif buttonpressed == "Manuel Antonio":
        image = ImageTk.PhotoImage(file="Manuel_Antonio_Pics.png")
        imagebox.config(image=image)
        imagebox.image = image
        buttonLabel["text"]= "Here we have a gorgeous lively beach where one can enjoy seafood by the beach, while having the company\n of monkeys! Monkeys often scurry along the power lines, visible from most restaurants. While visiting this\n lovely beach there is the Manuel Antonio National Park, which contains both jungle and beach. On the\n beach one can enjoy hermit crabs, warm seawater, and the strong UV rays!"
        buttonLabel.config(fg = "black", bg = "white", font="Oswald 10 bold")
        
#Define the geometry of the window
window.geometry("1920x1080")
window.title("Costa Rica")
window.config(bg="white")

#Quit Button
quitButton = tk.Button(window, text="QUIT", bg="red", command=quit)
quitButton.pack()
 
 
#Label That tells user to take a peek around the program 
tk.Label(window, text = "Select a City to Take a Peek!", fg = "black", bg = "white").pack()

#For the frame
f1 = tk.Frame(window)
f1.pack()



#The four buttons that the user can click on to display image and text
button1 = tk.Button(f1, 
    text = "La Fortuna",
    width = 20,
    height = 3,
    bg = "red",
    fg = "black", command=lambda: show_image("La Fortuna")
)
button1.grid(row=0, column=0)


button2 = tk.Button(f1,
    text = "Monteverde",
    width = 20,
    height = 3,                
    bg = "light blue",
    fg = "black", command=lambda: show_image("Monteverde")
)
button2.grid(row=0, column=1)


button3 = tk.Button(f1,
    text = "Palo Verde",
    width = 20,
    height = 3,                
    bg = "light green",
    fg = "black", command=lambda: show_image("Palo Verde")
)
button3.grid(row=0, column=2)


button4 = tk.Button(f1,
    text = "Manuel Antonio",
    width = 20,
    height = 3,                 
    bg = "orange",
    fg = "black", command=lambda: show_image("Manuel Antonio")
)
button4.grid(row=0, column=3)


#Display facts about city
#Show pictures 
buttonLabel = tk.Label(window, text='')
buttonLabel.pack()



#imagebox label
imagebox = tk.Label(window)
imagebox.pack()


#Introduction to the user
messagebox.showinfo("showinfo", "Thank you for visting our program!!!")


#Counter to display how long user has been visiting
counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)
    count()

start_time = time.time()
def count():
    counter += 1
for i in range(1000):
    pass
end_time = time.time()
print("Time spent visiting: ", end_time - start_time, "seconds")


root = tk.Tk()
root.title("Time Spent Visiting :)")
label = tk.Label(root, fg="black")
label.pack()
counter_label(label)
button = tk.Button(root, text="Stop", width=25, command=root.destroy)
button.pack()
root.mainloop()



#mainloop so program can run
window.mainloop()









        