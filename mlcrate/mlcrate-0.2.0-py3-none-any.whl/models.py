from collections import defaultdict
import numpy as np
import tqdm

class MarkovChain:
	def __init__(self, sequence, state_length=1, normalize=True):
		self.sequence = sequence
		self.state_length = state_length
		self.normalize = normalize
		self.chain = defaultdict(lambda: defaultdict(int))
		self.state_frequency = defaultdict(int)
		self.item_frequency = defaultdict(int)

		self._fit()

		if self.normalize:
			self._normalize()

	def _fit(self):
		ixs = np.arange(len(self.sequence) - self.state_length + 1)
		for ix in tqdm.tqdm(ixs):
			state = self.sequence[ix:ix+state_length]
			result = self.sequence[ix+state_length:ix+state_length+1]
			self.chain[state][result] += 1

			self.state_frequency[state] += 1
			self.item_frequency[result] += 1

	def _normalize(self):
		for state, frequency in self.state_frequency.items():
			for result in self.chain[state].keys():
				self.chain[state][result] /= frequency

