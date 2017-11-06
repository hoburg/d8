System-level Model
==================

The objective of the optimization problem presented in this work is to
minimize fuel consumption, or equivalently fuel weight,
:math:`W_{fuel}`, using an adaptation of the Breguet range formulation
introduced in :raw-tex:`\cite{hoburg2014geometric}`. The purpose of
the system-level model is threefold: it enforces system-level
performance constraints such as required range and minimum cruise speed,
it encodes weight and drag buildups, and it constrains system-level
properties such as the aircraft’s and moment of inertia. In doing these
things, it also couples the subsystem models.

Model Assumptions
-----------------

The model presented in this work is a set of constraints that describe
the performance and design of a conventional-configuration narrowbody
aircraft, with a simple cruise-only mission profile. A more
sophisticated mission profile is left for future work.

Model Description
-----------------

+---------------------------------------+
| Free Variables | Units | Description |
+=========================================+
| :math:`C_D` | :math:`~[-]` | Drag coefficient|
| :math:`D` | :math:`~\mathrm{[N]}` | Total aircraft drag (cruise)|
| :math:`D_{fuse}` | :math:`~\mathrm{[N]}` | Fuselage drag|
| :math:`D_{ht}` | :math:`~\mathrm{[N]}` | Horizontal tail drag|
| :math:`D_{vt}` | :math:`~\mathrm{[N]}` | Vertical tail drag|
| :math:`D_{wing}` | :math:`~\mathrm{[N]}` | Wing drag|
| :math:`\Delta x_{ac_w}` | :math:`~\mathrm{[m]}` | Wing aerodynamic
  center shift|
| :math:`f_{fuel}` | :math:`~\mathrm{[-]}` | Percent fuel remaining|
| :math:`I_{z_{fuse}}` | :math:`~\mathrm{[kg m^2]}` | Fuselage moment of
  inertia|
| :math:`I_{z_{tail}}` | :math:`~\mathrm{[kg m^2]}` | Tail moment of
  inertia|
| :math:`I_{z_{wing}}` | :math:`~\mathrm{[kg m^2]}` | Wing moment of
  inertia|
| :math:`I_{z}` | :math:`~\mathrm{[kg m^2]}` | Total aircraft moment of
  inertia|
| :math:`l_{fuse}` | :math:`~\mathrm{[m]}` | Fuselage length |
| :math:`l_{vt}` | :math:`~\mathrm{[m]}` | Vertical tail moment arm|
| :math:`M` | :math:`~[-]` | Cruise Mach number|
| :math:`R` | :math:`~\mathrm{[nm]}` | Segment range|
| :math:`S_w` | :math:`~\mathrm{[m^{2}]}` | Wing reference area|
| :math:`V_{TO}` | :math:`~\mathrm{[\tfrac{m}{s}]}` | Takeoff velocity|
| :math:`V_{\infty}` | :math:`~\mathrm{[\tfrac{m}{s}]}` | Cruise
  velocity|
| :math:`W` | :math:`~\mathrm{[lbf]}` | Aircraft takeoff weight|
| :math:`W_{avg}` | :math:`~\mathrm{[lbf]}` | Flight segment average
  aircraft weight|
| :math:`W_{buoy}` | :math:`~\mathrm{[lbf]}` | Buoyancy weight|
| :math:`W_{dry}` | :math:`~\mathrm{[lbf]}` | Aircraft dry weight|
| :math:`W_{end}` | :math:`~\mathrm{[lbf]}` | Aircraft weight at end of
  flight segment|
| :math:`W_{fuel}` | :math:`~\mathrm{[lbf]}` | Fuel weight|
| :math:`W_{f_{primary}}` | :math:`~\mathrm{[lbf]}` | Total fuel weight
  less reserves|
| :math:`W_{fuel_{wing}}` | :math:`~\mathrm{[lbf]}` | Maximum fuel
  weight carried in wing|
| :math:`W_{fuse}` | :math:`~\mathrm{[lbf]}` | Fuselage weight|
| :math:`W_{hpesys}` | :math:`~\mathrm{[lbf]}` | Power system weight|
| :math:`W_{ht}` | :math:`~\mathrm{[lbf]}` | Horizontal tail weight|
| :math:`W_{lg}` | :math:`~\mathrm{[lbf]}` | Landing gear weight|
| :math:`W_{misc}` | :math:`~\mathrm{[lbf]}` | Miscellanous system
  weight|
