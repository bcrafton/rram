
import numpy as np

class rram:

    def __init__(self, shape, gap_min, gap_max, gap_ini, deltaGap0, model_switch, I0, g0):
        self.shape = shape
        
        # Switch to select Standard Model (0) or Dynamic Model (1)
        # parameter integer	model_switch		= 0    from[0, 1];
        self.model_switch = model_switch
  
        # The following constants have been pre-defined in the constants.vams
        # Boltzmann's constant in joules/kelvin, 'parameter real kb =  1.3806503e-23'
        # parameter real		kb = `P_K;
        self.kb = 1.3806503e-23

        # charge of electron in coulombs, 'parameter real q =  1.6e-19'
        # parameter real		q = `P_Q;
        self.q = 1.6e-19

        # average switching fitting parameters g0, V0, I0, beta, gamma0
        # parameter real		g0		= 0.25e-9 from(0:2e-9);
        self.g0 = g0
        # parameter real		V0		= 0.25    from(0:10);
        # self.V0 = 0.5
        # parameter real		Vel0		= 10    from(0:20);
        self.Vel0 = 10
        # parameter real		I0		= 1000e-6 from(0:1e-2);
        self.I0 = I0
        # parameter real		beta		= 0.8    from(0:inf);
        self.beta = 0.8
        # parameter real		gamma0		= 16  from(0:inf); 
        self.gamma0 = 16

        # threshold temperature for significant random variations
        # parameter real		T_crit		= 450		from(390, 460);
        self.T_crit = 450

        # variations fitting parameters
        # parameter real          deltaGap0	= 0.02		from[0, 0.1);
        self.deltaGap0 = deltaGap0
        # parameter real		T_smth		= 500		from(400, 600);//  activation energy for vacancy generation
        self.T_smth = 500
        # parameter real		Ea		= 0.6 from(0:1);
        self.Ea = 0.6

        # atom spacing, a0
        # parameter real		a0		= 0.25e-9 from(0:inf);
        self.a0 = 0.25e-9
        # initial room temperature in devices
        # parameter real		T_ini		= 273 + 25 from(0:inf);
        self.T_ini = 273 + 25
        # minimum field requirement to enhance gap formation, F_min
        # parameter real		F_min		= 1.4e9 from(0:3e9);
        self.F_min = 1.4e9
        # initial gap distance, gap_ini
        # parameter real		gap_ini		= 2e-10 from(0:100e-10);
        self.gap_ini = gap_ini
        # minimum gap distance, gap_min
        # parameter real		gap_min		= 2e-10 from(0:100e-10);
        self.gap_min = gap_min
        # maximum gap distance, gap_max
        # parameter real		gap_max		= 17e-10 from(0:100e-10);
        self.gap_max = gap_max
        # thermal resistance
        # parameter real		Rth		= 2.1e3 from(0:inf);
        self.Rth = 2.1e3
        # oxide thickness, thickness
        # parameter real		tox		= 12e-9 from(0:100e-9);
        self.tox = 12e-9
        
        # initial random seed
        # parameter integer	rand_seed_ini	= 0 from(-1.6e9, 1.6e9);
        # rand_seed_ini	= 0
        
        # time step boundary
        # parameter real		time_step	= 1e-9 from(1e-15, 1);
        self.time_step = 1e-9

        ### vars ? not consts.

        #  voltage V(TE, BE), Vtb; current I(TE, BE), Itb
        # real			Vtb, Itb;  
        self.Vtb = 0.
        self.Itb = 0.

        # present temperature in devices, temp
        # real			T_cur;
        self.T_cur = 0.

        # gap time derivative, gap_ddt; random gap time derivative, gap_random_ddt
        # real			gap_ddt, gap_random_ddt;
        self.gap_ddt = 0.
        self.gap_random_ddt = 0.

        # present gap status
        # real			gap;
        self.gap = self.gap_ini

        # local enhancement factor, gamma
        # real			gamma;
        # real			gamma_ini;
        self.gamma = 0.
        self.gamma_ini = 0.

        #  random number
        # integer			rand_seed;
        # real			deltaGap;
        self.random_seed = 0
        self.deltaGap = 0.

    def step(self, Vin, dt):

        # parameter real pulse_width = 20n;
        # 	analog begin
        # // bound time step
        # 		$bound_step(time_step);
        # // present Vtb, Itb, and local device temperation calculation, T_cur
        # 		Vtb = V(TE,BE);
        self.Vtb = Vin

        # Itb = I(TE,BE);
        # dont reset this to zero !!
        # self.Itb = 0 

        # it has very little effect anyways.

        # T_cur = T_ini + abs( Vtb * Itb * Rth);
        self.T_cur = self.T_ini + abs( self.Vtb * self.Itb * self.Rth)
        
        self.gamma_ini = self.gamma0
        
        if (self.Vtb < 0):
		        self.gamma_ini = 16
		        
        self.gamma = self.gamma_ini - self.beta * np.power(((self.gap)/1e-9), 3)
		
        '''
        if ((self.gamma * abs(self.Vtb) / self.tox) < self.F_min):
            self.gamma = 0
        '''
		
        # calculate next time step gap situation
        # gap time derivative - determinant part
		    # gap_ddt = - Vel0 * exp(- q * Ea / kb / T_cur) * sinh(gamma * a0 / tox * q * Vtb / kb / T_cur);
        self.gap_ddt = -self.Vel0 * np.exp(-self.q * self.Ea / self.kb / self.T_cur) * np.sinh(self.gamma * self.a0 / self.tox * self.q * self.Vtb / self.kb / self.T_cur)

        # gap time derivative - variation part
		    # deltaGap = deltaGap0 * model_switch;
        self.deltaGap = self.deltaGap0 * self.model_switch
		
		    # gap_random_ddt = $rdist_normal(rand_seed, 0, 1) * deltaGap / (1 + exp((T_crit - T_cur)/T_smth));
        # self.gap_random_ddt = np.random.uniform(0., 1.) * self.deltaGap / (1. + np.exp((self.T_crit - self.T_cur) / self.T_smth))
        self.gap_random_ddt = 0.
		
		    # gap = idt(gap_ddt+gap_random_ddt, gap_ini);
        # look this up in manual we downloaded.
		    # its just integral(a) + b
		    # so we can just start gap at gap_ini and then add these 2 each time.
        self.gap += (self.gap_ddt + self.gap_random_ddt) * dt
		
        # this just a clip func
        '''
        if(self.gap < self.gap_min):
            self.gap = self.gap_min
        elif (self.gap > self.gap_max):
            self.gap = self.gap_max
        '''
        self.gap = np.clip(self.gap, self.gap_min, self.gap_max)
		
        # self.I0 = base resistance
        # self.g0 = ratio. g0 = gap_max -> range = 834. g0 = gap_min -> range = 75k (for I0 = 1e-6)
        # self.V0 = (see test_sinh.py). exponential. how can we have exponential wrt to voltage ? 
        # self.V0 = does both range and min/max
		    
        self.Itb = self.I0 * np.exp(-self.gap / self.g0) * self.Vtb # * np.sinh(self.Vtb / self.V0)
		
        return self.Itb
    
    def R(self):
        return 1. / (self.I0 * np.exp(-self.gap / self.g0)) 
        
        
        
       

