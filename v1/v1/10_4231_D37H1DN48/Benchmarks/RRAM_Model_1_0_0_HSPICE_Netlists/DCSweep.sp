DC Operation

* The first line in a spice deck is always the title of the deck

.OPTION POST

.OPTION RUNLVL=4



.hdl rram_v_1_0_0.va



* HRS initial: set (dynamic)

*X1 in 0 rram_v_1_0_0 gap_ini = 19e-10 model_switch = 1 deltaGap0 = 5e-5

* LRS initial: reset (dynamic)

*X1 in 0 rram_v_1_0_0 gap_ini = 2e-10 model_switch = 1 deltaGap0 = 5e-5



* HRS initial: set (standard mode)

* X1 in 0 rram_v_1_0_0 gap_ini = 19e-10 model_switch = 0 deltaGap0 = 1e-4

* LRS initial: reset (standard mode)

X1 in 0 rram_v_1_0_0 gap_ini = 2e-10 model_switch = 0 deltaGap0 = 1e-4







*DC SET 

*Vin in 0 pulse 0 2  1us   4ms  4ms  1us 10ms

*DC RESET

Vin in 0 pulse 0 -2  1us   4ms  4ms  1us 10ms

.tran 1us 8.1ms START=1us 

* use .print to see the measurement result please refer to manual

.end

