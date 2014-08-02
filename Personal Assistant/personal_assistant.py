import sublime
import sublime_plugin
import tasks


class PersonalAssistantCommand(sublime_plugin.WindowCommand):

    def process_command(self, command_text):
        parts = command_text.split()
        if len(parts) == 1:
            attr_name = parts[0]
        else:
            attr_name = '_'.join(parts)
        tasks.__getattribute__(attr_name).PersonalAssistantTask(self)

    def run(self):
        self.window.show_input_panel("Enter command:", '', self.process_command, None, None)
