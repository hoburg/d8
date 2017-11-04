from gpkit import units
from numpy import cos, tan, pi
import numpy as np

def get_optimal_777300ER_subs():
    """
    returns substitution dic for the TASOPT Boeing 777-300ER model
    """

    sweep = 32.583 # [deg]
    VTsweep = 28. #[deg]
    HTsweep = 33. #[deg]
    M4a = .2
    fan = 1.5958
    lpc  = 5.0
    hpc = 42./(fan*lpc)

    Mcruisemin = 0.84

    substitutions = {
            'N_{land}': 6.,
            'SPR': 10.,
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

            #BLI drag reduction factor
            'D_{reduct}': 1,

            # Fuselage subs
            'l_{nose}': 30*units('ft'),
            'f_{seat}': 0.1,
            'W\'_{seat}': 1. * units('N'),  # Seat weight determined by weight fraction instead
            'W_{cargo}': 0.1*units('N'), # Cargo weight determined by W_{avg. pass_{total}}
            'W_{avg. pass_{total}}':230.*units('lbf'),
            'f_{string}': 0.34,
            'h_{floor}': 8. * units('in'),
            '\\Delta P_{over}': 8.382 * units('psi'),

            # fuselage subs that make fuse circular
            '\\Delta R_{fuse}': 0.00001 * units('m'),
            '\\theta_{db}': 0.00001,

            # TASOPT Fuselage substitutions
            'f_{L_{total/wing}}': 1.127,

            # Power system and landing gear and engine weight fraction subs
            'f_{hpesys}': 0.01, # [TAS]
            'f_{pylon}': 0.05,

            # Fractional weights
            'f_{fadd}': 0.2,  # [TAS]
            'f_{frame}': 0.24,  # [Philippe]
            'f_{lugg,1}': 0.4,  # [Philippe]
            'f_{lugg,2}': 0.4,  # [Philippe]
            'f_{padd}': 0.35,  # [TAS]

            # Wing substitutions
            'C_{L_{w,max}}': 2.25/(cos(sweep* pi / 180.)**2), # [TAS]
            '\\tan(\\Lambda)': tan(sweep * pi / 180.),
            '\\cos(\\Lambda)': cos(sweep * pi / 180.),
            '\\eta': 0.97,
            '\\rho_0': 1.225*units('kg/m^3'),
            'b_{max}': 200 * units('ft'),
            '\\rho_{fuel}': 817.*units('kg/m^3'),  # Kerosene [TASOPT]
            'f_{wingfuel}': 0.5,
            '\\tau_{max_w}': 0.14208,
            'TipReduct': 1.0,

            # Wing fractional weights
            'FuelFrac': 0.9,
            'f_{flap}': 0.2,
            'f_{slat}': 0.1,
            'f_{aileron}': 0.04,
            'f_{lete}': 0.1,
            'f_{ribs}': 0.15,
            'f_{spoiler}': 0.02,
            'f_{watt}': 0.03,

            # VT substitutions
            'C_{D_{wm}}': 0.5, # [2] 
            'C_{L_{vt,max}}': 2.0, # [TAS]
            'V_1': 72.*units('m/s'),
            '\\rho_{TO}': 1.225*units('kg/m^3'),
            'c_{l_{vt,EO}}': 1.5, # [TAS]
            'e_{vt}': 0.8,
            'V_{land}': 75.*units('m/s'),
            '\\dot{r}_{req}': 0.175, # 10 deg/s/s yaw rate acceleration
            'y_{eng}': 32*units('ft'),
            'n_{vt}': 1.,
            'A_{vt}': 2.35,
            '\\lambda_{vt}': 0.25,
            '\\tan(\\Lambda_{vt})': tan(VTsweep * pi / 180.),  # tangent of VT sweep
            'N_{spar}': 1.,
            'f_{VT}': 0.4,
            '\\cos(\\Lambda_{vt})^3': cos(VTsweep * pi / 180.)**3,
            'c_{d_{fv}}': 0.0060,
            'c_{d_{pv}}': 0.0035,
            'V_{vt_{min}}': 0.0001,
            'Fsafetyfac': 1.8,

            # HT substitutions
            '\\lambda_{ht}': 0.32,
            '\\tan(\\Lambda_{ht})': tan(HTsweep * pi / 180.),  # tangent of HT sweep
            'C_{L_{ht,max}}': 1.5,  # [TAS]
            'C_{L_{ht,fCG}}': 0.7,
            '\\Delta x_{CG}': 11.97 * units('ft'),
            'x_{CG_{min}}': 117.31*units('ft'),
            'SM_{min}': .05,
            'f_{ht}': 0.3,
            '\\cos(\\Lambda_{ht})^3': cos(HTsweep * pi / 180.)**3,
            'c_{d_{fh}}': 0.0060,
            'c_{d_{ph}}': 0.0035,
            '\\eta_{ht}': 0.9, 

            #engine system subs
            'f_{pylon}': 0.1,
            'f_{eadd}': 0.1,

            #min altitude for start of cruise
            'MinCruiseAlt': 38000*units('ft'),

            #new engine params
            'OPR_{max}': 42,
            '\pi_{tn}': .995,
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

            'hold_{4a}': 1+.5*(1.313-1)*M4a**2,
            'r_{uc}': 0.01,
            '\\alpha_c': .156,
            'T_{t_f}': 435,

            'M_{takeoff}': .9539,

            'G_{f}': 1,

            'h_{f}': 43.003,

            'C_{p_{t1}}': 1257.3,
            'C_{p_{t2}}': 1217.0,
            'C_{p_{c}}': 1278.5,

            'HTR_{f_{SUB}}': 1-.3**2,
            'HTR_{lpc_{SUB}}': 1 - 0.6**2,

            # Minimum Cruise Mach Number
            'M_{min}': Mcruisemin,

            # engine system subs
            'r_{S_{nacelle}}': 12.,
            # nacelle drag calc parameter
            'r_{v_{nacelle}}': 1.02,
            'T_{t_{4.1_{max}}}': 1860.*units('K'),
            'f_{fuel_{res}}': .05,

            'MaxClimbTime': 15*units('min'),

            #LG subs
            'E': 205,
            'K': 2,
            'N_s': 2,
            '\\eta_s': 0.8,
            '\\lambda_{LG}': 2.5,
            '\\rho_{st}': 7850,
            '\\tan(\\gamma)': np.tan(2*np.pi/180),
            '\\tan(\\phi_{min})': np.tan(15*np.pi/180),
            '\\tan(\\psi_{max})': np.tan(75*np.pi/180),
            '\\tan(\\theta_{max})': np.tan(10*np.pi/180),
            '\\sigma_{y_c}': 470E6,
            'f_{add,m}': 1.5,
            'f_{add,n}': 1.5,
            'h_{hold}': 2,
            'h_{nacelle}': 0.5,
            'n_{mg}': 2,
            'n_{wps}': 4,
            'p_{oleo}': 1800,
            't_{nacelle}': 0.15,
            'w_{ult}': 10,
            'z_{CG}': 3.36,
            'z_{wing}': 0.84,
    }

    return substitutions
