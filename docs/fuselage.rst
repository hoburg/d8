Fuselage Model
**************

At a high level, the purpose of a conventional commercial aircraft fuselage can
be decomposed into two primary functions: integrating and connecting all of the
subsystems (e.g. wing, tail, landing gear), and carrying the payload, which
typically consists of passengers, luggage, and sometimes cargo. The design of
the fuselage is therefore coupled with virtually every aircraft subsystem.

Prof. Mark Drela performs a detailed, but still approximate,
analysis of fuselage structure and weight in TASOPT, considering pressure loads, torsion
loads, bending loads, buoyancy weight, window weight, payload-proportional
weights, the floor, and the tail cone. The majority of the constraints in this
model are adapted directly from these equations.

Model Assumptions
=================
This model assumes a single circular-cross-section fuselage. This is an approximation,
since narrow-body aircraft like the Boeing 737 and Airbus A320 do not have perfectly
circular cross sections.

The floor structural model and the horizontal bending model assume uniform
floor loading. The model leverages the analytical bending models from TASOPT,
which makes assumptions about symmetry in bending loads.
Shell buckling is not explicitly modeled while designing bending
structure, but is accounted for by the implementation of a lower yield stress
for bending reinforcement material relative to the nominal yield stress of the
material.

Model Description
=================

.. figure:: fuselage.pdf_tex
    :align: center
    :width: 300px
    Geometric variables of the fuselage model

.. figure:: fuse_cross_section.pdf_tex
    :align: center
    :width: 300px
    Geometric variables of the fuselage model cross-section

Under construction...

Cross sectional geometry constraints
------------------------------------

The fuselage must be wide enough to accommodate the width of the seats in a row
and the width of the aisle.

.. math::
	{2w_{fuse}} \geq (\mathit{SPR}) {w_{seat}} + n_{aisle} w_{aisle} + 2*{w_{sys}}

The cross sectional area of the fuselage skin is lower bounded using a thin
walled cylinder assumption.

.. math::
	{A_{skin}} \geq 2 \pi {R_{fuse}} {t_{skin}} \end{equation}
	
The cross sectional area of the fuselage is lower bounded using the radius of
the fuselage.
\begin{equation} {A_{fuse}} \geq \pi {R_{fuse}}^{2} \end{equation}

\subsubsection{Pressure loading constraints}

The axial and hoop stresses in the fuselage skin are constrained by the
pressurization load due to the difference between cabin pressure and ambient
pressure at cruise altitude. The thickness of the skin is therefore sized by
the maximum allowable stress of the chosen material.
\begin{align}
{\sigma_x} &= \frac{{\Delta P_{over}}}{2}\frac{{R_{fuse}}}{{t_{shell}}}\\
{\sigma_{\theta}} &= {\Delta P_{over}} \frac{{R_{fuse}} }{{t_{skin}}} \\
{\sigma_{skin}} &\geq {\sigma_x} \\
{\sigma_{skin}} &\geq {\sigma_{\theta}}
\end{align} % PK diff

\subsubsection{Floor loading constraints}

The floor must be designed to withstand at least the weight of the payload and
seats multiplied by a safety factor for an emergency landing.
\begin{equation}
{P_{floor}} \geq {N_{land}} ({W_{payload}} + {W_{seat}})
\end{equation}
The maximum moment and shear in the floor are determined based on this design
load and the width of the floor, assuming that the floor/wall joints are pinned
and there are no center supports.
\begin{align}
{S_{floor}} &= \frac{P_{floor}}{2}\\
{M_{floor}} &= \frac{{P_{floor}} {w_{floor}} }{8}
\end{align}

The floor beam cross sectional area is constrained by the maximum allowable cap
stress and shear web stress for the beams.
\begin{equation}
{A_{floor}} \geq 1.5\frac{{S_{floor}}}{{\tau_{floor}}}
+ 2\frac{{M_{floor}}}{{\sigma_{floor}} {h_{floor}}}
\end{equation}

\subsubsection{3-dimensional geometry constraints}

The nose must be long enough to have an aerodynamic profile and to accommodate
the cockpit. A reasonable, but arbitrary, lower bound is employed for this
work~\cite{drela2010tasopt}.
\begin{equation} {l_{nose}} \geq 5.2 \hspace{0.2cm} \rm{m} \end{equation}

