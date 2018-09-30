from find_compiler.find import find_match_in_path

def detect_toolchains(out):
  tools = []
  for f in ['clang', 'clang++', 'clang-*', 'clang++-*', 'gcc', 'gcc-*', 'g++', 'g++-*']:
    tools.extend(find_match_in_path(f))
  return tools
