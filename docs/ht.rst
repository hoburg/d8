Horizontal Tail Model
=====================

At a conceptual design level, the purpose of the horizontal tail is
threefold: to trim the aircraft such that it can fly in steady level
flight, to provide longitudinal stability, and to give the pilot pitch
control authority over a range of flight conditions.

Model Assumptions
-----------------

The horizontal tail model assumes that the horizontal stabilizer is
mounted to the fuselage and nominally produces downforce in cruise.

Model Description
-----------------

The horizontal tail model has 50 free variables and 33 constraints.

.. raw:: latex

    \begin{supertabular}{lcl}
    \toprule
    Free Variables & Units & Description \\ \midrule
    $A_{0h}$ & $~\mathrm{m^{2}}$ & Horizontal bending area constant A0h \\
    $A_{1h_{Land}}$ & $~\mathrm{m}$ & Horizontal bending area constant A1h (landing case) \\
    $A_{1h_{MLF}}$ & $~\mathrm{m}$ & Horizontal bending area constant A1h (max aero load case) \\
    $A_{2h_{Land}}$ & $~[-]$ & Horizontal bending area constant A2h (landing case) \\
    $A_{2h_{MLF}}$ & $~[-]$ & Horizontal bending area constant A2h (max aero load case) \\
    $A_{floor}$ & $~\mathrm{m^{2}}$ & Floor beam x-sectional area \\
    $A_{fuse}$ & $~\mathrm{m^{2}}$ & Fuselage x-sectional area \\
    $A_{hbendb_{Land}}$ & $~\mathrm{m^{2}}$ & Horizontal bending area at rear wingbox (landing case) \\
    $A_{hbendb_{MLF}}$ & $~\mathrm{m^{2}}$ & Horizontal bending area at rear wingbox (max aero load case) \\
    $A_{hbendf_{Land}}$ & $~\mathrm{m^{2}}$ & Horizontal bending area at front wingbox (landing case) \\
    $A_{hbendf_{MLF}}$ & $~\mathrm{m^{2}}$ & Horizontal bending area at front wingbox (max aero load case) \\
    $A_{skin}$ & $~\mathrm{m^{2}}$ & Skin cross sectional area \\
    $A_{vbend_{b}}$ & $~\mathrm{m^{2}}$ & Vertical bending material area at rear wingbox \\
    $B_{0v}$ & $~\mathrm{m^{2}}$ & Vertical bending area constant B0 \\
    $B_{1v}$ & $~\mathrm{m}$ & Vertical bending area constant B1 \\
    $C_{D_{fuse}}$ & $~[-]$ & Fuselage drag coefficient \\
    $D_{fuse}$ & $~\mathrm{N}$ & Fuselage drag \\
    $I_{h_{shell}}$ & $~\mathrm{m^{4}}$ & Shell horizontal bending inertia \\
    $I_{v_{shell}}$ & $~\mathrm{m^{4}}$ & Shell vertical bending inertia \\
    $L_{ht_{max}}$ & $~\mathrm{N}$ & Horizontal tail maximum load \\
    $L_{vt_{max}}$ & $~\mathrm{N}$ & Vertical tail maximum load \\
    $M$ & $~[-]$ & Cruise Mach number \\
    $M_{floor}$ & $~\mathrm{N\cdot m}$ & Max bending moment in floor beams \\
    $P_{floor}$ & $~\mathrm{N}$ & Distributed floor load \\
    $R_{fuse}$ & $~\mathrm{m}$ & Fuselage radius \\
    $S_{bulk}$ & $~\mathrm{m^{2}}$ & Bulkhead surface area \\
    $S_{floor}$ & $~\mathrm{N}$ & Maximum shear in floor beams \\
    $S_{nose}$ & $~\mathrm{m^{2}}$ & Nose surface area \\
    $V_{\infty}$ & $~\mathrm{[\tfrac{m}{s}]}$ & Cruise velocity \\
    $V_{bulk}$ & $~\mathrm{m^{3}}$ & Bulkhead skin volume \\
    $V_{cabin}$ & $~\mathrm{m^{3}}$ & Cabin volume \\
    $V_{cone}$ & $~\mathrm{m^{3}}$ & Cone skin volume \\
    $V_{cyl}$ & $~\mathrm{m^{3}}$ & Cylinder skin volume \\
    $V_{floor}$ & $~\mathrm{m^{3}}$ & Floor volume \\
    $V_{hbend_{b}}$ & $~\mathrm{m^{3}}$ & Horizontal bending material volume b \\
    $V_{hbend_{c}}$ & $~\mathrm{m^{3}}$ & Horizontal bending material volume c \\
    $V_{hbend_{f}}$ & $~\mathrm{m^{3}}$ & Horizontal bending material volume f \\
    $V_{hbend}$ & $~\mathrm{m^{3}}$ & Horizontal bending material volume \\
    $V_{nose}$ & $~\mathrm{m^{3}}$ & Nose skin volume \\
    $V_{vbend_{b}}$ & $~\mathrm{m^{3}}$ & Vertical bending material volume b \\
    $V_{vbend_{c}}$ & $~\mathrm{m^{3}}$ & Vertical bending material volume c \\
    $V_{vbend}$ & $~\mathrm{m^{3}}$ & Vertical bending material volume \\
    $W_{apu}$ & $~\mathrm{lbf}$ & APU weight \\
    $W_{buoy}$ & $~\mathrm{lbf}$ & Buoyancy weight \\
    $W_{cone}$ & $~\mathrm{lbf}$ & Cone weight \\
    $W_{fix}$ & $~\mathrm{lbf}$ & Fixed weights (pilots, cockpit seats, navcom) \\
    $W_{floor}$ & $~\mathrm{lbf}$ & Floor weight \\
    $W_{fuse}$ & $~\mathrm{lbf}$ & Fuselage weight \\
    $W_{hbend}$ & $~\mathrm{lbf}$ & Horizontal bending material weight \\
    $W_{insul}$ & $~\mathrm{lbf}$ & Insulation material weight \\
    $W_{lugg}$ & $~\mathrm{lbf}$ & Passenger luggage weight \\
    $W_{padd}$ & $~\mathrm{lbf}$ & Misc weights (galley, toilets, doors etc.) \\
    $W_{pass}$ & $~\mathrm{lbf}$ & Passenger weight \\
    $W_{payload}$ & $~\mathrm{lbf}$ & Payload weight \\
    $W_{seat}$ & $~\mathrm{lbf}$ & Seating weight \\
    $W_{shell}$ & $~\mathrm{lbf}$ & Shell weight \\
    $W_{skin}$ & $~\mathrm{lbf}$ & Skin weight \\
    $W_{tail}$ & $~\mathrm{lbf}$ & Total tail weight \\
    $W_{vbend}$ & $~\mathrm{lbf}$ & Vertical bending material weight \\
    $W_{window}$ & $~\mathrm{lbf}$ & Window weight \\
    $\lambda_{cone}$ & $ $~[-]$ $ & Tailcone radius taper ratio \\
    $\rho_{\infty}$ & $~\mathrm{[\tfrac{kg}{m^3}]}$ & Freestream density \\
    $\rho_{cabin}$ & $~\mathrm{\tfrac{kg}{m^{3}}}$ & Cabin air density \\
    $\sigma_x$ & $~\mathrm{\tfrac{N}{m^{2}}}$ & Axial stress in skin \\
    $\sigma_{M_h}$ & $~\mathrm{\tfrac{N}{m^{2}}}$ & Horizontal bending material stress \\
    $\sigma_{M_v}$ & $~\mathrm{\tfrac{N}{m^{2}}}$ & Vertical bending material stress \\
    $\sigma_{\theta}$ & $~\mathrm{\tfrac{N}{m^{2}}}$ & Skin hoop stress \\
    $\tau_{cone}$ & $~\mathrm{\tfrac{N}{m^{2}}}$ & Shear stress in tail cone \\
    $c_0$ & $~\mathrm{m}$ & Root chord of the wing \\
    $h_{fuse}$ & $~\mathrm{m}$ & Fuselage height \\
    $l_{cone}$ & $~\mathrm{m}$ & Cone length \\
    $l_{floor}$ & $~\mathrm{m}$ & Floor length \\
    $l_{fuse}$ & $~\mathrm{m}$ & Fuselage length \\
    $l_{shell}$ & $~\mathrm{m}$ & Shell length \\
    $n_{rows}$ & $ $~[-]$ $ & Number of rows \\
    $n_{seat}$ & $ $~[-]$ $ & Number of seats \\
    $t_{shell}$ & $~\mathrm{m}$ & Shell thickness \\
    $t_{skin}$ & $~\mathrm{m}$ & Skin thickness \\
    $w_{aisle}$ & $~\mathrm{m}$ & Aisle width \\
    $w_{floor}$ & $~\mathrm{m}$ & Floor half-width \\
    $w_{fuse}$ & $~\mathrm{m}$ & Fuselage half-width \\
    $x_b$ & $~\mathrm{m}$ & x-location of back of wingbox \\
    $x_f$ & $~\mathrm{m}$ & x-location of front of wingbox \\
    $x_{hbend_{Land}}$ & $~\mathrm{ft}$ & Horizontal zero bending location (landing case) \\
    $x_{hbend_{MLF}}$ & $~\mathrm{ft}$ & Horizontal zero bending location (maximum aero load case) \\
    $x_{shell1}$ & $~\mathrm{m}$ & Start of cylinder section \\
    $x_{shell2}$ & $~\mathrm{m}$ & End of cylinder section \\
    $x_{tail}$ & $~\mathrm{m}$ & x-location of tail \\
    $x_{vbend}$ & $~\mathrm{ft}$ & Vertical zero bending location \\
    $x_{wing}$ & $~\mathrm{m}$ & x-location of wing c/4 \\
    \bottomrule
    \end{supertabular}

