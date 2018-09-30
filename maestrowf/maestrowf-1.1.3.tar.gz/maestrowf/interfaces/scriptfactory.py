from importlib import import_module
import logging

LOGGER = logging.getLogger(__name__)
MAESTRO_INTERFACES = "maestrowf.interfaces.script"


class ScriptAdapterFactory(object):
    """A factory class for retrieve different types of ScriptAdapters."""

    _classes = {
        "slurm":           (".slurmscriptadapter", "SlurmScriptAdapter"),
        "local":           (".localscriptadapter", "LocalScriptAdapter"),
        "flux-spectrum":   (".fluxscriptadapter", "SpectrumFluxScriptAdapter"),
    }

    @classmethod
    def get_adapter(cls, adapter_id):
        """
        Look up and retrieve a ScripttAdapter by name.

        :param adapter_id: Name of the ScriptAdapter to find.
        :returns: A ScriptAdapter class matching the specifed adapter_id.
        """
        if adapter_id.lower() not in cls._classes:
            msg = "Adapter '{0}' not found. Specify an adapter that exists " \
                  "or implement a new one mapping to the '{0}'" \
                  .format(str(adapter_id))
            LOGGER.error(msg)
            raise Exception(msg)

        module = cls._classes[adapter_id]
        return getattr(
            import_module("{}{}".format(MAESTRO_INTERFACES, module[0])),
            module[1])

    @classmethod
    def get_valid_adapters(cls):
        """
        Get all valid ScriptAdapter names.

        :returns: A list of all available keys in the ScriptAdapterFactory.
        """
        return cls._classes.keys()
