import os
import re

_pat_e = re.compile(r"""([&<>"'])(?!(amp|lt|gt|quot|#39);)""")
def _escape(word):
    replace_with = {
        '<': '&gt;',
        '>': '&lt;',
        '&': '&amp;',
        '"': '&quot;', # should be escaped in attributes
        "'": '&#39'    # should be escaped in attributes
    }
    return re.sub(_pat_e, lambda x: replace_with[x.group(0)], word)

class CompileEnv:

	pat0 = re.compile(r'\\([\S]+) ([\S]+)')
	pat = re.compile(r'@\{\[([^\]]+)\](?: \| (\\([\S]+) ([\S]+) )+)?\}')
	pat1 = re.compile(r'@<<(?:(!)?(\+)? ([\S]+) \?)? \(([^)]+)\) >>')
	
	basic_path = '_basic'
	united_path = '_united'
	task_path = '_task'
	
	def __init__(self, root):
		self._root = root
		self._cache = {}
		self._filepath = {}
		
	def findfile(self, relname):
		if relname in self._filepath:
			return self._filepath[relname]
		if relname[:1] == '_' and not relname.startswith(self.task_path):
			path1 = os.path.join(self._root, self.basic_path, relname[1:])
			if os.path.exists(path1):
				self._filepath[relname] = path1
				return path1
			path1 = os.path.join(self._root, self.united_path, relname[1:])
			if os.path.exists(path1):
				self._filepath[relname] = path1
				return path1
			raise IOError("No such file [%s]" % relname)
		path1 = os.path.join(self._root, self.basic_path, relname)
		if os.path.exists(path1):
			self._filepath[relname] = path1
			return path1
		path1 = os.path.join(self._root, self.united_path, relname)
		if os.path.exists(path1):
			self._filepath[relname] = path1
			return path1
		path1 = os.path.join(self._root, relname)
		self._filepath[relname] = path1
		return path1
				
	def prog(self, relname, exts):
		path = self.findfile(relname)
		if len(exts) == 0 and (path in self._cache):
			return self._cache[path]
		def replacing(m):
			ext1 = {}
			if m.group(2) :
				args = self.pat0.finditer(m.group(2))
				if args:
					for token in args:
						name = token.group(1)
						value = token.group(2)
						if value[:1] == '*':
							if value[1:] not in exts:
								continue
							value = exts[value[1:]]
						ext1[name] = value
			return self.prog(m.group(1), ext1)
		text = open(path).read()
		text = self.pat.sub(replacing, text)
		def replacing2(m):
			if m.group(3) :
				if (not m.group(1)) and (m.group(3) not in exts):
					return ''
				if m.group(1) and (m.group(3) in exts) :
					return ''
			value = m.group(4)
			if value[:1] == '*':
				value = exts[value[1:]]
			if not m.group(2):
				value = _escape(value)
			return value
		return self.pat1.sub(replacing2, text)
				
def prog(root, relname, **exts):
	cv = CompileEnv(root)
	return cv.prog(relname, exts)
