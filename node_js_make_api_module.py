import os
import sys
import sublime
import sublime_plugin


def make_index_file():
    index_file = open('index.js', 'w')
    index_file.write("var ValidationManager = require( './validation' );\n")
    index_file.write("var DataManager = require( './data' );\n")
    index_file.write("var OutputManager = require( './output' );\n")
    index_file.write("var utils = require( '../utils' );\n")
    index_file.close()


def make_validation_file():
    validation_file = open('validation.js', 'w')
    validation_file.write("var validator = require( 'validator' );\n")
    validation_file.write("var DataManager = require( './data' );\n")
    validation_file.write("var utils = require( '../utils' );\n")
    validation_file.close()


def make_data_file():
    data_file = open('data.js', 'w')
    data_file.write("var appModels = require( '../models' );\n")
    data_file.close()


def make_output_file():
    output_file = open('output.js', 'w')
    output_file.close()


class NodeJsMakeApiModuleCommand(sublime_plugin.WindowCommand):

    directory_list = []
    selected_directory = ""

    def build_directory_list(self):

        project_folder = self.window.folders()[0]

        def directories_to_exclude(directory_name):
            if directory_name.startswith(project_folder + '/.'):
                return False
            if directory_name.startswith(project_folder + '/node_modules'):
                return False
            return True

        self.directory_list = filter(directories_to_exclude, [x[0] for x in os.walk(project_folder)])

    def build_module(self, module_name):
        os.chdir(self.selected_directory)
        os.mkdir(module_name)
        os.chdir(module_name)
        make_validation_file()
        make_data_file()
        make_output_file()
        make_index_file()

    def set_folder(self, selection_index):
        if selection_index != -1:
            self.selected_directory = self.directory_list[selection_index]
            self.window.show_input_panel("Enter module name:", '', self.build_module, None, None)

    def run(self):
        self.build_directory_list()
        self.window.show_quick_panel(self.directory_list, self.set_folder)
