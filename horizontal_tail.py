"""D8 horizontal tail model linked with a simple flight profile"""
from numpy import pi, tan
import numpy as np
from gpkit import Variable, Model, units, SignomialsEnabled, Vectorize, SignomialEquality
from gpkit.tools import te_exp_minus1
from gpkit.constraints.tight import Tight as TCS
from wingbox import WingBox

class HorizontalTailNoStruct(Model):
    """
    horizontal tail model from Philippe's thesis
    as a performance model without the wing box
    SKIP VERIFICATION

    References:
    [1] TASOPT code
    [2] http://adg.stanford.edu/aa241/stability/staticstability.HTml

    This model does not include the effects of wing downwash on tail
    effectiveness.
    """
    def setup(self):

        #variables
        p       = Variable('p_{ht}', '-', 'Substituted variable = 1 + 2*taper')
        q       = Variable('q_{ht}', '-', 'Substituted variable = 1 + taper')
        etaht   = Variable('\\eta_{ht}', '-', 'Tail efficiency')
        tanLh   = Variable('\\tan(\\Lambda_{ht})', '-',
                           'tangent of horizontal tail sweep')
        taper   = Variable('\lambda_{ht}', '-', 'Horizontal tail taper ratio')
        tau     = Variable('\\tau_{ht}', '-',
                           'Horizontal tail thickness/chord ratio')
        xcght   = Variable('x_{CG_{ht}}', 'm', 'Horizontal tail CG location')
        ymac    = Variable('y_{\\bar{c}_{ht}}', 'm',
                           'Spanwise location of mean aerodynamic chord')
        dxlead  = Variable('\\Delta x_{lead_{ht}}', 'm',
                            'Distance from CG to horizontal tail leading edge')
        dxtrail = Variable('\\Delta x_{trail_{ht}}', 'm',
                            'Distance from CG to horizontal tail trailing edge')
        lht     = Variable('l_{ht}', 'm', 'Horizontal tail moment arm')
        ARht     = Variable('AR_{ht}', '-', 'Horizontal tail aspect ratio')
        amax    = Variable('\\alpha_{ht,max}', '-', 'Max angle of attack, htail')
        e       = Variable('e_{ht}', '-', 'Oswald efficiency factor')
        Sh      = Variable('S_{ht}', 'm^2', 'Horizontal tail area')
        bht     = Variable('b_{ht}', 'm', 'Horizontal tail span')
        chma    = Variable('\\bar{c}_{ht}', 'm', 'Mean aerodynamic chord (ht)')
        croot   = Variable('c_{root_{ht}}', 'm', 'Horizontal tail root chord')
        ctip    = Variable('c_{tip_{ht}}', 'm', 'Horizontal tail tip chord')
        Lmax    = Variable('L_{ht_{max}}', 'N', 'Maximum load')
        fl      = Variable(r"f(\lambda_{ht})", '-',
                           'Empirical efficiency function of taper')
        CLhmax  = Variable('C_{L_{ht,max}}', '-', 'Max lift coefficient')
        CLfCG = Variable('C_{L_{ht,fCG}}', '-', 'HT CL During Max Forward CG')

        #new variables
        Vh = Variable('V_{ht}', '-', 'Horizontal Tail Volume Coefficient')
        mrat = Variable('m_{ratio}', '-', 'Wing to Tail Lift Slope Ratio')
        #variable just for the D8
        cattach = Variable('c_{attach}', 'm', 'HT Chord Where it is Mounted to the VT')

        #constraints
        constraints = []

        with SignomialsEnabled():

            constraints.extend([
                # Moment arm and geometry -- same as for vtail
                TCS([dxlead + ymac * tanLh + 0.25 * chma >= lht], reltol=1e-2),  # [SP]
                TCS([dxlead + croot <= dxtrail]),
                p >= 1 + 2*taper,
                2*q >= 1 + p,
                ymac == (bht/3)*q/p,

                SignomialEquality((2./3)*(1 + taper + taper**2)*croot/q,
                     chma),
                taper == ctip/croot,
                SignomialEquality(Sh, bht*(croot + ctip)/2),

                # Oswald efficiency
                # Nita, Scholz,
                # "Estimating the Oswald factor from basic
                # aircraft geometrical parameters"
                TCS([fl >= (0.0524*taper**4 - 0.15*taper**3
                            + 0.1659*taper**2
                            - 0.0706*taper + 0.0119)], reltol=0.2),
                # NOTE: slightly slack
                TCS([e*(1 + fl*ARht) <= 1]),

                ARht == bht**2/Sh,

                taper >= 0.2, # TODO: make less arbitrary
                taper <= 1,
                ])

        return constraints