| lcl Constants & Units & Description
| :math:`C_{L_{ht,max}}` & :math:`~[-]` & Max horizontal tail lift
  coefficient
| :math:`C_{L_{w,max}}` & :math:`~[-]` & Max lift coefficient, wing
| :math:`C_{m_{ac}}` & :math:`~[-]` & Moment coefficient about
  aerodynamic centre (wing)
| :math:`S.M._{min}` & :math:`~[-]` & Minimum allowed stability margin
| :math:`V_{ne}` & :math:`~\mathrm{[\tfrac{m}{s}]}` & Never exceed
  velocity
| :math:`\Delta x_{CG}` & :math:`~\mathrm{[m]}` & CG travel range
| :math:`\alpha_{ht,max}` & :math:`~[-]` & Max angle of attack, htail
| :math:`\eta_{ht}` & :math:`~[-]` & Tail efficiency
| :math:`\lambda_{ht_{min}} ` & :math:`~[-]` & Minimum horizontal tail
  taper ratio
| :math:`\rho_0` & :math:`~\mathrm{[\tfrac{kg}{m^{3}}]}` & Air density
  (0 ft)
| :math:`\tan(\Lambda_{ht})` & :math:`~[-]` & tangent of horizontal tail
  sweep
| :math:`g` & :math:`~\mathrm{[\tfrac{m}{s^{2}}]}` & Gravitational
  acceleration

