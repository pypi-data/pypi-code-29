
import fconfig.test.common as common

from fconfig.config_data_object import ConfigDataObject


def test_string_concatenation():
	config = common.load_test_config_file("string_concatenation")

	assert "String" == config["string"]
	assert "String composed" == config["string2"]
	assert "composed String" == config["string3"]
	assert "Stringcomposed String" == config["string4"]
	assert "String String" == config["string5"]
	assert "another String composed" == config["string6"]


def test_config_override():
	config = common.load_test_config_file("complete", "complete_override")

	assert "string replaced" == config["string"]
	assert "composed string replaced" == config["composed_string"]
	assert 654321 == config["integer"]
	assert 3.14 == config["float"]

	# / *object * /
	assert "object" in config
	assert isinstance(config["object"], ConfigDataObject)
	object = config["object"]
	assert "tset" == object["string"]
	assert 9 == object["integer"]
	assert 1.23 == object["float"]

	# / *array * /
	assert "array" in config
	assert isinstance(config["array"], ConfigDataObject)
	array = config["array"]
	assert 5 == array[0]

	# / *array  of objects * /
	assert "array_of_objects" in config
	assert isinstance(config["array_of_objects"], ConfigDataObject)
	arrayOfObjects = config["array_of_objects"]
	assert 0 in arrayOfObjects
	assert isinstance(arrayOfObjects[0], ConfigDataObject)
	objectInArray = arrayOfObjects[0]
	assert 571 == objectInArray["start"]
	assert 672 == objectInArray["end"]
	assert 1 in arrayOfObjects
	assert isinstance(arrayOfObjects[1], ConfigDataObject)
	objectInArray2 = arrayOfObjects[1]
	assert 572 == objectInArray2["start"]
	assert 673 == objectInArray2["end"]

	# / *object with composed * /
	assert "object_with_composed" in config
	assert isinstance(config["object_with_composed"], ConfigDataObject)
	objectWithComposedVariables = config["object_with_composed"]
	assert "string replaced that is composed" == objectWithComposedVariables["string"]
	assert "double composed string replaced" == objectWithComposedVariables["double_composed_string"]
	assert "string replaced that is composed within object replaced" == objectWithComposedVariables["inner_composition"]

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
	assert "string replaced is funny to compose" == innerObject["composed"]
	assert True == innerObject["boolean"]
	assert "chicken" == animal["animal"]
	assert 2 == animal["legs"]
	assert 1.23456 == innerInnerObject["float"]
	assert "string replaced is funny to compose multiple times" == innerInnerObject["composed"]
	assert 3 == innerInnerObjectArray[0]
	assert 2 == innerInnerObjectArray[1]
	assert 1 == innerInnerObjectArray[2]