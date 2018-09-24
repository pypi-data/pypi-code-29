
import fconfig.test.common as common

from fconfig.config_data_object import ConfigDataObject


def test_datatypes():
	config = common.load_test_config_file("dataTypes")

	assert "String" == config["string"]
	assert 1 == config["int"]
	assert 1.0 == config["double"]


def test_simple_array():
	config = common.load_test_config_file("simpleArray")

	assert "array" in config
	assert isinstance(config["array"], ConfigDataObject)

	array = config["array"]

	assert 1 == array[0]
	assert 3 == array[2]
	assert 6 == array[5]


def test_two_level_array():
	config = common.load_test_config_file("twoLevelArray")

	assert "array" in config
	assert isinstance(config["array"], ConfigDataObject)

	array = config["array"]

	assert 0 in array
	assert 1 in array

	assert isinstance(array[0], ConfigDataObject);
	assert isinstance(array[1], ConfigDataObject);

	inner_map = array[0]

	assert 1 == inner_map["start"]
	assert 2 == inner_map["end"]

	inner_map = array[1]

	assert 3 == inner_map["start"]
	assert 4 == inner_map["end"]


def test_complete():
	config = common.load_test_config_file("complete")

	assert "string" == config["string"]
	assert "composed string" == config["composed_string"]
	assert 123456 == config["integer"]
	assert 3.14 == config["float"]

	assert "object" in config
	assert isinstance(config["object"], ConfigDataObject)

	object = config["object"]
	assert "test" == object["string"]
	assert 9 == object["integer"]
	assert 1.23 == object["float"]

	# / *array * /
	assert "array" in config
	assert isinstance(config["array"], ConfigDataObject)

	array = config["array"]
	assert 1 == array[0]
	assert 5 == array[1]
	assert 6 == array[2]

	# / *array of objects * /
	assert "array_of_objects" in config
	assert isinstance(config["array_of_objects"], ConfigDataObject)

	arrayOfObjects = config["array_of_objects"]
	assert 0 in arrayOfObjects
	assert isinstance(arrayOfObjects[0], ConfigDataObject)
	objectInArray = arrayOfObjects[0]
	assert 571 == objectInArray["start"]
	assert 672 == objectInArray["end"]

	# / *object with composed * /
	assert "object_with_composed" in config
	assert isinstance(config["object_with_composed"], ConfigDataObject)

	objectWithComposedVariables = config["object_with_composed"]
	assert "string that is composed" == objectWithComposedVariables["string"]
	assert "double composed string" == objectWithComposedVariables["double_composed_string"]
	assert "string that is composed within object" == objectWithComposedVariables["inner_composition"]

	# / *hierarchy * /
	assert "object_hierarchy" in config
	assert isinstance(config["object_hierarchy"], ConfigDataObject)
	objectHierarchy = config["object_hierarchy"]

	assert "inner_object" in objectHierarchy
	assert isinstance(objectHierarchy["inner_object"], ConfigDataObject)
	innerObject = objectHierarchy["inner_object"]

	assert "array_of_objects" in objectHierarchy
	assert isinstance(objectHierarchy["array_of_objects"], ConfigDataObject)
	innerArrayOfObjects = objectHierarchy["array_of_objects"]

	assert 1 in innerArrayOfObjects
	assert isinstance(innerArrayOfObjects[1], ConfigDataObject)
	animal = innerArrayOfObjects[1]

	assert "inner_inner_object" in innerObject
	assert isinstance(innerObject["inner_inner_object"], ConfigDataObject)
	innerInnerObject = innerObject["inner_inner_object"]

	assert "array" in innerInnerObject
	assert isinstance(innerInnerObject["array"], ConfigDataObject)
	innerInnerObjectArray = innerInnerObject["array"]

	assert "another_string" == objectHierarchy["another_string"]
	assert 987654 == innerObject["integer"]
	assert "string is funny to compose" == innerObject["composed"]
	assert False == innerObject["boolean"]
	assert "chicken" == animal["animal"]
	assert 2, animal["legs"]
	assert 9.87654 == innerInnerObject["float"]
	assert "string is funny to compose multiple times" == innerInnerObject["composed"]
	assert 1 == innerInnerObjectArray[0]
	assert 2 == innerInnerObjectArray[1]
	assert 3 == innerInnerObjectArray[2]