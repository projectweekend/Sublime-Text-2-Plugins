import os
import subprocess
import sublime


class PersonalAssistantTask(object):

    def __init__(self, sublime_api):
        self._api = sublime_api
        self._api.window.show_input_panel("Enter directory name:", '', self.build_seed, None, None)

    def build_seed(self, folder_name):
        os.chdir('/Users/brian/dev')
        try:
            os.chdir(folder_name)
        except:
            message = "Directory '{0}' does not exist in '/Users/brian/dev'".format(folder_name)
            sublime.error_message(message)
        else:
            subprocess.call(['git', 'clone', 'https://github.com/projectweekend/Node-Backend-Seed.git', '.'])