| :math:`W_{mg}` | :math:`~\mathrm{[lbf]}` | Main landing gear weight|
| :math:`W_{ng}` | :math:`~\mathrm{[lbf]}` | Nose landing gear weight|
| :math:`W_{pay}` | :math:`~\mathrm{[lbf]}` | Payload weight|
| :math:`W_{start}` | :math:`~\mathrm{[lbf]}` | Aircraft weight at start
  of flight segment|
| :math:`W_{tail}` | :math:`~\mathrm{[lbf]}` | Total tail weight|
| :math:`W_{vt}` | :math:`~\mathrm{[lbf]}` | Vertical tail weight|
| :math:`W_{wing}` | :math:`~\mathrm{[lbf]}` | Wing weight|
| :math:`W_{zf}` | :math:`~\mathrm{[lbf]}` | Zero fuel weight|
| :math:`\AR_w` | :math:`~[-]` | Wing aspect ratio|
| :math:`\left(\frac{L}{D}\right)` | :math:`~[-]` | Lift/drag ratio|
| :math:`\xi` | :math:`~[-]` | Takeoff parameter|
| :math:`a` | :math:`~\mathrm{[\tfrac{m}{s}]}` | Speed of sound|
| :math:`b_w` | :math:`~\mathrm{[m]}` | Wing span|
| :math:`c_{root_{w}}` | :math:`~\mathrm{[m]}` | Wing root chord|
| :math:`t` | :math:`~\mathrm{[min]}` | Flight time|
| :math:`x_{CG}` | :math:`~\mathrm{[m]}` | x-location of CG|
| :math:`x_{CG_{lg}}` | :math:`~\mathrm{[m]}` | x-location of landing
  gear CG|
| :math:`x_{CG_{misc}}` | :math:`~\mathrm{[m]}` | x-location of
  miscellanous systems CG|
| :math:`x_{TO}` | :math:`~\mathrm{[m]}` | Takeoff distance
| :math:`x_{b}` | :math:`~\mathrm{[m]}` | Wing box forward bulkhead
  location|
| :math:`x_{misc}` | :math:`~\mathrm{[m]}` | Miscellaneous systems
  centroid|
| :math:`x_{hpesys}` | :math:`~\mathrm{[m]}` | Power systems centroid|
| :math:`x_{lg}` | :math:`~\mathrm{[m]}` | Landing gear centroid|
| :math:`x_{mg}` | :math:`~\mathrm{[m]}` | Main landing gear centroid|
| :math:`x_{ng}` | :math:`~\mathrm{[m]}` | Nose landing gear centroid|
| :math:`x_{tail}` | :math:`~\mathrm{[m]}` | Tail centroid|
| :math:`x_{wing}` | :math:`~\mathrm{[m]}` | Wing centroid|
| :math:`y` | :math:`~[-]` | Takeoff parameter|
| :math:`z_{bre}` | :math:`~[-]` | Breguet parameter|
+----------------------------------------------------+

[tab:ac\_fixedvars]

| lcl Constants & Units & Description
| :math:`C_{L_{w,max}}` & :math:`~[-]` & Max lift coefficient, wing
| :math:`M_{min}` & :math:`~[-]` & Minimum Mach number
| :math:`R_{req}` & :math:`~\mathrm{[nm]}` & Required total range
| :math:`T_e` & :math:`~\mathrm{[N]}` & Takeoff thrust
| :math:`W_{apu}` & :math:`~\mathrm{[N]}` & APU weight
| :math:`W_{eng}` & :math:`~\mathrm{[N]}` & Engine weight
| :math:`\rho_{TO}` & :math:`~\mathrm{[\tfrac{kg}{m^3}]}` & Takeoff
  density
| :math:`c_T` & :math:`~\mathrm{[\tfrac{lb}{\left(hr\cdot lbf\right)}]}`
  & Thrust specific fuel consumption