class HorizontalTailPerformance(Model):
    """
    Horizontal tail performance model
    SKIP VERIFICATION

    ARGUMENTS
    ---------
    fitDrag: True = use Martin's tail drag fits, False = use the TASOPT tail drag model
    """
    def setup(self, ht, state, fitDrag):
        self.HT = ht

        #variables
        D       = Variable('D_{ht}', 'N', 'Horizontal tail drag')
        Lh      = Variable('L_{ht}', 'N', 'Horizontal tail downforce')
        Rec     = Variable('Re_{c_h}', '-',
                           'Cruise Reynolds number (Horizontal tail)')
        CLah    = Variable('C_{L_{\\alpha,ht}}', '-', 'Lift curve slope (htail)')
        CLah0   = Variable('C_{L_{\\alpha,ht_0}}', '-',
                           'Isolated lift curve slope (htail)')
        CLh     = Variable('C_{L_{ht}}', '-', 'Lift coefficient (htail)')
        CDh     = Variable('C_{D_{ht}}', '-', 'Horizontal tail drag coefficient')
        CD0h    = Variable('C_{D_{0,ht}}', '-',
                           'Horizontal tail parasitic drag coefficient')

        alphah   = Variable('\\alpha_{ht}', '-', 'Horizontal tail angle of attack')

        constraints = []

        with SignomialsEnabled():

            constraints.extend([
                Lh == 0.5*state['\\rho']*state['V']**2*self.HT['S_{ht}']*CLh,

                # Angle of attack and lift slope constraints
                CLh == CLah*alphah,
                alphah <= self.HT['\\alpha_{ht,max}'],
                # Currently using TAT to approximate
                CLah0 == 2*3.14,

                # Drag
                D == 0.5*state['\\rho']*state['V']**2*self.HT['S_{ht}']*CDh,
                CDh >= CD0h + CLh**2/(pi*self.HT['e_{ht}']*self.HT['AR_{ht}']),

                #cruise Reynolds number
                Rec == state['\\rho']*state['V']*self.HT['\\bar{c}_{ht}']/state['\\mu'],
             ])

        if fitDrag:
            constraints.extend([
                #Martin's TASOPT tail drag fit
                   CD0h**6.48983 >= (5.28751e-20 * (Rec)**0.900672 * (self.HT['\\tau_{ht}'])**0.912222 * (state['M'])**8.64547
                        + 1.67605e-28 * (Rec)**0.350958 * (self.HT['\\tau_{ht}'])**6.29187 * (state['M'])**10.2559
                        + 7.09757e-25 * (Rec)**1.39489 * (self.HT['\\tau_{ht}'])**1.96239 * (state['M'])**0.567066
                        + 3.73076e-14 * (Rec)**-2.57406 * (self.HT['\\tau_{ht}'])**3.12793 * (state['M'])**0.448159
                        + 1.44343e-12 * (Rec)**-3.91046 * (self.HT['\\tau_{ht}'])**4.66279 * (state['M'])**7.68852)

                #Philippe thesis drag fit
##                CD0h**0.125 >= 0.19*(self.HT['\\tau_{ht}'])**0.0075 *(Rec)**0.0017
##                            + 1.83e+04*(self.HT['\\tau_{ht}'])**3.54*(Rec)**-0.494
##                            + 0.118*(self.HT['\\tau_{ht}'])**0.0082 *(Rec)**0.00165
##                            + 0.198*(self.HT['\\tau_{ht}'])**0.00774*(Rec)**0.00168,
                ])
        else:
            #HT drag constraints in AircraftP
            None

        return constraints