The cylindrical shell of the fuselage sits between the nosecone and tailcone.
The variables $x_{shell1}$ and $x_{shell2}$ define the beginning and end of the
cylindrical section of the fuselage, respectively, in the aircraft x-axis.
\begin{align}
{x_{shell1}} &= {l_{nose}} \\
{x_{shell2}} &\geq {l_{nose}} + {l_{shell}}
\end{align}

The number of seats is equal to the product of the seats per row and the number
of rows. Note that non-integer numbers of rows are allowed and necessary for GP
compatibility. It is assumed that the load factor is one, so that the number of
passengers is equal to the number of seats.
\begin{align}
{n_{seat}} &= {(\mathit{SPR})} {n_{rows}} \\
{n_{pass}} &= n_{seat}
\end{align}

The seat pitch and the number of rows of seats constrain the length of the
shell. The passenger floor length is lower bounded by the shell length and
twice the fuselage radius, to account for the space provided by pressure
bulkheads.
\begin{align}
{l_{shell}} &\geq {n_{rows}} {p_s} \\
{l_{floor}} &\geq 2{R_{fuse}} + {l_{shell}}
\end{align}

The length of the fuselage is constrained by the sum of the nose, shell and tail
cone lengths. A signomial equality is needed, because increased $l_{fuse}$ is
not coupled directly to increased structural weight although it results in
improved tail control authority.
\begin{equation} l_{fuse} = l_{nose} +
l_{shell} + l_{cone} \end{equation}

Other locations to constrain are the wing mid-chord and the wingbox fore and aft
bulkheads, which serve as integration limits when calculating bending loads.
\begin{align}
x_f \leq x_{wing} + 0.5 c_0 r_{w/c}\\
x_b  + 0.5 c_0 r_{w/c} \geq x_{wing}
\end{align}

The skin surface area, and, in turn, skin volume for the nose, main cabin, and
rear bulkhead are constrained. The surface area of the nose, which is
approximated as an ellipse, is lower bounded using Cantrell's
approximation~\cite{drela2010tasopt}.
\begin{align}
{S_{nose}}^{\frac85} &\geq \left(2 \pi {R_{fuse}^2}\right)^{\frac85}
	\left(\frac13 + \frac23
	\left(\frac{l_{nose}}{R_{fuse}}\right)^{\frac85} \right) \\
{S_{bulk}} &= 2 \pi {R_{fuse}}^{2} \\
{V_{cyl}} &= {A_{skin}} {l_{shell}} \\
{V_{nose}} &= {S_{nose}} {t_{skin}} \\
{V_{bulk}} &= {S_{bulk}} {t_{skin}}
\end{align}

The cabin volume is constrained assuming a cylinder with hemispherical end
caps. This is necessary for capturing buoyancy weight.
\begin{equation}
{V_{cabin}}\geq{A_{fuse}}\left(\frac23{l_{nose}} + {l_{shell}} +
\frac23{R_{fuse}} \right)
\end{equation}

\subsubsection{Tail cone constraints}

The tail cone needs to be able to transfer the loads exerted on the vertical
tail to the rest of the fuselage. The maximum torsion moment imparted by the
vertical tail depends on the maximum force exerted on the tail as well as its
span and taper ratio.  This torsion moment, along with the cone
cross sectional area and the maximum shear stress of the cone material,
bounds the necessary cone skin thickness. The cone cross sectional area,
which varies along the cone, is coarsely approximated to be the
fuselage cross sectional area (i.e. the cross sectional area of the cone base).
\begin{align}
\label{eq:Qv1} {Q_v} &= \frac{{L_{vt_{max}}}
{b_{vt}}}{3} \frac{{1 + 2{\lambda_v}}} {{1 + {\lambda_v}}} \\
\label{eq:Qv2}
{t_{cone}}&= \frac{Q_v}{2{A_{fuse}} {\tau_{cone}} }
\end{align}
The volume of the cone is a definite integral from the base to the tip of the
cone. This integral is evaluated~\cite{drela2010tasopt} and combined with
Equations \eqref{eq:Qv1} and \eqref{eq:Qv2} to give a single signomial constraint on
the cone skin volume.
\begin{equation}
R_{fuse}\tau_{cone}(1+p_{\lambda_v})V_{cone} \frac{1+\lambda_{cone}}{4 l_{cone}}
\geq L_{vt_{max}} b_{vt} \frac{p_{\lambda_v}}{3}
\end{equation}
A change of variables is used for compatibility with the tail model, which uses
$p_{\lambda_v} = 1 + 2\lambda_v$ to make a structural constraint
\gls{GP}-compatible. The same taper lower bound is introduced as in the tail
model.
\begin{equation} {p_{\lambda_v}} \geq 1.6 \end{equation}
The cone skin shear stress is constrained to equal the maximum allowable stress
in the skin material.
\begin{equation} {\tau_{cone}} = {\sigma_{skin}} \end{equation}
The tail cone taper ratio constrains the length of the cone relative to the
radius of the fuselage.
\begin{equation}
{l_{cone}} = \frac{{R_{fuse}}}{{\lambda_{cone}}}
\end{equation}

