import time
import sys
import os
##
from code import controller, models

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def controller_summary(controller):
    # always show: ID, name, max/current health
    # "{}"
    print("====="*6)
    header_line = '   ID | name                    | health | Round %d' % controller.round_number
    print(header_line)
    for tranche_id in controller.agents_by_order.keys():
        tranche = controller.agents_by_order[tranche_id]
        # for agent_id in tranche:

        for agent in tranche:
            # agent = controller.agents_by_id[agent_id]
            print(agent)
    print("====="*6)
    # print("=====\nfarts\n=====")
    return 

def flash_alerts(controller):
    if len(controller.alerts) == 0:
        return
    print("*****"*6)
    for alert in controller.alerts:
        print(alert)
    print("*****"*6)
    controller.alerts = []

def string_parser(controller, cmd_string):
    split_string = cmd_string.split(' ')
    if split_string[0]=='next':
        controller.turn_end()
        controller_summary(controller)
        return
    if split_string[0] in ('summary', 'ls'):
        controller_summary(controller)
        return
    if split_string[0] in ('cls', 'clear'):
        clear()
        return
    if split_string[0]=='exit':
        exit()
        return
    if len(split_string) == 1:
        return
    if split_string[1] == 'damaged':
        controller.damaged(
            int(split_string[0]),
            int(split_string[2])
            )
        return
    if split_string[1] == 'healed':
        controller.damaged(
            int(split_string[0]),
            -int(split_string[2])
            )
        return
    if split_string[1] == 'add_condition':
        subject_id = int(split_string[0])
        duration = None
        if len(split_string) == 4:
            duration = int(split_string[3])
        condition = models.Condition(split_string[2], duration)
        controller.add_condition(
            subject_id,
            condition
            )
        return
    print(cmd_string, "didn't trigger any command flags")

def main():
    tally = 0
    # while True:
    #     sys.stdout.write("\rDoing thing {time:=4d}".format(time=tally))
    #     sys.stdout.flush()
    #     time.sleep(1)
    #     tally += 1
    print('what the fuck is main being run for?')
    stdscr = curses.initscr()
    # loaded_scenario2 = Controller(scenario = test_scenario2)


if __name__ == '__main__':
    main()

