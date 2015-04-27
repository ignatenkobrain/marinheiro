#!/usr/bin/env python3
from yapsy.PluginManager import PluginManager
from blessings import Terminal
import argparse
import os

import marinheiro

def main():
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces([os.path.join(os.path.dirname(__file__), "tests")])
    manager.setCategoriesFilter({
        "Web" : marinheiro.tests.WebTest,
    })
    manager.collectPlugins()

    term = Terminal()

    parser = argparse.ArgumentParser(prog="marinheiro")
    parser.add_argument("-c", metavar="CAT", dest="cat",
                        choices=manager.getCategories(),
                        help="""
                             Specify test category to run.
                             Available: {}.
                             Without we will run tests in all categories.
                             """.format(", ".join(manager.getCategories())))
    args = parser.parse_args()
    if not args.cat:
        categories = manager.getAllPlugins()
    else:
        categories = manager.getPluginsOfCategory(args.cat)

    for plugin in categories:
        try:
            output = plugin.plugin_object.run()
        except marinheiro.exceptions.FailedTest as err:
            status = "{t.red}FAILED{t.normal}".format(t=term)
            output = err.msg
        else:
            status = "{t.green}PASSED{t.normal}".format(t=term)
        finally:
            print("{t.bold}Name{t.normal}: {}".format(plugin.name, t=term))
            print("{t.bold}Description{t.normal}: {}".format(plugin.description, t=term))
            print("{t.bold}Status{t.normal}: {}".format(status, t=term))
            print("{t.bold}Output{t.normal}: {}".format(output, t=term))
            print()

if __name__ == "__main__":
    main()
