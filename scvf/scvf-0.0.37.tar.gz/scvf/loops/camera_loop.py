from scvf.constants import settings_keys


def camera_loop(img, camera_manager, settings, running):
    while running():
        if settings.is_updated():
            camera_manager.set_exposure(settings.get(settings_keys["exposure"], ""))
            camera_manager.set_camera(settings.get(settings_keys["camera_id"], ""))

        img = camera_manager.get_image()
    camera_manager.release()