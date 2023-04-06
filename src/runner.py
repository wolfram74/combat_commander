from code import view_cli, controller

def main():
    current_session = controller.Controller(scenario = './data/scenario_test_ordered.json')
    view_cli.controller_summary(current_session)

if __name__ == '__main__':
    main()
    