\subsubsection{Fuselage area moment of inertia constraints}

The fuselage shell consists of the skin and stringers. Its area moment of
inertia determines how effectively the fuselage is able to resist bending
loads. A shell with uniform skin thickness and stringer density has a constant
area moment of inertia in both of its bending axes, shown by the dark red line
in the lower plot of Figure~\ref{fig:fuse_bending_loads}.

To be consistent with~\cite{drela2010tasopt}, the horizontal bending
moments are defined as the moments around the aircraft's y-axis, caused by horizontal
tail loads and fuselage inertial loads, and vertical bending moments as the moments
around the aircraft's z-axis, caused by vertical tail loads.
\begin{figure}[h]
\centering
\includegraphics[width=1.0\textwidth]{figs/fuse_bending_loads.png}
\caption{TASOPT fuselage bending models (from\cite{drela2010tasopt}). The top
	graph shows the bending load distribution on the fuselage, whereas the
	bottom graph shows the area moment of inertia distribution. The
	horizontal bending loads are shown in blue, and the vertical bending
loads are shown in red.}\label{fig:fuse_bending_loads}
\end{figure}

The effective modulus-weight shell thickness is lower bounded by assuming that
only the skin and stringers contribute to bending. This constraint also uses an
assumed fractional weight of stringers that scales with the thickness of the
skin.
\begin{equation}
{t_{shell}} \geq {t_{skin}}\left(1 + {f_{string}} {r_E}
\frac{{\rho_{skin}} }{{\rho_{bend}}} \right)
\end{equation}

It is important to consider the effects of pressurization on the yield strength
of the bending material. Since pressurization stresses the airframe, the actual
yield strength of the fuselage bending material is lower than its nominal yield
strength, an effect captured using posynomial constraints.
\begin{align}
\sigma_{M_h} + r_E \frac{\Delta P_{over} R_{fuse}}{2 t_{shell}}&\leq
	\sigma_{bend} \\
\sigma_{M_v} + r_E \frac{\Delta P_{over} R_{fuse}}{2 t_{shell}}&\leq
	\sigma_{bend}
\end{align}

The aircraft shell, which is composed of the pressurized skin and stringers,
must satisfy the following horizontal and vertical area moment of inertia
constraints.
\begin{align}
I_{hshell} &\leq \pi R_{fuse}^3 t_{shell} \\
I_{vshell} &\leq \pi R_{fuse}^3 t_{shell}
\end{align}

\subsubsection{Horizontal bending model}

There are two load cases that determine the required \gls{HBM}: maximum load
factor (MLF) at $V_{ne}$, where
\begin{align}
N &= N_{lift} \\
L_{ht} &= L_{ht_{max}}
\end{align}
and emergency landing impact, where
\begin{align}
N &= N_{land} \\
L_{ht} &= 0.
\end{align}

Both load cases are considered at the aircraft's maximum takeoff weight (MTOW).
The constraints for each case are distinguished by the subscripts $MLF$ and
$Land$. Assuming the fuselage weight is uniformly distributed
throughout the shell, the bending loads due to fuselage inertial loads increase
quadratically from the ends of the fuselage shell to the aircraft \gls{CG}, as
shown by the blue line representing $M_h(x)$ in
Figure~\ref{fig:fuse_bending_loads}. The tail loads are point loads at
$x_{tail}$, and so the horizontal tail moment increases linearly from
$x_{tail}$ to the aircraft's \gls{CG}. In the maximum load factor
case, the maximum moment exerted by the horizontal tail is superimposed on the
maximum fuselage inertial moment at load factor $N_{lift}$ to size the
\gls{HBM} required. For the emergency landing impact case, only the fuselage
inertial loads are considered at $N_{land}$, assuming an unloaded horizontal
tail.

Several intermediate variables are introduced and used in constraints that
capture \gls{HBM} relationships. $A_{0h}$ represents the \gls{HBM} area that is
contributed by the aircraft shell.
\begin{equation} A_{0h} = \frac{I_{hshell}} {r_{E} h_{fuse}^2} \end{equation}

