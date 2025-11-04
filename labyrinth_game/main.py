#!/usr/bin/env python3
from .constants import ROOMS
from .utils import describe_current_room, solve_puzzle, attempt_open_treasure, show_help
from .player_actions import show_inventory, get_input, move_player, take_item, use_item

def main():
    """main function with message"""
    print("Добро пожаловать в лабиринт сокровищ!!")
    describe_current_room(game_state)

    def process_command(game_state_in, command):
        command=command.split()
        match command[0]:
            case 'help':
                show_help()
            case 'look':
                describe_current_room(game_state)
            case 'use':
                use_item(game_state, command[1])
            case 'go':
                move_player(game_state, command[1])
            case 'take':
                take_item(game_state, command[1])
            case 'inventory':
                show_inventory(game_state)
            case 'solve':
                solve_puzzle(game_state)
            case 'quit':
                print('Игра окончена')
                game_state['game_over']=True
            case _:
                print('Неизвестная команда. Попробуйте снова, для получения списка команд введите help')
                

    while game_state['game_over']!=True:
        process_command(game_state, get_input())        
    
if __name__=="__main__":
    main()
    
game_state={
    'player_inventory':[],
    'current_room':'entrance',
    'game_over':False,
    'steps_taken':0
}

main()