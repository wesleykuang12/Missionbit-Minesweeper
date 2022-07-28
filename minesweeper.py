from tkinter import *
from cell import Cell
import settings
import utility


root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Wesley's Minesweeper")
root.resizable(False, False)

# Top Frame
top_frame = Frame(
  root, 
  bg = 'black', 
  width = settings.WIDTH, 
  height = utility.height_percent(25)
)

top_frame.place(x=0, y=0)

# Left Frame
left_frame = Frame(
  root, 
  bg = 'black', 
  width = utility.width_percent(25), 
  height = utility.height_percent(75)
)

left_frame.place(
  x=0, 
  y=utility.height_percent(25)
)

# Center Frame
center_frame = Frame(
  root,
  bg = 'black',
  width = utility.width_percent(75),
  height = utility.height_percent(75)
)

center_frame.place(
  x=utility.width_percent(25), 
  y=utility.height_percent(25)
)

# Grid
for x in range(settings.GRID_SIZE):
  for y in range(settings.GRID_SIZE):
    c = Cell(x, y)
    c.create_button_object(center_frame)
    c.cell_button_object.grid(
      column=x, row=y
    )


Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
  x=0, 
  y=0
)
    
# Randomize mines
Cell.randomize_mines()


# Run the window
root.mainloop()



# Example for creating grid with buttons
"""
c1 = Cell()
c1.create_button_object(center_frame)
c1.cell_button_object.grid(
  column=0, row=0
)

c2 = Cell()
c2.create_button_object(center_frame)
c2.cell_button_object.grid(
  column=0, row=1
)
"""