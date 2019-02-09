
import numpy as np

class rram:

    def __init__(self, x0, w0):

        self.a = 0.25e-9      # unit: m  distance between adjacent oxygen vacancy 
        self.f = 1e13         # unit: HZ  vibration frequency of oxygen atom in VO
        self.Ea = 0.7         # unit: ev  average active energy of VO
        self.Eh = 1.12        # unit: ev    hopping barrier of oxygen ion (O2-)     
        self.Ei = 0.82        # unit: ev   energy barrier between the electrode and oxide
        self.r = 1.5          # enhancement factor of external voltage
        self.alphah = 0.75e-9 # unit: m   enhancement factor in lower Ea & Eh
        self.alpha = 0.75e-9  # unit: m    enhancement factor in lower Ea & Eh
        self.Z = 1            #
        self.XT = 0.4e-9      # unit: m          
        self.VT = 0.4         # unit: V
        self.L0 = 3e-9        # unit: m     L0 is defined as the initial fixed length of the RRAM switching layer
        # self.x0 = 3e-9        # unit: m    x0 is defined as the initial length of gap region during both SET/RESET (for SET: x0=L0)
        # self.w0 = 0.5e-9  	  # unit: m    initial CF width
        self.x0 = x0
        self.w0 = w0
        self.WCF = 5e-9       # unit: m   fixed width of the RRAM switching layer
        self.weff = 0.5e-9    # unit: m     effective CF extending width
        self.I0 = 1e13        # unit: A/m^2    hopping current density in the gap region
        self.rou = 1.9635e-5  # unit: ohm*m   resistivity of the formed conductive filament (CF)
        self.pi = 3.1415926
        self.Rth = 5e5        # unit: K/W   effective thermal resistance
        self.Kb = 8.61733e-5  # unit: ev/K
        self.T0 = 300.        # unit: K   ambient temperature

        self.switch = 1      # switch = 1: variation-included ; switch = 0: no variations
        self.deltaGap	= 4e-5 #	gap distance variation amplitude
        self.deltaCF = 1e-4  # filament radius variation amplitude
        self.crit_x = 0.5e-9 # decided by measured variation amplitude
        self.user_seed = 0   # specified user seed for random number generator 

        self.Temp = self.T0
        self.x = self.x0
        self.w = self.w0
        
        self.Itb = 0.

        self.gap_random_ddt = 0.
        self.cf_random_ddt = 0.

    def step(self, Vtb, dt):
    
        dxr1 = 0.
        dxr2 = 0.
        dxs = 0.
        dx = 0.  
        dw = 0.

        self.Temp = self.T0 + abs(self.Itb * Vtb) * self.Rth
        I1 = self.I0 * np.pi*(self.WCF * self.WCF / 4. - self.w * self.w / 4.) * np.exp(-self.L0 / self.XT) * np.sinh(Vtb / self.VT)
        RCF = self.rou * (self.L0 - self.x) / (np.pi * self.w * self.w / 4.)         
        Vg = Vtb - (self.Itb - I1) * RCF

        ###############################

        if ( Vtb > 0 ):
        
            if ( self.x > 0. ):
                dxs = -self.a * self.f * np.exp(-(self.Ea - Vg * self.alpha * self.Z / self.x) / (self.Kb * self.Temp))
                if ( abs(dxs) <= 1e2 ):
                    dx = dxs
                else:
                    dx = -1e2
            elif ( self.x <= 0. ):
                dx = 0.
			
            if ( self.w < self.WCF ):
                # why are we multiplying by 0...
                dw = (self.x > 0.) * 0. + (self.x <= 0.) * (self.weff + np.power(self.weff, 2) / (2 * self.w)) * self.f * np.exp(-(self.Ea-Vtb * self.alpha * self.Z / self.L0) / (self.Kb * self.Temp))
                if ( dw > 1e2 ):
                    dw = 1e2	      
            elif ( self.w >= self.WCF):
                dw = 0.

        elif ( Vtb < 0. ):
            dw = 0.
            if ( self.x <= 0. ): 
                dxr1 = self.a * self.f * np.exp(-(self.Ei + self.r * self.Z * Vg) / (self.Kb * self.Temp))
                dx = dxr1
            elif ( self.x > 0. ):
                if ( self.x < self.L0 ):
	                  dxr1 = self.a * self.f * np.exp(-(self.Ei + self.r * self.Z * Vg) / (self.Kb * self.Temp))
	                  dxr2 = self.a * self.f * np.exp(-self.Eh / (self.Kb * self.Temp)) * np.sinh(self.alphah * self.Z * -1. * Vg / (self.x * self.Kb * self.Temp))
	                  dx = (dxr1 < dxr2) * dxr1 + (dxr2 <= dxr1) * dxr2
                elif ( self.x >= self.L0 ):
                    dx = 0.

        elif ( Vtb == 0. ):
            dx = 0.
            dw = 0.
			  
			  ###############################
			    
        if ( Vtb == 0. ):
            self.Itb = 0.
            
        elif ( Vtb > 0. ):
            if ( self.x > 0. ):
                self.Itb = I1 + self.I0 * np.pi * (self.w * self.w / 4.) * np.exp(-self.x / self.XT) * np.sinh(Vg/self.VT)
            elif ( self.x <= 0. ):
                self.Itb = I1 + Vtb / (self.rou * self.L0 / (np.pi * self.w * self.w / 4.))  
                
        elif ( Vtb < 0. ):
            self.Itb = I1 + self.I0 * np.pi * (self.w * self.w / 4.) * np.exp(-self.x / self.XT) * np.sinh(Vg / self.VT)

        ###############################

        if ( self.switch ):
            if ( Vtb > 0. ):
                if ( dw == 0. ):
	                  self.cf_random_ddt = 0.
                else:
	                  self.cf_random_ddt = np.random.uniform(low=0., high=1.) * self.deltaCF
	                  
            elif ( Vtb < 0. ):
                if ( self.x < self.crit_x ):
	                  self.gap_random_ddt = 0.
                elif ( self.x >= self.crit_x ):
	                  self.gap_random_ddt = np.random.uniform(low=0., high=1.) * self.deltaGap
	              
            else:
                self.gap_random_ddt = 0.
                self.cf_random_ddt = 0.

        else:
            self.gap_random_ddt = 0.
            self.cf_random_ddt = 0.

        self.x += (dx + self.gap_random_ddt) * dt
        self.w += (dw + self.cf_random_ddt) * dt

        if ( self.x < 0. ):
            self.x = 0.
        if ( self.x > self.L0 ):
            self.x = self.L0
        if ( self.w > self.WCF ):
            self.w = self.WCF

        return self.Itb




