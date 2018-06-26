from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
from SPaircraft import Mission
from saveSol import gendes, gencsm
from shutil import copyfile

from subs.optimalD8 import get_optimalD8_subs
from aircraft import Mission

EXIT = [False]
ID = 0
LASTSOL = [None]


def genfiles(m, sol):
    global ID
    gensoltxt(m, sol, ID)
    genFile('.csm', sol, 'optimalD8')
    copyfile("d82.csm", "d82_%03i.csm" % ID)
    ID += 1


def gensoltxt(m, sol, ID):
    with open("sol_%03i.txt" % ID, "w") as f:
        for var in sorted(m.varkeys, key=str):
            f.write("%s [%s]\t\t%f\n" % (var, var.unitstr(options=":~",
                                                          dimless="-"),
                                         sol["variables"][var]))


class SPaircraftServer(WebSocket):

    def handleMessage(self):
        print "< received", repr(self.data)
        try:
            self.data = json.loads(self.data)
            print self.data

            objective = 'W_{f_{total}}'
            aircraft = 'optimalD8'
            substitutions = get_optimalD8_subs()
            fixedBPR = False
            pRatOpt = True
            mutategparg = True
            m.cost = m['W_{f_{total}}']

            for name, value in self.data.items():
                try:
                    key = m.design_parameters[name]
                    m.substitutions[key] = value
                except KeyError as e:
                    print repr(e)

            sol = m.localsolve(x0=x0)
            LASTSOL[0] = ((Ncoldpipes, Nhotpipes), sol)
            genfiles(m, sol)

            self.send({"status": "optimal",
                       "msg": ("Successfully optimized."
                               " Optimal heat transfer: %.1f watts "
                               % sol["variables"][m.Q])})
        except Exception as e:
            self.send({"status": "unknown", "msg": "The last solution"
                      " raised an exception; tweak it and send again."})
            print type(e), e

    def send(self, msg):
        print "> sent", repr(msg)
        self.sendMessage(unicode(json.dumps(msg)))

    def handleConnected(self):
        print self.address, "connected"

    def handleClose(self):
        print self.address, "closed"
        EXIT[0] = True


if __name__ == "__main__":
    objective = 'W_{f_{total}}'
    aircraft = 'optimald8'
    substitutions = get_optimalD8_subs()
    fixedBPR = False
    pRatOpt = True
    mutategparg = True
    sol, m, m_relax = optimize_aircraft(objective, aircraft, substitutions, fixedBPR, pRatOpt, mutategparg)
    sol = m.localsolve()
    LASTSOL[0] = ((3, 3), sol)
    genfiles(m, sol)
    server = SimpleWebSocketServer('', 8000, HXGPServer)
    while not EXIT[0]:
        server.serveonce()
    print "Python server has exited."
