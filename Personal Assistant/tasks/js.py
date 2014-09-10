import os

import sublime_plugin


SCRATCH_FILE = '/Users/brian/Desktop/scratch_js/scratch.js'


class PersonalAssistantTask(object):

    def __init__(self, sublime_api):
        self._api = sublime_api
        view = self._api.window.open_file(SCRATCH_FILE)
        self._api.window.focus_view(view)
