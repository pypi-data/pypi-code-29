import tensorflow as tf
import math


class UtilityLoss:
    @staticmethod
    def softmax_cross_entropy(prediction,
                              truth,
                              selections,
                              keep_ratio,
                              name,
                              debug=False):
        """

        :param prediction:
        :param truth: ground truth category. int32, int64 only
        :param selections: a list of selected categories.
        :param keep_ratio: keep top high 0.7 of cross entropy.
        :param name: a name for tf.summary
        :param debug: True: return loss,
                            valid_index,
                            raw_cross_entropy,
                            valid_cross_entropy,
                            top_cross_entropy;
                      False: return loss
        :return:
        """

        selection_0 = selections.pop(0)

        """
        valid index
        """
        valid_index = tf.equal(truth, selection_0)

        for selection in selections:
            valid_index = tf.logical_or(
                valid_index,
                tf.equal(truth, selection)
            )

        valid_total = tf.reduce_sum(
            tf.cast(
                valid_index,
                dtype=tf.float32)
        )

        mask_b = tf.multiply(
            tf.ones_like(truth),
            selection_0
        )
        truth = tf.cast(
            tf.where(
                valid_index,
                truth,
                mask_b
            ),
            tf.int32
        )

        """
        cross entropy
        """
        raw_cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=truth,
            logits=prediction
        )

        mask_0 = tf.zeros_like(raw_cross_entropy)

        valid_cross_entropy = tf.where(
            valid_index,
            raw_cross_entropy,
            mask_0
        )

        """
        keep ratio
        """
        keep_number = tf.cast(
            keep_ratio * valid_total,
            dtype=tf.int32
        )

        top_cross_entropy, _ = tf.nn.top_k(valid_cross_entropy, k=keep_number)

        """
        loss
        """
        loss = tf.reduce_mean(top_cross_entropy)

        tf.summary.scalar(name=name,
                          tensor=loss)

        if debug:
            return loss, valid_index, raw_cross_entropy, valid_cross_entropy, top_cross_entropy
        else:
            return loss

    @staticmethod
    def l2(prediction,
           truth,
           categories,
           selections,
           keep_ratio,
           name,
           debug=False):
        """

        :param prediction:
        :param truth:
        :param categories: category label for each sample
        :param selections: a list of selected categories.
        :param keep_ratio: keep top high 0.7 of square error.
        :param name: a name for tf.summary
        :param debug: True: return loss,
                            valid_index,
                            raw_square_error,
                            valid_square_error,
                            top_square_error;
                      False: return loss
        :return:
        """

        selection_0 = selections.pop(0)

        """
        valid index
        """
        valid_index = tf.equal(categories, selection_0)

        for selection in selections:
            valid_index = tf.logical_or(
                valid_index,
                tf.equal(categories, selection)
            )

        valid_total = tf.reduce_sum(
            tf.cast(
                valid_index,
                dtype=tf.float32)
        )

        """
        square error
        """
        raw_square_error = tf.reduce_sum(
            tf.square(prediction - truth),
            axis=1
        )

        mask_0 = tf.zeros_like(raw_square_error)
        valid_square_error = tf.where(
            valid_index,
            raw_square_error,
            mask_0
        )

        """
        keep ratio
        """
        keep_num = tf.cast(
            keep_ratio * valid_total,
            dtype=tf.int32
        )

        top_square_error, _ = tf.nn.top_k(valid_square_error, k=keep_num)

        """
        loss
        """
        loss = tf.reduce_mean(top_square_error)

        tf.summary.scalar(name=name,
                          tensor=loss)

        if debug:
            return loss, valid_index, raw_square_error, valid_square_error, top_square_error
        else:
            return loss

    @staticmethod
    def arcface(x,
                weight,
                truth,
                margin,
                selections,
                keep_ratio,
                name,
                s=64,
                debug=False):
        """

        :param x: [[x1],[x2],[x3]]
        :param weight: [[w11,w12,w13],[w21,w22,w23]]
        :param truth: [t1,t2,t3]
        :param margin:
        :param selections:
        :param keep_ratio:
        :param name:
        :param s:
        :param debug:
        :return:
        """

        """
        valid index
        """
        category_number = len(selections)
        selection_0 = selections.pop(0)
        valid_index = tf.equal(truth, selection_0)

        for selection in selections:
            valid_index = tf.logical_or(
                valid_index,
                tf.equal(truth, selection)
            )

        valid_total = tf.reduce_sum(
            tf.cast(
                valid_index,
                dtype=tf.float32)
        )

        """
        mask out no selected category
        """
        mask_b = tf.multiply(
            tf.ones_like(truth),
            selection_0
        )
        truth = tf.cast(
            tf.where(
                valid_index,
                truth,
                mask_b
            ),
            tf.int32
        )

        """
        add margin
        """
        cos_m = math.cos(margin)
        sin_m = math.sin(margin)

        x_norm = tf.nn.l2_normalize(x, 1)
        w_norm = tf.nn.l2_normalize(weight, 0)

        cos_theta = tf.matmul(x_norm, w_norm)
        sin_theta = tf.sqrt(
            1.0 - tf.square(cos_theta)
        )

        threshold = math.cos(math.pi - margin)
        cos_theta_m = tf.where(
            cos_theta >= threshold,
            cos_theta * cos_m - sin_theta * sin_m,
            cos_theta - margin * sin_m
        )

        truth_one_hot = tf.one_hot(indices=truth, depth=category_number)

        gap_cos_theta = tf.where(
            truth_one_hot == 1,
            cos_theta_m,
            cos_theta
        )

        gap_cos_theta *= s

        """
        cross entropy
        """
        raw_cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=truth,
            logits=gap_cos_theta
        )

        zeros = tf.zeros_like(raw_cross_entropy)

        valid_cross_entropy = tf.where(
            valid_index,
            raw_cross_entropy,
            zeros
        )

        """
        keep ratio
        """
        keep_number = tf.cast(
            keep_ratio * valid_total,
            dtype=tf.int32
        )

        top_k_cross_entropy, _ = tf.nn.top_k(valid_cross_entropy, k=keep_number)

        """
        loss
        """
        loss = tf.reduce_mean(top_k_cross_entropy)

        tf.summary.scalar(name=name,
                          tensor=loss)

        if debug:
            return loss, valid_index, raw_cross_entropy, valid_cross_entropy, top_k_cross_entropy
        else:
            return loss


