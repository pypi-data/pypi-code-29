"""
# This file controls which input names call which functions.

"""

operations_dict = {
    "Normalization": {
        "zscorenorm": "vectoolslib.normalization.z_score_normalization",
        "quantnorm":  "vectoolslib.normalization.quantile_normalization",
        "medpolish":  "vectoolslib.normalization.median_polish_normalization"
    },
    "Math": {
        "add":         "vectoolslib.mathematics.add",
        "subtract":    "vectoolslib.mathematics.subtract",
        "multiply":    "vectoolslib.mathematics.multiply",
        "dotproduct":  "vectoolslib.mathematics.dot_product",
        "inverse":     "vectoolslib.mathematics.inverse",
        "determinant": "vectoolslib.mathematics.determinant",
        "eigenvec":    "vectoolslib.mathematics.eigen_vectors",
        "eigenvalues": "vectoolslib.mathematics.eigen_values",
        "sum":         "vectoolslib.mathematics.sum_up"
    },
    "Manipulation": {
        "append":       "vectoolslib.manipulation.append_values_to",
        "aggregate":    "vectoolslib.manipulation.aggregate",
        "creatematrix": "vectoolslib.manipulation.create_matrix",
        "format":       "vectoolslib.manipulation.format_vec",
        "chop":         "vectoolslib.manipulation.chop",
        "concat":       "vectoolslib.manipulation.concatenate",
        "join":         "vectoolslib.manipulation.join",
        "vrep":         "vectoolslib.manipulation.vrep",
        "slice":        "vectoolslib.manipulation.vec_slice",
        "sort":         "vectoolslib.manipulation.vector_sort",
        "transpose":    "vectoolslib.manipulation.transpose",
        "unique":       "vectoolslib.manipulation.unique"
        # "to_svmlight": manipulation.to_svmlight,
        # "svml_to_csv": manipulation.to_csv,
        # "makeaddable": makeaddable,
        # "append_matrix": append_matrix,
        # "max": colmax,
    },
    "Analysis and Statistics": {
        # "runLDA":     "vectoolslib.analysis.run_lda",
        "min":        "vectoolslib.analysis.minimum",
        "max":        "vectoolslib.analysis.maximum",
        "median":     "vectoolslib.analysis.median",
        "sd":         "vectoolslib.analysis.sd",
        "mean":       "vectoolslib.analysis.average",
        "percentile": "vectoolslib.analysis.percentile",
        "pearson":    "vectoolslib.analysis.pearson_group",
        "pca":        "vectoolslib.analysis.run_pca",
        "spearman":   "vectoolslib.analysis.spearman",
        "confmat":    "vectoolslib.analysis.confusion_matrix",
        "roc":        "vectoolslib.analysis.roc_curve",
        "shape": "vectoolslib.analysis.shape"
    },
    "Descriptors": {
        "ncomp":   "vectoolslib.descriptor_CLI_interfaces.ncomposition_command_line",
        "trans": "vectoolslib.descriptor_CLI_interfaces.transitions_command_line",
        "grouped": "vectoolslib.descriptor_CLI_interfaces.grouped_n_composition_command_line",
        # "splitncomp":  "vectoolslib.descriptor_CLI_interfaces.split_ncomposition_command_line",
        # "physchem":    "vectoolslib.descriptor_CLI_interfaces.physicochemical_properties_ncomposition_command_line",
        # "geary":       "vectoolslib.descriptor_CLI_interfaces.geary_autocorrelation_command_line",
        # "mbroto":      "vectoolslib.descriptor_CLI_interfaces.normalized_moreaubroto_autocorrelation_command_line",
        # "moran":       "vectoolslib.descriptor_CLI_interfaces.moran_autocorrelation_command_line",
        # "pseudoaac":   "vectoolslib.descriptor_CLI_interfaces.pseudo_amino_acid_composition_command_line",
        # "seqordcoup":  "vectoolslib.descriptor_CLI_interfaces.sequence_order_coupling_number_total_command_line",
        # "quasiseqord": "vectoolslib.descriptor_CLI_interfaces.quasi_sequence_order_command_line",
        "summary":     "vectoolslib.analysis.summary"
    },
    "Supervised Learning": {
        "svmtrain":    "vectoolslib.supervised_learning.svm_train",
        "svmclassify": "vectoolslib.supervised_learning.svm_classify",
        "linreg":      "vectoolslib.supervised_learning.linear_regression",
        # "neuralnet":   "vectoolslib.supervised_learning.neural_network",
        # "randforest":  "vectoolslib.supervised_learning.random_forest"
    },
    "Unsupervised Learning": {
        "kmeans":   "vectoolslib.unsupervised_learning.k_means_clustering",
        "dbscan":   "vectoolslib.unsupervised_learning.DBSCAN",
        "affcl":    "vectoolslib.unsupervised_learning.affinity_propagation_clustering",
        "hierarc":  "vectoolslib.unsupervised_learning.hierarchical_cluster",
        "silscore": "vectoolslib.unsupervised_learning.silhouette_score",
    },
    "Graph Operations": {
        "edges":       "vectoolslib.graph.listedges",
        "addedge":     "vectoolslib.graph.addedge",
        "addnode":     "vectoolslib.graph.addnode",
        "paths":       "vectoolslib.graph.listpaths",
        "graphformat": "vectoolslib.graph.graphformat",
    }
}
