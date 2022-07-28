from tkinter import Button, Label
import random
import settings


class Cell:
  all = []
  cell_count_label_object = None
  
  def __init__(self, x, y, is_mine=False):
    self.is_mine = is_mine
    self.cell_button_object = None
    self.x = x
    self.y = y

    # Append the object to the Cell.all list 
    Cell.all.append(self)
    
  def create_button_object(self, location):
    btn = Button(
      location,
      width = 4,
      height = 2
    )
    
    #Left Click
    btn.bind('<Button-1>',self.left_click_actions)
    # Right Click
    btn.bind('<Button-3>',self.right_click_actions)
    self.cell_button_object = btn

  @staticmethod
  def create_cell_count_label(location):
    label = Label(
      location,
      text = f"Cells Left:{settings.CELLS_TOTAL}"
    )
    Cell.cell_count_label_object = label
  
  def left_click_actions(self, event):
    if self.is_mine:
      self.reveal_mine()
    else:
      if self.surrounded_cells_mines_length == 0:
        for cell_obj in self.surrounded_cells:
          cell_obj.reveal_cell()
      self.reveal_cell()

  def get_cell_by_axis(self, x, y):
    # return cell object based on x,y value
    for cell in Cell.all:
      if cell.x == x and cell.y == y:
        return cell

  @property
  def surrounded_cells(self):
    cells = [
      self.get_cell_by_axis(self.x - 1, self.y - 1),
      self.get_cell_by_axis(self.x - 1, self.y),
      self.get_cell_by_axis(self.x - 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y - 1),
      self.get_cell_by_axis(self.x + 1, self.y),
      self.get_cell_by_axis(self.x + 1, self.y + 1),
      self.get_cell_by_axis(self.x, self.y + 1)
    ]

    cells = [cell for cell in cells if cell is not None]
    return cells

  @property
  def surrounded_cells_mines_length(self):
    counter = 0
    for cell in self.surrounded_cells:
      if cell.is_mine:
        counter += 1
        
      return counter  
  
  def reveal_cell(self):
    self.cell_button_object.configure(text=self.surrounded_cells_mines_length)
  
  def reveal_mine(self):
    # End game and display game over message
    self.cell_button_object.configure(bg='red')
  
  def right_click_actions(self, event):
    print(event)
    print("I am right clicked!")

  @staticmethod
  def randomize_mines():
    picked_cells = random.sample(
      Cell.all, settings.MINES_TOTAL
    )
    for picked_cell in picked_cells:
      picked_cell.is_mine = True

  def __repr__(self):
    return f"Cell({self.x},{self.y})"
    