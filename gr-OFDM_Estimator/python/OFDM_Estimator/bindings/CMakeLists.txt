# Copyright 2020 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

########################################################################
# Check if there is C++ code at all
########################################################################
if(NOT OFDM_Estimator_sources)
    MESSAGE(STATUS "No C++ sources... skipping python bindings")
    return()
endif(NOT OFDM_Estimator_sources)

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

list(APPEND OFDM_Estimator_python_files
    OFDM_Estimator_python.cc python_bindings.cc)

GR_PYBIND_MAKE_OOT(OFDM_Estimator
   ../../..
   gr::OFDM_Estimator
   "${OFDM_Estimator_python_files}")

# copy bindings extension for use in QA test module
add_custom_command(TARGET OFDM_Estimator_python POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:OFDM_Estimator_python>
    ${PROJECT_BINARY_DIR}/test_modules/gnuradio/OFDM_Estimator/
)

install(TARGETS OFDM_Estimator_python DESTINATION ${GR_PYTHON_DIR}/gnuradio/OFDM_Estimator COMPONENT pythonapi)
