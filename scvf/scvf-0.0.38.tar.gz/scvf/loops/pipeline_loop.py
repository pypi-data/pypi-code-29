from scvf.constants import settings_keys


def pipeline_loop(img, pipeline_manager, settings, output_consumer, running):
    while running():
        if settings.is_updated():
            pipeline_manager.set_pipeline(settings.get(settings_keys["pipeline_name"], ''))
        print(img)
        if img is not None:
            pipeline_manager.process(img)
            output_consumer(pipeline_manager.get_output())
