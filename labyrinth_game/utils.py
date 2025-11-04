from .constants import ROOMS
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
            if input()==ROOMS[game_state_in['current_room']]['puzzle'][1]:
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

def show_help():
    print('Доступные команды: ')
    print('go direction - (north,south,east,west)')
    print('look - осмотреть комнату')
    print('take item - взять предмет')
    print('use item - использовать предмет из инвентаря')
    print('inventory - показать инвентарь')
    print('solve - попытаться решить загадку в комнате')
    print('quit - выйти из игры')
    print('help - показать это сообщение9')