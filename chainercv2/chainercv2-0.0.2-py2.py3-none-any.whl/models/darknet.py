"""
    DarkNet, implemented in Chainer.
    Original source: 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.
"""

__all__ = ['DarkNet', 'darknet_ref', 'darknet_tiny', 'darknet19']

import os
import chainer.functions as F
import chainer.links as L
from chainer import Chain
from functools import partial
from chainer.serializers import load_npz
from .common import SimpleSequential


class DarkConv(Chain):
    """
    DarkNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    kernel_size : int or tuple/list of 2 int
        Convolution window size.
    pad : int or tuple/list of 2 int
        Padding value for convolution layer.
    """
    def __init__(self,
                 in_channels,
                 out_channels,
                 ksize,
                 pad):
        super(DarkConv, self).__init__()
        with self.init_scope():
            self.conv = L.Convolution2D(
                in_channels=in_channels,
                out_channels=out_channels,
                ksize=ksize,
                pad=pad,
                nobias=True)
            self.bn = L.BatchNormalization(size=out_channels)
            self.activ = partial(
                F.leaky_relu,
                slope=0.1)

    def __call__(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.activ(x)
        return x


def dark_conv1x1(in_channels,
                 out_channels):
    """
    1x1 version of the DarkNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """
    return DarkConv(
        in_channels=in_channels,
        out_channels=out_channels,
        ksize=1,
        pad=0)


def dark_conv3x3(in_channels,
                 out_channels):
    """
    3x3 version of the DarkNet specific convolution block.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    """
    return DarkConv(
        in_channels=in_channels,
        out_channels=out_channels,
        ksize=3,
        pad=1)


def dark_convYxY(in_channels,
                 out_channels,
                 pointwise=True):
    """
    DarkNet unit.

    Parameters:
    ----------
    in_channels : int
        Number of input channels.
    out_channels : int
        Number of output channels.
    pointwise : bool
        Whether use 1x1 (pointwise) convolution or 3x3 convolution.
    """
    if pointwise:
        return dark_conv1x1(
            in_channels=in_channels,
            out_channels=out_channels)
    else:
        return dark_conv3x3(
            in_channels=in_channels,
            out_channels=out_channels)


class DarkNet(Chain):
    """
    DarkNet model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    channels : list of list of int
        Number of output channels for each unit.
    odd_pointwise : bool
        Whether pointwise convolution layer is used for each odd unit.
    avg_pool_size : int
        Window size of the final average pooling.
    cls_activ : bool
        Whether classification convolution layer uses an activation.
    in_channels : int, default 3
        Number of input channels.
    classes : int, default 1000
        Number of classification classes.
    """
    def __init__(self,
                 channels,
                 odd_pointwise,
                 avg_pool_size,
                 cls_activ,
                 in_channels=3,
                 classes=1000):
        super(DarkNet, self).__init__()

        with self.init_scope():
            self.features = SimpleSequential()
            with self.features.init_scope():
                for i, channels_per_stage in enumerate(channels):
                    stage = SimpleSequential()
                    with stage.init_scope():
                        for j, out_channels in enumerate(channels_per_stage):
                            setattr(stage, "unit{}".format(j + 1), dark_convYxY(
                                in_channels=in_channels,
                                out_channels=out_channels,
                                pointwise=(len(channels_per_stage) > 1) and not(((j + 1) % 2 == 1) ^ odd_pointwise)))
                            in_channels = out_channels
                        if i != len(channels) - 1:
                            setattr(stage, "pool{}".format(i + 1), partial(
                                F.max_pooling_2d,
                                ksize=2,
                                stride=2,
                                cover_all=False))
                    setattr(self.features, "stage{}".format(i + 1), stage)

            self.output = SimpleSequential()
            with self.output.init_scope():
                setattr(self.output, 'final_conv', L.Convolution2D(
                    in_channels=in_channels,
                    out_channels=classes,
                    ksize=1))
                if cls_activ:
                    setattr(self.output, 'final_activ', partial(
                        F.leaky_relu,
                        slope=0.1))
                setattr(self.output, 'final_pool', partial(
                    F.average_pooling_2d,
                    ksize=avg_pool_size,
                    stride=1))
                setattr(self.output, 'final_flatten', partial(
                    F.reshape,
                    shape=(-1, classes)))

    def __call__(self, x):
        x = self.features(x)
        x = self.output(x)
        return x


def get_darknet(version,
                model_name=None,
                pretrained=False,
                root=os.path.join('~', '.chainer', 'models'),
                **kwargs):
    """
    Create DarkNet model with specific parameters.

    Parameters:
    ----------
    version : str
        Version of SqueezeNet ('ref', 'tiny' or '19').
    model_name : str or None, default None
        Model name for loading pretrained model.
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """

    if version == 'ref':
        channels = [[16], [32], [64], [128], [256], [512], [1024]]
        odd_pointwise = False
        avg_pool_size = 3
        cls_activ = True
    elif version == 'tiny':
        channels = [[16], [32], [16, 128, 16, 128], [32, 256, 32, 256], [64, 512, 64, 512, 128]]
        odd_pointwise = True
        avg_pool_size = 14
        cls_activ = False
    elif version == '19':
        channels = [[32], [64], [128, 64, 128], [256, 128, 256], [512, 256, 512, 256, 512],
                    [1024, 512, 1024, 512, 1024]]
        odd_pointwise = False
        avg_pool_size = 7
        cls_activ = False
    # elif version == '53':
    #     init_block_channels = 32
    #     layers = [2, 8, 8, 4]
    #     channels_per_layers = [64, 128, 256, 512, 1024]
    #     channels = [[ci] * li for (ci, li) in zip(channels_per_layers, layers)]
    #     odd_pointwise = False
    #     avg_pool_size = 7
    #     cls_activ = False
    else:
        raise ValueError("Unsupported DarkNet version {}".format(version))

    net = DarkNet(
        channels=channels,
        odd_pointwise=odd_pointwise,
        avg_pool_size=avg_pool_size,
        cls_activ=cls_activ,
        **kwargs)

    if pretrained:
        if (model_name is None) or (not model_name):
            raise ValueError("Parameter `model_name` should be properly initialized for loading pretrained model.")
        from .model_store import get_model_file
        load_npz(
            file=get_model_file(
                model_name=model_name,
                local_model_store_dir_path=root),
            obj=net)

    return net


def darknet_ref(**kwargs):
    """
    DarkNet 'Reference' model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="ref", model_name="darknet_ref", **kwargs)


def darknet_tiny(**kwargs):
    """
    DarkNet Tiny model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="tiny", model_name="darknet_tiny", **kwargs)


def darknet19(**kwargs):
    """
    DarkNet-19 model from 'Darknet: Open source neural networks in c,' https://github.com/pjreddie/darknet.

    Parameters:
    ----------
    pretrained : bool, default False
        Whether to load the pretrained weights for model.
    ctx : Context, default CPU
        The context in which to load the pretrained weights.
    root : str, default '~/.chainer/models'
        Location for keeping the model parameters.
    """
    return get_darknet(version="19", model_name="darknet19", **kwargs)


def _test():
    import numpy as np
    import chainer

    chainer.global_config.train = False

    pretrained = True

    models = [
        # darknet_ref,
        darknet_tiny,
        # darknet19,
    ]

    for model in models:

        net = model(pretrained=pretrained)
        weight_count = net.count_params()
        print("m={}, {}".format(model.__name__, weight_count))
        assert (model != darknet_ref or weight_count == 7319416)
        assert (model != darknet_tiny or weight_count == 1042104)
        assert (model != darknet19 or weight_count == 20842376)

        x = np.zeros((1, 3, 224, 224), np.float32)
        y = net(x)
        assert (y.shape == (1, 1000))


if __name__ == "__main__":
    _test()
