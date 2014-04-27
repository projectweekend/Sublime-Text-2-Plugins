import os
import sys

import sublime, sublime_plugin


class NodeMakeApiModuleCommand(sublime_plugin.WindowCommand):

    def display_module_name(self, module_name):
        sublime.message_dialog(module_name)

    def run(self):
        self.window.show_input_panel("Enter module name:", "", self.display_module_name, None, None)
