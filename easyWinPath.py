import sublime
import sublime_plugin
import subprocess
import os

print("EasyWinPath plugin loaded")


class OpenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                # s = s.replace('\\\\', "\\")
                # self.view.replace(region, s)
                print("Will open {0}".format(s))
                os.startfile(s)
            if region.empty():
                print("Region is empty")


class EscapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                s = self.view.substr(region)
                if (s.startswith(r'\\\\') or ((not s.startswith(r'\\\\')) and (r'\\' in s) and (not s.startswith(r'\\')))):
                    s = s.replace('\\\\', "\\")
                else:
                    s = s.replace('\\', "\\\\")
                self.view.replace(edit, region, s)
            if region.empty():
                print("Region is empty")
