from .constants import ROOMS
from .utils import *
def show_inventory(game_state_in):
    if len(game_state_in['player_inventory'])==0:
        print('Инвентарь пуст')
    else:
        print(type(game_state_in['player_inventory']), game_state_in['player_inventory'])
        print(f'В инвентаре есть: - {', '.join(game_state_in['player_inventory'])}')

def get_input(prompt="> "):
    try:
        command=input(prompt)
        return command
    except (KeyBoardInterrupt, EOFError):
        print('\nВыход из игры')
        return "quit"

def move_player(game_state_in, direction):
    if ROOMS[game_state_in['current_room']]['exits'].get(direction):
        if ROOMS[game_state_in['current_room']]['exits'].get(direction)=='treasure_room':
            if 'rusty_key' in game_state_in['player_inventory']:
                print('Вы используете найденный ключ чтобы открыть путь в комнату сокровищ')
                game_state_in['current_room']=ROOMS[game_state_in['current_room']]['exits'].get(direction)
                game_state_in['steps_taken']+=1
                describe_current_room(game_state_in)
                random_event(game_state_in)
            else: print('Дверь заперта. Чтобы пройти дальше нужен ключ')
        else: 
            game_state_in['current_room']=ROOMS[game_state_in['current_room']]['exits'].get(direction)
            game_state_in['steps_taken']+=1
            describe_current_room(game_state_in)
            random_event(game_state_in)
    else: 
        print("Нельзя пойти в этом направлении")

def take_item(game_state_in, item_name):
    if item_name=='treasure_chest':
        print('Вы не можете взять сундук, он слишком тяжелый')
    elif item_name in ROOMS[game_state_in['current_room']]['items'] and item_name not in game_state_in['player_inventory']:
        game_state_in['player_inventory'].append(item_name)
        ROOMS[game_state_in['current_room']]['items'].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else: print("Такого предмета здесь нет")

def use_item(game_state_in, item_name):
    if item_name in game_state_in['player_inventory']:
        match item_name:
            case 'torch':
                print('Стало светлее')
            case 'sword':
                print('Стало уверенее')
            case 'bronze_box':
                if 'rusty_key' not in game_state_in['player_inventory']:
                    print('Открыта шкатулка')
                    game_state_in['player_inventory'].append('rusty_key')
            case _:
                print('Неясно как использовать этот предмет')
    else: print('У вас нет такого предмета')