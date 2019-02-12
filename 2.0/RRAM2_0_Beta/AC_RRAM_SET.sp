.title <AC_RRAM_SET>

.hdl RRAM_v_2_0_Beta.va

.option converge = 0
.option RUNLVL = 6
.option METHOD=GEAR 
.option INGOLD=1

.param C_RRAM = 1f
.param VDD = 2
.param Vselect = 1.28
.param edge = 10ns
.param width = 80ns
.param total = 100ns


************RRAMRC_SET Cell*************************
.subckt RRAMRC_SET p1 p2 
R1 p1 mid1 20
Rh mid1 mid2 2e9
Cp mid1 mid2 C_RRAM
X1 mid1 mid2 RRAM_v_2_0_Beta x0=3e-9 w0=0.5e-9 
R2 mid2 p2 20
.ends RRAMRC_SET
***********************************************


********1T-1R test structure*********
M1 d g 0 0 mos1 W=10u L=1u
.model mos1 NMOS LEVEL=1 VTO=0.7 KP=6E-5

X_RRAM 1 d RRAMRC_SET

Vsl g 0 PULSE Vselect Vselect 0 edge edge width total
Vin 1 0 PULSE 0V VDD 0 edge edge width total


.tran 0.1ns total

.print PAR('-I(Vin)')
.print V(1)
.end

