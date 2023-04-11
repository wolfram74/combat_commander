import sys

from code import view_cli, controller

def demo():
    current_session = controller.Controller(scenario = './data/demo.json')
    view_cli.controller_summary(current_session)
    # input()
    print('1 damaged 14')
    view_cli.string_parser(current_session, '1 damaged 14')
    # input()
    print('next')
    view_cli.string_parser(current_session, 'next')
    # input()
    print('2 damaged 3')
    view_cli.string_parser(current_session, '2 damaged 3')
    view_cli.flash_alerts(current_session)
    # input()
    print('next')
    view_cli.string_parser(current_session, 'next')
    # input()
    print('1 add_condition transformed 3')    
    view_cli.string_parser(current_session, '1 add_condition transformed 3')
    # input()
    print('1 add_condition grappled')    
    view_cli.string_parser(current_session, '1 add_condition grappled')
    # input()
    print('next')
    view_cli.string_parser(current_session, 'next')
    print('set_order 1 3 2')
    print('ID order_position NEW_POSITION')
    print('help')
    view_cli.string_parser(current_session, 'help')


def main(scenario_address):
    try:
        current_session = controller.Controller(scenario = scenario_address)
    except:
        print(scenario_address)    
        print("couldn't find anything there")    

    view_cli.controller_summary(current_session)
    while True:
        cmd_str = input('command: ')
        try:
            view_cli.string_parser(current_session, cmd_str)
        except:
            print(cmd_str, "Well dang, that broke something")
        view_cli.flash_alerts(current_session)




if __name__ == '__main__':
    if len(sys.argv)==1:
        demo()
        exit()
    main(sys.argv[1])
    # print(sys.argv)
    