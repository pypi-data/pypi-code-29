import numpy
import cv2
import math

from easy_net_tf.utility.file import UtilityFile
from easy_net_tf.utility.image import UtilityImage


class UtilityLandmark:

    @staticmethod
    def normalize(batch_rectangle, landmark):
        """

        :param batch_rectangle: [batch, 4]
        :param landmark: [2n]
        :return: narry [batch, 2n]
        """

        """
        prepare
        """
        batch, _ = numpy.shape(batch_rectangle)

        landmark = numpy.reshape(landmark, [-1, 2])
        n_landmark = list()

        """
        normalize landmark
        """
        for rectangle in batch_rectangle:
            for x, y in landmark:
                n_landmark.append(
                    (x - rectangle[0]) / (rectangle[2] - rectangle[0] + 1)
                )

                n_landmark.append(
                    (y - rectangle[1]) / (rectangle[3] - rectangle[1] + 1)
                )

        """
        reshape
        """
        n_landmark = numpy.reshape(
            numpy.array(
                n_landmark,
                dtype=numpy.float32
            ),
            [batch, -1]
        )

        return n_landmark

    @staticmethod
    def regress_rectangle(batch_rectangle,
                          batch_landmark):
        """
        calibrate landmarks to real scale
        :param batch_rectangle: [batch, 4]
        :param batch_landmark: [batch, 10]
        :return:
        """
        batch_width = batch_rectangle[:, 2] - batch_rectangle[:, 0] + 1
        batch_height = batch_rectangle[:, 3] - batch_rectangle[:, 1] + 1

        batch_landmark[:, 0] = batch_landmark[:, 0] * batch_width + batch_rectangle[:, 0]
        batch_landmark[:, 1] = batch_landmark[:, 1] * batch_height + batch_rectangle[:, 1]

        batch_landmark[:, 2] = batch_landmark[:, 2] * batch_width + batch_rectangle[:, 0]
        batch_landmark[:, 3] = batch_landmark[:, 3] * batch_height + batch_rectangle[:, 1]

        batch_landmark[:, 4] = batch_landmark[:, 4] * batch_width + batch_rectangle[:, 0]
        batch_landmark[:, 5] = batch_landmark[:, 5] * batch_height + batch_rectangle[:, 1]

        batch_landmark[:, 6] = batch_landmark[:, 6] * batch_width + batch_rectangle[:, 0]
        batch_landmark[:, 7] = batch_landmark[:, 7] * batch_height + batch_rectangle[:, 1]

        batch_landmark[:, 8] = batch_landmark[:, 8] * batch_width + batch_rectangle[:, 0]
        batch_landmark[:, 9] = batch_landmark[:, 9] * batch_height + batch_rectangle[:, 1]

        return batch_landmark

    @staticmethod
    def align_face(image, landmarks, template):
        image_height, image_width, _ = image.shape

        landmarks = numpy.reshape(landmarks, [-1, 2])
        template = numpy.reshape(template, [-1, 2])

        # maybe it is unnecessary, wait for proving!!!
        for index, _ in enumerate(landmarks):
            landmarks[index][0] *= image_width
            landmarks[index][1] *= image_height

            template[index][0] *= image_width
            template[index][1] *= image_height

        mat = cv2.estimateRigidTransform(src=landmarks,
                                         dst=template,
                                         fullAffine=True)

        align_image = cv2.warpAffine(src=image,
                                     M=mat,
                                     dsize=(image_height, image_width))

        return align_image

    @staticmethod
    def horizontally_flip(batch_normal_landmark):
        """
        
        :param batch_normal_landmark: shape:[10 * batch]
        :return: 
        """

        copy = numpy.copy(batch_normal_landmark)
        copy = numpy.reshape(copy, [-1, 2])

        copy[:, 0] = 1.0 - copy[:, 0]

        copy = numpy.reshape(copy, [-1, 10])

        for value in copy:
            # left eye <-> right eye
            value[0], value[2] = value[2], value[0]
            value[1], value[3] = value[3], value[1]

            # left mouth <-> right mouth
            value[6], value[8] = value[8], value[6]
            value[7], value[9] = value[9], value[7]

        copy = numpy.reshape(copy, [-1])

        return copy

    @staticmethod
    def rotate(landmark, center, angle):
        """

        :param landmark: shape: [ 10 ]
        :param center:
        :param angle:
        :return:
        """

        copy = landmark.copy()
        copy = numpy.reshape(
            numpy.array(copy,
                        dtype=numpy.float32),
            [-1, 2]
        )
        rotate_mat = cv2.getRotationMatrix2D(center, angle, 1)

        landmark_out = list()
        for x, y in copy:
            landmark_out.append(rotate_mat[0][0] * x + rotate_mat[0][1] * y + rotate_mat[0][2])
            landmark_out.append(rotate_mat[1][0] * x + rotate_mat[1][1] * y + rotate_mat[1][2])

        return landmark_out

    @staticmethod
    def mmlab_2_circle(read_path,
                       write_path,
                       log=False):
        info_generator = UtilityFile.get_line_generator(
            read_path=read_path,
            shuffle=False
        )

        sample_index = 0
        with open(write_path, 'w') as file:
            while True:
                if log:
                    sample_index += 1
                    print('Log: '
                          '[%s.%s] '
                          'sample: %d' % (UtilityLandmark.__name__,
                                          UtilityLandmark.mmlab_2_circle.__name__,
                                          sample_index)
                          )
                try:
                    info = info_generator.__next__().strip().split(' ')
                    image_path = info.pop(0)
                    x_1 = int(info.pop(0))
                    x_2 = int(info.pop(0))
                    y_1 = int(info.pop(0))
                    y_2 = int(info.pop(0))

                    circle = [(x_1 + x_2) / 2,
                              (y_1 + y_2) / 2,
                              math.sqrt(
                                  math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2)
                              ) / 2]

                    new_info = image_path + ';' \
                               + ' '.join(map(str, circle)) + ';' \
                               + ' '.join(map(str, info)) + '\n'

                    file.write(new_info)

                except StopIteration:
                    break

        return

    @staticmethod
    def verify_mmlab(read_path,
                     image_dir,
                     delay=500,
                     log=False):

        """
        verify and show original label
        :param read_path:
        :param image_dir:
        :param delay:
        :param log:
        :return:
        """
        info_generator = UtilityFile.get_line_generator(
            read_path=read_path,
            shuffle=False
        )

        sample_index = 0

        while True:
            if log:
                sample_index += 1
                print('Log: '
                      '[%s.%s] '
                      'sample: %d' % (UtilityLandmark.__name__,
                                      UtilityLandmark.mmlab_2_circle.__name__,
                                      sample_index)
                      )
            try:
                info = info_generator.__next__().strip().split(' ')
                image_path = info.pop(0)
                image = cv2.imread(image_dir + '/' + image_path)

                x_1 = int(info.pop(0))
                x_2 = int(info.pop(0))
                y_1 = int(info.pop(0))
                y_2 = int(info.pop(0))

                image = UtilityImage.draw_rectangle(image=image,
                                                    batch_rectangle=[[x_1, y_1, x_2, y_2]],
                                                    color=(0, 255, 0))

                landmark = numpy.reshape(
                    a=numpy.array(list(map(float, info)), dtype=numpy.int32),
                    newshape=[-1, 2]
                )
                image = UtilityImage.draw_point(image=image,
                                                batch_point=landmark,
                                                color=(0, 255, 0))

                cv2.imshow('Original Landmark verify',
                           image)
                cv2.waitKey(delay)
            except StopIteration:
                break

        return

    @staticmethod
    def verify_circle(read_path,
                      image_dir,
                      delay=500,
                      log=False):
        """
        verify circle format label
        :param read_path:
        :param image_dir:
        :param delay:
        :param log:
        :return:
        """
        info_generator = UtilityFile.get_line_generator(
            read_path=read_path,
            shuffle=False
        )

        sample_index = 0

        while True:
            if log:
                sample_index += 1
                print('Log: '
                      '[%s.%s] '
                      'sample: %d' % (UtilityLandmark.__name__,
                                      UtilityLandmark.mmlab_2_circle.__name__,
                                      sample_index)
                      )
            try:
                info = info_generator.__next__().strip().split(';')
                image_path = info.pop(0)
                image = cv2.imread(image_dir + '/' + image_path)

                circle = list(map(float, info.pop(0).split(' ')))

                image = UtilityImage.draw_circle(image=image,
                                                 batch_circle=[circle])

                landmark = numpy.reshape(
                    a=numpy.array(list(map(float, info.pop(0).split(' '))), dtype=numpy.int32),
                    newshape=[-1, 2]
                )
                image = UtilityImage.draw_point(image=image,
                                                batch_point=landmark,
                                                color=(0, 255, 0))

                cv2.imshow('Original Landmark verify',
                           image)
                cv2.waitKey(delay)
            except StopIteration:
                break

        return


if __name__ == '__main__':
    UtilityLandmark.mmlab_2_circle(
        read_path='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/train/labels.txt',
        write_path='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/train/labels-c.txt',
        log=True
    )

    # UtilityLandmark.verify_mmlab(
    #     read_path='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/train/trainImageList.txt',
    #     image_dir='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/image',
    #     log=True
    # )

    # UtilityLandmark.verify_circle(
    #     read_path='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/train/labels-c.txt',
    #     image_dir='/home/yehangyang/Documents/Gitlab/AI_database/mmlab/data_set/image',
    #     log=True
    # )
