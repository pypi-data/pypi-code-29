import oyaml as yaml

from edam.reader.models import Station
from edam.reader.models import UnitsOfMeasurement
from edam.reader.utilities import check_compatibility_among_templates, create_relation_among_units, check_if_path_exists
from edam.viewer.app.InvalidUsage import InvalidUsage
from edam.viewer.app.TargetTemplate import TargetTemplate


def render_target_template_meta(targetTemplateFileName):
    templateFile = "%s.tmpl" % targetTemplateFileName
    templateExists, templateFile_type, templateFile_path, templateFile_object = check_if_path_exists(templateFile)
    
    if not templateExists:
        raise InvalidUsage(status_code=500, message='*%s* template does not exist' % (
            targetTemplateFileName))
    
    metadataFile = "%s.yaml" % targetTemplateFileName
    metadataExists, metadataFile_type, metadataFile_path, metadataFile_object = check_if_path_exists(metadataFile)
    
    try:
        content = yaml.load(metadataFile_object)
    except yaml.YAMLError as exc:
        return exc
    
    all_observable_ids = list()
    units_as_dict = dict()
    if content['Units of Measurement'] is None:
        raise InvalidUsage(status_code=500, message='*%s* template does not have metadata' % (
            targetTemplateFileName))
    
    else:
        for counter, uom in enumerate(content['Units of Measurement']):
            uom_as_dict = uom  # type: dict
            if uom_as_dict['relevant_observables'] == '':
                relevant_observables = all_observable_ids
            else:
                relevant_observables = uom_as_dict['relevant_observables'].split(',')  # type: list
                # remove spaces
                relevant_observables = map(str.strip, relevant_observables)
                # No need to keep it any more
            del uom_as_dict['relevant_observables']
            unit = UnitsOfMeasurement.fromdictionary(uom_as_dict)
            
            unit_id = counter + 1
            
            unit.id = unit_id
            for template_id in relevant_observables:
                units_as_dict[template_id] = unit.symbol
    target_template = TargetTemplate(name=targetTemplateFileName, mappings=units_as_dict,
                                     filepath=templateFile_path)

    return target_template


def check_template_source_compatibility(target_template_object: TargetTemplate, station_object: Station):
    """
    :param target_template_object:
    :param station_object:
    :return:
    """
    error_to_return = None
    target_observable_ids = target_template_object.mappings
    station_observable_ids = {helper.observable_id: helper.uom.symbol for helper in station_object.helper}
    match, mapping, error_to_return = check_compatibility_among_templates(source_template=station_object.name,
                                                                          target_template=target_template_object.name)

    if match:
        final_mapping = create_relation_among_units(source=station_observable_ids, target=target_observable_ids,
                                                    mapping=mapping)
        return True, final_mapping
    else:
        if error_to_return is None:
            error_to_return = InvalidUsage(status_code=500,
                                           message='*%s* station and *%s* template are incompatible' % (
                                               station_object.name, target_template_object.name))
    
        return error_to_return, None


if __name__ == "__main__":
    render_target_template_meta("Yucheng")
