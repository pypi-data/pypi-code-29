import subprocess
import os
import time

def resize_images(images_dir):
    if not os.path.exists(os.path.join(images_dir, 'for_video')):
        os.mkdir(os.path.join(images_dir, 'for_video'))
    cmd = ['ffmpeg', '-i', os.path.join(images_dir, 'image-%05d.jpg'), '-vf', 'scale=640:480',
           os.path.join(images_dir, 'for_video', 'image-%05d.jpg')]
    try:
        subprocess.check_call(cmd)
    except OSError:
        print("cmd ffmpeg not found. please install ffmpeg in your computer first")
    except subprocess.CalledProcessError as e:
        print("error when execute command, error msg: %s" % e)


def convert_images_to_video(images_dir, videos_dir):
    if not os.path.exists(images_dir):
        print("images_dir: %s not exists" % images_dir)
        return
    if not os.path.exists(videos_dir):
        os.mkdir(videos_dir)

    print("resizing images...")
    resize_images(images_dir)
    time.sleep(5)
    image_path = images_dir + '/for_video'
    image_counts = len([f for f in os.listdir(image_path)
                  if os.path.isfile(os.path.join(image_path, f)) and f.endswith('.jpg')])
    print("...finish, %d images are resized" % image_counts)

    image_iter = int(image_counts / 100)
    image_num = image_counts % 100
    movie_counts = 0
    print("start converting....")
    if image_num != 0:
        frames = str(60*image_num)
        if os.path.exists(os.path.join(videos_dir, 'slide00.mp4')):
            os.remove(os.path.join(videos_dir, 'slide00.mp4'))
        cmd = ['ffmpeg', '-start_number', '00000', '-r', '1/2', '-i', os.path.join(image_path, 'image-%05d.jpg'),
               '-c:v', 'libx264', '-r', '30', '-vframes', frames, '-pix_fmt', 'yuv420p',
               os.path.join(videos_dir, 'slide00.mp4')]
        try:
            subprocess.check_call(cmd)
        except OSError:
            print("cmd ffmpeg not found. please install ffmpeg in your computer first")
            return
        except subprocess.CalledProcessError as e:
            print("error when execute command, error msg: %s" % e)
            return
        movie_counts += 1
        time.sleep(5)

    for i in range(0, image_iter):
        start_number = "%05d" % (image_num+1)
        out_name = 'slide%02d.mp4' % movie_counts
        if os.path.exists(os.path.join(videos_dir, out_name)):
            os.remove(os.path.join(videos_dir, out_name))
        cmd = ['ffmpeg', '-start_number', start_number, '-r', '1/2', '-i', os.path.join(image_path, 'image-%05d.jpg'),
               '-c:v', 'libx264', '-r', '30', '-vframes', '6000', '-pix_fmt', 'yuv420p',
               os.path.join(videos_dir, out_name)]
        try:
            subprocess.check_call(cmd)
        except OSError:
            print("cmd ffmpeg not found. please install ffmpeg in your computer first")
            break
        except subprocess.CalledProcessError as e:
            print("error when converting images from %d to %d, error msg: %s" % (image_num, image_num+100, e))
        image_num += 100
        movie_counts += 1
        time.sleep(5)

    print("...finish, %d movies generated." % movie_counts)