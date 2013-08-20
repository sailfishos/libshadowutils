cmake_minimum_required(VERSION 2.8)

project(libshadowutils)

include_directories(${libshadowutils_SOURCE_DIR}/include)

file(GLOB LIBSHADOWUTILS_SOURCES "${libshadowutils_SOURCE_DIR}/src/*.c")
file(GLOB LIBSHADOWUTILS_HEADERS "${libshadowutils_SOURCE_DIR}/include/*.h")


# Shared library

set(LIBSHADOWUTILS_MAJOR_VERSION "0")
set(LIBSHADOWUTILS_MINOR_VERSION "0")
set(LIBSHADOWUTILS_PATCH_VERSION "1")
set(LIBSHADOWUTILS_VERSION "${LIBSHADOWUTILS_MAJOR_VERSION}.${LIBSHADOWUTILS_MINOR_VERSION}.${LIBSHADOWUTILS_PATCH_VERSION}")
set(LIBSHADOWUTILS_VERSION_SONAME "${LIBSHADOWUTILS_MAJOR_VERSION}")

add_library(shadowutils SHARED ${LIBSHADOWUTILS_SOURCES})
set_target_properties(shadowutils PROPERTIES
    VERSION ${LIBSHADOWUTILS_VERSION}
    SOVERSION ${LIBSHADOWUTILS_VERSION_SONAME})


# Unit tests

enable_testing()
add_executable(test_getdef tests/test_getdef.c)
target_link_libraries(test_getdef shadowutils)
add_test(test_getdef test_getdef)


# Installation

option(ENABLE_MULTIARCH "Enable support for multi-arch distros (lib64)" OFF)

set(LIB_DEST "lib")
if (ENABLE_MULTIARCH)
    if (${CMAKE_C_SIZEOF_DATA_PTR} EQUAL 8)
        set(LIB_DEST "lib64")
    endif()
endif()

configure_file(${libshadowutils_SOURCE_DIR}/libshadowutils.pc.in
    ${CMAKE_CURRENT_BINARY_DIR}/libshadowutils.pc
    @ONLY)

install(TARGETS shadowutils
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION ${LIB_DEST}
    ARCHIVE DESTINATION ${LIB_DEST})

install(FILES ${LIBSHADOWUTILS_HEADERS}
    DESTINATION include/libshadowutils)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/libshadowutils.pc
    DESTINATION ${LIB_DEST}/pkgconfig)
