Sublime-Text-2-Plugins
======================


### Personal Assistant Plugin

This is a task launcher for other custom plugins. The key combination `ctrl+shift+a` opens a text command box. The available commands correspond to **tasks** which are saved in the plugin's `/tasks` folder. Each of these task files is a Python file defining some sort of custom action in a class named: `PersonalAssistantTask`.

The `PersonalAssistantTask` object takes one input on `init`. The Sublime Text Plugin API will be passed in from the command launcher process so that it is accessible for crafting the functionality in the `PersonalAssistantTask`.

Naming of each Python file in the `/tasks` folder determines the text comand used to launch the task in the command box referenced above. For example a task file named `open_projects.py` would be launched with the command: `open projects`.
