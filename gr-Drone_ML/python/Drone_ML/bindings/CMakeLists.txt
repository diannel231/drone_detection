# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT Drone_ML_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT Drone_ML_sources)

########################################################################
# Check for pygccxml
########################################################################
GR_PYTHON_CHECK_MODULE_RAW(
    "pygccxml"
    "import pygccxml"
    PYGCCXML_FOUND
    )

include(GrPybind)

########################################################################
# Python Bindings
########################################################################

list(APPEND Drone_ML_python_files
    python_bindings.cc)

GR_PYBIND_MAKE_OOT(Drone_ML
   ../../..
   gr::Drone_ML
   "${Drone_ML_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET Drone_ML_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:Drone_ML_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/Drone_ML/
)

install(TARGETS Drone_ML_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/Drone_ML COMPONENT pythonapi)
