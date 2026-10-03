import tkinter as tk
import random
window = tk.Tk()
window.title("Snake Game")
window.geometry("800x600")
kg = tk.Canvas(window, width=800, height=600, bg="black")
kg.pack()
snake_x = 390
snake_y = 290
than_ran = []
than_ran.append((370,290))
than_ran.append((350,290))
than_2_x = than_ran[1][0]
than_2_y = than_ran[1][1]
than_2 = kg.create_rectangle(than_2_x, than_2_y, than_2_x + 20, than_2_y + 20, fill = "green")
than_x = than_ran[0][0]
than_y = than_ran[0][1]
than = kg.create_rectangle(than_x, than_y, than_x + 20, than_y + 20, fill = "green")
than_hinh = [than, than_2]
snake = kg.create_rectangle(snake_x,snake_y,snake_x + 20,snake_y + 20, fill = "green")
food_x = random.randrange(0,800,20)
food_y = random.randrange(0,600,20)
food = kg.create_oval(food_x, food_y, food_x + 20, food_y + 20, fill = "red")
huong = "right"
def move_snake():
    global snake_x,snake_y, snake
    global food_x, food_y, food
    kg.delete(snake)
    cu_x = snake_x
    cu_y = snake_y
    if huong == "right":
        snake_x += 20
    elif huong == "left":
        snake_x -= 20
    elif huong == "up":
        snake_y -= 20
    elif huong == "down":
        snake_y += 20
    if snake_x < 0 or snake_x >= 800 or snake_y < 0 or snake_y >= 600:
        print("Game Over!")
        return
    if (snake_x <= food_x + 20 and
        snake_x + 20 >= food_x and
        snake_y <= food_y + 20 and
        snake_y + 20 >= food_y):
        print("Da an!")
        kg.delete(food)
        food_x = random.randrange(0,800,20)
        food_y = random.randrange(0,600,20)
        food = kg.create_oval(food_x, food_y, food_x + 20, food_y + 20, fill = "red")
        than_ran.append(than_ran[-1])
        than_moi_x = than_ran[-1][0]
        than_moi_y = than_ran[-1][1]
        than_moi = kg.create_rectangle(than_moi_x, than_moi_y, than_moi_x + 20, than_moi_y + 20, fill = "green")
        than_hinh.append(than_moi)
    for i in range(len(than_ran) -1, 0, -1):
        than_ran[i] = than_ran[i-1]
    than_ran[0]= (cu_x, cu_y)
    for i in range(len(than_ran)):
        kg.coords(than_hinh[i], than_ran[i][0], than_ran[i][1], than_ran[i][0] + 20, than_ran[i][1] + 20)
    snake = kg.create_rectangle(snake_x,snake_y,snake_x + 20,snake_y + 20, fill = "green")
    window.after(100, move_snake)
def di_chuyen(event):
    global huong
    if event.keysym == "Right" and huong != "left":
        huong = "right"
    elif event.keysym == "Left" and huong != "right":
        huong = "left"
    elif event.keysym == "Up" and huong != "down":
        huong = "up"
    elif event.keysym == "Down" and huong != "up":
        huong = "down"
window.bind("<Key>",di_chuyen)
move_snake()
window.mainloop()
