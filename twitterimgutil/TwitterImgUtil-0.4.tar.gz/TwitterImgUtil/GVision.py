import io
import os
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from google.cloud import videointelligence
from google.cloud import vision
from google.cloud.vision import types

def get_image_client(credential_file):
    return vision.ImageAnnotatorClient.from_service_account_file(credential_file)

def get_video_client(credential_file):
    return videointelligence.VideoIntelligenceServiceClient.from_service_account_file(credential_file)

def get_labels_from_image(image_client, image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    try:
        image = types.Image(content=content)
        response = image_client.label_detection(image=image)
        labels = response.label_annotations
        return [label.description for label in labels[:3]]
    except Exception as e:
        print("Error when detecting labels from image: %s" % image_path)
        print("error msg: %s" % e)
        return []

def draw_text_on_images(file_path, text, save_path):
    try:
        image = Image.open(file_path)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 24)
        width, height = image.size
        x, y = (0.1*width, 0.5*height)
        w, h = font.getsize(text)

        draw.rectangle((x, y, x+w, y+h), fill='black')
        draw.text((x, y), text, fill='white', font=font)

        image.save(save_path)
        return True
    except Exception as e:
        print("Error when writing labels for image: %s" % file_path)
        print("error msg: %s" % e)
        if os.path.exists(save_path):
            os.remove(save_path)
        return False

def draw_labels_on_images(image_client, image_dir, save_dir):
    if image_dir == save_dir:
        print("input image dir cannot equal to output save dir")
        return
    images_list = [f for f in os.listdir(image_dir)
                   if os.path.isfile(os.path.join(image_dir, f)) and f.endswith('.jpg')]
    count = 0
    for file_name in images_list:
        save_name = 'image-%05d.jpg' % count
        labels = get_labels_from_image(image_client, os.path.join(image_dir, file_name))
        if len(labels) != 0:
            labels_str = ",".join([label for label in labels])
            if draw_text_on_images(os.path.join(image_dir, file_name), labels_str,
                                   os.path.join(save_dir, save_name)) is True:
                count += 1

def get_labels_from_video(video_client, video_path, overtime=90):
    features = [videointelligence.enums.Feature.LABEL_DETECTION]
    with io.open(video_path, 'rb') as movie:
        input_content = movie.read()
    operation = video_client.annotate_video(
        input_content=input_content, features=features)
    print('\nProcessing video for label annotations:')

    result = operation.result(timeout=overtime)
    print('\nFinished processing.')

    # Process video/segment level label annotations
    segment_labels = result.annotation_results[0].segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        print('Video label description: {}'.format(
            segment_label.entity.description))
        for category_entity in segment_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))

        for i, segment in enumerate(segment_label.segments):
            start_time = (segment.segment.start_time_offset.seconds +
                          segment.segment.start_time_offset.nanos / 1e9)
            end_time = (segment.segment.end_time_offset.seconds +
                        segment.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = segment.confidence
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')

    # Process shot level label annotations
    shot_labels = result.annotation_results[0].shot_label_annotations
    for i, shot_label in enumerate(shot_labels):
        print('Shot label description: {}'.format(
            shot_label.entity.description))
        for category_entity in shot_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))

        for i, shot in enumerate(shot_label.segments):
            start_time = (shot.segment.start_time_offset.seconds +
                          shot.segment.start_time_offset.nanos / 1e9)
            end_time = (shot.segment.end_time_offset.seconds +
                        shot.segment.end_time_offset.nanos / 1e9)
            positions = '{}s to {}s'.format(start_time, end_time)
            confidence = shot.confidence
            print('\tSegment {}: {}'.format(i, positions))
            print('\tConfidence: {}'.format(confidence))
        print('\n')

    # Process frame level label annotations
    frame_labels = result.annotation_results[0].frame_label_annotations
    for i, frame_label in enumerate(frame_labels):
        print('Frame label description: {}'.format(
            frame_label.entity.description))
        for category_entity in frame_label.category_entities:
            print('\tLabel category description: {}'.format(
                category_entity.description))

        # Each frame_label_annotation has many frames,
        # here we print information only about the first frame.
        frame = frame_label.frames[0]
        time_offset = frame.time_offset.seconds + frame.time_offset.nanos / 1e9
        print('\tFirst frame time offset: {}s'.format(time_offset))
        print('\tFirst frame confidence: {}'.format(frame.confidence))
        print('\n')