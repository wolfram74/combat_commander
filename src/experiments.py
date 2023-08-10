from code import view_cli, controller


def bug_replication1():
    current_session = controller.Controller(scenario = './data/scenario_test_recursed.json')
    view_cli.string_parser(current_session, "ls")
    view_cli.string_parser(current_session,"set_order 4 3 5 2 1")
    view_cli.string_parser(current_session, "ls")
    view_cli.string_parser(current_session,"5 add_condition concentration")
    view_cli.string_parser(current_session, "ls")


def main():
    bug_replication1()

if __name__ == '__main__':
    main()