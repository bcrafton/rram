.title <test_RRAM_RESET>


*****************Important Note*************************
*This dynamic model reproduces DC switching behaviors
*by simulating stairlike voltage sweep operations using
*transient mode of HSPICE simulation.
********************************************************


.hdl RRAM_v_2_0_Beta.va

.option converge = 0
.option RUNLVL = 6
.option METHOD=GEAR 
.option INGOLD=1

.param C_RRAM = 1f
.param VDD = 2



************RRAMRC Cell*************************
.subckt RRAMRC_RESET p1 p2 
R1 p1 mid1 20
Rh mid1 mid2 2e9
Cp mid1 mid2 C_RRAM
X1 mid1 mid2 RRAM_v_2_0_Beta x0=0 w0=5e-9 Ei=0.82 Eh=1.12 deltaGap=4e-5   **x0=0, w0=5nm are initial conditions for RESET
R2 mid2 p2 20
.ends RRAMRC_RESET
***********************************************


X_RRAM 0 1 RRAMRC_RESET

Vin 1 0 PULSE 0V VDD 0 100us 100us 0 200us


.tran 0.2us 200us 

.print PAR('-I(Vin)')
.print V(1)

.end

