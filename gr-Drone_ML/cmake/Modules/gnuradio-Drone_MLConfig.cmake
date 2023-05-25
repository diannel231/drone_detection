find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_DRONE_ML gnuradio-Drone_ML)

FIND_PATH(
    GR_DRONE_ML_INCLUDE_DIRS
    NAMES gnuradio/Drone_ML/api.h
    HINTS $ENV{DRONE_ML_DIR}/include
        ${PC_DRONE_ML_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_DRONE_ML_LIBRARIES
    NAMES gnuradio-Drone_ML
    HINTS $ENV{DRONE_ML_DIR}/lib
        ${PC_DRONE_ML_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-Drone_MLTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_DRONE_ML DEFAULT_MSG GR_DRONE_ML_LIBRARIES GR_DRONE_ML_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_DRONE_ML_LIBRARIES GR_DRONE_ML_INCLUDE_DIRS)
