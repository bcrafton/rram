.title <test_RRAM_RESET>

.hdl RRAM_v_2_0_Beta.va

.option converge = 0
.option RUNLVL = 6
.option METHOD=GEAR 
.option INGOLD=1

.param C_RRAM = 1f
.param VDD = 2
.param edge = 10ns
.param width = 80ns
.param total = 100ns



************RRAMRC Cell*************************
.subckt RRAMRC_RESET p1 p2 
R1 p1 mid1 20
Rh mid1 mid2 2e9
Cp mid1 mid2 C_RRAM
X1 mid1 mid2 RRAM_v_2_0_Beta x0=0 w0=5e-9 Ei=0.82 Eh=1.13 deltaGap=4e-5 
R2 mid2 p2 20
.ends RRAMRC_RESET
***********************************************


X_RRAM 0 1 RRAMRC_RESET

Vin 1 0 PULSE 0V VDD 0 edge edge width total


.tran 0.1ns total 

.print PAR('-I(Vin)')
.print V(1)

.end

