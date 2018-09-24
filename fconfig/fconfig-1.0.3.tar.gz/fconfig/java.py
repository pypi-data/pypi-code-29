
DIR_SEPARATOR = "/"

keywords = [
	"abstract", "assert", "boolean", "break", "byte", "case",
	"catch", "char", "class", "const", "continue",
	"default", "do", "double", "else", "extends",
	"false", "final", "finally", "float", "for",
	"goto", "if", "implements", "import", "instanceof",
	"int", "interface", "long", "native", "new",
	"null", "package", "private", "protected", "public",
	"return", "short", "static", "strictfp", "super",
	"switch", "synchronized", "this", "throw", "throws",
	"transient", "true", "try", "void", "volatile",
	"while"
]

def is_java_keyword(keyword):
	return keyword in keywords


def sanitize_property_name(property_name):
	if is_java_keyword(property_name):
		property_name += "Property"

	return property_name


def get_property_name(snake_case_property_name):
	components = snake_case_property_name.split('_')

	# We capitalize the first letter of each component except the first one
	# with the 'title' method and join them together.
	property_name =  components[0] + "".join(x.title() for x in components[1:])
	return sanitize_property_name(property_name)


def package_to_path(package_structure):
	return package_structure.replace('.', DIR_SEPARATOR)
