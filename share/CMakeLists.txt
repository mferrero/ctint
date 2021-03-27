add_subdirectory(cmake)

if(NOT CMAKE_INSTALL_PREFIX STREQUAL TRIQS_ROOT)

  configure_file(ctint_tutorial.modulefile.in ctint_tutorial.modulefile @ONLY)
  configure_file(ctint_tutorialvars.sh.in ctint_tutorialvars.sh @ONLY)

  install(
    FILES
      ${CMAKE_CURRENT_BINARY_DIR}/ctint_tutorial.modulefile
      ${CMAKE_CURRENT_BINARY_DIR}/ctint_tutorialvars.sh
    DESTINATION share
  )
 
  message(STATUS "***************************************************************")
  message(STATUS "* Custom install Location. Use:                                ")
  message(STATUS "*                                                              ")
  message(STATUS "*   source ${CMAKE_INSTALL_PREFIX}/share/ctint_tutorialvars.sh      ")
  message(STATUS "*                                                              ")
  message(STATUS "* to set up the environment variables                          ")
  message(STATUS "***************************************************************")

endif()