| :math:`f_{fuel_{res}}` & :math:`~[-]` & Fuel reserve fraction
| :math:`g` & :math:`~\mathrm{[\tfrac{m}{s^{2}}]}` & Gravitational
  acceleration
| :math:`h` & :math:`~\mathrm{[m]}` & Cruise altitude
| :math:`l_r` & :math:`~[-]` & Max Runway length
| :math:`n_{eng}` & :math:`~[-]` & number of engines
| :math:`y_{eng}` & :math:`~\mathrm{[m]}` & Engine moment arm

Flight Performance
~~~~~~~~~~~~~~~~~~

The Breguet range formulation is discretized over multiple cruise
segments to improve accuracy, meaning the constraints
from :raw-tex:`\cite{hoburg2014geometric}` apply during each of the
:math:`N` flight segments. The :math:`n` subscript is used to represent
the :math:`n^{th}` flight segment where :math:`n=1...N`. For
readability, these subscripts are not used in the remainder of the
manuscript, but still apply.

.. math::

   \begin{aligned}
   \sum_{n=1}^{N} R_{n} &\geq R_{req} \\
   R_{n+1} &= R_{n} \\
   R_{n} &\leq \frac{V_{\infty_{n}}}{n_{eng}c_{T_{n}} g} \frac{W_{{avg}_{n}}}{D_{n}} z_{bre_{n}}\\
   W_{fuel_{n}} &\geq \left(z_{bre_{n}} + \frac{z_{bre_{n}}^2}{2}  
   + \frac{z_{bre_{n}}^{3}}{6} \right) W_{end_{n}} \\
   W_{fuel_{n}} &\geq n_{eng} {c_{T_{n}}} D_{n} t_{n} \\
   \sum_{n=1}^{N}W_{fuel_{n}} &\leq W_{f_{primary}} \\
   V_{\infty_{n}} t_{n} &= R_{n} \\
   W_{start_{n}} &\geq W_{end_{n}} + W_{fuel_{n}} \\
   W_{start_{n+1}} &= W_{end_{n}} \\
   W &\geq W_{dry} + W_{payload} + f_{fuel_{res}} W_{f_{primary}} \\
   W_{start_{0}} &= W \\
   W_{end_{N}} &\geq W_{dry} + W_{payload} + f_{fuel_{res}} W_{f_{primary}}\\
   W_{avg_{n}} &\geq \sqrt{W_{start_{n}} W_{end_{N}}} + W_{buoy_{n}} \\
   \left(\frac{L}{D}\right)_{n} &= \frac{W_{avg_{n}}}{D_{n}}\end{aligned}

 In the remainder of this manuscript, :math:`W` refers to the
corresponding flight segment’s :math:`W_{avg}`.

The dry weight and drag of the aircraft are constrained using simple
buildups of each component’s weight and drag.

.. math::

   \begin{aligned}
   W_{dry} &\geq W_{wing} + W_{fuse} + W_{vt} + W_{ht} + W_{lg} + W_{eng} + W_{misc} \\
   D_n &\geq D_{wing_n} + D_{fuse_n} + D_{vt_n} + D_{ht_n}\end{aligned}

Mach number is constrained to be greater than a user-specified minimum
value.

.. math::

   \begin{aligned}
   M &= \frac{V_{\infty}}{a} \\
   M &\geq M_{min}\end{aligned}

The takeoff model is taken directly
from :raw-tex:`\cite{hoburg2014geometric}`. An additional constraint
on takeoff velocity is added to ensure adequate margin above stall
speed :raw-tex:`\cite{anderson2005introduction}`.

.. math::

   \begin{aligned}
   {x_{TO}} &\leq {l_r} \\
   1 + {y} &\leq  2\frac{ {g} {x_{TO}}{T_e}}{{V_{TO}}^{2} {W}}  \\
   1 &\geq  0.0464\frac{{\xi}^{2.7}}{{y}^{2.9}} + \frac{{\xi}^{0.3}}{{y}^{0.049}}\\
   {\xi} &\geq \frac12 \frac{{\rho_{TO}}{V_{TO}}^{2} {S_w}{C_D}}{{T_e}} \\
   {V_{TO}} &= 1.2\sqrt{\frac{2{W}}{C_{L_{w,max}}} {S_w} {\rho_{TO}}} \end{aligned}

