

`include "constants.vams"`include "disciplines.vams"
module rram_v_1_0_0(TE, BE);//  electrical properties, top electrode, TE, bottom electrode BE
inout			TE, BE;
electrical		TE, BE;
//  Version Parameter
parameter real		version		= 1.00 from(0:inf);
// Switch to select Standard Model (0) or Dynamic Model (1)
parameter integer	model_switch		= 0    from[0, 1];

//  The following constants have been pre-defined in the constants.vams
//  Boltzmann's constant in joules/kelvin, 'parameter real kb =  1.3806503e-23'
parameter real		kb		= `P_K;
//  charge of electron in coulombs, 'parameter real q =  1.6e-19'
parameter real		q		= `P_Q;
  //  average switching fitting parameters g0, V0, I0, beta, gamma0
parameter real		g0		= 0.25e-9 from(0:2e-9);
parameter real		V0		= 0.25    from(0:10);
parameter real		Vel0		= 10    from(0:20);
parameter real		I0		= 1000e-6 from(0:1e-2);
parameter real		beta		= 0.8    from(0:inf);
parameter real		gamma0		= 16  from(0:inf); 
//  threshold temperature for significant random variations
parameter real		T_crit		= 450		from(390, 460);
//  variations fitting parameters
parameter real          deltaGap0	= 0.02		from[0, 0.1);

parameter real		T_smth		= 500		from(400, 600);//  activation energy for vacancy generation
parameter real		Ea		= 0.6 from(0:1);
//  atom spacing, a0
parameter real		a0		= 0.25e-9 from(0:inf);
//  initial room temperature in devices
parameter real		T_ini		= 273 + 25 from(0:inf);
//  minimum field requirement to enhance gap formation, F_min
parameter real		F_min		= 1.4e9 from(0:3e9);
//  initial gap distance, gap_ini
parameter real		gap_ini		= 2e-10 from(0:100e-10);
//  minimum gap distance, gap_min
parameter real		gap_min		= 2e-10 from(0:100e-10);
//  maximum gap distance, gap_max
parameter real		gap_max		= 17e-10 from(0:100e-10);
//  thermal resistance
parameter real		Rth		= 2.1e3 from(0:inf);
//  oxide thickness, thickness
parameter real		tox		= 12e-9 from(0:100e-9);
// initial random seed
parameter integer	rand_seed_ini	= 0 from(-1.6e9, 1.6e9);
// time step boundary
parameter real		time_step	= 1e-9 from(1e-15, 1);
//  voltage V(TE, BE), Vtb; current I(TE, BE), Itb
real			Vtb, Itb;  
//  present temperature in devices, temp
real			T_cur;
//  gap time derivative, gap_ddt; random gap time derivative, gap_random_ddt
real			gap_ddt, gap_random_ddt;
//  present gap status
real			gap;
//  local enhancement factor, gamma
real			gamma;
real			gamma_ini;
//  random number
integer			rand_seed;
real			deltaGap;


parameter real		pulse_width = 20n;
	analog begin
// bound time step
		$bound_step(time_step);
// present Vtb, Itb, and local device temperation calculation, T_cur
		Vtb = V(TE,BE);
		Itb = I(TE,BE);
		T_cur = T_ini + abs( Vtb * Itb * Rth);
// initialize random seed, rand_seed
		@(initial_step) 
			rand_seed = rand_seed_ini;
			
// calculate local enhancement factor, reference RRAM_CompactModel_I.pdf
// added
		gamma_ini = gamma0;
//added		
		if(Vtb < 0) begin
			gamma_ini = 16;
		end	
		gamma = gamma_ini - beta * pow((( gap )/1e-9), 3);

		if ((gamma * abs( Vtb )/ tox) < F_min) begin
			gamma = 0;
		end
		
// calculate next time step gap situation
// gap time derivative - determinant part
		gap_ddt = - Vel0 * exp(- q * Ea / kb / T_cur) * sinh(gamma * a0 / tox * q * Vtb / kb / T_cur);
// gap time derivative - variation part
		deltaGap = deltaGap0 * model_switch;
		gap_random_ddt = $rdist_normal(rand_seed, 0, 1) * deltaGap / (1 + exp((T_crit - T_cur)/T_smth));
		gap = idt(gap_ddt+gap_random_ddt, gap_ini);
		if(gap<gap_min) begin
			gap = gap_min;
		end else if ( gap>gap_max) begin
			gap=gap_max;
		end
		Itb = I0 * exp(-gap/g0)*sinh(Vtb/V0);
		I(TE,BE)<+Itb;
		end
endmodule
