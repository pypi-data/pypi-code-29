# -*- coding: utf-8 -*-

"""SQLAlchemy database models."""

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import backref, relationship

from .constants import MODULE_NAME

__all__ = [
    'Sequence',
    'MatureSequence',
    'Species',
    'Base',
]

Base: DeclarativeMeta = declarative_base()

DESCRIPTOR_TABLE_NAME = f'{MODULE_NAME}_mirna'
SPECIES_TABLE_NAME = f'{MODULE_NAME}_species'
MATURE_TABLE_NAME = f'{MODULE_NAME}_mature'


class Species(Base):
    """Represents a taxonomy."""

    __tablename__ = SPECIES_TABLE_NAME

    id = Column(Integer, primary_key=True)

    code = Column(String(16), unique=True, index=True, doc='Three letter species code')


class Sequence(Base):
    """Represents an miRBase sequence.

    See https://www.ebi.ac.uk/miriam/main/datatypes/MIR:00000078
    """

    __tablename__ = DESCRIPTOR_TABLE_NAME

    id = Column(Integer, primary_key=True)

    mirbase_id = Column(String(255), nullable=False, unique=True, index=True,
                        doc='miRBase sequence matching ``MI\d{7}``')

    name = Column(String(255), nullable=False, unique=True, index=True)
    description = Column(Text, nullable=False)

    species_id = Column(ForeignKey(f'{SPECIES_TABLE_NAME}.id'))
    species = relationship(Species)

    def __repr__(self):  # noqa: D105
        return str(self.mirbase_id)


class MatureSequence(Base):
    """Represents a miRBase mature sequence.

    See: https://www.ebi.ac.uk/miriam/main/datatypes/MIR:00000235

    Regular Expression:
    """

    __tablename__ = MATURE_TABLE_NAME

    id = Column(Integer, primary_key=True)

    mirbase_mature_id = Column(String(255), nullable=False, unique=True, index=True,
                               doc='miRBase mature sequence matching ``MIMAT\d{7}``')

    name = Column(String(255), nullable=False, index=True)

    start = Column(Integer)
    stop = Column(Integer)

    sequence_id = Column(ForeignKey(f'{DESCRIPTOR_TABLE_NAME}.id'))
    sequence = relationship(Sequence, backref=backref('mature_sequences'))
