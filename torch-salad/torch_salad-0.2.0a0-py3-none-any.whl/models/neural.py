from torch.utils.data import Dataset
from PIL import Image
import numpy as np
import pickle

import torch
from torch import nn

class MonkeyDataset(Dataset):

    """ Access dataset from Cadena et al (2018) in PyTorch
    """

    path = '/gpfs01/bethge/home/sschneider/amadeus.pkl'
    seed = 1000

    def __init__(self, which='train', domains=['original'], transform=None):

        assert which in ['train', 'val', 'test']

        with open(MonkeyDataset.path, 'rb') as g:
            Data = pickle.load(g, encoding='latin1')
        Data = Data[0]

        self.data = MonkeyDataLoader(Data, seed = MonkeyDataset.seed,
                                     types_train=domains, types_test=domains)
        self.images, self.responses, _ = self._load(which)
        self.transform = transform


    def _load(self, key):
        if    key == 'train' : return self.data.train()
        elif  key == 'val'   : return self.data.val()
        elif  key == 'test'  : return self.data.test()
        else: raise NotImplementedError

    def __len__(self):

        return len(self.images)

    def __getitem__(self, index):

        np_im = self.images[index].squeeze()
        if self.responses.ndim == 2:
            y     = self.responses[index]
        else:
            y = self.responses[:,index]

        im = Image.fromarray(np.uint8(np_im))
        y  = torch.from_numpy(y)

        if self.transform is not None:
            im = self.transform(im)

        return im, y

class MonkeyDataLoader:

    """ Provided by Santiago
    """

    def __init__(self, data, seed=None, train_frac=0.8 , subsample=1, crop=0,
                types_train=['original'],types_test=['original']):
        idc = slice(crop, -crop if crop > 0 else None, subsample)
        images = data['images'][:,idc,idc,None]
        responses = data['responses'].astype(np.float32)
        real_resps = data['is_realresponse'].astype(np.float32)

        # dimensions
        num_reps, num_images, num_neurons = responses.shape
        num_train_images = int(num_images * train_frac)

        # normalize images
        image_ids = data['image_ids'].flatten()
        image_types = data['image_types'].flatten()

        #imgs_mean = np.mean(images)
        #imgs_sd = np.std(images)
        #images = (images - imgs_mean) / imgs_sd

        self.num_reps = num_reps

        self.images = np.tile(images[:num_train_images,:,:,:], [num_reps, 1, 1, 1])
        self.images_test = images[num_train_images:,:,:,:]

        self.responses = responses[:,:num_train_images,:].reshape([num_train_images*num_reps, num_neurons])
        self.responses_test = responses[:,num_train_images:,:]

        self.real_resps = real_resps[:,:num_train_images,:].reshape([num_train_images*num_reps, num_neurons])
        self.real_resps_test = real_resps[:,num_train_images:,:]

        self.image_ids = np.tile(image_ids[:num_train_images], [num_reps])
        self.image_ids_test = image_ids[num_train_images:]

        self.types = np.tile(image_types[:num_train_images], [num_reps])
        self.types_test = image_types[num_train_images:]

        # Select indices of image types
        idx_trn = np.array([True if x in types_train else False for x in self.types])
        idx_tst = np.array([True if x in types_test else False for x in self.types_test])

        self.images = self.images[idx_trn,]
        self.images_test = self.images_test[idx_tst,]

        self.responses = self.responses[idx_trn,]
        self.responses_test = self.responses_test[:,idx_tst,:]

        self.real_resps = self.real_resps[idx_trn,]
        self.real_resps_test = self.real_resps_test[:,idx_tst,:]

        self.image_ids = self.image_ids[idx_trn]
        self.image_ids_test = self.image_ids_test[idx_tst]

        self.types = self.types[idx_trn]
        self.types_test = self.types_test[idx_tst]


        self.num_neurons = num_neurons
        self.num_images = num_images
        self.num_train_images = int(self.images.shape[0] / num_reps)
        self.px_x = images.shape[1]
        self.px_y = images.shape[2]
        if seed:
            np.random.seed(seed)
        perm = np.random.permutation(self.num_train_images)
        train_idx = np.sort(perm[:round(self.num_train_images * train_frac)])
        self.train_idx = np.hstack([train_idx + i * self.num_train_images for i in range(num_reps)])
        val_idx = np.sort(perm[round(self.num_train_images * train_frac):])
        self.val_idx = np.hstack([val_idx + i * self.num_train_images for i in range(num_reps)])
        self.num_train_samples = self.train_idx.size
        self.next_epoch()

        self.subject_id  = data['subject_id']
        self.repetitions = data['repetitions']
        self.depth_layer = data['depth_layer']

    def val(self):
        return self.images[self.val_idx], self.responses[self.val_idx], self.real_resps[self.val_idx]

    def train(self):
        return self.images[self.train_idx], self.responses[self.train_idx], self.real_resps[self.train_idx]

    def nanarray(self,real_resps,resps):
        return np.where(real_resps, resps, np.nan)

    def test(self):
        return self.images_test, self.responses_test, self.real_resps_test

    def test_av(self):
        return self.images_test, np.nanmean(self.nanarray(self.real_resps_test,self.responses_test),axis=0)

    def images_rgb(self,images=None):
        if images is None:
            ims = np.tile(data.images,[1,3,1,1])
        else:
            ims = np.tile(images,[1,3,1,1])
        return ims

    def minibatch(self, batch_size):
        im = self.images[self.train_idx]
        res = self.responses[self.train_idx]
        isreal = self.real_resps[self.train_idx]
        if self.minibatch_idx + batch_size > len(self.train_perm):
            self.next_epoch()
        idx = self.train_perm[self.minibatch_idx + np.arange(0, batch_size)]
        self.minibatch_idx += batch_size
        return im[idx, :, :], res[idx, :], isreal[idx,:]

    def next_epoch(self):
        self.minibatch_idx = 0
        self.train_perm = np.random.permutation(self.num_train_samples)
