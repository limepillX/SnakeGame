from tkinter import *
from random import *

Win_width = 1400
Win_height = int(round(Win_width / 2))
Amount_Of_squares = 20
Step = int(Win_height / Amount_Of_squares)
BackgroundColor = 'gray22'
CanvasColor = 'gray12'
AppleColor = 'red'
SnakeLength = 20
Speed = 100
HeadColor = 'white'
BodyColor = 'orange'

score = 0
apl = Win_width / 2


class Snake:
    def __init__(self):
        self.snake_lenght = SnakeLength
        self.coord = [[0, 0]] * self.snake_lenght
        self.squares = []

        for x, y in self.coord:
            square = canvas.create_rectangle(x, y, x + Step, y + Step, fill=BodyColor)
            self.squares.append(square)


class Apple:
    def __init__(self):
        x = randint(0, int((Win_width / Step) - 1)) * Step
        y = randint(0, int((Win_height / Step) - 1)) * Step

        self.coord = [x, y]

        canvas.create_rectangle(x, y, x + Step, y + Step, fill=AppleColor, outline="black")


def move(snake, apple):
    global score
    for x, y in snake.coord:
        canvas.create_rectangle(x, y, x + Step, y + Step, fill=BodyColor)
    x, y = snake.coord[0]

    if direction == 'down':
        y += Step
    elif direction == 'up':
        y -= Step
    elif direction == 'left':
        x -= Step
    elif direction == 'right':
        x += Step
    snake.coord.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + Step, y + Step, fill=HeadColor)
    snake.squares.insert(0, square)

    if x == apple.coord[0] and y == apple.coord[1]:
        canvas.delete('apple')
        apple = Apple()
        score += 1
        ScoreText.configure(text='Score: ' + str(score) + ' 000')
    else:
        x, y = snake.coord[-1]
        canvas.create_rectangle(x, y, x + Step, y + Step, fill=CanvasColor, outline='gray12')

        del snake.coord[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
    window.after(Speed, move, snake, apple)


def crategrid():
    for i in range(1, int(Win_width / Step)):
        canvas.create_line(i * Step, 0, i * Step, Win_height, fill='gray11')

    for i in range(1, int(Win_height / Step)):
        canvas.create_line(0, i * Step, Win_width, i * Step, fill='gray11')


def keypressed_up(event):
    global direction
    direction = 'up'


def keypressed_left(event):
    global direction
    direction = 'left'


def keypressed_down(event):
    global direction
    direction = 'down'


def keypressed_right(event):
    global direction
    direction = 'right'


def makeitmove():
    SettingsText.destroy()
    BlankText.destroy()
    BlankText2.destroy()
    StartButton.destroy()
    rad1.destroy()
    rad2.destroy()
    rad3.destroy()
    snake = Snake()
    apple = Apple()
    move(snake, apple)


def difficulty():
    global Speed
    Speed = selected.get()


window = Tk()
window.title("Змейка")
window.resizable(width=False, height=False)
window.geometry(str(Win_width + 3) + 'x' + str(Win_height + 42))
window.configure(bg='gray22')

BlankText = Label(window, text=' ', font=('Arial', int(Win_width / 10)), fg='white', bg=BackgroundColor)
BlankText.pack()

SettingsText = Label(window, text='Сложность', font=('Arial', 20), fg='white', bg=BackgroundColor)
SettingsText.pack()

selected = IntVar()
rad1 = Radiobutton(window, text='Легко', value=150, bg=BackgroundColor, fg='orange', variable=selected,
                   command=difficulty)
rad2 = Radiobutton(window, text='Нормально', value=100, bg=BackgroundColor, fg='orange', variable=selected,
                   command=difficulty)
rad3 = Radiobutton(window, text='Сложно', value=60, bg=BackgroundColor, fg='orange', variable=selected,
                   command=difficulty)
rad1.pack()
rad2.pack()
rad3.pack()

StartButton = Button(window, text='Press to start', bg=BackgroundColor, fg='white', command=makeitmove)
StartButton.pack()

BlankText2 = Label(window, text=' ', font=('Arial', 1000), fg='white', bg=BackgroundColor)
BlankText2.pack()

direction = 'down'
ScoreText = Label(window, text='Score: ' + str(score), font=('Arial', 20), fg='black', bg=BackgroundColor)
ScoreText.pack()
canvas = Canvas(window, height=Win_height, width=Win_width, bg=CanvasColor)
canvas.pack()
# border = canvas.create_rectangle(2, 2, Win_width, Win_height, outline=BorderColor)
crategrid()

window.bind("<Up>", keypressed_up)
window.bind("<Left>", keypressed_left)
window.bind("<Down>", keypressed_down)
window.bind("<Right>", keypressed_right)

window.mainloop()
