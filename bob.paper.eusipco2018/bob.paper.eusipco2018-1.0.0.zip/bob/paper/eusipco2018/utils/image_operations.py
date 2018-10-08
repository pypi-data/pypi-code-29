#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

from __future__ import print_function

import bob.io.base
import bob.ip.base

import numpy as np
import math
import cv2


def openpose_to_bounding_box(pose):
    # pose_noneck contains coordinates for nose, neck, eyes, and ears
    # exclude neck coordinates first
    pose_noneck = np.concatenate([[pose[0]], pose[2:]])
    if not pose_noneck[0].all():
        return None
    bbx = dict(center_x=0, center_y=0, half_size=0)
    # since, some pose points are fail to be detected and become zeros,
    # exclude zeros from our computation of the bounding box
    x_nonzeros = pose_noneck[(pose_noneck[:, 0] > 0).nonzero(), 0]
    if not x_nonzeros.size:
        return None  # all key points are zeros
    xmin = x_nonzeros.min()
    xmax = x_nonzeros.max()
    # ymin = pose_noneck[:, 1].min()
    # ymax = pose_noneck[:, 1].max()
    # bbx['center_x'] = (xmax + xmin) / 2.0
    # bbx['center_y'] = (ymax + ymin) / 2.0
    # center on the nose
    bbx['center_x'] = int(pose_noneck[0, 0])
    bbx['center_y'] = int(pose_noneck[0, 1])
    bbx['half_size'] = int((xmax - xmin) / 2.0 * 1.3)
    return bbx

def get_mouth_deltas_coordinates(mouth_lmks):
    """
    Compute distances between different mouth landmark points
    Args:
        mouth_lmks: 20 points of the mouth landmarks ordered as in this image:
        http://www.pyimagesearch.com/wp-content/uploads/2017/04/facial_landmarks_68markup.jpg

    Returns:
        42 deltas between landmark points: 14 vertical, 10 horizontal, 9 right-top diagonal, and
        9 left-bottom diagonal deltas.

    """

    # vertical deltas, (5+3+3+3)=14 of them
    deltas = np.array([mouth_lmks[1:6], mouth_lmks[11:6:-1]])
    deltas = np.concatenate((deltas, np.array([mouth_lmks[13:16], mouth_lmks[19:16:-1]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[2:5], mouth_lmks[19:16:-1]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[13:16], mouth_lmks[10:7:-1]])), axis=1)
    # horizontal deltas, (5+5)=10 of them
    deltas = np.concatenate((deltas, np.array([mouth_lmks[0:3], mouth_lmks[6:3:-1]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[11:9:-1], mouth_lmks[7:9]])), axis=1)
    deltas = np.concatenate((deltas, np.array([[mouth_lmks[0]], [mouth_lmks[12]]])), axis=1)
    deltas = np.concatenate((deltas, np.array([[mouth_lmks[16]], [mouth_lmks[6]]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[13:11:-1], mouth_lmks[15:17]])), axis=1)
    deltas = np.concatenate((deltas, np.array([[mouth_lmks[19]], [mouth_lmks[17]]])), axis=1)
    # diagonal deltas, (5+5+4+4)=18 of them
    deltas = np.concatenate((deltas, np.array([[mouth_lmks[0]], [mouth_lmks[2]]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[8:12], mouth_lmks[6:2:-1]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[0:5], mouth_lmks[10:5:-1]])), axis=1)
    deltas = np.concatenate((deltas, np.array([[mouth_lmks[12]], [mouth_lmks[13]]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[19:16:-1], mouth_lmks[14:17]])), axis=1)
    deltas = np.concatenate((deltas, np.array([mouth_lmks[12:16], mouth_lmks[19:15:-1]])), axis=1)

    deltas = np.swapaxes(deltas, 0, 1)
    return np.array(deltas, dtype=np.int32)



# Calculates rotation matrix to euler angles
# The result is the same as MATLAB except the order
# of the euler angles ( x and z are swapped ).
# taken from:
# https://programtalk.com/vs2/python/8766/deepgaze/deepgaze/head_pose_estimation.py
def _rotationMatrixToEulerAngles(R):
    # assert(isRotationMatrix(R))

    # To prevent the Gimbal Lock it is possible to use
    # a threshold of 1e-6 for discrimination
    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x, y, z])


def face_pose_yaw(lmk, frame_dim):
    # 3D model points.
    model_points = np.array([
        (0.0, 0.0, 0.0),  # Nose tip
        (0.0, -330.0, -65.0),  # Chin
        (-225.0, 170.0, -135.0),  # Left eye left corner
        (225.0, 170.0, -135.0),  # Right eye right corner
        (-150.0, -150.0, -125.0),  # Left Mouth corner
        (150.0, -150.0, -125.0)  # Right mouth corner

    ], dtype=np.float32)
    tracked_points_from_dlib = [30, 8, 36, 45, 48, 54]

    if np.all(lmk) == 0:
        return None
    # import ipdb;
    # ipdb.set_trace()
    focal_length = frame_dim[0]  # width of the frame
    # first width, then height
    center = (frame_dim[0] / 2, frame_dim[1] / 2)
    # focal_length = center[0] / np.tan(60 / 2 * np.pi / 180)
    camera_matrix = np.array(
        [[focal_length, 0, center[0]],
         [0, focal_length, center[1]],
         [0, 0, 1]], dtype=np.float32
    )
    # 2D image points. If you change the image, you need to change vector
    image_points = np.array(lmk[tracked_points_from_dlib], dtype=np.float32)
    camera_distortion_coeff = np.zeros((4, 1))  # Assuming no lens distortion
    success, rotation_vector, translation_vector = cv2.solvePnP(model_points, image_points,
                                                                camera_matrix, camera_distortion_coeff,
                                                                flags=cv2.SOLVEPNP_ITERATIVE)
    rmat, _ = cv2.Rodrigues(rotation_vector)
    # pitch, yaw, and roll
    angles = _rotationMatrixToEulerAngles(rmat)
    return [angles, image_points, camera_matrix, rotation_vector, translation_vector, camera_distortion_coeff]


