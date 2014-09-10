from config import JS_SCRATCH_FILE


class PersonalAssistantTask(object):

    def __init__(self, sublime_api):
        self._api = sublime_api
        view = self._api.window.open_file(JS_SCRATCH_FILE)
        self._api.window.focus_view(view)
