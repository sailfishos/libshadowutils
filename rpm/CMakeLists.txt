cmake_minimum_required(VERSION 3.2)

project(libshadowutils
    LANGUAGES C
    VERSION ${LIBSHADOWUTILS_VERS})

include(GNUInstallDirs)

include_directories(${libshadowutils_SOURCE_DIR}/lib)

file(GLOB LIBSHADOWUTILS_SOURCES
    "${libshadowutils_SOURCE_DIR}/lib/getdef.c"
    "${libshadowutils_SOURCE_DIR}/lib/getlong.c"
    "${libshadowutils_SOURCE_DIR}/lib/getulong.c")
file(GLOB LIBSHADOWUTILS_HEADERS
    "${libshadowutils_SOURCE_DIR}/lib/getdef.h")
set(LIBSHADOWUTILS_DOC
    "README")

# Shared library

add_library(shadowutils SHARED ${LIBSHADOWUTILS_SOURCES})
set_target_properties(shadowutils PROPERTIES
    VERSION ${LIBSHADOWUTILS_VERSION}
    SOVERSION ${LIBSHADOWUTILS_VERSION_SONAME})


# Unit tests

enable_testing()
add_executable(test_getdef test_getdef.c)
target_link_libraries(test_getdef shadowutils)
add_test(test_getdef test_getdef)


# Installation

configure_file(${libshadowutils_SOURCE_DIR}/libshadowutils.pc.in
    ${CMAKE_CURRENT_BINARY_DIR}/libshadowutils.pc
    @ONLY)

install(TARGETS shadowutils
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR})

install(FILES ${LIBSHADOWUTILS_HEADERS}
    DESTINATION include/libshadowutils)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/libshadowutils.pc
    DESTINATION ${CMAKE_INSTALL_LIBDIR}/pkgconfig)
install(FILES ${LIBSHADOWUTILS_DOC}
    DESTINATION ${CMAKE_INSTALL_DOCDIR})
