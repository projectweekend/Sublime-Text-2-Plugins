import os


class PersonalAssistantTask(object):

    directory_list = []
    selected_directory = ""

    def __init__(self, sublime_api):
        self._api = sublime_api
        self.build_directory_list()
        self._api.window.show_quick_panel(self.directory_list, self.set_folder)

    def build_directory_list(self):
        project_folder = self._api.window.folders()[0]
        def directories_to_exclude(directory_name):
            if directory_name.startswith(project_folder + '/.'):
                return False
            if directory_name.startswith(project_folder + '/node_modules'):
                return False
            return True
        self.directory_list = filter(directories_to_exclude, [x[0] for x in os.walk(project_folder)])

    def make_index_file(self):
        index_file = open('index.js', 'w')
        index_file.write("var async = require( 'async' );\n");
        index_file.write("var ValidationManager = require( './validation' );\n")
        index_file.write("var DataManager = require( './data' );\n")
        index_file.write("var OutputManager = require( './output' );\n")
        index_file.write("var utils = require( '../utils' );\n")
        index_file.close()

    def make_validation_file(self):
        validation_file = open('validation.js', 'w')
        validation_file.write("var validator = require( 'validator' );\n")
        validation_file.write("var DataManager = require( './data' );\n")
        validation_file.write("var utils = require( '../utils' );\n")
        validation_file.write("var validationError = require( '../utils' ).validationError;\n")
        validation_file.close()

    def make_data_file(self):
        data_file = open('data.js', 'w')
        data_file.write("var appModels = require( '../models' );\n")
        data_file.write("var systemError = require( '../utils' ).systemError;\n")
        data_file.close()

    def make_output_file(self):
        output_file = open('output.js', 'w')
        output_file.close()

    def set_folder(self, selection_index):
        if selection_index != -1:
            self.selected_directory = self.directory_list[selection_index]
            self._api.window.show_input_panel("Enter module name:", '', self.build_module, None, None)

    def build_module(self, module_name):
        os.chdir(self.selected_directory)
        os.mkdir(module_name)
        os.chdir(module_name)
        self.make_validation_file()
        self.make_data_file()
        self.make_output_file()
        self.make_index_file()
