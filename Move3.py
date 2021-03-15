# Regular moves

def F(cube):
	# Face Corners
	cube["FLD"], cube["FRD"], cube["FRU"], cube["FLU"] = cube["FRD"], cube["FRU"], cube["FLU"], cube["FLD"]
	# Face Edges
	cube["FL"], cube["FD"], cube["FR"], cube["FU"] = cube["FD"], cube["FR"], cube["FU"], cube["FL"]
	# Right Side Corners
	cube["LFD"], cube["DRF"], cube["RFU"], cube["ULF"] = cube["DRF"], cube["RFU"], cube["ULF"], cube["LFD"]
	# Side Edges
	cube["LF"], cube["DF"], cube["RF"], cube["UF"] = cube["DF"], cube["RF"], cube["UF"], cube["LF"]
	# Left Side Corners
	cube["LFU"], cube["DLF"], cube["RFD"], cube["URF"] = cube["DLF"], cube["RFD"], cube["URF"], cube["LFU"]

	return cube

def Fp(cube):
	# Face Corners
	cube["FRD"], cube["FLD"], cube["FLU"], cube["FRU"] = cube["FLD"], cube["FLU"], cube["FRU"], cube["FRD"]
	# Face Edges
	cube["FR"], cube["FD"], cube["FL"], cube["FU"] = cube["FD"], cube["FL"], cube["FU"], cube["FR"]
	# Right Side Corners
	cube["RFU"], cube["DRF"], cube["LFD"], cube["ULF"] = cube["DRF"], cube["LFD"], cube["ULF"], cube["RFU"]
	# Side Edges
	cube["RF"], cube["DF"], cube["LF"], cube["UF"] = cube["DF"], cube["LF"], cube["UF"], cube["RF"]
	# Left Side Corners
	cube["RFD"], cube["DLF"], cube["LFU"], cube["URF"] = cube["DLF"], cube["LFU"], cube["URF"], cube["RFD"]

	return cube

def F2(cube):
	# Face Corners
	cube["FLU"], cube["FRD"], cube["FRU"], cube["FLD"] = cube["FRD"], cube["FLU"], cube["FLD"], cube["FRU"]
	# Face Edges
	cube["FU"], cube["FD"], cube["FL"], cube["FR"] = cube["FD"], cube["FU"], cube["FR"], cube["FL"]
	# Right Side Corners
	cube["ULF"], cube["DRF"], cube["LFD"], cube["RFU"] = cube["DRF"], cube["ULF"], cube["RFU"], cube["LFD"]
	# Side Edges
	cube["UF"], cube["DF"], cube["LF"], cube["RF"] = cube["DF"], cube["UF"], cube["RF"], cube["LF"]
	# Left Side Corners
	cube["URF"], cube["DLF"], cube["LFU"], cube["RFD"] = cube["DLF"], cube["URF"], cube["RFD"], cube["LFU"]

	return cube

def B(cube):
	# Face Corners
	cube["BRD"], cube["BLD"], cube["BLU"], cube["BRU"] = cube["BLD"], cube["BLU"], cube["BRU"], cube["BRD"]
	# Face Edges
	cube["BR"], cube["BD"], cube["BL"], cube["BU"] = cube["BD"], cube["BL"], cube["BU"], cube["BR"]
	# Right Side Corners
	cube["RBD"], cube["DLB"], cube["LBU"], cube["URB"] = cube["DLB"], cube["LBU"], cube["URB"], cube["RBD"]
	# Side Edges
	cube["RB"], cube["DB"], cube["LB"], cube["UB"] = cube["DB"], cube["LB"], cube["UB"], cube["RB"]
	# Left Side Corners
	cube["RBU"], cube["DRB"], cube["LBD"], cube["ULB"] = cube["DRB"], cube["LBD"], cube["ULB"], cube["RBU"]

	return cube