def just_face_yaw(lmk, frame_dim):
    res = face_pose_yaw(lmk, frame_dim)
    if res is None:
        return 0.9
    return res[0][1]  # yaw in angles


def find_yaw_line(image_points, camera_matrix, rotation_vector, translation_vector, dist_coeffs):
    projection_direction = (0, 0, 800.0)
    # Project a 3D point (0, 0, 1000.0) onto the image plane.
    # We use this to draw a line sticking out of the nose
    nose_end_point2D, jacobian = cv2.projectPoints(np.array([projection_direction]), rotation_vector,
                                                   translation_vector, camera_matrix, dist_coeffs)

    p1 = (int(image_points[0][0]), int(image_points[0][1]))
    p2 = (int(nose_end_point2D[0][0][0]), int(nose_end_point2D[0][0][1]))

    return p1, p2


# Convention for a coordinate is Matrix convention, not xy
def add_svg_head(hw):
    """
    Return .svg header

    Input: [height,width] or a tuple
    """
    return "<svg xmlns='http://www.w3.org/2000/svg'" \
    " xmlns:svg='http://www.w3.org/2000/fp'" \
    " xmlns:inkscape='http://www.inkscape.org/namespaces/inkscape'" \
    " xmlns:xlink='http://www.w3.org/1999/xlink' version='1.0'" \
    " height='{}' width='{}'>". \
    format(hw[0], hw[1])


def add_svg_tail():
    """
    Return closing tag
    """
    return "</svg>"


def add_svg_circle(hw, r, color="red"):
    """
    Return a svg circle description

    Input: for the centre, [h,w], not (x.y)
    """
    return "<circle cx='{}' cy='{}' r='{}' fill='{}' />". \
    format(hw[1], hw[0], r, color)


def add_svg_rect(hwHW, stroke=1, color="red"):
    """

    """
    return "<rect x='{}' y='{}' height='{}' width='{}' style='fill:none;stroke-width:{};stroke:{}' />". \
    format(hwHW[1], hwHW[0], hwHW[2], hwHW[3], stroke, color)


def add_svg_image(hw, filename):
    """
    """
    return "<image x='0' y='0' height='{}' width='{}' xlink:href='{}' />". \
    format(hw[0], hw[1], filename)


def save_hdf5(hdf5, sub_group_name, variables, variables_names):
    """
    """
    if len(variables_names) == len(variables):
        hdf5.create_group(sub_group_name)
        hdf5.cd(sub_group_name)
        for i in range(len(variables)):
            hdf5.set(variables_names[i], variables[i])
        hdf5.cd("..")

    else:
        print("Expect same size")


def load_hdf5(file_name):
    """
    Return the content of the .hdf5 file saved with save_hdf5() with the
    following format:

    data = {
      frame_id: {
        "mouths":    [ [h_centre, w_centre, height, width], ... ],
        "landmarks": [ [(h1,w1), (h2,w2), <68 landmarks>], ...]
      },
      ...
    }

    Multiple detection can be. In this case, data[id]["mouths"][i] and
    data[id]["landmarks"][i] correspond to the same face.

    For the landmarks, look at

      http://openface-api.readthedocs.io/en/latest/_images/dlib-landmark-mean.png

    for the order of the landmarks.
    """
    hdf5 = bob.io.base.HDF5File(file_name, 'r')

    data = {}

    for sub_group in hdf5.sub_groups():
        # Get frame index
        no_frame = sub_group[1:]
        no_frame = int(no_frame)
        if no_frame not in data:
            data[no_frame] = {}

        hdf5.cd(sub_group)

        for key in ["mouths", "landmarks", "joints"]:
            if hdf5.has_key(key):
                value = hdf5.read(key)
                data[no_frame][key] = value

        hdf5.cd("..")

    return data


def crop_mouth_from_landmarks(image,
                              landmarks,
                              mouth_size = 65,
                              crop_size = (128,128),
                              mouth_center = (64,64)):
    """
    Return the rotated-cropped image of the mouth.

    Args:

    image: input bob image (numpy array CxWxH)

    landmarks: a list of the 68 landmarks of the dlib model, in which
    the bottom of the nose is at position 33, starting from 0.
    (http://openface-api.readthedocs.io/en/latest/_images/dlib-landmark-mean.png)

    mouth_size: distance in pixel between normalised left/right mouth
    points

    crop_size: size of output image

    mouth_center: how to align the mouth

    Returns:

    crop_mouth: the image area return by bob.ip.base.FaceEyesNorm, of
    size crop_size, with the 2 mouth landmarks spaced of mouth_size

    """
    mouth_normaliser = bob.ip.base.FaceEyesNorm(eyes_distance = mouth_size,
                                                crop_size = crop_size,
                                                eyes_center = mouth_center)

    crop_mouth = mouth_normaliser(image,
                                  right_eye = tuple(landmarks[48]),
                                  left_eye =  tuple(landmarks[54]))

    return crop_mouth
