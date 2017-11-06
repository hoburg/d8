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

| lcl Free Variables & Units & Description
| :math:`C_{D_{ht}}` & :math:`~[-]` & Horizontal tail drag coefficient
| :math:`C_{D_{0_{ht}}}` & :math:`~[-]` & Horizontal tail parasitic drag
  coefficient
| :math:`C_{L_{ht}}` & :math:`~[-]` & Lift coefficient (htail)
| :math:`C_{L_w}` & :math:`~[-]` & Lift coefficient (wing)
| :math:`C_{L_{\alpha h_{0}}}` & :math:`~[-]` & Isolated lift curve
  slope (htail)
| :math:`C_{L_{\alpha,ht}}` & :math:`~[-]` & Lift curve slope (htail)
| :math:`C_{L_{\alpha,w}}` & :math:`~[-]` & Lift curve slope (wing)
| :math:`D_{ht}` & :math:`~\mathrm{[N]}` & Horizontal tail drag
| :math:`L_{ht}` & :math:`~\mathrm{[N]}` & Horizontal tail downforce
| :math:`L_{ht_{max}}` & :math:`~\mathrm{[N]}` & Maximum tail load
| :math:`M` & :math:`~[-]` & Mach number
| :math:`Re_{ht}` & :math:`~[-]` & Horizontal tail Reynolds number
| :math:`S.M.` & :math:`~[-]` & Stability margin
| :math:`S_{ht}` & :math:`~\mathrm{[m^{2}]}` & Horizontal tail area
| :math:`V_{\infty}` & :math:`~\mathrm{[\tfrac{m}{s}]}` & Freestream
  velocity
| :math:`V_{ht}` & :math:`~[-]` & Horizontal tail volume
| :math:`W_{ht}` & :math:`~\mathrm{[lbf]}` & Horizontal tail weight
| :math:`AR_w` & :math:`~[-]` & Wing aspect ratio
| :math:`AR_{ht}` & :math:`~[-]` & Horizontal tail aspect ratio
| :math:`\Delta x_{lead_{ht}}` & :math:`~\mathrm{[m]}` & Distance from
  CG to HT leading edge
| :math:`\Delta x_{trail_{ht}}` & :math:`~\mathrm{[m]}` & Distance from
  CG to HT trailing edge
| :math:`\alpha_{ht}` & :math:`~[-]` & Horizontal tail angle of attack
| :math:`\bar{c}_w` & :math:`~\mathrm{[m]}` & Mean aerodynamic chord
  (wing)
| :math:`\bar{c}_{ht}` & :math:`~\mathrm{[m]}` & Mean aerodynamic chord
  (ht)
| :math:`\lambda_{ht}` & :math:`~[-]` & Horizontal tail taper ratio
| :math:`\mu` & :math:`~\mathrm{[\tfrac{N\cdot s}{m^{2}}]}` & Dynamic
  viscosity
| :math:`\rho_{\infty}` & :math:`~\mathrm{[\tfrac{kg}{m^{3}}]}` &
  Freestream density
| :math:`\tau_{ht}` & :math:`~[-]` & Horizontal tail thickness/chord
  ratio
| :math:`b_{ht}` & :math:`~\mathrm{[m]}` & Horizontal tail span
| :math:`c_{root_{ht}}` & :math:`~\mathrm{[m]}` & Horizontal tail root
  chord
| :math:`c_{tip_{ht}}` & :math:`~\mathrm{[m]}` & Horizontal tail tip
  chord
| :math:`e_{ht}` & :math:`~[-]` & Oswald efficiency factor
| :math:`f(\lambda_{ht})` & :math:`~[-]` & Empirical efficiency function
  of taper
| :math:`l_{fuse}` & :math:`~\mathrm{[m]}` & Fuselage length
| :math:`l_{ht}` & :math:`~\mathrm{[m]}` & Horizontal tail moment arm
| :math:`m_{ratio}` & :math:`~[-]` & Ratio of HT and wing lift curve
  slopes
| :math:`p_{ht}` & :math:`~[-]` & Substituted variable = 1 + 2\*taper
| :math:`q_{ht}` & :math:`~[-]` & Substituted variable = 1 + taper
| :math:`w_{fuse}` & :math:`~\mathrm{[m]}` & Fuselage width
| :math:`x_w` & :math:`~\mathrm{[m]}` & Position of wing aerodynamic
  center
| :math:`x_{CG}` & :math:`~\mathrm{[m]}` & x-location of CG
| :math:`y_{\bar{c}_{ht}}` & :math:`~\mathrm{[m]}` & Spanwise location
  of mean aerodynamic chord

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
   \epsilon &\approx \frac{2 C_{L_w}}{\pi AR_w} \\
   \implies \frac{\partial \epsilon}{\partial \alpha} &\approx
   \frac{2 C_{L_{\alpha,w}}}{\pi AR_w}\end{aligned}

 Thus, an additional posynomial constraint is introduced to constrain
the corrected lift curve slope.

.. math::

   C_{L_{\alpha,ht}} + \frac{2 C_{L_{\alpha,w}} }{\pi AR_w}  \eta_{ht} C_{L_{\alpha,ht_0}}
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