class HorizontalTail(Model):
    """
    horiziontal tail model from Philippe's thesis
    as a performance model without the wing box
    SKIP VERIFICATION

    References:
    [1] TASOPT code
    [2] http://adg.stanford.edu/aa241/stability/staticstability.HTml
    """
    def setup(self):
        self.HTns = HorizontalTailNoStruct()
        self.wb = WingBox(self.HTns, "horizontal_tail")

        #HT system weight variable
        Wht = Variable('W_{ht}', 'N', 'HT System Weight')
        fht = Variable('f_{ht}' ,'-', 'Rudder etc. fractional weight')

        #margin and sensitivity
        Cht = Variable('C_{ht}', 1, '-', 'HT Weight Margin and Sensitivity Factor')

        #variables only used for the TASOPT tail drag formulation
        cdfh = Variable('c_{d_{fh}}', '-', 'VT friction drag coefficient')
        cdph = Variable('c_{d_{ph}}', '-', 'VT pressure drag coefficient')
        coslamcube = Variable('\\cos(\\Lambda_{ht})^3', '-', 'Cosine of tail sweep cubed')

        constraints = []
        with SignomialsEnabled():
            constraints.append([
                self.wb['L_{ht_{rect}}'] >= self.HTns['L_{ht_{max}}']/2.*self.HTns['c_{tip_{ht}}']*self.HTns['b_{ht}']/self.HTns['S_{ht}'],
                self.wb['L_{ht_{tri}}'] >= self.HTns['L_{ht_{max}}']/4.*(1-self.wb['taper'])*self.HTns['c_{root_{ht}}']*self.HTns['b_{ht}']/self.HTns['S_{ht}'], #[SP]
                Wht >= Cht*(self.wb['W_{struct}'] + self.wb['W_{struct}']  * fht),
            ])

        return self.HTns, self.wb, constraints


    def dynamic(self, state, fitDrag):
        """"
        creates a horizontal tail performance model
        """
        return HorizontalTailPerformance(self, state, fitDrag)

## Old code not maintained. Can be used for subsystem testing.

##if __name__ == '__main__':
##    plot = True
##
##    #build required submodels
##    aircraft = Aircraft()
##
##    substitutions = {
####            'V_{stall}': 120,
##            'R_{req}': 500, #('sweep', np.linspace(500,2000,4)),
##            'CruiseAlt': 30000, #('sweep', np.linspace(20000,40000,4)),
##            'numeng': 2,
##            'W_{pass}': 91 * 9.81,
##            'n_{pass}': 150,
##            'pax_{area}': 1,
##            'e': .9,
##            'b_{max}': 60,
##
##            #HT subs
##            'C_{L_{ht,max}}': 2.5,
##            '\\tan(\\Lambda_{ht})': tan(30*pi/180),
##            'w_{fuse}': 6,
##            'c_{m_{w}}': 1,
##            'C_{L_{max}}': 2,
##            '\\alpha_{ht,max}': 2.5,
##            'SM_{min}': 0.5,
##            '\\Delta x_{CG}': 4,
##
####            'x_{CG}': [17, 18],
##            #think about how to constrain this
##            'x_w': 19,
##            'mac': 2,
##            }
##    mission = Mission(aircraft)
##    m = Model(mission['W_{f_{total}}'], [aircraft, mission], substitutions)
##    sol = m.localsolve(solver='mosek', verbosity = 4)
##
##import matplotlib.pyplot as plt
##from gpkit.small_scripts import mag
##from simple_ac_imports_no_engine import Wing, Fuselage, Engine, CruiseP, ClimbP, FlightState, CruiseSegment, ClimbSegment

