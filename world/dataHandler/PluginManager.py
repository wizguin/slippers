import importlib
import json
import os


class PluginManager(object):
    """
    Loads plugins and allows them to interact with a world.
    """

    def __init__(self, handler):
        self.DIR = "plugins"
        self.FILE = "plugin.json"
        self.events = {}
        self.load_plugins(handler)
        # Listens for events, and calls get_event upon receiving one
        handler.obs.on("event", self.get_event)

    def load_plugins(self, handler):
        # Searches plugin directory for valid plugins
        for count, plugin in enumerate(os.listdir(self.DIR), 1):
            config_file = "{}/{}/{}".format(self.DIR, plugin, self.FILE)

            if os.path.isfile(config_file):
                file = open(config_file, "r")
                plugin_config = json.loads(file.read())

                # Imports the plugin dynamically using its string, and then creates an object of said plugin
                plugin_module = importlib.import_module("{}.{}.{}".format(self.DIR,
                                                                          plugin_config["name"].lower(),
                                                                          plugin_config["name"]))

                # Creates the plugin object
                plugin_object = getattr(plugin_module, plugin_config["name"])(handler.users,
                                                                              {"rooms": handler.rooms, "items": handler.items},
                                                                              handler.packet)

                # Loads plugin events
                self.load_events(plugin_object, plugin_config["events"])

        print("[PluginManager] {} plugins loaded".format(count))

    def load_events(self, plugin, events):
        """Loads plugin events into self.events."""
        for event in events:
            self.events[event] = getattr(plugin, events[event])

    def get_event(self, event, data, user):
        """Matches event type with its function reference."""
        try:
            self.events[event](data, user)
        except KeyError:
            print("[PluginManager] Event not handled: {} {}".format(event, data))
        except Exception as e:
            print("[PluginManager] Error handling event: {} {}\nError: {}".format(event, data, e))
