/* -*- c++ -*- */
/*
 * Copyright 2023 gr-OFDM_Estimator author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_H
#define INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_H

#include <gnuradio/OFDM_Estimator/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace OFDM_Estimator {

    /*!
     * \brief <+description of block+>
     * \ingroup OFDM_Estimator
     *
     */
    class OFDM_ESTIMATOR_API OFDM_Estimator : virtual public gr::sync_block
    {
     public:
      typedef std::shared_ptr<OFDM_Estimator> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of OFDM_Estimator::OFDM_Estimator.
       *
       * To avoid accidental use of raw pointers, OFDM_Estimator::OFDM_Estimator's
       * constructor is in a private implementation
       * class. OFDM_Estimator::OFDM_Estimator::make is the public interface for
       * creating new instances.
       */
	static sptr make(double samp_rate,
		     int signal,
		     int min_items,
		     const std::vector<int>& typ_len,
		     const std::vector<int>& typ_cp);
	virtual void set_samp_rate(double d_samp_rate) = 0;
    };

  } // namespace OFDM_Estimator
} // namespace gr

#endif /* INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_H */
