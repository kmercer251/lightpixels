from PIL import Image
import tkinter

# Function to pass image directory to the coordinate function (another thing that can be done better in later revisions)

def btnEvent(event):
    global ent_path
    getCoords(ent_path)

# Function to open the user-given image, return the dimensions of the image in pixels, and return the x and y coordinates of each pixel lighter than 0

def getCoords(ent_path):

# Open output file for writing, get path of image

    outFile = open("Coordinateoutput.txt", "w")

    imgPath = ent_path.get()
    img = Image.open(imgPath)

# Convert image to grayscale and get width/height

    grayImg = img.convert("L")
    width = grayImg.width
    height = grayImg.height

# Print image dimensions

    global ent_dims
    ent_dims.insert(0, "Width: {w}px, Height: {h}px".format(w = width, h = height))

# Print coordinates of light pixels

    global txt_pixels
    for x in range(width):
        for y in range(height):
            if grayImg.getpixel((x,y)) > 0:
                txt_pixels.insert("1.0", "\nX: {x}, Y: {y}".format(x = x, y = y))
                outFile.write("\nX: {x}, Y: {y}".format(x = x, y = y))
    
    outFile.close()

# Function to clear all fields

def clearAll(event):
    global ent_path
    ent_path.delete(0, tkinter.END)
    global ent_dims
    ent_dims.delete(0, tkinter.END)
    global txt_pixels
    txt_pixels.delete("1.0", tkinter.END)

# Set up main GUI window and add greeting text at top

window = tkinter.Tk()
lbl_greeting = tkinter.Label(text = "Image Coordinate Thing")
lbl_greeting.pack()

# Frame for execute and clear buttons (this could be done better)

frm_buttons = tkinter.Frame()
btn_coords = tkinter.Button(
    master = frm_buttons,
    text = "Get Coordinates",
    width = 15,
    height = 3,
    bg = "#56c8d8",
    fg = "#006978",
)
btn_coords.pack()
btn_clear = tkinter.Button(
    master = frm_buttons,
    text = "Clear all fields",
    width = 15,
    height = 3,
    bg = "#56c8d8",
    fg = "#006978",
)
btn_clear.bind("<Button-1>", clearAll)
btn_clear.pack()
frm_buttons.pack(side = tkinter.LEFT)

# Frame for directory input field and label

frm_path = tkinter.Frame()
lbl_entry = tkinter.Label(master = frm_path, text = "Enter abolute path to image (wihout ~):")
lbl_entry.pack()
ent_path = tkinter.Entry(master = frm_path, fg = "black", bg = "#ffffff", width = 50)
ent_path.pack()
frm_path.pack()

# Bind execute button down here because the ent_path var has to be declared first, and changing the frame order messes up formatting (also can be done better)

btn_coords.bind("<Button-1>", btnEvent)

# Frame to print image dimensions

frm_dims = tkinter.Frame()
lbl_dims = tkinter.Label(master = frm_dims, text = "Image Dimensions:")
lbl_dims.pack()
ent_dims = tkinter.Entry(master = frm_dims, fg = "black", bg = "#ffffff", width = 50)
ent_dims.pack()
frm_dims.pack()

# Frame for outputting main info, coordinates of all pixels above a certain value

frm_lightpixels = tkinter.Frame()
lbl_pixels = tkinter.Label(master = frm_lightpixels, text = "Coordinates of pixels lighter than 0:")
lbl_pixels.pack()
txt_pixels = tkinter.Text(master = frm_lightpixels, fg = "black", bg = "#ffffff")
txt_pixels.pack()
frm_lightpixels.pack()

# Window main loop

window.mainloop()