if __name__ == '__main__':
    from easydict import EasyDict

    predicted = EasyDict()
    predicted.category = tf.constant([[0.0, 1.0],
                                      [0.1, 0.9],
                                      [0.2, 0.8],
                                      [0.3, 0.7],
                                      [0.4, 0.6],
                                      [0.5, 0.5],
                                      [0.6, 0.4],
                                      [0.7, 0.3],
                                      [0.8, 0.2],
                                      [0.9, 0.1]])
    predicted.offset = tf.constant([[0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1],
                                    [0.1, 0.1, 0.1, 0.1]])

    ground_truth = EasyDict()
    ground_truth.category = tf.constant([1,
                                         -2,
                                         -2,
                                         1,
                                         -2,
                                         1,
                                         0,
                                         -2,
                                         0,
                                         1])
    ground_truth.offset = tf.constant([[0.0, 0.1, 0.1, 0.1],
                                       [0.0, 0.0, 0.1, 0.1],
                                       [0.0, 0.0, 0.0, 0.1],
                                       [0.0, 0.0, 0.0, 0.0],
                                       [0.3, 0.1, 0.1, 0.1],
                                       [0.3, 0.3, 0.1, 0.1],
                                       [0.3, 0.3, 0.3, 0.1],
                                       [0.3, 0.3, 0.3, 0.3],
                                       [0.1, 0.5, 0.1, 0.1],
                                       [0.1, 0.5, 0.1, 0.1]])

    cross_entropy_op = UtilityLoss.softmax_cross_entropy(prediction=predicted.category,
                                                         truth=ground_truth.category,
                                                         selections=[0, 1],
                                                         keep_ratio=1,
                                                         name='category',
                                                         debug=False)

    offset_loss_op = UtilityLoss.l2(prediction=predicted.offset,
                                    truth=ground_truth.offset,
                                    categories=ground_truth.category,
                                    selections=[2],
                                    keep_ratio=0.7,
                                    name='offset',
                                    debug=True)

    with tf.Session() as sess:
        cross_entropy = sess.run(cross_entropy_op)
        print(cross_entropy)

        # offset_loss = sess.run(offset_loss_op)
        # print(offset_loss)
