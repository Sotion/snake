import random
import time

import PySimpleGUI as sg

# CONSTRAINTS
FIELD_SIZE = 400
POINT_SIZE = int((FIELD_SIZE * 2.5) / 33)
POINT_MOVE = int((FIELD_SIZE * 3) / 33)

sg.theme('Green')

field = sg.Graph(
    canvas_size=(FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left=(0, 0),
    graph_top_right=(FIELD_SIZE, FIELD_SIZE),
    background_color='white',
    key="point")

layout = [[sg.Text('Press any arrow to start')], [field]]

layout_loose_text = [[sg.Text('You lose.')], [sg.Submit(), sg.Cancel()]]

window = sg.Window('Snake', layout, return_keyboard_events=True)
window.Finalize()

graph = window.Element("point")

# variables
fruit_point_color = 'red'
snake_point_color = 'green'
started_parameter_x = random.randrange(0, FIELD_SIZE, POINT_MOVE)
started_parameter_y = random.randrange(0, FIELD_SIZE, POINT_MOVE)
last_postion_x = started_parameter_x
last_postion_y = started_parameter_y
end_left_parameter = 0
end_right_parameter = FIELD_SIZE
end_up_parameter = FIELD_SIZE
end_down_parameter = 0
table_of_snake_point = []
count_of_moves = 0


# FUNCTIONS
# def get_location_of_snake_point(x, y):
#     return x, y

def draw_fruit_point():
    fruit_x = random.randrange(0, FIELD_SIZE, POINT_MOVE)
    fruit_y = random.randrange(0, FIELD_SIZE, POINT_MOVE)
    fruit_point_id = graph.draw_point((fruit_x, fruit_y), POINT_SIZE, fruit_point_color)
    return fruit_x, fruit_y, fruit_point_id

def draw_snake_point(snake_x, snake_y):
    if event == 'Left:37': snake_point_id = graph.draw_point((snake_x, snake_y), POINT_SIZE, snake_point_color)
    if event == 'Right:39': snake_point_id = graph.draw_point((snake_x, snake_y), POINT_SIZE, snake_point_color)
    if event == 'Up:38': snake_point_id = graph.draw_point((snake_x, snake_y), POINT_SIZE, snake_point_color)
    if event == 'Down:40': snake_point_id = graph.draw_point((snake_x, snake_y), POINT_SIZE, snake_point_color)
    return snake_x, snake_y, snake_point_id


def clear_point(point_id):
    graph.delete_figure(point_id)


# Generate snake starting position
first_snake_point = graph.draw_point((started_parameter_x, started_parameter_y), POINT_SIZE, snake_point_color)
# Append first snake point to table of snake points
table_of_snake_point.append(first_snake_point)
# Generate fruit starting position
last_fruit_point = draw_fruit_point()

start = time.time()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    last_snake_point = []

    if event == 'Left:37':
        if (last_postion_x - POINT_MOVE) >= end_left_parameter:

            last_snake_point = draw_snake_point(last_postion_x - POINT_MOVE, last_postion_y)
            table_of_snake_point.append(last_snake_point[2])
            last_postion_x -= POINT_MOVE
            count_of_moves += 1
        else:
            sg.popup('You crashed into the wall!')
            break

    if event == 'Up:38':
        if (last_postion_y + POINT_MOVE) <= end_up_parameter:

            last_snake_point = draw_snake_point(last_postion_x, last_postion_y + POINT_MOVE)
            table_of_snake_point.append(last_snake_point[2])
            last_postion_y += POINT_MOVE
            count_of_moves += 1
        else:
            sg.popup('You crashed into the wall!')
            break

    if event == 'Right:39':
        if (last_postion_x + POINT_MOVE) <= end_right_parameter:

            last_snake_point = draw_snake_point(last_postion_x + POINT_MOVE, last_postion_y)
            table_of_snake_point.append(last_snake_point[2])
            last_postion_x += POINT_MOVE
            count_of_moves += 1
        else:
            sg.popup('You crashed into the wall!')
            break

    if event == 'Down:40':
        if (last_postion_y - POINT_MOVE) >= end_down_parameter:

            last_snake_point = draw_snake_point(last_postion_x, last_postion_y - POINT_MOVE)
            table_of_snake_point.append(last_snake_point[2])
            last_postion_y -= POINT_MOVE
            count_of_moves += 1
        else:
            sg.popup('You crashed into the wall!')
            break

    if last_fruit_point[0:2] == last_snake_point[0:2]:
        print("OK")
        # Removing last fruit point
        clear_point(last_fruit_point[2])
        # Regenerate fruit point
        last_fruit_point = draw_fruit_point()
    else:
        print("Bad!")
        # Removing last snake point
        clear_point(table_of_snake_point[0])
        table_of_snake_point.pop(0)

    print(table_of_snake_point)
window.close()

stop = time.time()
print("Time: ", stop-start)