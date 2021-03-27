configure_file(ctint_tutorial-config.cmake.in ctint_tutorial-config.cmake @ONLY)
configure_file(ctint_tutorial-config-version.cmake.in ctint_tutorial-config-version.cmake @ONLY)
install(
  FILES
    ${CMAKE_CURRENT_BINARY_DIR}/ctint_tutorial-config.cmake
    ${CMAKE_CURRENT_BINARY_DIR}/ctint_tutorial-config-version.cmake
  DESTINATION lib/cmake/ctint_tutorial
)

install(EXPORT ctint_tutorial-targets NAMESPACE ctint_tutorial:: DESTINATION lib/cmake/ctint_tutorial)