def Bp(cube):
	# Face Corners
	cube["BLD"], cube["BRD"], cube["BRU"], cube["BLU"] = cube["BRD"], cube["BRU"], cube["BLU"], cube["BLD"]
	# Face Edges
	cube["BL"], cube["BD"], cube["BR"], cube["BU"] = cube["BD"], cube["BR"], cube["BU"], cube["BL"]
	# Right Side Corners
	cube["LBU"], cube["DLB"], cube["RBD"], cube["URB"] = cube["DLB"], cube["RBD"], cube["URB"], cube["LBU"]
	# Side Edges
	cube["LB"], cube["DB"], cube["RB"], cube["UB"] = cube["DB"], cube["RB"], cube["UB"], cube["LB"]
	# Left Side Corners
	cube["LBD"], cube["DRB"], cube["RBU"], cube["ULB"] = cube["DRB"], cube["RBU"], cube["ULB"], cube["LBD"]

	return cube

def B2(cube):
	# Face Corners
	cube["BRU"], cube["BLD"], cube["BLU"], cube["BRD"] = cube["BLD"], cube["BRU"], cube["BRD"], cube["BLU"]
	# Face Edges
	cube["BU"], cube["BD"], cube["BR"], cube["BL"] = cube["BD"], cube["BU"], cube["BL"], cube["BR"]
	# Right Side Corners
	cube["URB"], cube["DLB"], cube["RBD"], cube["LBU"] = cube["DLB"], cube["URB"], cube["LBU"], cube["RBD"]
	# Side Edges
	cube["UB"], cube["DB"], cube["RB"], cube["LB"] = cube["DB"], cube["UB"], cube["LB"], cube["RB"]
	# Left Side Corners
	cube["ULB"], cube["DRB"], cube["RBU"], cube["LBD"] = cube["DRB"], cube["ULB"], cube["LBD"], cube["RBU"]

	return cube
	
def L(cube):
	# Face Corners
	cube["LBD"], cube["LFD"], cube["LFU"], cube["LBU"] = cube["LFD"], cube["LFU"], cube["LBU"], cube["LBD"]
	# Face Edges
	cube["LB"], cube["LD"], cube["LF"], cube["LU"] = cube["LD"], cube["LF"], cube["LU"], cube["LB"]
	# Right Side Corners
	cube["BLD"], cube["DLF"], cube["FLU"], cube["ULB"] = cube["DLF"], cube["FLU"], cube["ULB"], cube["BLD"]
	# Side Edges
	cube["BL"], cube["DL"], cube["FL"], cube["UL"] = cube["DL"], cube["FL"], cube["UL"], cube["BL"]
	# Left Side Corners
	cube["BLU"], cube["DLB"], cube["FLD"], cube["ULF"] = cube["DLB"], cube["FLD"], cube["ULF"], cube["BLU"]

	return cube

def Lp(cube):
	# Face Corners
	cube["LFD"], cube["LBD"], cube["LBU"], cube["LFU"] = cube["LBD"], cube["LBU"], cube["LFU"], cube["LFD"]
	# Face Edges
	cube["LF"], cube["LD"], cube["LB"], cube["LU"] = cube["LD"], cube["LB"], cube["LU"], cube["LF"]
	# Right Side Corners
	cube["FLU"], cube["DLF"], cube["BLD"], cube["ULB"] = cube["DLF"], cube["BLD"], cube["ULB"], cube["FLU"]
	# Side Edges
	cube["FL"], cube["DL"], cube["BL"], cube["UL"] = cube["DL"], cube["BL"], cube["UL"], cube["FL"]
	# Left Side Corners
	cube["FLD"], cube["DLB"], cube["BLU"], cube["ULF"] = cube["DLB"], cube["BLU"], cube["ULF"], cube["FLD"]

	return cube

def L2(cube):
	# Face Corners
	cube["LBU"], cube["LFD"], cube["LFU"], cube["LBD"] = cube["LFD"], cube["LBU"], cube["LBD"], cube["LFU"]
	# Face Edges
	cube["LU"], cube["LD"], cube["LB"], cube["LF"] = cube["LD"], cube["LU"], cube["LF"], cube["LB"]
	# Right Side Corners
	cube["ULB"], cube["DLF"], cube["BLD"], cube["FLU"] = cube["DLF"], cube["ULB"], cube["FLU"], cube["BLD"]
	# Side Edges
	cube["UL"], cube["DL"], cube["BL"], cube["FL"] = cube["DL"], cube["UL"], cube["FL"], cube["BL"]
	# Left Side Corners
	cube["ULF"], cube["DLB"], cube["BLU"], cube["FLD"] = cube["DLB"], cube["ULF"], cube["FLD"], cube["BLU"]

	return cube
	
