#!/usr/bin/env python3
from yapsy.PluginManager import PluginManager
import cmd2
import os

import marinheiro

class MarinheiroCmdApp(cmd2.Cmd):
    def __init__(self):
        super().__init__()
        self.manager = PluginManager(
            plugin_info_ext="marinheiro-test",
            directories_list=[os.path.join(os.path.dirname(__file__), "tests")],
            categories_filter={
                "Web" : marinheiro.tests.WebTest,
            })
        self.manager.collectPlugins()

    @cmd2.options([cmd2.make_option("-c", "--category", action="store",
                                    help="Specify test category.")])
    def do_list(self, arg, opts=None):
        if opts.category:
            categories = self.manager.getPluginsOfCategory(opts.category)
        else:
            categories = self.manager.getAllPlugins()

        for plugin in categories:
            print("{}: {p.name}".format(self.colorize("Name", "bold"), p=plugin))
            print("{}: {p.description}".format(self.colorize("Description", "bold"), p=plugin))
            print()

    @cmd2.options([cmd2.make_option("-c", "--category", action="store",
                                    help="Specify test category.")])
    def do_run(self, arg, opts=None):
        if opts.category:
            categories = self.manager.getPluginsOfCategory(opts.category)
        else:
            categories = self.manager.getAllPlugins()

        for plugin in categories:
            print("{}: {p.name}".format(self.colorize("Name", "bold"), p=plugin))
            print("{}: {p.description}".format(self.colorize("Description", "bold"), p=plugin))
            try:
                output = plugin.plugin_object.run()
            except marinheiro.exceptions.FailedTest as err:
                status = self.colorize("FAILED", "red")
                output = err.msg
            else:
                status = self.colorize("PASSED", "green")
            finally:
                print("{}: {}".format(self.colorize("Status", "bold"), status))
                print("{}: {}".format(self.colorize("Output", "bold"), output))
                print()

def main():
    cmd = MarinheiroCmdApp()
    cmd.default_to_shell = True
    cmd.cmdloop()

if __name__ == "__main__":
    main()