Variables $A_{1h_{Land}}$ and $A_{1h_{MLF}}$ are the \gls{HBM} lengths that are
required to sustain bending loads from the tail. Note that as the distance from
the tail increases, the moment exerted from the tail increases linearly.
\begin{align}
A_{1h_{Land}} &\geq N_{land} \frac{W_{tail} + W_{apu}}{h_{fuse} \sigma_{M_h}}\\
A_{1h_{MLF}} &\geq N_{lift} \frac{W_{tail} + W_{apu} + r_{M_h}
L_{ht_{max}}}{h_{fuse} \sigma_{M_h}}
\end{align}

Variables $A_{2h_{Land}}$ and $A_{2h_{MLF}}$ represent the \gls{HBM} required to
sustain the distributed loads in the fuselage. As the distance from the nose or
the tail increases, the moment exerted due to the distributed load grows with
the square of length.
\begin{align}
A_{2h_{Land}} &\geq N_{land} \frac{W_{payload} + W_{padd} + W_{shell} +
W_{window} + W_{insul} + W_{floor} + W_{seat}} {2 l_{shell} h_{fuse}
\sigma_{bend}} \\
A_{2h_{MLF}} &\geq N_{lift} \frac{W_{payload} + W_{padd} + W_{shell} +
W_{window} + W_{insul} + W_{floor }+ W_{seat}} {2 l_{shell} h_{fuse}
\sigma_{M_h}}
\end{align}

Bending reinforcement material in the aircraft exists where the shell inertia is
insufficient to sustain the local bending moment. Constraints are used to
determine the location over the rear fuselage $x_{hbend_\zeta}$ forward of which
additional  \gls{HBM} is required. Some simple constraints on geometry are added
to ensure a meaningful solution.  Constraints \eqref{eq:dupBend_1} through
\eqref{eq:dupBend_2} occur for both aforementioned load cases in the model (with
subscript $\zeta$ replaced by $MLF$ or $Land$) for worst-case fuselage sizing,
but have been included once in the paper to reduce redundancy.
\begin{align}
\label{eq:dupBend_1} A_{0h} &= A_{2h_\zeta} (x_{shell2} - x_{hbend_\zeta}) ^ 2 +
A_{1h_\zeta}  (x_{tail} - x_{hbend_\zeta}) \\ x_{hbend_\zeta} &\geq x_{wing}\\ x_{hbend_\zeta}
&\leq l_{fuse}  \end{align}

To be able to constrain the volume of \gls{HBM} required, the area of \gls{HBM}
required must be constrained and integrated over the length of the fuselage. As
shown by \cite{drela2010tasopt}, with some conservative approximation, the
volume of \gls{HBM} may be determined through the integration of the forward
and rear wingbox \gls{HBM} areas over the rear fuselage.
\begin{align}
A_{hbendf_\zeta} &\geq A_{2h_\zeta} (x_{shell2} - x_{f})^2 + A_{1h_\zeta}
	(x_{tail} - x_{f}) - A_{0h} \\
A_{hbendb_\zeta} &\geq A_{2h_\zeta} (x_{shell2} - x_{b})^2 + A_{1h_\zeta}
	(x_{tail} - x_{b}) - A_{0h}
\end{align}

\gls{HBM} volumes forward, over and behind the wingbox are lower bounded by the
integration of the \gls{HBM} areas over the three fuselage sections.
\begin{align}
V_{hbend_{f}} &\geq \frac{A_{2h_\zeta}} {3} ((x_{shell2} - x_{f})^3 -
	(x_{shell2} - x_{hbend_\zeta})^3) \\
&+ \frac{A_{1h_\zeta}} {2} ((x_{tail} - x_{f})^2 - (x_{tail} -
	x_{hbend_\zeta})^2) - A_{0h} (x_{hbend_\zeta} - x_{f})\nonumber\\
V_{hbend_{b}} &\geq \frac{A_{2h_\zeta}}{3} ((x_{shell2} - x_{b})^3 -
	(x_{shell2} - x_{hbend_\zeta})^3) \\
&+ \frac{A_{1h_\zeta}}{2} ((x_{tail} - x_{b})^2 - (x_{tail} -
	x_{hbend_\zeta})^2) - A_{0h} (x_{hbend_\zeta} - x_{b}) \nonumber\\
