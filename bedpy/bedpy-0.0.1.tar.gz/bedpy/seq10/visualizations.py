import seaborn as sns
import matplotlib.pyplot as plt

def img_as_sns(sequence_as_img, sequence_characters):
    return sns.heatmap(
        [*zip(*sequence_as_img)],
        square=False,
        cmap=['white', 'black'],
        cbar=False,
        xticklabels=50,
        yticklabels=list(sequence_characters)
    )

def cls_as_sns(classes_as_img, classes):
    return sns.heatmap(
        [*zip(*classes_as_img)],
        square=False,
        cmap='GnBu',
        cbar=True,
        xticklabels=50,
        yticklabels=classes
    )
