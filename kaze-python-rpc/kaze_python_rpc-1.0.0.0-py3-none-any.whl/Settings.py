"""

Sets up your RPC endpoints


"""


class SettingsHolder:
    """
    This class holds all the settings. Needs to be setup with one of the
    `setup` methods before using it.
    """
    RPC_LIST = None

    # Setup methods
    def setup(self, addr_list):
        """ Load settings from a JSON config file """
        self.RPC_LIST = addr_list

    def setup_mainnet(self):
        """ Load settings from the mainnet JSON config file """
        self.setup(
            [
                "http://node1.kaze.solutions:22886",
                "http://node2.kaze.solutions:22886",
                "http://node3.kaze.solutions:22886",
                "http://node4.kaze.solutions:22886"
            ]
        )

    def setup_testnet(self):
        self.setup(
            [
                "http://node1.kaze.solutions:44886",
                "http://node2.kaze.solutions:44886",
                "http://node3.kaze.solutions:44886",
                "http://node4.kaze.solutions:44886"
            ]
        )

    def setup_privnet(self):
        """ Load settings from the privnet JSON config file """
        self.setup(
            [
                "http://127.0.0.1:30333"
            ]
        )


# Settings instance used by external modules
settings = SettingsHolder()

# Load testnet settings as default
settings.setup_testnet()