V_{hbend_{c}} &\geq 0.5 (A_{hbendf_\zeta} + A_{hbendb_\zeta}) c_{0} r_{w/c}
\label{eq:dupBend_2}
\end{align}

The total \gls{HBM} volume is lower bounded by the sum of the volumes of
\gls{HBM} required in each fuselage section.
\begin{equation}
V_{hbend} \geq V_{hbend_{c}} + V_{hbend_{f}} + V_{hbend_{b}}
\end{equation}

\subsubsection{Vertical bending model}

The \gls{VBM} is constrained by considering the
maximum tail loads that a fuselage must sustain. The vertical bending moment,
shown in red as $M_v(x)$ in Figure~\ref{fig:fuse_bending_loads}, increases
linearly from the tail to the aircraft \gls{CG}, since the tail
lift is assumed to be a point force.

As with horizontal bending, several intermediate variables are introduced
and used in constraints that capture \gls{VBM} relationships.
$B_{1v}$ is the \gls{VBM} length required to sustain the maximum vertical tail
load $L_{vt_{max}}$.  When multiplied by the moment arm of the tail relative to
the fuselage cross-sectional location, it gives the local \gls{VBM} area
required to sustain the loads.
\begin{equation}
B_{1v} = \frac{r_{M_v} L_{vt_{max}}} {w_{fuse} \sigma_{M_{v}}}
\end{equation}

$B_{0v}$ is the equivalent \gls{VBM} area provided by the fuselage shell.
\begin{equation} {B_{0v}} = \frac{{I_{vshell}}}{{r_E} {w_{fuse}}^{2}}
\end{equation}

Since tail loads are the only vertical loads to consider, the location forward
of which additional bending material is required can be determined. $x_{vbend}$
is the location where the vertical bending moment of the inertia of the
fuselage is exactly enough to sustain the maximum vertical bending loads from
the tail, expressed by a signomial equality.
\begin{align} B_{0v} &= B_{1v} (x_{tail} - x_{vbend}) \\ x_{vbend}
&\geq x_{wing} \\ x_{vbend} &\leq l_{fuse}
\end{align}

The \gls{VBM} area required at the rear of the wingbox is lower bounded by the
tail bending moment area minus the shell vertical bending moment area.
\begin{equation}
A_{vbend_{b}} \geq B_{1v} (x_{tail} - x_{b}) - B_{0v}
\end{equation}

The vertical bending volume rear of the wingbox is then constrained by
integrating $A_{vbend}$ over the rear fuselage, which yields the following
constraint.
\begin{equation}
V_{vbend_{b}} \geq 0.5 B_{1v} ((x_{tail}-x_{b})^2 - (x_{tail} - x_{vbend})^2) -
B_{0v} (x_{vbend} - x_{b})
\end{equation}

The vertical bending volume over the wingbox is the average of the bending area
required in the front and back of the wingbox. Since no vertical bending
reinforcement is required in the forward fuselage, the resulting constraint is
simply:
\begin{equation}
V_{vbend_{c}} \geq 0.5 A_{vbend_{b}} c_{0} r_{w/c}
\end{equation}

The total vertical bending reinforcement volume is the sum of the volumes over
the wingbox and the rear fuselage.
\begin{equation}
V_{vbend} \geq V_{vbend_{b}} + V_{vbend_{c}}
\end{equation}

\subsubsection{Weight build-up constraints}

The weight of the fuselage skin is the product of the skin volumes (bulkhead,
cylindrical shell, and nosecone) and the skin density.
\begin{equation}
{W_{skin}} \geq {\rho_{skin}} {g}  \left({V_{bulk}} + {V_{cyl}}
+ {V_{nose}} \right)
\end{equation}
The weight of the fuselage shell is then constrained by accounting for the
weights of the frame, stringers, and other structural components, all of which
are assumed to scale with the weight of the skin.
\begin{equation} {W_{shell}} \geq {W_{skin}}\left(1 + {f_{fadd}} +  {f_{frame}}
+  {f_{string}} \right)
\end{equation}

The weight of the floor is lower bounded by the density of the floor beams
multiplied by the floor beam volume, in addition to an assumed weight/area
density for planking.
\begin{align}
{V_{floor}} &\geq {A_{floor}} {w_{floor}} \\
{W_{floor}}&\geq{V_{floor}}{\rho_{floor}}{g}+{W''_{floor}}{l_{floor}} {w_{floor}}
\end{align}

