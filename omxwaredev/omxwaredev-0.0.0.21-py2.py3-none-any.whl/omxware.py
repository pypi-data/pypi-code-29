# -*- coding: utf-8 -*-
"""
OMXWare Services Package
"""
import simplejson as json
import sys
from omxware.AESCipher import AESCipher
from omxware.Utils import rand
from omxware.Config import Configuration
from omxware.Connect import Connection

from omxware.Genus import Genus
from omxware.Genome import Genome
from omxware.Gene import Gene
from omxware.Protein import Protein

token = ''

"""
Verify the credentials and get a User Token

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""
def getToken(username, password):
    if username is None:
        sys.exit("Username cannot be empty!");

    if password is None:
        sys.exit("Password cannot be empty!");

    # Verify username and password

    cipher = AESCipher()
    omxware_token = cipher.encrypt(rand()+"::::"+username+"::::"+password)

    return omxware_token

class omxware:
    connection: Connection
    config: Configuration

    def __init__(self, omxware_token, omx_server='https://omxware.sl.cloud9.ibm.com:9421'):
        self.config = Configuration(omxware_token, server_url=omx_server);
        self.initOMXConnection()

    def initOMXConnection(self):
        self.connection = Connection(self.config)

    # GENUS #

    def all_genera(self):
        """Return all the Genera
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}

        methodurl = "/genus/all"

        params = {'fromCache': 'true'}

        genusResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)

        if genusResp is not None:
            genusRepJ = genusResp.json()
            if len(genusRepJ["result"]) <= 0:
                return None
            else:

                genusJ = genusRepJ["result"]
                genera = []
                for genus in genusJ:
                    genera.append((Genus(self.connection, genus)))

                return genera
        else:
            return None

            # GENOMES #

    def genome(self, accession_number):
        """Return the meta data about a genome with a given genome accession_number

            Arguments:
              accession_number -- genome accession number
        """

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}

        genomemethodurl = "/api/public/genomes/id:" + str(accession_number)
        params = json.dumps({"fromCache": "true"})

        genomeResp = self.connection.get(methodurl=genomemethodurl, headers=headers, payload=params)
        if genomeResp is not None:
            genomeRepJ = genomeResp.json()
            if len(genomeRepJ["result"]) <= 0:
                return None
            else:
                genomeJ = genomeRepJ["result"][0]
                return (Genome(self.connection, genomeJ))
        else:
            return None

    def genomes_by_genus(self, genus_name):
        """Return all the Genomes encoding a Genus - by genus name

            Arguments:
              genus_name -- Genus name
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/name:" + str(genus_name)
        params = {'fromCache': 'true'}
        genomeResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genomeResp is not None:
            genomeRepJ = genomeResp.json()
            if len(genomeRepJ["result"]) <= 0:
                return None
            else:

                genomesJ = genomeRepJ["result"]
                genomes = []
                for genome in genomesJ:
                    genomes.append((Genome(self.connection, genome)))

                return genomes
        else:
            return None

    def genes_by_genome(self, accession_number):
        """Return all the genes encoding a genome - by genome accession_number

            Arguments:
              accession_number -- genome accession number
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/id:" + str(accession_number) + "/all/genes"
        params = {'fromCache': 'true'}
        genesResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genesResp is not None:
            genesRespJ = genesResp.json()
            if len(genesRespJ["result"]) <= 0:
                return None
            else:

                genesJ = genesRespJ["result"]
                genes = []
                for gene in genesJ:
                    genes.append((Gene(self.connection, gene)))

                return genes
        else:
            return None

    def resistant_genes_by_genome(self, accession_number):
        """Return all the resistant genes encoding a genome - by genome accession_number

            Arguments:
              accession_number -- genome accession number
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/id:" + str(accession_number) + "/all/genes:resistant"
        params = {'fromCache': 'true'}
        genesResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genesResp is not None:
            genesRespJ = genesResp.json()
            if len(genesRespJ["result"]) <= 0:
                return None
            else:

                genesJ = genesRespJ["result"]
                genes = []
                for gene in genesJ:
                    genes.append((Gene(self.connection, gene)))

                return genes
        else:
            return None

    def genera_with_resistant_genes_by_genome(self, accession_number):
        """Return all the Genera containing the resistant genes encoding a genome - by genome accession_number

            Arguments:
              accession_number -- genome accession number
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/id:" + str(accession_number) + "/all/genes:resistant/genera"
        params = {'fromCache': 'true'}
        generaResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if generaResp is not None:
            generaRespJ = generaResp.json()
            if len(generaRespJ["result"]) <= 0:
                return None
            else:

                generaJ = generaRespJ["result"]
                genera = []
                for genus in generaJ:
                    genera.append((Genus(self.connection, genus)))

                return genera
        else:
            return None

    def genomes_with_resistant_genes_by_genome(self, accession_number):
        """Return all the Genomes containing the resistant genes encoding a genome - by genome accession_number

            Arguments:
              accession_number -- genome accession number
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/id:" + str(accession_number) + "/all/genes:resistant/genomes"
        params = {'fromCache': 'true'}
        genomesResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genomesResp is not None:
            genomesRespJ = genomesResp.json()
            if len(genomesRespJ["result"]) <= 0:
                return None
            else:

                genomesJ = genomesRespJ["result"]
                genomes = []
                for genome in genomesJ:
                    genomes.append((Genus(self.connection, genome)))

                return genomes
        else:
            return None

    def proteins_by_genome(self, accession_number):
        """Return all the proteins encoding a genome - by genome accession_number

            Arguments:
              accession_number -- genome accession number
        """
        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genomes/id:" + str(accession_number) + "/all/proteins"
        params = {'fromCache': 'true'}
        proteinsResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if proteinsResp is not None:
            proteinsRespJ = proteinsResp.json()
            if len(proteinsRespJ["result"]) <= 0:
                return None
            else:

                proteinsJ = proteinsRespJ["result"]
                proteins = []
                for protein in proteinsJ:
                    proteins.append((Protein(self.connection, protein)))

                return proteins
        else:
            return None

            # GENES #

    def gene(self, GENE_UID_KEY):
        '''
            Gene by GENE_UID_KEY
            :param GENE_UID_KEY:
            :return: Gene
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genes/id:" + str(GENE_UID_KEY)
        params = json.dumps({"fromCache": "true"})

        geneResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if geneResp is not None:
            geneRepJ = geneResp.json()
            if len(geneRepJ["result"]) <= 0:
                return None
            else:
                geneJ = geneRepJ["result"][0]
                return (Gene(self.connection, geneJ))
        else:
            return None

    def genes_by_name(self, GENE_FULLNAME):
        '''
        Genes by name
        :param GENE_FULLNAME:
        :return: List<Gene>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genes/name:" + str(GENE_FULLNAME)
        params = {'fromCache': 'true'}
        geneResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if geneResp is not None:
            geneRepJ = geneResp.json()
            if len(geneRepJ["result"]) <= 0:
                return None
            else:

                genesJ = geneRepJ["result"]
                genes = []
                for gene in genesJ:
                    genes.append((Gene(self.connection, gene)))

                return genes
        else:
            return None

    def resistant_genes(self):
        '''
        Get all Resistant Genes
        :return: List<Gene>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genes/all/genes:resistant"
        params = {'fromCache': 'true'}
        geneResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if geneResp is not None:
            geneRepJ = geneResp.json()
            if len(geneRepJ["result"]) <= 0:
                return None
            else:

                genesJ = geneRepJ["result"]
                genes = []
                for gene in genesJ:
                    genes.append((Gene(self.connection, gene)))

                return genes
        else:
            return None

    def genera_by_gene_name(self, GENE_FULLNAME):
        '''
            Get all the Genera containing genes by Gene name
            :param GENE_FULLNAME:
            :return: List<Genus>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genes/name:" + str(GENE_FULLNAME) + "/all/genera"
        params = {'fromCache': 'true'}
        generaResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if generaResp is not None:
            generaRepJ = generaResp.json()
            if len(generaRepJ["result"]) <= 0:
                return None
            else:

                generaJ = generaRepJ["result"]
                genera = []
                for genus in generaJ:
                    genera.append((Genus(self.connection, genus)))

                return genera
        else:
            return None

    def genomes_by_gene_name(self, GENE_FULLNAME):
        '''
            Get all the Genomes containing genes by Gene name
            :param GENE_FULLNAME:
            :return: List<Genome>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/genes/name:" + str(GENE_FULLNAME) + "/all/genomes"
        params = {'fromCache': 'true'}
        genomesResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genomesResp is not None:
            genomesRepJ = genomesResp.json()
            if len(genomesRepJ["result"]) <= 0:
                return None
            else:

                genomesJ = genomesRepJ["result"]
                genomes = []
                for genome in genomesJ:
                    genomes.append((Genus(self.connection, genome)))

                return genomes
        else:
            return None

            # PROTEINS #

    def protein(self, PROTEIN_UID_KEY):
        '''
            Protein by PROTEIN_UID_KEY
            :param PROTEIN_UID_KEY:
            :return: Protein
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/proteins/id:" + str(PROTEIN_UID_KEY)
        params = json.dumps({"fromCache": "true"})

        proteinResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if proteinResp is not None:
            proteinRepJ = proteinResp.json()
            if len(proteinRepJ["result"]) <= 0:
                return None
            else:
                proteinJ = proteinRepJ["result"][0]
                return (Protein(self.connection, proteinJ))
        else:
            return None

    def proteins_by_name(self, PROTEIN_FULLNAME):
        '''
        Proteins by name
        :param PROTEIN_FULLNAME:
        :return: List<Protein>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/proteins/name:" + str(PROTEIN_FULLNAME)
        params = {'fromCache': 'true'}
        proteinResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if proteinResp is not None:
            proteinRepJ = proteinResp.json()
            if len(proteinRepJ["result"]) <= 0:
                return None
            else:

                proteinsJ = proteinRepJ["result"]
                proteins = []
                for protein in proteinsJ:
                    proteins.append((Protein(self.connection, protein)))

                return proteins
        else:
            return None

    def genera_by_protein_name(self, PROTEIN_FULLNAME):
        '''
            Get all the Genera containing proteins by Protein name
            :param PROTEIN_FULLNAME:
            :return: List<Genus>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/proteins/name:" + str(PROTEIN_FULLNAME) + "/all/genera"
        params = {'fromCache': 'true'}
        generaResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if generaResp is not None:
            generaRepJ = generaResp.json()
            if len(generaRepJ["result"]) <= 0:
                return None
            else:

                generaJ = generaRepJ["result"]
                genera = []
                for genus in generaJ:
                    genera.append((Genus(self.connection, genus)))

                return genera
        else:
            return None

    def genomes_by_protein_name(self, PROTEIN_FULLNAME):
        '''
            Get all the Genomes containing proteins by Protein name
            :param PROTEIN_FULLNAME:
            :return: List<Genome>
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/proteins/name:" + str(PROTEIN_FULLNAME) + "/all/genomes"
        params = {'fromCache': 'true'}
        genomesResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if genomesResp is not None:
            genomesRepJ = genomesResp.json()
            if len(genomesRepJ["result"]) <= 0:
                return None
            else:

                genomesJ = genomesRepJ["result"]
                genomes = []
                for genome in genomesJ:
                    genomes.append((Genome(self.connection, genome)))

                return genomes
        else:
            return None

    def search(self, keyword):
        '''

        :param keyword: Search keyword
        :return: Results grouped by entity type
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/public/search" + str(keyword)
        params = {'fromCache': 'true'}
        searchResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if searchResp is not None:
            searchRepJ = searchResp.json()
            if len(searchRepJ["result"]) <= 0:
                return None
            else:
                genesJ = searchRepJ["result"]["GENE"]
                generaJ = searchRepJ["result"]["GENUS"]
                genomesJ = searchRepJ["result"]["GENOME"]
                # proteinsJ = searchRepJ["result"]["PROTEIN"]

                genera = []
                genomes = []
                genes = []
                # proteins = []

                for genus in generaJ:
                    genera.append((Genus(self.connection, genus)))

                for genome in genomesJ:
                    genomes.append((Genome(self.connection, genome)))

                for gene in genesJ:
                    genes.append((Gene(self.connection, gene)))

                # for protein in proteinsJ:
                #     proteins.append((Protein(self.connection, protein)))

                result = {}
                result['genera'] = genera
                result['genomes'] = genomes
                result['genes'] = genes
                # result['proteins'] = proteins

                return result
        else:
            return None

    def sql(self, sql_query, fromCache=True):
        '''

        :param sql_query: SQL to query OMX DB
        :return: SQL query result as JSON
        '''

        self.initOMXConnection()

        headers = {'content-type': 'application/json',
                   'content-language': 'en-US',
                   'accept': 'application/json'}
        methodurl = "/api/secure/query/db/omxdb"

        # params = json.dumps({'fromCache':str(fromCache)})
        # params = {'fromCache': 'true'}

        params = {'fromCache': str(fromCache), 'sql_query': sql_query}

        sqlResp = self.connection.get(methodurl=methodurl, headers=headers, payload=params)
        if sqlResp is not None:
            sqlRepJ = sqlResp.json()
            if len(sqlRepJ["result"]) <= 0:
                return None
            else:
                return sqlRepJ["result"]

