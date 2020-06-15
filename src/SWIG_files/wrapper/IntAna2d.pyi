from enum import IntEnum
from typing import overload, NewType, Optional, Tuple

from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.gp import *


class IntAna2d_AnaIntersection:
	@overload
	def __init__(self) -> None: ...
	@overload
	def __init__(self, L1: gp_Lin2d, L2: gp_Lin2d) -> None: ...
	@overload
	def __init__(self, C1: gp_Circ2d, C2: gp_Circ2d) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d, C: gp_Circ2d) -> None: ...
	@overload
	def __init__(self, L: gp_Lin2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def __init__(self, C: gp_Circ2d, Co: IntAna2d_Conic) -> None: ...
	@overload
	def __init__(self, E: gp_Elips2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def __init__(self, P: gp_Parab2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def __init__(self, H: gp_Hypr2d, C: IntAna2d_Conic) -> None: ...
	def IdenticalElements(self) -> bool: ...
	def IsDone(self) -> bool: ...
	def IsEmpty(self) -> bool: ...
	def NbPoints(self) -> int: ...
	def ParallelElements(self) -> bool: ...
	@overload
	def Perform(self, L1: gp_Lin2d, L2: gp_Lin2d) -> None: ...
	@overload
	def Perform(self, C1: gp_Circ2d, C2: gp_Circ2d) -> None: ...
	@overload
	def Perform(self, L: gp_Lin2d, C: gp_Circ2d) -> None: ...
	@overload
	def Perform(self, L: gp_Lin2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def Perform(self, C: gp_Circ2d, Co: IntAna2d_Conic) -> None: ...
	@overload
	def Perform(self, E: gp_Elips2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def Perform(self, P: gp_Parab2d, C: IntAna2d_Conic) -> None: ...
	@overload
	def Perform(self, H: gp_Hypr2d, C: IntAna2d_Conic) -> None: ...
	def Point(self, N: int) -> IntAna2d_IntPoint: ...

class IntAna2d_Conic:
	@overload
	def __init__(self, C: gp_Circ2d) -> None: ...
	@overload
	def __init__(self, C: gp_Lin2d) -> None: ...
	@overload
	def __init__(self, C: gp_Parab2d) -> None: ...
	@overload
	def __init__(self, C: gp_Hypr2d) -> None: ...
	@overload
	def __init__(self, C: gp_Elips2d) -> None: ...
	def Coefficients(self) -> Tuple[float, float, float, float, float, float]: ...
	def Grad(self, X: float, Y: float) -> gp_XY: ...
	def NewCoefficients(self, Axis: gp_Ax2d) -> Tuple[float, float, float, float, float, float]: ...
	def ValAndGrad(self, X: float, Y: float, Grd: gp_XY) -> float: ...
	def Value(self, X: float, Y: float) -> float: ...

class IntAna2d_IntPoint:
	@overload
	def __init__(self, X: float, Y: float, U1: float, U2: float) -> None: ...
	@overload
	def __init__(self, X: float, Y: float, U1: float) -> None: ...
	@overload
	def __init__(self) -> None: ...
	def ParamOnFirst(self) -> float: ...
	def ParamOnSecond(self) -> float: ...
	def SecondIsImplicit(self) -> bool: ...
	@overload
	def SetValue(self, X: float, Y: float, U1: float, U2: float) -> None: ...
	@overload
	def SetValue(self, X: float, Y: float, U1: float) -> None: ...
	def Value(self) -> gp_Pnt2d: ...

# harray1 classes
# harray2 classes
# hsequence classes
