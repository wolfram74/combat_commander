import time
import sys
import os
##
from code import controller, models

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def controller_summary(controller):
    # always show: ID, name, max/current health
    print("====="*6)
    header_line = '   ID | name                    | health | Round %d' % controller.round_number
    print(header_line)
    for tranche in controller.agents_by_order:
        for agent in tranche:
            print(agent)
    print("====="*6)
    return 

def flash_alerts(controller):
    if len(controller.alerts) == 0:
        return
    print("*****"*6)
    for alert in controller.alerts:
        print(alert)
    print("*****"*6)
    controller.alerts = []

#valid commands
def view_next(controller, args):
    controller.turn_end()
    controller_summary(controller)

def view_summary(controller, args):
    controller_summary(controller)

def view_clear(controller, args):
    clear()

def view_exit(controller, args):
    exit()
    return

def view_help(controller, args):
    print('valid commands are:')
    print(', '.join(cmd_list.keys()))

def view_damage(controller, args):
    controller.damaged(int(args[0]), int(args[2]))

def view_heal(controller, args):
    controller.damaged(int(args[0]), -int(args[2]))

def view_add_condition(controller, args):
    agent_id = int(args[0])
    duration = None
    if len(args) == 4:
        duration = int(args[3])
    condition = models.Condition(args[2], duration)
    controller.add_condition(agent_id, condition)

def view_remove_condition(controller, args):
    agent_id = int(args[0])
    controller.remove_condition(agent_id, args[-1])


def view_set_order(controller, args):
    ordering = []
    for item in args[1:]:
        # print(item)
        if ',' in item:
            ids = [int(el) for el in item.split(',')]
            ordering.append(ids)
            continue
        ordering.append(int(item))
    controller.set_new_order(ordering)

cmd_list = {
    'next': view_next,
    'summary': view_summary,
    'ls': view_summary,
    'clear': view_clear,
    'cls': view_clear,
    'exit': view_exit,
    'help': view_help,
    'end_session': view_exit,
    'damaged': view_damage,
    'healed': view_heal,
    'add_condition': view_add_condition,
    'remove_condition': view_remove_condition,
    'set_order': view_set_order,
}

def string_parser(controller, cmd_string):
    split_string = cmd_string.split(' ')

    if split_string[0] in cmd_list:
        cmd_list[split_string[0]](controller, split_string)
        return

    if len(split_string) != 1:
        if split_string[1] in cmd_list:
            cmd_list[split_string[1]](controller, split_string)
            return

    print(cmd_string, "didn't trigger any command flags")

def main():
    tally = 0


if __name__ == '__main__':
    main()

