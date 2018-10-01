# -*- coding: utf-8 -*-

"""Bio2BEL miRBase manager."""

import logging
from typing import Dict, List, Mapping

from tqdm import tqdm

from bio2bel import AbstractManager
from bio2bel.manager.flask_manager import FlaskMixin
from bio2bel.manager.namespace_manager import BELNamespaceManagerMixin
from pybel.manager.models import Namespace, NamespaceEntry
from .constants import MODULE_NAME
from .download import download
from .models import Base, MatureSequence, Sequence, Species
from .parser import parse_mirbase

__all__ = [
    'Manager',
]

log = logging.getLogger(__name__)


class Manager(AbstractManager, BELNamespaceManagerMixin, FlaskMixin):
    """A manager for Bio2BEL miRBase."""

    _base = Base
    module_name = MODULE_NAME
    flask_admin_models = [Sequence, MatureSequence, Species]

    namespace_model = Sequence
    identifiers_recommended = 'miRBase'
    identifiers_pattern = 'MI\d{7}'
    identifiers_miriam = 'MIR:00000078'
    identifiers_namespace = 'mirbase'
    identifiers_url = 'http://identifiers.org/mirbase/'

    def count_sequences(self) -> int:
        """Count the sequences in the database."""
        return self._count_model(Sequence)

    def count_mature_sequences(self) -> int:
        """Count the mature sequences in the database."""
        return self._count_model(MatureSequence)

    def count_species(self) -> int:
        """Count the species in the database."""
        return self._count_model(Species)

    def summarize(self) -> Mapping[str, int]:
        """Summarize the contents of the database."""
        return dict(
            sequences=self.count_sequences(),
            mature_sequences=self.count_mature_sequences(),
            species=self.count_species()
        )

    def is_populated(self) -> bool:
        """Check if the database is populated."""
        return 0 < self.count_sequences()

    def populate(self, force_download: bool = False) -> None:
        """Populate the database."""
        path = download(force_download=force_download)
        mirbase_list = parse_mirbase(path)
        self._populate_list(mirbase_list)

    def _populate_list(self, mirbase_list: List[Dict]) -> None:
        mature_sequences = {}

        for entry in tqdm(mirbase_list, desc='models'):
            sequence = Sequence(
                mirbase_id=entry['identifier'],
                name=entry['name'],
                description=entry['description']
            )

            for product in entry.get('products', []):
                mirbase_mature_id = product['accession']

                mature_sequence = mature_sequences.get(mirbase_mature_id)
                if mature_sequence is None:
                    start, stop = map(int, product['location'].split('..'))

                    mature_sequences[mirbase_mature_id] = mature_sequence = MatureSequence(
                        name=product['product'],
                        mirbase_mature_id=mirbase_mature_id,
                        start=start,
                        stop=stop,
                    )

                sequence.mature_sequences.append(mature_sequence)

            self.session.add(sequence)
        self.session.commit()

    def _create_namespace_entry_from_model(self, model: Sequence, namespace: Namespace) -> NamespaceEntry:
        return NamespaceEntry(
            name=model.name,
            identifier=model.mirbase_id,
            encoding='GM',
            namespace=namespace,
        )

    @staticmethod
    def _get_identifier(model: Sequence) -> str:
        return model.mirbase_id
