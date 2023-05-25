find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_ENERGY_DETECTOR gnuradio-Energy_Detector)

FIND_PATH(
    GR_ENERGY_DETECTOR_INCLUDE_DIRS
    NAMES gnuradio/Energy_Detector/api.h
    HINTS $ENV{ENERGY_DETECTOR_DIR}/include
        ${PC_ENERGY_DETECTOR_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_ENERGY_DETECTOR_LIBRARIES
    NAMES gnuradio-Energy_Detector
    HINTS $ENV{ENERGY_DETECTOR_DIR}/lib
        ${PC_ENERGY_DETECTOR_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-Energy_DetectorTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_ENERGY_DETECTOR DEFAULT_MSG GR_ENERGY_DETECTOR_LIBRARIES GR_ENERGY_DETECTOR_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_ENERGY_DETECTOR_LIBRARIES GR_ENERGY_DETECTOR_INCLUDE_DIRS)
