/* -*- c++ -*- */
/*
 * Copyright 2023 gr-OFDM_Estimator author.
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 */

#ifndef INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_IMPL_H
#define INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_IMPL_H

#include <gnuradio/fft/fft.h>
#include <gnuradio/OFDM_Estimator/OFDM_Estimator.h>

namespace gr {
  namespace OFDM_Estimator {

    class OFDM_Estimator_impl : public OFDM_Estimator
    {
     private:
	double d_samp_rate;
	unsigned int d_signal;
	std::vector<int> d_typ_len, d_typ_cp;
	gr_complex* d_Rxx;
	fft::fft_complex_fwd* d_fft;
	unsigned int d_tmpbuflen;
	int d_min_items;
	double d_signalAvg;
	double d_Threshold;

     public:
	OFDM_Estimator_impl(double samp_rate,
		    int signal,
		    int min_items,
		    const std::vector<int>& typ_len,
		    const std::vector<int>& typ_cp);
	~OFDM_Estimator_impl();

	void message_handler_ED(pmt::pmt_t ed_msg);

	std::vector<float> autocorr(const gr_complex* in, int len);

	gr_complex* tv_autocorr(const gr_complex* in, int len, int shift);

	int round_to_list(int val, std::vector<int>* list);

	void resize_fft(int size);

	void set_samp_rate(double d_samp_rate);

	pmt::pmt_t pack_message(float subc, float time, int fft, int cp, double sig_avg, double threshold);

	//pmt::pmt_t pack_message(float subc, float time, int fft, int cp);

	// Where all the action really happens
	int work(int noutput_items,
	     gr_vector_const_void_star& input_items,
	     gr_vector_void_star& output_items);
	};

  } // namespace OFDM_Estimator
} // namespace gr

#endif /* INCLUDED_OFDM_ESTIMATOR_OFDM_ESTIMATOR_IMPL_H */
