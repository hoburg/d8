"""
script to generate the values in the SP Aircraft different objective table
"""
from gpkit import units
from aircraft import Mission
from SPaircraft import optimize_aircraft
from subs.optimalD8 import get_optimalD8_subs

# solve all the cases
Nclimb = 3 # number of climb segments
Ncruise = 2 # number of cruise segments
Nmission = 1 # number of missions
config = 'optimalD8' # String describing configuration:
m = Mission(Nclimb, Ncruise, config, Nmission)
substitutions = get_optimalD8_subs()
substitutions.update({'R_{req}': 3000.*units('nmi'),
                         'n_{pass}': 180.})
# Additional options
fixedBPR = False
pRatOpt = True
mutategparg = True
sol = {}
objectives = [m['W_{f_{total}}'],m['W_{dry}'],m['b'],m['AR'],m['W_{engine}'],m['TotalTime'],m['L/D'][Nclimb],m['W_{lg}']]
for i in range(0,8):
    m.cost = objectives[i].sum()
    sol[i] = optimize_aircraft(m, substitutions, fixedBPR, pRatOpt, mutategparg)
basesol = sol[0]

# output the columns of the table
for i in range(0,8):
    print ("column %s" % i)
    print "\n"
    print [sol[i](objectives[j])/basesol(objectives[j]) for j in range(0,8)]
    print "\n"
    print "\n"