def R(cube):
	# Face Corners
	cube["RFD"], cube["RBD"], cube["RBU"], cube["RFU"] = cube["RBD"], cube["RBU"], cube["RFU"], cube["RFD"]
	# Face Edges
	cube["RF"], cube["RD"], cube["RB"], cube["RU"] = cube["RD"], cube["RB"], cube["RU"], cube["RF"]
	# Right Side Corners
	cube["FRD"], cube["DRB"], cube["BRU"], cube["URF"] = cube["DRB"], cube["BRU"], cube["URF"], cube["FRD"]
	# Side Edges
	cube["FR"], cube["DR"], cube["BR"], cube["UR"] = cube["DR"], cube["BR"], cube["UR"], cube["FR"]
	# Left Side Corners
	cube["FRU"], cube["DRF"], cube["BRD"], cube["URB"] = cube["DRF"], cube["BRD"], cube["URB"], cube["FRU"]

	return cube

def Rp(cube):
	# Face Corners
	cube["RBD"], cube["RFD"], cube["RFU"], cube["RBU"] = cube["RFD"], cube["RFU"], cube["RBU"], cube["RBD"]
	# Face Edges
	cube["RB"], cube["RD"], cube["RF"], cube["RU"] = cube["RD"], cube["RF"], cube["RU"], cube["RB"]
	# Right Side Corners
	cube["BRU"], cube["DRB"], cube["FRD"], cube["URF"] = cube["DRB"], cube["FRD"], cube["URF"], cube["BRU"]
	# Side Edges
	cube["BR"], cube["DR"], cube["FR"], cube["UR"] = cube["DR"], cube["FR"], cube["UR"], cube["BR"]
	# Left Side Corners
	cube["BRD"], cube["DRF"], cube["FRU"], cube["URB"] = cube["DRF"], cube["FRU"], cube["URB"], cube["BRD"]

	return cube

def R2(cube):
	# Face Corners
	cube["RFU"], cube["RBD"], cube["RBU"], cube["RFD"] = cube["RBD"], cube["RFU"], cube["RFD"], cube["RBU"]
	# Face Edges
	cube["RU"], cube["RD"], cube["RF"], cube["RB"] = cube["RD"], cube["RU"], cube["RB"], cube["RF"]
	# Right Side Corners
	cube["URF"], cube["DRB"], cube["FRD"], cube["BRU"] = cube["DRB"], cube["URF"], cube["BRU"], cube["FRD"]
	# Side Edges
	cube["UR"], cube["DR"], cube["FR"], cube["BR"] = cube["DR"], cube["UR"], cube["BR"], cube["FR"]
	# Left Side Corners
	cube["URB"], cube["DRF"], cube["FRU"], cube["BRD"] = cube["DRF"], cube["URB"], cube["BRD"], cube["FRU"]

	return cube
	
def U(cube):
	# Face Corners
	cube["ULF"], cube["URF"], cube["URB"], cube["ULB"] = cube["URF"], cube["URB"], cube["ULB"], cube["ULF"]
	# Face Edges
	cube["UL"], cube["UF"], cube["UR"], cube["UB"] = cube["UF"], cube["UR"], cube["UB"], cube["UL"]
	# Right Side Corners
	cube["LFU"], cube["FRU"], cube["RBU"], cube["BLU"] = cube["FRU"], cube["RBU"], cube["BLU"], cube["LFU"]
	# Side Edges
	cube["LU"], cube["FU"], cube["RU"], cube["BU"] = cube["FU"], cube["RU"], cube["BU"], cube["LU"]
	# Left Side Corners
	cube["LBU"], cube["FLU"], cube["RFU"], cube["BRU"] = cube["FLU"], cube["RFU"], cube["BRU"], cube["LBU"]

	return cube

