Pulse Operation
* The first line in a spice deck is always the title of the deck
.OPTION POST
.OPTION RUNLVL=4
.hdl rram_v_1_0_0.va

* HRS initial: set (dynamic)

*X1 in 0 rram_v_1_0_0 gap_ini = 19e-10 model_switch = 1 deltaGap0 = 0.05
* LRS initial: reset (dynamic)

*X1 in 0 rram_v_1_0_0 gap_ini = 2e-10 model_switch = 1 deltaGap0 = 0.05

* HRS initial: set (standard mode)

* X1 in 0 rram_v_1_0_0 gap_ini = 19e-10 model_switch = 0 deltaGap0 = 0.05

* LRS initial: reset (standard mode)

X1 in 0 rram_v_1_0_0 gap_ini = 2e-10 model_switch = 0 deltaGap0 = 0.05


*Pulse SET
*Vin in 0 pulse 0 1.8  10ps   10ps  10ps  100ns 200ns
*Pulse RESET
Vin in 0 pulse 0 -1.3  10ps   10ps  10ps  100ns 200ns
*.tran tstep tstop tstart delmax
.tran 1ps 205ns START=-1ns 
* use .print to see the measurement result please refer to manual
.end
