import sys

from code import view_cli, controller

def demo():
    current_session = controller.Controller(scenario = './data/scenario_test_recursed.json')
    view_cli.controller_summary(current_session)
    print('1 damaged 14')
    view_cli.string_parser(current_session, '1 damaged 14')
    print('next')
    view_cli.string_parser(current_session, 'next')
    print('2 damaged 3')
    view_cli.string_parser(current_session, '2 damaged 3')
    view_cli.flash_alerts(current_session)
    print('next')
    view_cli.string_parser(current_session, 'next')
    print('1 add_condition transformed 3')    
    view_cli.string_parser(current_session, '1 add_condition transformed 3')
    print('1 add_condition grappled')    
    view_cli.string_parser(current_session, '1 add_condition grappled')
    print('next')
    view_cli.string_parser(current_session, 'next')
    print('help')
    view_cli.string_parser(current_session, 'help')


def main(scenario_address):
    try:
        current_session = controller.Controller(scenario = scenario_address)
    except:
        print(scenario_address)    
        print(err)    
        print("couldn't find anything there")    

    view_cli.controller_summary(current_session)
    while True:
        cmd_str = input('command: ')
        try:
            view_cli.string_parser(current_session, cmd_str)
        except Exception as err:
            print(cmd_str, "Well dang, that broke something")
            print(err)    

        view_cli.flash_alerts(current_session)




if __name__ == '__main__':
    if len(sys.argv)==1:
        demo()
        exit()
    main(sys.argv[1])
    # print(sys.argv)
    