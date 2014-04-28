import sublime
import sublime_plugin
import tasks


class PersonalAssistantCommand(sublime_plugin.WindowCommand):

    def process_command(self, command_text):
        attr_name = '_'.join(command_text.split())
        tasks.__getattribute__(attr_name).PersonalAssistantTask(self)

    def run(self):
        self.window.show_input_panel("Enter command:", '', self.process_command, None, None)
