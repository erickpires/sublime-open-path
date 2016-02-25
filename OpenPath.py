import sublime, sublime_plugin, os
from subprocess import call

def open_path(folder, where) :
    settings = sublime.load_settings("OpenPath.sublime-settings")
    if where == "file_manager" :
        command = settings.get("file_manager", "explorer /e /root,\"{0}\"")
    else :
        command = settings.get("terminal", "notify-send \"Open Path\" \"{0}\"")

    command = command.format(folder)
    call(command, shell=True)

class OpenPath(sublime_plugin.WindowCommand):
  def run(self, path):
    open_path(path)

class OpenFolder(sublime_plugin.WindowCommand):
    def run(self, **args):
        path = None
        if args["folder"] == "project" :
            if len(self.window.folders()) == 0:
                return
            path = self.window.folders()[0]
        else :
            if self.window.active_view() is None:
                return
            path = os.path.dirname(self.window.active_view().file_name())

        open_path(path, args["where"])
