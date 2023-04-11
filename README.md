# combat_commander
command line tool to offload some of the book keeping efforts for table top rpg GMs

instructions:
while in the "src" directory, run the command

`python3 runner.py SCENARIO_ADDRESS`

an example scenario can be run with `python3 runner.py ./data/demo.json`

This will start a session populated with agents featuring at least unique IDs and show the summary of the beginning.

valid commands are 
- `next` to advance to the next agents turn.
- `summary` or `ls` will display the current scenario status `>>` indicates agents whose turn it currently is.
- `clear` or `cls` clears the screen of content
- `help` lists valid commands
- `ID damaged AMOUNT` to deal some amount of damage to a given agent
- `ID healed AMOUNT` to heal some amount of damage to a given agent
- `ID add_condition NAME DURATION` to apply a condition to a given agent with an optional duration, conditions with durations will be automatically removed from agents when the duration reaches 0 and an alert will flash.
- `ID remove_condition NAME` to remove a condition from a given agent.
- `set_order LIST_OF_IDS` the list of ids will interpert space separated IDs as having their own turn, while comma separated IDs will have a shared turn. Unspecified IDs will be placed last.
- `exit` ends current session
- `exit` or `end_session` ends current session


The scenarios are stored as JSON files for ease of editability and loading. If needed, a variety of JSON editors online exist that will [check syntax](http://json.parser.online.fr/). To build a scenario from other scenario files, list them in the `files` field, giving their address relative to the file it's being loaded from. For example:

`
data/
    main_scenario.json
    sub_scenario.json
`
to load `sub_scenario.json` from `main_scenario.json` you would have the field  `"files":["./sub_scenario.json"]` in `main_scenario.json`


