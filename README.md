# combat_commander
command line tool to offload some of the book keeping efforts for table top rpg GMs

instructions:
while in the "src" directory, run the command

`python3 runner.py SCENARIO_ADDRESS`

an example scenario can be run with `python3 runner.py ./data/demo.json`

This will start a session populated with agents featuring at least unique IDs and show the summary of the beginning.

valid commands are 
-`next` to advance to the next agents turn.
-`id damaged amount` to deal some amount of damage to a given agent
-`id add_condition name (duration)` to apply a condition to a given agent with an optional duration, conditions with durations will be automatically removed from agents when the duration reaches 0.
<!-- -`order list_of_ids` the list of ids should be space separated to be given unique turns, or comma separated to give shared turns. Unspecified ids will be placed last. -->

The scenarios are stored as JSON files for ease of editability and loading. If needed, a variety of JSON editors online exist that will [check syntax](http://json.parser.online.fr/)