As with the shell, the tail cone weight is bounded using assumed proportional
weights for additional structural elements, stringers, and frames.
\begin{equation}
{W_{cone}}\geq{\rho_{cone}}{g}{V_{cone}}\left(1+{f_{fadd}}+{f_{frame}} +
f_{string}\right)
\end{equation} % PK different

The weight of the horizontal and vertical bending material is the product of
the bending material density and the \gls{HBM} and \gls{VBM} volumes required
respectively.
\begin{align}
W_{hbend} &\geq \rho_{bend} g V_{hbend} \\
W_{vbend} &\geq \rho_{bend} g V_{vbend}
\end{align}

The weight of luggage is lower bounded by a buildup of 2-checked-bag
customers, 1-checked-bag customers, and average carry-on weight.
\begin{equation}
{W_{lugg}} \geq 2{W_{checked}} {f_{lugg,2}} {n_{pass}} +
{W_{checked}} {f_{lugg,1}} {n_{pass}} + {W_{carry on}}
\end{equation}

The window and insulation weight are lower bounded using assumed weight/length
and weight/area densities respectively. It is assumed that only the passenger
compartment of the the cabin is insulated and that the passenger compartment
cross sectional area is approximately 55\% of the fuselage cross sectional
area.
\begin{align}
{W_{window}} &= {W'_{window}} {l_{shell}} \\
{W_{insul}} &\geq {W''_{insul}} \left( 0.55\left({S_{bulk}}
+ {S_{nose}} \right) + 1.1\pi{R_{fuse}} {l_{shell}} \right)
\end{align}

The APU and other payload
proportional weights are accounted for using weight fractions.
$W_{padd}$ includes flight attendants, food, galleys, toilets, furnishing, doors,
lighting, air conditioning, and in-flight entertainment systems. The total seat
weight is a product of the weight per seat and the number of seats.
\begin{align}
{W_{apu}} &= {W_{payload}} {f_{apu}} \\
{W_{padd}} &= {W_{payload}} {f_{padd}} \\
{W_{seat}} &= {W'_{seat}} {n_{seat}}
\end{align}

The effective buoyancy weight of the aircraft is constrained using a specified
cabin pressure $p_{cabin}$, the ideal gas law and the approximated cabin
volume.  A conservative approximation for the buoyancy weight that does not
subtract the ambient air density from the cabin air density is used.
\begin{align}
\rho_{cabin}&= \frac{p_{cabin}}{{R} {T_{cabin}}} \\
{W_{buoy}} &= \rho_{cabin} {g} {V_{cabin}}
\end{align}

There are two methods in the model that can be used to lower bound the payload
weight. The first is the sum of the cargo, luggage, and passenger weights
(Constraint~\eqref{eq:payload1st}).  The second is through the definition of
variable $W_{avg. pass_{total}}$, which is an average payload weight per
passenger metric (Constraint~\eqref{eq:payload2nd}). For the purposes of this
paper, the second method is used, and as a result Constraint~\eqref{eq:payload1st}
is inactive.
\begin{align}
W_{pass} &= W_{avg. pass} n_{pass} \\
{W_{payload}} &\geq {W_{cargo}} + {W_{lugg}} + {W_{pass}}\label{eq:payload1st} \\
{W_{payload}} &\geq {W_{avg. pass_{total}}} {{n_{pass}}} \label{eq:payload2nd}
\end{align}

The total weight of the fuselage is lower bounded by the sum of all of the
constituent weights. The fixed weight $W_{fix}$ incorporates pilots, cockpit
windows, cockpit seats, flight instrumentation, navigation and communication
equipment, which are expected to be roughly the same for all
aircraft~\cite{drela2010tasopt}.
\begin{align}
{W_{fuse}} &\geq {W_{apu}} + {W_{buoy}} + {W_{cone}} + {W_{floor}} + W_{hbend}
	+ W_{vbend} + {W_{insul}} \\ &+ {W_{padd}} + {W_{seat}} + {W_{shell}} +
	{W_{window}} + {W_{fix}} \nonumber
\end{align}

\subsubsection{Aerodynamic constraints}

The drag of the fuselage is constrained using $C_{D_{fuse}}$ from TASOPT, which
calculates the drag using a pseudo-axisymmetric viscous/inviscid calculation,
and scaling appropriately by fuselage dimensions and Mach number.
\begin{equation}
D_{fuse} = \frac{1}{2} \rho_{\infty} V_{\infty}^2 C_{D_{fuse}} \left( l_{fuse} R_{fuse}
\frac{M^2}{M_{fuseD}^2} \right)
\end{equation}