def Up(cube):
	# Face Corners
	cube["URF"], cube["ULF"], cube["ULB"], cube["URB"] = cube["ULF"], cube["ULB"], cube["URB"], cube["URF"]
	# Face Edges
	cube["UR"], cube["UF"], cube["UL"], cube["UB"] = cube["UF"], cube["UL"], cube["UB"], cube["UR"]
	# Right Side Corners
	cube["RBU"], cube["FRU"], cube["LFU"], cube["BLU"] = cube["FRU"], cube["LFU"], cube["BLU"], cube["RBU"]
	# Side Edges
	cube["RU"], cube["FU"], cube["LU"], cube["BU"] = cube["FU"], cube["LU"], cube["BU"], cube["RU"]
	# Left Side Corners
	cube["RFU"], cube["FLU"], cube["LBU"], cube["BRU"] = cube["FLU"], cube["LBU"], cube["BRU"], cube["RFU"]

	return cube

def U2(cube):
	# Face Corners
	cube["ULB"], cube["URF"], cube["URB"], cube["ULF"] = cube["URF"], cube["ULB"], cube["ULF"], cube["URB"]
	# Face Edges
	cube["UB"], cube["UF"], cube["UL"], cube["UR"] = cube["UF"], cube["UB"], cube["UR"], cube["UL"]
	# Right Side Corners
	cube["BLU"], cube["FRU"], cube["LFU"], cube["RBU"] = cube["FRU"], cube["BLU"], cube["RBU"], cube["LFU"]
	# Side Edges
	cube["BU"], cube["FU"], cube["LU"], cube["RU"] = cube["FU"], cube["BU"], cube["RU"], cube["LU"]
	# Left Side Corners
	cube["BRU"], cube["FLU"], cube["LBU"], cube["RFU"] = cube["FLU"], cube["BRU"], cube["RFU"], cube["LBU"]

	return cube

def D(cube):
	# Face Corners
	cube["DLB"], cube["DRB"], cube["DRF"], cube["DLF"] = cube["DRB"], cube["DRF"], cube["DLF"], cube["DLB"]
	# Face Edges
	cube["DL"], cube["DB"], cube["DR"], cube["DF"] = cube["DB"], cube["DR"], cube["DF"], cube["DL"]
	# Right Side Corners
	cube["LBD"], cube["BRD"], cube["RFD"], cube["FLD"] = cube["BRD"], cube["RFD"], cube["FLD"], cube["LBD"]
	# Side Edges
	cube["LD"], cube["BD"], cube["RD"], cube["FD"] = cube["BD"], cube["RD"], cube["FD"], cube["LD"]
	# Left Side Corners
	cube["LFD"], cube["BLD"], cube["RBD"], cube["FRD"] = cube["BLD"], cube["RBD"], cube["FRD"], cube["LFD"]

	return cube

def Dp(cube):
	# Face Corners
	cube["DRB"], cube["DLB"], cube["DLF"], cube["DRF"] = cube["DLB"], cube["DLF"], cube["DRF"], cube["DRB"]
	# Face Edges
	cube["DR"], cube["DB"], cube["DL"], cube["DF"] = cube["DB"], cube["DL"], cube["DF"], cube["DR"]
	# Right Side Corners
	cube["RFD"], cube["BRD"], cube["LBD"], cube["FLD"] = cube["BRD"], cube["LBD"], cube["FLD"], cube["RFD"]
	# Side Edges
	cube["RD"], cube["BD"], cube["LD"], cube["FD"] = cube["BD"], cube["LD"], cube["FD"], cube["RD"]
	# Left Side Corners
	cube["RBD"], cube["BLD"], cube["LFD"], cube["FRD"] = cube["BLD"], cube["LFD"], cube["FRD"], cube["RBD"]

	return cube

