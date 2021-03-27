file(GLOB_RECURSE sources *.cpp)
add_library(ctint_tutorial_c ${sources})

# Link against triqs and enable warnings
target_link_libraries(ctint_tutorial_c PUBLIC triqs PRIVATE project_warnings)

# Configure compilation
target_compile_options(ctint_tutorial_c PUBLIC -fPIC)
target_include_directories(ctint_tutorial_c PUBLIC $<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/c++>)
target_compile_definitions(ctint_tutorial_c PUBLIC
				CTINT_TUTORIAL_GIT_HASH=${PROJECT_GIT_HASH}
				TRIQS_GIT_HASH=${TRIQS_GIT_HASH}
				$<$<CONFIG:Debug>:CTINT_TUTORIAL_DEBUG>
				$<$<CONFIG:Debug>:TRIQS_DEBUG>
				$<$<CONFIG:Debug>:TRIQS_ARRAYS_ENFORCE_BOUNDCHECK>
			  )

# Install library and headers
install(TARGETS ctint_tutorial_c EXPORT ctint_tutorial-targets DESTINATION lib)
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} DESTINATION include FILES_MATCHING PATTERN "*.hpp" PATTERN "*.h")


# ========= Static Analyzer Checks ==========

option(ANALYZE_SOURCES OFF "Run static analyzer checks if found (clang-tidy, cppcheck)")
if(ANALYZE_SOURCES)

  # Locate static analyzer tools
  find_program(CPPCHECK_EXECUTABLE NAMES "cppcheck" PATHS ENV PATH)
  find_program(CLANG_TIDY_EXECUTABLE NAMES "clang-tidy" PATHS ENV PATH)

  # Run clang-tidy if found
  if(CLANG_TIDY_EXECUTABLE)
    message(STATUS "clang-tidy found: ${CLANG_TIDY_EXECUTABLE}")
    set_target_properties(ctint_tutorial_c PROPERTIES CXX_CLANG_TIDY "${CLANG_TIDY_EXECUTABLE}")
  else()
    message(STATUS "clang-tidy not found in $PATH. Please consider installing clang-tidy for additional checks!")
  endif()

  # Run cppcheck if found
  if(CPPCHECK_EXECUTABLE)
    message(STATUS "cppcheck found: ${CPPCHECK_EXECUTABLE}")
    add_custom_command(
	TARGET ctint_tutorial_c
	COMMAND ${CPPCHECK_EXECUTABLE}
	  --enable=warning,style,performance,portability
	  --std=c++17
	  --template=gcc
	  --verbose
	  --quiet
          ${sources}
    )
  else()
    message(STATUS "cppcheck not found in $PATH. Please consider installing cppcheck for additional checks!")
  endif()

endif()


# ========= Dynamic Analyzer Checks ==========

option(ASAN OFF "Compile library and executables with LLVM Address Sanitizer")
option(UBSAN OFF "Compile library and executables with LLVM Undefined Behavior Sanitizer")

if(ASAN)
  find_package(sanitizer REQUIRED "asan")
  target_link_libraries(ctint_tutorial_c PUBLIC asan)
  install(TARGETS asan EXPORT ctint_tutorial-targets)
endif()
if(UBSAN)
  find_package(sanitizer REQUIRED "ubsan")
  target_link_libraries(ctint_tutorial_c PUBLIC ubsan)
  install(TARGETS ubsan EXPORT ctint_tutorial-targets)
endif()