Horizontal Tail Geometry and Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The horizontal tail model employs many of the same geometric constraints
as the wing and vertical tail. More specifically, analogous versions of
Constraints [eq:planformarea,eq:meanaerochord,eq:spanwisemac,eq:taperratio,eq:mintaperratio]
and Constraints [eq:vtmomentarm,eq:vtleading,eq:vttrailing] enforce
planform relationships and constrain the horizontal tail moment arm,
respectively. As with the vertical tail, Constraint  needs to be
implemented as a signomial equality constraint. The horizontal tail also
reuses the same structural model
from :raw-tex:`\cite{hoburg2014geometric}`.

Trim Condition
~~~~~~~~~~~~~~

The first sizing requirement is that the aircraft must satisfy the trim
condition :raw-tex:`\cite{burton_thesis}`, which implicitly requires
that the full aircraft moment coefficient be zero.

.. math::

   \frac{x_w}{\bar{c}_w} \leq \frac{x_{CG}}{\bar{c}_w} + \frac{C_{m_{ac}}}{C_{L_w}} 
   + \frac{V_{ht} C_{L_{ht}}}{C_{L_w}}

 Thin airfoil theory is used to constrain the horizontal tail’s isolated
lift curve slope :raw-tex:`\cite{anderson_aero}`.

.. math::

   \begin{aligned}
   C_{L_{ht}} &= C_{L_{\alpha,ht}} \alpha\end{aligned}

 However, the horizontal tail’s lift curve slope is reduced by downwash,