def D2(cube):
	# Face Corners
	cube["DLF"], cube["DRB"], cube["DRF"], cube["DLB"] = cube["DRB"], cube["DLF"], cube["DLB"], cube["DRF"]
	# Face Edges
	cube["DF"], cube["DB"], cube["DL"], cube["DR"] = cube["DB"], cube["DF"], cube["DR"], cube["DL"]
	# Right Side Corners
	cube["FLD"], cube["BRD"], cube["LBD"], cube["RFD"] = cube["BRD"], cube["FLD"], cube["RFD"], cube["LBD"]
	# Side Edges
	cube["FD"], cube["BD"], cube["LD"], cube["RD"] = cube["BD"], cube["FD"], cube["RD"], cube["LD"]
	# Left Side Corners
	cube["FRD"], cube["BLD"], cube["LFD"], cube["RBD"] = cube["BLD"], cube["FRD"], cube["RBD"], cube["LFD"]

	return cube



# Wide moves

def f(cube):
	cube = B(cube)
	cube = Z(cube)
	
	return cube

def fp(cube):
	cube = Bp(cube)
	cube = Zp(cube)
	
	return cube

def f2(cube):
	cube = B2(cube)
	cube = Z2(cube)
	
	return cube

def b(cube):
	cube = F(cube)
	cube = Zp(cube)
	
	return cube

def bp(cube):
	cube = Fp(cube)
	cube = Z(cube)
	
	return cube

def b2(cube):
	cube = F2(cube)
	cube = Z2(cube)
	
	return cube

def l(cube):
	cube = R(cube)
	cube = Xp(cube)
	
	return cube

def lp(cube):
	cube = Rp(cube)
	cube = X(cube)
	
	return cube

def l2(cube):
	cube = R2(cube)
	cube = X2(cube)
	
	return cube

def r(cube):
	cube = L(cube)
	cube = X(cube)
	
	return cube

def rp(cube):
	cube = Lp(cube)
	cube = Xp(cube)
	
	return cube

def r2(cube):
	cube = L2(cube)
	cube = X2(cube)
	
	return cube

def u(cube):
	cube = D(cube)
	cube = Y(cube)
	
	return cube

def up(cube):
	cube = Dp(cube)
	cube = Yp(cube)
	
	return cube

def u2(cube):
	cube = D2(cube)
	cube = Y2(cube)
	
	return cube

def d(cube):
	cube = U(cube)
	cube = Yp(cube)
	
	return cube

def dp(cube):
	cube = Up(cube)
	cube = Y(cube)
	
	return cube

def d2(cube):
	cube = U2(cube)
	cube = Y2(cube)
	
	return cube



# Slice moves

def M(cube):
	# Centers
	cube["F"], cube["U"], cube["B"], cube["D"] = cube["U"], cube["B"], cube["D"], cube["F"]
	# Bottom Edges
	cube["FD"], cube["UF"], cube["BU"], cube["DB"] = cube["UF"], cube["BU"], cube["DB"], cube["FD"]
	# Top Edges
	cube["FU"], cube["UB"], cube["BD"], cube["DF"] = cube["UB"], cube["BD"], cube["DF"], cube["FU"]

	return cube

def Mp(cube):
	# Centers
	cube["U"], cube["B"], cube["D"], cube["F"] = cube["F"], cube["U"], cube["B"], cube["D"]
	# Bottom Edges
	cube["UF"], cube["BU"], cube["DB"], cube["FD"] = cube["FD"], cube["UF"], cube["BU"], cube["DB"]
	# Top Edges
	cube["UB"], cube["BD"], cube["DF"], cube["FU"] = cube["FU"], cube["UB"], cube["BD"], cube["DF"]

	return cube

def M2(cube):
	# Centers
	cube["F"], cube["U"], cube["B"], cube["D"] = cube["B"], cube["D"], cube["F"], cube["U"]
	# Bottom Edges
	cube["FD"], cube["UF"], cube["BU"], cube["DB"] = cube["BU"], cube["DB"], cube["FD"], cube["UF"]
	# Top Edges
	cube["FU"], cube["UB"], cube["BD"], cube["DF"] = cube["BD"], cube["DF"], cube["FU"], cube["UB"]

	return cube

