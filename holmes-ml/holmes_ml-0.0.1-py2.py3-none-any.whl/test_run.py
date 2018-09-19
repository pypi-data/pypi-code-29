from dataloader import DataLoader
from features import FeatureSynthesis

loader = DataLoader()
synthesizer = FeatureSynthesis()
es, transactions = loader.load()
fl = synthesizer.synthesize(es, baseline=True)
fm = synthesizer.feature_matrix(es, transactions, fl)
print(fl)
print(fm)
