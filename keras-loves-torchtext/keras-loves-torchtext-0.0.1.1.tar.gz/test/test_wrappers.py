import unittest
from torchtext import data

from kltt import WrapIterator, WrapDataset


class TestWrappers(unittest.TestCase):
    BATCH_SIZE = 2

    def setUp(self):
        text_field = lambda: data.Field()
        label_field = lambda: data.Field(sequential=False, unk_token=None)

        x1 = ['dog', 'work', 'red', 'house']
        x2 = ['Hund', 'arbeiten', 'Rot', 'Haus']

        y1 = ['sub', 'verb', 'adj', 'sub']
        y2 = [10, 15, 20, 25]

        def build_dataset(data_fields, fields):
            examples = [data.Example.fromlist(datum, fields) for datum in zip(*data_fields)]
            return data.Dataset(examples, fields)

        self.dataset1 = build_dataset([x1, y1], [
            ('text', text_field()),
            ('label', label_field())
        ])

        self.dataset2 = build_dataset([x1, x2, y1], [
            ('text1', text_field()),
            ('text2', text_field()),
            ('label', label_field())
        ])

        self.dataset3 = build_dataset([x1, x2, y1, y2], [
            ('text1', text_field()),
            ('text2', text_field()),
            ('label1', label_field()),
            ('label2', label_field())
        ])

        for dataset in [self.dataset1, self.dataset2, self.dataset3]:
            for field in dataset.fields.values():
                field.build_vocab(dataset)

    def test_wrap_iterator_dataset1(self):
        iterator = data.Iterator(self.dataset1, self.BATCH_SIZE, repeat=False)
        data_gen = WrapIterator(iterator, ['text'], ['label'])

        self.assertEqual(len(data_gen), len(self.dataset1) // self.BATCH_SIZE)

        for batch in iter(data_gen):
            self.assertEqual(len(batch), self.BATCH_SIZE)

            x, y = batch

            self.assertEqual(len(x), 1)
            self.assertEqual(len(y), 1)

            self.assertEqual(x[0].shape, (2, 1))
            self.assertEqual(y[0].shape, (2,))

    def test_wrap_iterator_dataset2(self):
        iterator = data.Iterator(self.dataset2, self.BATCH_SIZE, repeat=False)
        data_gen = WrapIterator(iterator, ['text1', 'text2'], ['label'])

        self.assertEqual(len(data_gen), len(self.dataset2) // self.BATCH_SIZE)

        for batch in iter(data_gen):
            self.assertEqual(len(batch), self.BATCH_SIZE)

            x, y = batch

            self.assertEqual(len(x), 2)
            self.assertEqual(len(y), 1)

            self.assertEqual(x[0].shape, (2, 1))
            self.assertEqual(x[1].shape, (2, 1))
            self.assertEqual(y[0].shape, (2,))

    def test_wrap_iterator_dataset3(self):
        iterator = data.Iterator(self.dataset3, self.BATCH_SIZE, repeat=False)
        data_gen = WrapIterator(iterator, ['text1', 'text2'], ['label1', 'label2'])

        self.assertEqual(len(data_gen), len(self.dataset3) // self.BATCH_SIZE)

        label2_acc = set()

        for batch in iter(data_gen):
            self.assertEqual(len(batch), self.BATCH_SIZE)

            x, y = batch

            self.assertEqual(len(x), 2)
            self.assertEqual(len(y), 2)

            self.assertEqual(x[0].shape, (2, 1))
            self.assertEqual(x[1].shape, (2, 1))
            self.assertEqual(y[0].shape, (2,))
            self.assertEqual(y[1].shape, (2,))

            label2_acc.update(set(list(y[1])))

        # Check whether numerical labels representing non-categorical ids are correctly handled
        # and start with a zero index.
        self.assertEqual(label2_acc, set(range(4)))
