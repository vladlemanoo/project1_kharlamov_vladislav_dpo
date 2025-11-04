from .constants import ROOMS
import math

def describe_current_room(game_state_in):
    print(game_state_in['current_room'].upper())
    print(f'Описание комнаты - {ROOMS[game_state_in['current_room']]['description']}')
    print(f'Заметные предметы: {' '.join(ROOMS[game_state_in['current_room']]['items'])}')
    print(f'Выходы: {ROOMS[game_state_in['current_room']]['exits']}')
    if ROOMS[game_state_in['current_room']]['puzzle']!=None: 
        print("Кажется, здесь есть загадка (используйте команду solve)")

def solve_puzzle(game_state_in):
    if ROOMS[game_state_in['current_room']]['puzzle']==None:
        print('Загадок здесь нет.')
    elif game_state_in['current_room']=='treasure_room':
        attempt_open_treasure(game_state_in)
    else:
        print(ROOMS[game_state_in['current_room']]['puzzle'][0])
        if (input()==ROOMS[game_state_in['current_room']]['puzzle'][1]):
            print('Ответ правильный, вам выдана награда')
            ROOMS[game_state_in['current_room']]['puzzle']=None
            if len(ROOMS[game_state_in['current_room']]['items'])!=0:
                game_state_in['player_inventory'].extend(ROOMS[game_state_in['current_room']]['items'])
                ROOMS[game_state_in['current_room']]['items']=[]
        else:
            if game_state_in['current_room']=='trap_room':
                trigger_trap(game_state_in)
            if game_state_in['game_over']!=True:
                print('Неверно. Попробуйте снова.')
                solve_puzzle(game_state_in)

def attempt_open_treasure(game_state_in):
    if 'treasure_key' in game_state_in['player_inventory']:
        print('Вы применяете ключ, и замок щелкает. Сундук открыт!')
        ROOMS[game_state_in['current_room']]['items'].remove('treasure_chest')
        print('В сундуке сокровище! Вы победили!')
        game_state_in['game_over']=True
        game_state_in['player_inventory']=[]
        game_state_in['current_room']='entrance'
        game_state_in['steps_taken']=0
    else:
        if input('Сундук заперт... Ввести код ? (да/нет)')=="да":
            if input() in (ROOMS[game_state_in['current_room']]['puzzle'][1], 'десять'):
                print('Сундук открыт!')
                ROOMS[game_state_in['current_room']]['items'].remove('treasure_chest')
                print('В сундуке сокровище! Вы победили!')
                game_state_in['game_over']=True
                game_state_in['player_inventory']=[]
                game_state_in['current_room']='entrance'
                game_state_in['steps_taken']=0
            else:
                print('Ошибка')
        else: print('Вы отступаете от сундука')

def show_help(COMMANDS_IN):
    for k,v in COMMANDS_IN.items():
        print(f'{k:<16} {v}')


def pseudo_random(seed, modulo):
    value=math.sin(seed * 12.9898)*43758.5453
    value-=math.floor(value)
    return int(value*modulo)

def trigger_trap(game_state_in):
    print('Ловушка активирована')
    if len(game_state_in['player_inventory'])!=0:
        rand=pseudo_random(game_state_in['steps_taken'], len(game_state_in['player_inventory']))
        print(f'Предмет {game_state_in['player_inventory'][rand]} удален из вашего инвентаря')
        game_state_in['player_inventory'].pop(rand)
    else:
        rand=pseudo_random(1, 9)
        if rand<3:
            print('Поражение')
            game_state_in['game_over']=True
        else: print("Вы уцелели")

def random_event(game_state_in):
    randVal=pseudo_random(-5, 10)
    if randVal<=5:
        randVal=pseudo_random(1,4)
        if randVal==1:
            print('Находка! Вы видите на полу монетку, возьмите её:)')
            ROOMS[game_state_in['current_room']]['items'].append('coin')
        elif randVal==2:
            print('Вы слышите шорох...')
            if 'sword' in game_state_in['player_inventory']:
                print('Вам удалось отпугнуть существо')
        else:
            if game_state_in['current_room']=='trap_room' and 'torch' not in game_state_in['player_inventory']:
                print('Ловушка.... Опасность....')
                trigger_trap(game_state_in)