def E(cube):
	# Centers
	cube["F"], cube["L"], cube["B"], cube["R"] = cube["R"], cube["F"], cube["L"], cube["B"]
	# Right Edges
	cube["FR"], cube["LF"], cube["BL"], cube["RB"] = cube["RB"], cube["FR"], cube["LF"], cube["BL"]
	# Left Edges
	cube["FL"], cube["LB"], cube["BR"], cube["RF"] = cube["RF"], cube["FL"], cube["LB"], cube["BR"]

	return cube

def Ep(cube):
	# Centers
	cube["R"], cube["F"], cube["L"], cube["B"] = cube["F"], cube["L"], cube["B"], cube["R"]
	# Right Edges
	cube["RB"], cube["FR"], cube["LF"], cube["BL"] = cube["FR"], cube["LF"], cube["BL"], cube["RB"]
	# Left Edges
	cube["RF"], cube["FL"], cube["LB"], cube["BR"] = cube["FL"], cube["LB"], cube["BR"], cube["RF"]

	return cube

def E2(cube):
	# Centers
	cube["F"], cube["L"], cube["B"], cube["R"] = cube["B"], cube["R"], cube["F"], cube["L"]
	# Right Edges
	cube["FR"], cube["LF"], cube["BL"], cube["RB"] = cube["BL"], cube["RB"], cube["FR"], cube["LF"]
	# Left Edges
	cube["FL"], cube["LB"], cube["BR"], cube["RF"] = cube["BR"], cube["RF"], cube["FL"], cube["LB"]

	return cube

def S(cube):
	# Centers
	cube["U"], cube["R"], cube["D"], cube["L"] = cube["L"], cube["U"], cube["R"], cube["D"]
	# Right Edges
	cube["UR"], cube["RD"], cube["DL"], cube["LU"] = cube["LU"], cube["UR"], cube["RD"], cube["DL"]
	# Left Edges
	cube["UL"], cube["RU"], cube["DR"], cube["LD"] = cube["LD"], cube["UL"], cube["RU"], cube["DR"]

	return cube

def Sp(cube):
	# Centers
	cube["L"], cube["U"], cube["R"], cube["D"] = cube["U"], cube["R"], cube["D"], cube["L"]
	# Right Edges
	cube["LU"], cube["UR"], cube["RD"], cube["DL"] = cube["UR"], cube["RD"], cube["DL"], cube["LU"]
	# Left Edges
	cube["LD"], cube["UL"], cube["RU"], cube["DR"] = cube["UL"], cube["RU"], cube["DR"], cube["LD"]

	return cube

def S2(cube):
	# Centers
	cube["U"], cube["R"], cube["D"], cube["L"] = cube["D"], cube["L"], cube["U"], cube["R"]
	# Right Edges
	cube["UR"], cube["RD"], cube["DL"], cube["LU"] = cube["DL"], cube["LU"], cube["UR"], cube["RD"]
	# Left Edges
	cube["UL"], cube["RU"], cube["DR"], cube["LD"] = cube["DR"], cube["LD"], cube["UL"], cube["RU"]

	return cube



# Cube rotations

def X(cube):
	cube = R(cube)
	cube = Lp(cube)
	cube = Mp(cube)

	return cube

def Xp(cube):
	cube = Rp(cube)
	cube = L(cube)
	cube = M(cube)

	return cube

def X2(cube):
	cube = R2(cube)
	cube = L2(cube)
	cube = M2(cube)

	return cube

def Y(cube):
	cube = U(cube)
	cube = Dp(cube)
	cube = E(cube)

	return cube

def Yp(cube):
	cube = Up(cube)
	cube = D(cube)
	cube = Ep(cube)

	return cube

def Y2(cube):
	cube = U2(cube)
	cube = D2(cube)
	cube = E2(cube)

	return cube

def Z(cube):
	cube = F(cube)
	cube = Bp(cube)
	cube = S(cube)

	return cube

def Zp(cube):
	cube = Fp(cube)
	cube = B(cube)
	cube = Sp(cube)

	return cube

def Z2(cube):
	cube = F2(cube)
	cube = B2(cube)
	cube = S2(cube)

	return cube