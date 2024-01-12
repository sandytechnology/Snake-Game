from tkinter import *
import random

GAME_WIDTH=700
GAME_HEIGHT=600
SPEED=100
SPACE_SIZE=50
BODY_PARTS=3
SNAKE_COLOR="green"
FOOD_COLOR="red"
BACKGROUND_COLOR="black"

class Snake:
      def __init__(self):
            self.body_size=BODY_PARTS
            self.coordinates=[]
            self.squares=[]

            for i in range(0,BODY_PARTS):
                  self.coordinates.append([0,0])

            for x,y in self.coordinates:
                  square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
                  self.squares.append(square)
                  
class Food:
      def __init__(self):
            x=random.randint(0,(GAME_WIDTH / SPACE_SIZE)-1)*SPACE_SIZE
            y=random.randint(0,(GAME_HEIGHT / SPACE_SIZE)-1)*SPACE_SIZE

            self.coordinates=[x,y]
            canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")
            
def next_turn(snake,food):
      x,y=snake.coordinates[0]

      if direction=="up":
            y=y-SPACE_SIZE
      elif direction=="down":
            y=y+SPACE_SIZE
      elif direction=="left":
            x=x-SPACE_SIZE
      elif direction=="right":
            x=x+SPACE_SIZE

      snake.coordinates.insert(0,(x,y))
      square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
      snake.squares.insert(0,square)

      if x==food.coordinates[0] and y==food.coordinates[1]:
            global score,high_score
            score +=5
            scor_label.config(text="Score:{}".format(score))
            canvas.delete("food")
            food=Food()
      else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

      if check_collision(snake):
            game_over()
      else:
            root.after(SPEED,next_turn,snake,food)

def change_direction(new_direction):
      global direction

      if new_direction=="left":
            if direction !="right":
                  direction= new_direction
      if new_direction=="right":
            if direction !="left":
                  direction= new_direction
      if new_direction=="up":
            if direction !="down":
                  direction= new_direction
      if new_direction=="down":
            if direction !="up":
                  direction= new_direction
                  
def check_collision(snake):
      x,y=snake.coordinates[0]
      if x<0 or x>=GAME_WIDTH:
            return True
      elif y<0 or y>=GAME_HEIGHT:
            return True
      for body_part in snake.coordinates[1:]:
            if x==body_part[0] and y==body_part[1]:
                  return True
      return False

def game_over():
      canvas.delete(ALL)
      canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("Times New Roman",30),
                         text="GAME OVER",fill="red",tag="gameover")

root=Tk()
root.title("snake game")
root.resizable(False,False)

score=0
direction="down"

label=Label(root,text="SNAKE GAME",font=("aerial",30),fg="blue")
label.pack()

scor_label=Label(root,text="Score:{}".format(score),font=("aerial",20),fg="blue")
scor_label.pack()

btn=Button(root,text="EXIT",font=("aerial",15),fg="blue",command=root.destroy)
btn.pack()


canvas=Canvas(root,bg=BACKGROUND_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()
root.update()

root_width=root.winfo_width()
root_height=root.winfo_height()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

x=int((screen_width/2)-(root_width/2))
y=int((screen_height/2)-(root_height/2))

root.geometry(f"{root_width}x{root_height}+{100}+{10}")
root.bind("<Left>",lambda event:change_direction("left"))
root.bind("<Right>",lambda event:change_direction("right"))
root.bind("<Up>",lambda event:change_direction("up"))
root.bind("<Down>",lambda event:change_direction("down"))

snake=Snake()
food=Food()
next_turn(snake,food)
             
root.mainloop()

















