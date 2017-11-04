from gpkit import units
from numpy import cos, tan, pi
import numpy as np

def get_D8_no_BLI_subs():
        """
        returns substitution dic for the rear-engined D8 with no BLI
        """
        sweep = 13.237  # [deg]
        VTsweep = 25.0 #[deg]
        HTsweep = 8.0 #[deg]
        M4a = .2
        fan = 1.60474
        lpc  = 4.98
        hpc = 35./8.

        Mcruisemin = 0.72

        substitutions = {
                'N_{land}': 6.,
                'p_s': 81.*units('cm'),
                'n_{eng}': 2.,
                'n_{aisle}':2.,
                'W_{avg. pass}': 180.*units('lbf'),
                'W_{carry on}': 15.*units('lbf'),
                'W_{checked}':40.*units('lbf'),
                'W_{fix}': 3000.*units('lbf'),
                'w_{aisle}': 0.51*units('m'),
                'w_{seat}': 0.5*units('m'),
                'w_{sys}': 0.1*units('m'),
                'r_E': 1.,  # [TAS]
                'p_{\\lambda_{vt}}':1.6,
                '\\lambda_{cone}': 0.3,  # [TAS]
                '\\rho_{cone}': 2700.,#*units('kg/m^3'),  # [TAS]
                '\\rho_{bend}': 2700.,#*units('kg/m^3'),  # [TAS]
                '\\rho_{floor}': 2700.,#*units('kg/m^3'),  # [TAS]
                '\\rho_{skin}': 2700.,#*units('kg/m^3'),  # [TAS]
                '\\sigma_{floor}': 30000. / 0.000145, # [TAS] [Al]
                '\\sigma_{skin}': 15000. / 0.000145,  # [TAS] [Al]
                '\\sigma_{bend}': 30000. / 0.000145, # [TAS] [Al]
                '\\tau_{floor}': 30000. / 0.000145, # [TAS] [Al]
                'W\'\'_{floor}': 60.,  # [TAS]
                'W\'\'_{insul}': 22.,  # [TAS]
                'W\'_{window}': 145.*3.*units('N/m'),  # [TAS]
                'V_{mn}': 133.76*units('m/s'), 'V_{ne}':143.92*units('m/s'),

                'D_{reduct}': 1,

                # Fuselage subs
                'f_{seat}': 0.1,
                'W\'_{seat}': 1.,  # Seat weight determined by weight fraction instead
                'W_{cargo}': 0.1*units('N'), # Cargo weight determined by W_{avg. pass_{total}}
                'W_{avg. pass_{total}}':215.*units('lbf'),
                'f_{string}': 0.35,

                'h_{floor}': 5.12*units('in'),
                'w_{db}': 0.93*units('m'),
                '\\Delta P_{over}': 8.382 * units('psi'),
                'SPR': 8.,

                # TASOPT Fuselage substitutions
                'l_{nose}': 29.*units('ft'),
                'f_{L_{total/wing}}': 1.195,

                # Power system and landing gear subs
                'f_{hpesys}': 0.01, # [TAS]

                # Fractional weights
                'f_{fadd}': 0.2,  # [TAS]
                'f_{frame}': 0.25,  # [Philippe]
                'f_{lugg,1}': 0.4,  # [Philippe]
                'f_{lugg,2}': 0.1,  # [Philippe]
                'f_{padd}': 0.35,  # [TAS]

                # Wing substitutions
                'C_{L_{w,max}}': 2.15/(cos(sweep)**2), # [TAS]
                '\\tan(\\Lambda)': tan(sweep * pi / 180.),
                '\\cos(\\Lambda)': cos(sweep * pi / 180.),
                '\\eta': 0.97,
                '\\rho_0': 1.225*units('kg/m^3'),
                '\\rho_{fuel}': 817.*units('kg/m^3'),  # Kerosene [TASOPT]
                'b_{max}': 140.0 * 0.3048*units('m'),
                '\\tau_{max_w}': 0.14733,
                'f_{wingfuel}': 1.0,
                'TipReduct': 1.0,

                # Wing fractional weights
                'FuelFrac': 0.9,
                'f_{flap}': 0.2,
                'f_{slat}': 0.001,
                'f_{aileron}': 0.04,
                'f_{lete}': 0.1,
                'f_{ribs}': 0.15,
                'f_{spoiler}': 0.02,
                'f_{watt}': 0.03,

                # VT substitutions
                'C_{D_{wm}}': 0.5, # [2]
                'C_{L_{vt,max}}': 2.6, # [TAS]
                'V_1': 70.*units('m/s'),
                '\\rho_{TO}': 1.225*units('kg/m^3'),
                'c_{l_{vt,EO}}': 0.5, # [TAS]
                'e_{vt}': 0.8,
                'V_{land}': 72.*units('m/s'),
                '\\dot{r}_{req}': 0.1475, # 10 deg/s/s yaw rate acceleration
                'N_{spar}': 1,
                'f_{VT}': 0.4,
                'n_{vt}': 2.,
                'A_{vt}' : 2.2,
                '\\lambda_{vt}': 0.3,
                '\\tan(\\Lambda_{vt})': tan(VTsweep * pi / 180.),  # tangent of VT sweep
                '\\cos(\\Lambda_{vt})^3': cos(VTsweep * pi / 180.)**3,
                'c_{d_{fv}}': 0.0060,
                'c_{d_{pv}}': 0.0035,
                'V_{vt_{min}}': 0.001,#0.065,
                'Fsafetyfac': 1.0,

                # HT substitutions
                '\\alpha_{ht,max}': 2.5,
                'C_{L_{ht,max}}': 2.0, # [TAS]
                'SM_{min}': 0.05,
                '\\Delta x_{CG}': 6*units('ft'),
                'x_{CG_{min}}' : 56.02*units('ft'),
                'C_{L_{ht,fCG}}': 0.85,
                'f_{ht}': 0.3,
                '\\lambda_{ht}': 0.3,
                '\\tan(\\Lambda_{ht})': tan(HTsweep * pi / 180.),  # tangent of HT sweep
                '\\cos(\\Lambda_{ht})^3': cos(HTsweep * pi / 180.)**3,
                'c_{d_{fh}}': 0.0060,
                'c_{d_{ph}}': 0.0035,
                '\\eta_{ht}': 1, 
                
                #engine system subs
                'r_{S_{nacelle}}': 16.,
                'f_{pylon}': 0.11,
                'f_{eadd}': 0.1,

                #nacelle drag calc parameter
                'r_{v_{nacelle}}': 1.0,

                # Cabin air substitutions in AircraftP

                #set the fuel reserve fraction
                'f_{fuel_{res}}': .20,

                # Minimum Cruise Mach Number
                'M_{min}': Mcruisemin,

                'MinCruiseAlt': 38478.0*units('ft'),

                # Engine substitutions
                'OPR_{max}': 35,
                '\\pi_{tn}': .995,
                '\\pi_{b}': .94,
                '\\pi_{d}': .995,
                '\\pi_{fn}': .985,
                'T_{ref}': 288.15,
                'P_{ref}': 101.325,
                '\\eta_{HPshaft}': .978,
                '\\eta_{LPshaft}': .99,
                '\\eta_{B}': .985,

                '\\pi_{f_D}': fan,
                '\\pi_{hc_D}': hpc,
                '\\pi_{lc_D}': lpc,

                'hold_{4a}': 1.+.5*(1.313-1.)*M4a**2.,
                'r_{uc}': .01,
                '\\alpha_c': .16,
                'T_{t_f}': 435.,

                'M_{takeoff}': .9556,

                'G_{f}': 1.,

                'h_{f}': 42.5,

                'C_{p_{t1}}': 1236.5,
                'C_{p_{t2}}': 1200.4,
                'C_{p_{c}}': 1253.9,

                'HTR_{f_{SUB}}': 1. - .3 ** 2.,
                'HTR_{lpc_{SUB}}': 1. - 0.6 ** 2.,

                'T_{t_{4.1_{max}}}': 1567.*units('K'),

##                'T_{t_{4.1_{max-Cruise}}}': 1125.*units('K'),

                'MaxClimbTime': 16*units('min'),

                #LG subs
                'E': 205,
                'K': 2,
                'N_s': 2,
                '\\eta_s': 0.8,
                '\\lambda_{LG}': 2.5,
                '\\rho_{st}': 7850,
                '\\tan(\\gamma)': np.tan(5*np.pi/180),
                '\\tan(\\phi_{min})': np.tan(15*np.pi/180),
                '\\tan(\\psi_{max})': np.tan(63*np.pi/180),
                '\\tan(\\theta_{max})': np.tan(15*np.pi/180),
                '\\sigma_{y_c}': 470E6,
                'f_{add,m}': 1.5,
                'f_{add,n}': 1.5,
                'h_{hold}': 1,
                'n_{mg}': 2,
                'n_{wps}': 2,
                'p_{oleo}': 1800,
                't_{nacelle}': 0.15,
                'w_{ult}': 10,
                'z_{CG}': 2,
                'z_{wing}': 0.5,
        }

        return substitutions