:math:`\epsilon`, from the wing and
fuselage :raw-tex:`\cite{kroo2001aircraft}`. Note
:math:`\eta_{h_{lift}}` is the horizontal tail sectional lift
efficiency.

.. math::

   C_{L_{\alpha,ht}} = C_{L_{\alpha,ht_0}} \left(1 - \frac{\partial \epsilon}
   {\partial \alpha}\right) \eta_{h_{lift}}

 The downwash can be approximated as the downwash far behind an
elliptically loaded wing.

.. math::

   \begin{aligned}
   \epsilon &\approx \frac{2 C_{L_w}}{\pi \AR_w} \\
   \implies \frac{\partial \epsilon}{\partial \alpha} &\approx
   \frac{2 C_{L_{\alpha,w}}}{\pi \AR_w}\end{aligned}

 Thus, an additional posynomial constraint is introduced to constrain
the corrected lift curve slope.

.. math::

   C_{L_{\alpha,ht}} + \frac{2 C_{L_{\alpha,w}} }{\pi \AR_w}  \eta_{ht} C_{L_{\alpha,ht_0}}
   \leq C_{L_{\alpha,ht_0}} \eta_{ht}

Minimum Stability Margin
~~~~~~~~~~~~~~~~~~~~~~~~

The second condition is that the aircraft must maintain a minimum
stability margin at both the forward and aft
limits:raw-tex:`\cite{burton_thesis}`.

.. math::

   \begin{aligned}
   \label{e:SM_CG}
   S.M._{min} + \frac{\Delta x_{CG}}{\bar{c}_w} + \frac{C_{m_{ac}}}{C_{L_{w,max}}} 
   &\leq V_{ht} m_{ratio} + \frac{V_{ht} C_{L_{h,max}}}{C_{L_{w,max}}}\end{aligned}

 The ratio of the horizontal tail and wing lift curve slopes,
:math:`m_{ratio}`, appears in Equation and is constrained using the
relationship in :raw-tex:`\cite{burton_thesis}`. The constraint is a
signomial equality because it is not possible to know a priori whether
there will be upward or downward pressure on :math:`m_{ratio}`.

.. math:: m_{ratio} = \left(1+\frac{2}{AR_w}\right) 1 + \frac{2}{AR_{ht}}

Stability Margin
~~~~~~~~~~~~~~~~

The third condition is that the stability margin must be greater than a
minimum specified value for all intermediate locations.

.. math::

   \begin{aligned}
   S.M. &\leq \frac{x_w - x_{CG}}{\bar{c}_w}\\
   S.M. &\geq S.M._{min}\end{aligned}

Horizontal Tail Drag
~~~~~~~~~~~~~~~~~~~~

The horizontal tail employs the same drag model as the wing
(Constraints [eq:wingdrag,eq:wingdragcoeff,eq:wingpdragcoeff,eq:wingRe,eq:induceddrag]),
with the exception of the parasitic drag coefficient fit. The wing’s
parasitic drag fit  is replaced by a fit to XFOIL
:raw-tex:`\cite{drela1989xfoil}` data for the
TASOPT:raw-tex:`\cite{drela2010tasopt}` T-series airfoils. The TASOPT
T-series airfoils are horizontal tail airfoils intended for transonic
use. The fit considers airfoil thickness, Reynolds number, and Mach
number. The softmax affine function fit is developed with
GPfit:raw-tex:`\cite{gpfitpaper,gpfit}` and has an RMS error of 1.14%.

.. math::

   \begin{aligned}
   \label{e:HT_drag}
       {C_{D_{0_{ht}}}}^{6.49} & \geq  5.288\times10^{-20} (Re_{h})^{0.901}  
       (\tau_{h})^{0.912} (M)^{8.645}\\
       &+ 1.676\times10^{-28} (Re_{h})^{0.351} (\tau_{h})^{6.292}
       (M)^{10.256} \nonumber \\
       &+ 7.098\times10^{-25} (Re_{h})^{1.395} (\tau_{h})^{1.962} 
       (M)^{0.567} \nonumber \\
       &+ 3.731\times10^{-14} (Re_{h})^{-2.574} (\tau_{h})^{3.128} 
       (M)^{0.448} \nonumber \\
       &+ 1.443\times10^{-12} (Re_{h})^{-3.910} (\tau_{h})^{4.663} 
       (M)^{7.689} \nonumber \end{aligned}
