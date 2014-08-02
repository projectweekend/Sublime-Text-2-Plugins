import os

import sublime_plugin


class PersonalAssistantTask(object):

    def __init__(self, sublime_api):
        self._api = sublime_api
        self._api.window.run_command("prompt_select_project")
