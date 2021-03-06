# Configure the version
configure_file(version.py.in version.py)

# All Python files. Copy them in the build dir to have a complete package for the tests.
file(GLOB_RECURSE python_sources RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.py)
file(GLOB_RECURSE wrap_generators RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *_desc.py)
list(REMOVE_ITEM python_sources "${wrap_generators}")
foreach(file ${python_sources})
  configure_file(${file} ${file} COPYONLY)
endforeach()

# Build any python modules
foreach(gen ${wrap_generators})
  string(REPLACE "_desc.py" "" gen ${gen})
  get_filename_component(module_name ${gen} NAME_WE)
  get_filename_component(module_dir ${gen} DIRECTORY)
  add_cpp2py_module(NAME ${module_name} DIRECTORY ${module_dir})
  target_link_libraries(${module_name} triqs_ctint_c triqs_py)
endforeach()

# Install python modules to proper location
set(PYTHON_LIB_DEST ${TRIQS_PYTHON_LIB_DEST_ROOT}/triqs_ctint)
get_property(CPP2PY_MODULES_LIST GLOBAL PROPERTY CPP2PY_MODULES_LIST)
install(TARGETS ${CPP2PY_MODULES_LIST} DESTINATION ${PYTHON_LIB_DEST})
install(FILES ${python_sources} ${CMAKE_CURRENT_BINARY_DIR}/version.py DESTINATION ${PYTHON_LIB_DEST})