##    class Aircraft(Model):
##    "Aircraft class"
##    def setup(self):
##        #create submodels
##        self.fuse = Fuselage()
##        self.wing = Wing()
##        self.engine = Engine()
##        self.HT = HorizontalTail()
##
##        #variable definitions
##        numeng = Variable('numeng', '-', 'Number of Engines')
##        Vne     = Variable('V_{ne}', 144, 'm/s', 'Never exceed velocity')
##        rho0    = Variable('\\rho_0', 1.225, 'kg/m^3', 'Air density (0 ft)')
##
##        SMmin = Variable('SM_{min}', '-', 'Minimum Static Margin')
##        dxCG = Variable('\\Delta x_{CG}', 'm', 'Max CG Travel Range')
##
##        constraints = []
##
##        constraints.extend([
##            numeng == numeng, #need numeng in the model
##            ])
##
##        self.components = [self.fuse, self.wing, self.engine, self.HT]
##
##        return self.components, constraints
##
##    def dynamic(self, state):
##        """
##        creates an aircraft climb performance model, given a state
##        """
##        return AircraftP(self, state)
##
##    def climb_dynamic(self, state):
##        """
##        creates an aircraft climb performance model, given a state
##        """
##        return ClimbP(self, state)
##
##    def cruise_dynamic(self, state):
##        """
##        creates an aircraft cruise performance model, given a state
##        """
##        return CruiseP(self, state)
##
##class AircraftP(Model):
##    """
##    aircraft performance models superclass, contains constraints true for
##    all flight segments
##    """
##    def  setup(self, aircraft, state):
##        #make submodels
##        self.aircraft = aircraft
##        self.wingP = aircraft.wing.dynamic(state)
##        self.fuseP = aircraft.fuse.dynamic(state)
##        self.engineP = aircraft.engine.dynamic(state)
##        self.HTP = aircraft.HT.dynamic(aircraft.fuse, aircraft.wing, state)
##
##        self.Pmodels = [self.wingP, self.fuseP, self.engineP, self.HTP]
##
##        #variable definitions
##        Vstall = Variable('V_{stall}', 'knots', 'Aircraft Stall Speed')
##        D = Variable('D', 'N', 'Total Aircraft Drag')
##        W_avg = Variable('W_{avg}', 'N', 'Geometric Average of Segment Start and End Weight')
##        W_start = Variable('W_{start}', 'N', 'Segment Start Weight')
##        W_end = Variable('W_{end}', 'N', 'Segment End Weight')
##        W_burn = Variable('W_{burn}', 'N', 'Segment Fuel Burn Weight')
##        WLoadmax = Variable('W_{Load_{max}}', 'N/m^2', 'Max Wing Loading')
##        WLoad = Variable('W_{Load}', 'N/m^2', 'Wing Loading')
##        t = Variable('tmin', 'min', 'Segment Flight Time in Minutes')
##        thours = Variable('thr', 'hour', 'Segment Flight Time in Hours')
##
##        xAC = Variable('x_{AC}', 'm', 'Aerodynamic Center Location')
##        xCG     = Variable('x_{CG}', 'm', 'CG location')
##
##
##        constraints = []
##        with SignomialsEnabled():
##            constraints.extend([
##                #speed must be greater than stall speed
##                state['V'] >= Vstall,
##
##
##                #Figure out how to delete
##                Vstall == 120*units('kts'),
##                WLoadmax == 6664 * units('N/m^2'),
##
##                #compute the drag
##                TCS([D >= self.wingP['D_{wing}'] + self.fuseP['D_{fuse}'] + self.HTP['D_{ht}']]),
##
##                #constraint CL and compute the wing loading
##                W_avg == .5*self.wingP['C_{L}']*self.aircraft['S']*state.atm['\\rho']*state['V']**2,
##                WLoad == .5*self.wingP['C_{L}']*self.aircraft['S']*state.atm['\\rho']*state['V']**2/self.aircraft.wing['S'],
##
##                #set average weight equal to the geometric avg of start and end weight
##                W_avg == (W_start * W_end)**.5,
##
##                #constrain the max wing loading
##                WLoad <= WLoadmax,
##
##                #compute fuel burn from TSFC
##                W_burn == aircraft['numeng']*self.engineP['TSFC'] * thours * self.engineP['F'],
##
##                #time unit conversion
##                t == thours,
##
##                #make lift equal weight --> small angle approx in climb
##                self.wingP['L_{wing}'] >= W_avg,
##                 ])
##
##        return self.Pmodels, constraints
##
##class Mission(Model):
##    """
##    mission class, links together all subclasses
##    """
##    def setup(self, aircraft):
##        #define the number of each flight segment
##        Nclimb = 2
##        Ncruise = 2
##
##        #Vectorize
##        with Vectorize(Nclimb):
##            climb = ClimbSegment(aircraft)
##
##        with Vectorize(Ncruise):
##            cruise = CruiseSegment(aircraft)
##
##        #declare new variables
##        W_ftotal = Variable('W_{f_{total}}', 'N', 'Total Fuel Weight')
##        W_fclimb = Variable('W_{f_{climb}}', 'N', 'Fuel Weight Burned in Climb')
##        W_fcruise = Variable('W_{f_{cruise}}', 'N', 'Fuel Weight Burned in Cruise')
##        W_total = Variable('W_{total}', 'N', 'Total Aircraft Weight')
##        CruiseAlt = Variable('CruiseAlt', 'ft', 'Cruise Altitude [feet]')
##        ReqRng = Variable('R_{req}', 'nautical_miles', 'Required Cruise Range')
##        W_dry = Variable('W_{dry}', 'N', 'Aircraft Dry Weight')
##
##        h = climb['h']
##        hftClimb = climb['hft']
##        dhft = climb['dhft']
##        hftCruise = cruise['hft']
##
##        #make overall constraints
##        constraints = []
##
##        constraints.extend([
##            #weight constraints
##            TCS([aircraft['W_{e}'] + aircraft['W_{payload}'] + aircraft['numeng'] * aircraft['W_{engine}'] + aircraft['W_{wing}'] + aircraft.HT['W_{struct}'] <= W_dry]),
##            TCS([W_ftotal + W_dry <= W_total]),
##
##            climb['W_{start}'][0] == W_total,
##            climb['W_{end}'][-1] == cruise['W_{start}'][0],
##
##            # similar constraint 1
##            TCS([climb['W_{start}'] >= climb['W_{end}'] + climb['W_{burn}']]),
##            # similar constraint 2
##            TCS([cruise['W_{start}'] >= cruise['W_{end}'] + cruise['W_{burn}']]),
##
##            climb['W_{start}'][1:] == climb['W_{end}'][:-1],
##            cruise['W_{start}'][1:] == cruise['W_{end}'][:-1],
##
##            TCS([W_dry <= cruise['W_{end}'][-1]]),
##
##            TCS([W_ftotal >=  W_fclimb + W_fcruise]),
##            TCS([W_fclimb >= sum(climb['W_{burn}'])]),
##            TCS([W_fcruise >= sum(cruise['W_{burn}'])]),
##
##            #altitude constraints
##            hftCruise == CruiseAlt,
##            TCS([hftClimb[1:Ncruise] >= hftClimb[:Ncruise-1] + dhft]),
##            TCS([hftClimb[0] >= dhft[0]]),
##            hftClimb[-1] <= hftCruise,
##
##            #compute the dh
##            dhft == hftCruise/Nclimb,
##
##            #constrain the thrust
##            climb.climbP['F'] <= 2 * max(cruise.cruiseP['F']),
##
##            #set the range for each cruise segment, doesn't take credit for climb
##            #down range disatnce covered
##            cruise.cruiseP['Rng'] == ReqRng/(Ncruise),
##
##            #set the TSFC
##            climb['TSFC'] == .7*units('1/hr'),
##            cruise['TSFC'] == .5*units('1/hr'),
##
##            # climb['C_{L_{ht}}'] == 2*3.14*climb['\\alpha_{ht}],
##            # cruise['C_{L_{ht}}'] == 2*3.14*cruise['\\alpha_{ht}],
##            ])
##
##        #Horizontal Tail Constraints
##        with SignomialsEnabled():
##            constraints.extend([
##
##                # Trim condition for each flight segment
##                TCS([cruise['x_{AC}']/aircraft.wing['mac'] <= aircraft.wing['c_{m_{w}}']/cruise['C_{L}'] + \
##                     cruise['x_{CG}']/aircraft.wing['mac'] + aircraft.HT['V_{ht}']*(cruise['C_{L_{ht}}']/cruise['C_{L}'])]),
##                TCS([climb['x_{AC}']/aircraft.wing['mac'] <= aircraft.wing['c_{m_{w}}']/climb['C_{L}'] + \
##                     climb['x_{CG}']/aircraft.wing['mac'] + aircraft.HT['V_{ht}']*(climb['C_{L_{ht}}']/climb['C_{L}'])]),
##
##
##                aircraft.HT['L_{ht_{max}}'] == 0.5*aircraft['\\rho_0']*aircraft['V_{ne}']**2*aircraft.HT['S_{ht}']*aircraft.HT['C_{L_{ht,max}}'],
##                #compute mrat, is a signomial equality
##                SignomialEquality(aircraft.HT['m_{ratio}']*(1+2/aircraft.wing['AR']), 1 + 2/aircraft.HT['AR_{ht}']),
##
##                #tail volume coefficient
##                aircraft.HT['V_{ht}'] == aircraft.HT['S_{ht}']*aircraft.HT['x_{CG_{ht}}']/(aircraft.wing['S']*aircraft.wing['mac']),
##
##                #enforce max tail location is the end of the fuselage
##                aircraft.HT['x_{CG_{ht}}'] <= aircraft.fuse['l_{fuse}'],
##                aircraft.HT['l_{ht}'] >= aircraft.HT['x_{CG_{ht}}'] - cruise['x_{CG}'],
##                aircraft.HT['l_{ht}'] >= aircraft.HT['x_{CG_{ht}}'] - climb['x_{CG}'],
##
##                #Stability constraint, is a signomial
##                TCS([aircraft['SM_{min}'] + aircraft['\\Delta x_{CG}']/aircraft.wing['mac'] + aircraft.wing['c_{m_{w}}']/aircraft.wing['C_{L_{max}}'] <= aircraft.HT['V_{ht}']*aircraft.HT['m_{ratio}'] + aircraft.HT['V_{ht}']*aircraft.HT['C_{L_{ht,max}}']/aircraft.wing['C_{L_{max}}']]),
##
##                # TCS([aircraft.wing['x_w'] >= cruise['x_{CG}'] + cruise['\\Delta x_w']]),
##                # TCS([aircraft.wing['x_w'] >= climb['x_{CG}'] + climb['\\Delta x_w']]),
##
##
##                TCS([cruise['x_{CG}'] + cruise['\\Delta x_{trail_{ht}}'] <= aircraft.fuse['l_{fuse}']], reltol=0.002),
##                TCS([climb['x_{CG}'] + climb['\\Delta x_{trail_{ht}}'] <= aircraft.fuse['l_{fuse}']], reltol=0.002),
##
##                #compute the aerodynamic center location
##                #TODO: this sets xAC to xW in a stupid and long winded way
##                # TCS([climb['x_{AC}'] <= climb['x_{CG}'] + climb['\\Delta x_w'] ]),
##                # TCS([cruise['x_{AC}'] <= cruise['x_{CG}'] + cruise['\\Delta x_w'] ]),
##
####                SignomialEquality(cruise['x_{ac}'],xcg + cruise['\\Delta x_w'] ),
####                SignomialEquality(climb['x_{ac}'],xcg + climb['\\Delta x_w'] ),
##                TCS([aircraft.HT['x_{CG_{ht}}'] >= climb['x_{CG}'] + (climb['\\Delta x_{lead_{ht}}']+climb['\\Delta x_{trail_{ht}}'])/2]),
##                TCS([aircraft.HT['x_{CG_{ht}}'] >= cruise['x_{CG}'] + (cruise['\\Delta x_{lead_{ht}}']+cruise['\\Delta x_{trail_{ht}}'])/2]),
##                #---------------------------------------------------------#
##
##                # Substitutions for xCG and xAC
##                cruise['x_{CG}'] == 15*units('m'),
##                climb['x_{CG}'] == 15*units('m'),
##                cruise['x_{AC}'] == aircraft.wing['x_w'],
##                climb['x_{AC}'] == aircraft.wing['x_w'],
##
##                #compute the HT chord at its attachment point to the VT
##                (aircraft.HT['b_{ht}']/aircraft.fuse['w_{fuse}'])*aircraft.HT['\lambda_{ht}']*aircraft.HT['c_{root_{ht}}'] == aircraft.HT['c_{attach}']
##
##                ])
##
##        return climb, cruise, constraints
