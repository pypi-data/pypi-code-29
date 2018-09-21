import matplotlib
#matplotlib.use('PS')
import matplotlib.pyplot as plt
import numpy as np
import itertools

labels = [0, 1, 2]
normalise = False

cm = np.array([[1, 2, 1], [1, 1, 1], [2, 2, 2]])
cmap = plt.get_cmap("Blues")

plt.imshow(cm, interpolation="nearest", cmap=cmap)
plt.title("", fontsize=10)
plt.colorbar()

tick_marks = np.arange(len(labels))
plt.xticks(tick_marks, labels, rotation=45)
plt.yticks(tick_marks, labels)

if normalise:
    if cm.sum(axis=None) > 0.:
        numerator = cm.astype("float")
        denom = cm.sum(axis=1)
        cm = np.divide(numerator, denom, out=np.zeros_like(numerator), where=denom!=0)
    else:
        cm = cm.astype("float")

thresh = cm.max() / 1.5 if normalise else cm.max() / 2
for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
    if normalise:
        s = "{:0.2f}"
    else:
        s = "{:,}"
    plt.text(j, i, s.format(cm[i, j]),
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black",
             fontsize=8)

#plt.tight_layout()
plt.ylabel("Label")
plt.xlabel("Label")
plt.show()