Atmospheric pressure, density, temperature, and speed of sound are
constrained using the atmosphere model described in
:raw-tex:`\cite{sp_engine}`. Dynamic viscosity is constrained using
the viscosity model developed in :raw-tex:`\cite{kirschen_thesis}`
which is based off the Sutherland viscosity
model:raw-tex:`\cite{sutherland1893lii}`.

System-level Properties
~~~~~~~~~~~~~~~~~~~~~~~

The constraint for the aircraft is -compatible, and is satisfied during
each flight segment. The fuselage and payload weights are assumed to be
evenly distributed through the length of the fuselage, and the wing
weight acts directly at its area centroid, :math:`x_{wing} + \Delta
x_{ac_w}`. It is assumed that the fuel weight shifts in proportion to
the remaining fuel fraction, :math:`f_{fuel}`, and that a reserve fuel
fraction, :math:`f_{fuel_{res}}`, remains in the wing. The wingbox
forward bulkhead location, :math:`x_b`, is used as a surrogate variable
for engine .

.. math::

   \begin{aligned}
   W x_{CG_{n}} &\geq W_{wing} \left(x_{wing} + \Delta x_{ac_w}\right) 
    + W_{f_{primary}} \left(f_{fuel_{n}} + f_{fuel_{res}}\right) \left(x_{wing} +
    \Delta x_{ac_w} f_{fuel_{n}}\right)  \\
   & +\frac{1}{2} \left(W_{fuse} + W_{payload}\right) l_{fuse}
   + W_{ht} x_{CG_{ht}} + \left(W_{vt} + W_{cone} \right) x_{CG_{vt}} \nonumber \\
   & + n_{eng} W_{eng} x_b + W_{lg} x_{lg} + W_{misc} x_{misc} \nonumber\end{aligned}

In the prior constraint, :math:`f_{fuel}` is the percent of primary fuel
remaining. :math:`f_{fuel}` is represented adequately by a posynomial
inequality since it has downward pressure.

.. math:: f_{fuel_{n}} \geq \frac{\sum_{n=1}^{n}W_{fuel_{n}}}{W_{f_{primary}}}

The landing gear is constrained by the moment of each set of landing
gear about the nose of the aircraft.

.. math:: W_{lg} x_{lg} \geq W_{mg} x_m + W_{ng} x_n

The miscellaneous equipment includes only power systems in the current
model, but is defined to allow for refinements in CG modeling in future
work.

.. math::

   \begin{aligned}
   W_{misc} x_{misc} &\geq W_{hpesys} x_{hpesys}\end{aligned}

The aircraft’s moment of inertia is the sum of the inertias of its
components.

.. math::

   \label{e:Iz_sum}
   I_z \geq I_{z_{wing}} + I_{z_{fuse}} + I_{z_{tail}}

The wing moment of inertia model includes the moment of inertia of the
fuel systems and engines. It assumes that the wing and fuel weight are
evenly distributed on the planform of the wing. This is an overestimate
of the wing moment of inertia with full fuel tanks.

.. math::

   \label{e:Iz_wing}
   I_{z_{wing}} \geq \frac{n_{eng} W_{engine} y_{eng}^2}{g} + 
   \left(\frac{W_{fuel_{wing}} + W_{wing}}{g}\right) \frac{{b_{w}}^3 c_{root_{w}}}{16 S_{w}} 
   \left(\lambda_w + \frac{1}{3}\right)

The fuselage moment of inertia includes the payload moment of inertia.
It is assumed that payload and fuselage weight are evenly distributed
along the length of the fuselage. The wing root quarter-chord location
acts as a surrogate for the of the aircraft.

.. math::

   I_{z_{fuse}} \geq \left(\frac{W_{fuse} + W_{pay}}{g}\right)
   \left(\frac{x_{wing}^3 + l_{vt}^3}{3l_{fuse}}\right)

The moment of inertia of the tail is constrained by treating the tail as
a point mass.

.. math::

   \label{e:Iz_tail}
   I_{z_{tail}} \geq \left(\frac{W_{apu} + W_{tail}}{g}\right) l_{vt}^2
