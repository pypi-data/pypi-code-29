import cv2
import numpy
import math

from pathlib import Path


class UtilityImage:
    NORMALIZE_DEFAULT = 'default'
    NORMALIZE_EACH_CHANNEL = 'normalize each channel to [low,high]'
    NORMALIZE_ALL_CHANNEL = 'normalize all channel to [low,high]'
    NORMALIZE_NONE = 'no normalization'
    LOW = 0
    HIGH = 1

    @staticmethod
    def normalize(image,
                  params=(LOW, HIGH, NORMALIZE_DEFAULT)):
        """

        :param image:
        :param params:
        :return:
        """

        low, high, mode = params
        copy = numpy.copy(image)

        if mode == UtilityImage.NORMALIZE_DEFAULT:
            copy = (copy - 127.5) / 128

        # normalize each channel separately to [-1, 1]
        elif mode == UtilityImage.NORMALIZE_EACH_CHANNEL:
            height, width, channels = copy.shape
            for channel in range(channels):
                maximum = numpy.max(copy[:, :, channel])
                minimum = numpy.min(copy[:, :, channel])
                copy[:, :, channel] = ((copy[:, :, channel] - minimum) /
                                       numpy.clip(a=maximum - minimum, a_min=1e-10, a_max=None)
                                       ) * (high - low) + low

        # normalize all channels together to [-1, 1]
        elif mode == UtilityImage.NORMALIZE_ALL_CHANNEL:
            maximum = numpy.max(copy)
            minimum = numpy.min(copy)
            copy = ((copy - minimum) / (numpy.clip(a=maximum - minimum, a_min=1e-10, a_max=None))
                    ) * (high - low) + low

        # no normalization
        elif mode == UtilityImage.NORMALIZE_NONE:
            pass

        return copy

    @staticmethod
    def resize(image, new_size):
        """

        :param image:
        :param new_size: (new_width, new_height)
        :return:
        """
        copy = numpy.copy(image)

        copy = cv2.resize(copy,
                          new_size,
                          interpolation=cv2.INTER_LINEAR)
        return copy

    @staticmethod
    def rotate(image, center, angle):
        """

        :param image:
        :param center: rotation center (x, y)
        :param angle:
        :return:
        """

        copy = numpy.copy(image)

        rotate_mat = cv2.getRotationMatrix2D(center, angle, 1)
        copy = cv2.warpAffine(copy, rotate_mat, (copy.shape[1], copy.shape[0]))

        return copy

    @staticmethod
    def horizontally_flip(image):
        """

        :param image:
        :return:
        """

        """
        image flip
        """
        if image is None:
            print('Error: '
                  '[UtilityImage.horizontally_flip] '
                  'image_in cant be None')
            return

        copy = numpy.copy(image)
        copy = cv2.flip(copy, 1)

        return copy

    @staticmethod
    def vertical_flip(image,
                      landmark_in):
        if image is None:
            return None, None
        copy = numpy.copy(image)
        copy = cv2.flip(copy, 0)

        for i in range(numpy.size(landmark_in)):
            if i % 2 == 1:
                # vertical flip
                landmark_in[i] = 1.0 - landmark_in[i]

        return copy, landmark_in

    @staticmethod
    def draw_rectangle(image,
                       batch_rectangle,
                       batch_tag=None,
                       color=(255, 0, 0),
                       font_style=(cv2.FONT_HERSHEY_SIMPLEX,
                                   1,
                                   1,
                                   True)):
        """
        draw bounding rectangles on image
        :param image:
        :param batch_rectangle: [x1, y1, x2, y2]
        :param batch_tag: a list of str
        :param color: (B, G, R)
        :param font_style: (fontFace, fontScale, thickness)
        :return:
        """
        copy = numpy.copy(image)
        height, width, _ = copy.shape

        for index, rectangle in enumerate(batch_rectangle):
            x_1 = int(round(max(rectangle[0], 0)))
            y_1 = int(round(max(rectangle[1], 0)))
            x_2 = int(round(min(rectangle[2], width - 1)))
            y_2 = int(round(min(rectangle[3], height - 1)))

            cv2.rectangle(copy,
                          (x_1, y_1),
                          (x_2, y_2),
                          color,
                          2)

            if batch_tag is not None:
                copy = UtilityImage.draw_tag(
                    image=copy,
                    content=str(batch_tag[index]),
                    position=(x_2, y_2),
                    color=color,
                    style=font_style
                )

        return copy

    @staticmethod
    def draw_point(image,
                   batch_point,
                   color=(255, 0, 0)):
        """
        draw landmarks on image
        :param image:
        :param batch_point: shape:[None, 2]
        :param color:
        :return:
        """
        copy = numpy.copy(image)

        for x, y in batch_point:
            cv2.circle(img=copy,
                       center=(int(round(x)), int(round(y))),
                       radius=2,
                       color=color,
                       thickness=-1)

        return copy

    @staticmethod
    def draw_circle(image,
                    batch_circle,
                    batch_tag=None,
                    color=(255, 0, 0),
                    style=(cv2.FONT_HERSHEY_SIMPLEX,
                           1,
                           1)):
        """

        :param image:
        :param batch_circle:
        :param batch_tag:
        :param color:
        :param style: (fontFace, fontScale, thickness)
        :return:
        """
        copy = numpy.copy(image)

        for index, circle in enumerate(batch_circle):
            x, y, r = circle

            cv2.circle(
                img=copy,
                center=(int(round(x)),
                        int(round(y))),
                radius=int(round(r)),
                color=color
            )

            if batch_tag is not None:
                copy = UtilityImage.draw_tag(
                    image=copy,
                    content=str(batch_tag[index]),
                    position=(int(round(x + r / math.sqrt(2))),
                              int(round(y + r / math.sqrt(2)))),
                    color=color,
                    style=style
                )

        return copy

    @staticmethod
    def draw_tag(image,
                 content,
                 position,
                 color=(255, 0, 0),
                 style=(cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        1,
                        True)):
        copy = numpy.copy(image)

        if style[3]:
            cv2.rectangle(
                img=copy,
                pt1=(position[0], position[1] - style[1] * 20),
                pt2=(position[0] + style[1] * 15 * len(content), position[1]),
                color=color,
                thickness=-1
            )

        cv2.putText(
            img=copy,
            text=str(content),
            org=position,
            fontFace=style[0],
            fontScale=style[1],
            thickness=style[2],
            color=(255, 255, 255) if style[3] else color
        )
        return copy

    @staticmethod
    def add_coordinate(batch_image,
                       add_r,
                       normalize,
                       debug=False):
        """

        :param batch_image: a batch of images
        :param add_r: r coordinate=sqrt((x-width/2)^2+(y-height/2)^2)
        :param normalize:
        :param debug:
        :return:
        """

        """
        prepare
        """
        image_out = numpy.copy(batch_image)
        batch, height, width, channels = numpy.shape(image_out)

        """
        x coordinate
        """
        x_ones = numpy.ones(
            [batch, height],
            dtype=numpy.int32
        )

        x_ones = numpy.expand_dims(x_ones, -1)

        x_range = numpy.tile(
            numpy.expand_dims(
                numpy.arange(width),
                0
            ),
            [batch, 1]
        )

        x_range = numpy.expand_dims(x_range, 1)
        x_channel = numpy.matmul(x_ones, x_range)
        x_channel = numpy.expand_dims(x_channel, -1)

        """
        y coordinate
        """
        y_ones = numpy.ones(
            [batch, width],
            dtype=numpy.int32
        )
        y_ones = numpy.expand_dims(y_ones, 1)
        y_range = numpy.tile(
            numpy.expand_dims(
                numpy.arange(height),
                0
            ),
            [batch, 1]
        )
        y_range = numpy.expand_dims(y_range, -1)
        y_channel = numpy.matmul(y_range, y_ones)
        y_channel = numpy.expand_dims(y_channel, -1)

        """
        r coordinate
        """
        r_channel = numpy.sqrt(
            numpy.square(x_channel - (width - 1) / 2.0)
            + numpy.square(y_channel - (height - 1) / 2.0)
        )

        """
        normalize
        """
        if normalize:
            x_channel = x_channel / (width - 1.0) * 2.0 - 1.0
            y_channel = y_channel / (height - 1.0) * 2.0 - 1.0

            maximum = numpy.max(r_channel)
            minimum = numpy.min(r_channel)
            r_channel = ((r_channel - minimum) / (maximum - minimum)) * 2.0 - 1.0

        """
        concatenate
        """
        image_out = numpy.concatenate(
            (image_out, x_channel, y_channel),
            axis=-1
        )
        if add_r:
            if debug:
                print('Log: '
                      '[%s.%s] '
                      'add r coordinate.' % (UtilityImage.__name__,
                                             UtilityImage.add_coordinate.__name__))
            image_out = numpy.concatenate(
                (image_out, r_channel),
                axis=-1
            )

        return image_out

    VALID = 'VALID'
    SAME = 'SAME'

    @staticmethod
    def cut_out_rectangle(image,
                          rectangle,
                          padding=VALID):
        """

        :param image:
        :param rectangle: [x1, y1, x2, y2]
        :param padding: 'VALID': output valid image area; 'SAME': padding '0' if rectangle exceeds image
        :return:
        """

        image_copy = numpy.copy(image)
        rectangle = numpy.round(rectangle)

        if padding == UtilityImage.VALID:
            image_out = image_copy[
                        int(rectangle[1]):int(rectangle[3] + 1),
                        int(rectangle[0]):int(rectangle[2] + 1),
                        :
                        ]

        elif padding == UtilityImage.SAME:
            height, width, channels = image_copy.shape

            x_1 = rectangle[0]
            y_1 = rectangle[1]
            x_2 = rectangle[2]
            y_2 = rectangle[3]

            m_height = y_2 - y_1 + 1
            m_width = x_2 - x_1 + 1

            if x_1 < 0:
                m_x_1 = -x_1
                x_1 = 0
            else:
                m_x_1 = 0

            if y_1 < 0:
                m_y_1 = -y_1
                y_1 = 0
            else:
                m_y_1 = 0

            if x_2 >= width:
                m_x_2 = m_width - 1 - (x_2 - (width - 1))
                x_2 = width - 1
            else:
                m_x_2 = m_width - 1

            if y_2 >= height:
                m_y_2 = m_height - 1 - (y_2 - (height - 1))
                y_2 = height - 1
            else:
                m_y_2 = m_height - 1

            # generate crop size mask
            image_out = numpy.zeros(
                shape=(int(m_height),
                       int(m_width),
                       int(channels)),
                dtype=numpy.uint8
            )
            image_out[
            int(m_y_1):int(m_y_2) + 1,
            int(m_x_1):int(m_x_2) + 1,
            :
            ] = image_copy[
                int(y_1):int(y_2) + 1,
                int(x_1):int(x_2) + 1,
                :
                ]

        else:
            print('Error: '
                  '[%s.%s] '
                  'padding should be ''VALID'' or ''SAME'''
                  % (UtilityImage.__name__,
                     UtilityImage.cut_out_rectangle.__name__))
            image_out = None

        return image_out

    @staticmethod
    def cut_out_rectangles(image,
                           batch_rectangle,
                           size_out):
        """
        1.repair exceeding rectangles to valid rectangles, padding '0' in exceeding area
        2.resize to net input size;
        :param image:
        :param batch_rectangle:
        :param size_out: resize size
        :return: a batch of resize cropped image
        """

        copy = numpy.copy(image)

        image_height, image_width, channels = copy.shape
        batch_rectangle = numpy.around(batch_rectangle).astype(numpy.int32)
        rectangle_number = batch_rectangle.shape[0]

        batch_x_1 = batch_rectangle[:, 0]
        batch_y_1 = batch_rectangle[:, 1]
        batch_x_2 = batch_rectangle[:, 2]
        batch_y_2 = batch_rectangle[:, 3]

        batch_width = batch_x_2 - batch_x_1 + 1
        batch_height = batch_y_2 - batch_y_1 + 1

        c_x_1 = numpy.zeros(
            (batch_rectangle.shape[0],),
            numpy.int32
        )
        c_y_1 = numpy.zeros(
            (batch_rectangle.shape[0],),
            numpy.int32
        )
        c_x_2 = batch_width.copy() - 1
        c_y_2 = batch_height.copy() - 1

        index = numpy.where(numpy.greater(batch_x_2, image_width - 1))[0]
        if numpy.size(index) > 0:
            c_x_2[index] = (batch_width[index] - 1) - (batch_x_2[index] - (image_width - 1))
            batch_x_2[index] = image_width - 1

        index = numpy.where(batch_y_2 > image_height - 1)
        if numpy.size(index) > 0:
            c_y_2[index] = (batch_height[index] - 1) - (batch_y_2[index] - (image_height - 1))
            batch_y_2[index] = image_height - 1

        index = numpy.where(batch_x_1 < 0)
        if numpy.size(index) > 0:
            c_x_1[index] = 0 - batch_x_1[index]
            batch_x_1[index] = 0

        index = numpy.where(batch_y_1 < 0)
        if numpy.size(index) > 0:
            c_y_1[index] = 0 - batch_y_1[index]
            batch_y_1[index] = 0

        images_out = numpy.zeros((rectangle_number,
                                  size_out,
                                  size_out,
                                  channels),
                                 dtype=numpy.uint8)

        for i in range(rectangle_number):
            container = numpy.zeros((batch_height[i],
                                     batch_width[i],
                                     channels),
                                    dtype=numpy.uint8)
            container[
            c_y_1[i]:c_y_2[i] + 1,
            c_x_1[i]:c_x_2[i] + 1,
            :
            ] = copy[
                batch_y_1[i]:batch_y_2[i] + 1,
                batch_x_1[i]:batch_x_2[i] + 1,
                :
                ]

            images_out[i, :, :, :] = cv2.resize(
                container,
                (size_out, size_out)
            )

        return images_out

    @staticmethod
    def save_image(image,
                   category,
                   save_dir,
                   datum_from,
                   stride,
                   rotation=None,
                   landmarks=None,
                   offsets=None):
        """

        :param image:
        :param category: a list(negative:0, positive:1, partial:-1, landmark:-2).
        :param save_dir: directory of saving specific category
        :param datum_from: str
        :param stride: (folder save stride, label save stride)
        :param rotation:
        :param landmarks:
        :param offsets:
        :return:
        """

        """
        prepare
        """
        # check image
        if image is None:
            print('Error: [%s,%s] image can not be None'
                  % (UtilityImage.__name__,
                     UtilityImage.save_image.__name__))

        # get stride
        stride_folder, stride_label = stride

        # get image index
        save_dir.mkdir(parents=True, exist_ok=True)
        cache_path = save_dir / '.cache'

        if cache_path.exists():
            with open(cache_path.__str__(), 'r') as file:
                entity_index = int(file.readline().strip())
            with open(cache_path.__str__(), 'w') as file:
                file.write('%d\n' % (entity_index + 1))
        else:
            cache_path.parent.mkdir(parents=True, exist_ok=True)

            entity_index = 0
            with open(cache_path.__str__(), 'w') as file:
                file.write('%d\n' % (entity_index + 1))

        """
        save image
        """
        image_name = '%s/%d/%d.jpg' % (datum_from,
                                       int(entity_index / stride_folder),
                                       entity_index)

        image_path = save_dir / 'image' / image_name
        image_path.parent.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(filename=image_path.__str__(),
                    img=image)

        """
        save labels
        """
        label = ';' + ' '.join(map(str, category))

        if rotation is not None:
            label += ';' + ' '.join(map(str, rotation))

        if offsets is not None:
            label += ';' + ' '.join(map(str, offsets))

        if landmarks is not None:
            label += ';' + ' '.join(map(str, landmarks))

        content = image_name.__str__() + label + '\n'

        filename = Path('%d.txt' % int(entity_index / stride_label))
        label_path = save_dir / 'label' / filename
        label_path.parent.mkdir(parents=True, exist_ok=True)

        with label_path.open('a') as file:
            file.write(content)

        return entity_index


if __name__ == '__main__':
    # img = numpy.array([1, 2, 3])
    #
    # for i in range(1000):
    #     UtilityImage.save_image(
    #         image=img,
    #         category=[0, 2],
    #         save_dir=Path('./delete'),
    #         datum_from='mmlab',
    #         stride=(5, 3),
    #         rotation=[19],
    #         landmarks=[0, 1, 4, 7.0, 8.9],
    #         offsets=[0.54, 0.89, 0.13]
    #     )
    img = cv2.imread('/home/yehangyang/Desktop/crew/f_rgb_face_85100_34.jpg')

    img = UtilityImage.draw_rectangle(
        image=img,
        batch_rectangle=[
            [5, 5, 20, 20]
        ],
        batch_tag=[
            'hello'
        ],
    )

    cv2.imshow('test', img)
    cv2.waitKey(0)
