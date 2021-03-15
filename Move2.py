# Regular moves

def F(cube):
	# Face Corners
	cube["FLD"], cube["FRD"], cube["FRU"], cube["FLU"] = cube["FRD"], cube["FRU"], cube["FLU"], cube["FLD"]
	# Right Side Corners
	cube["LFD"], cube["DRF"], cube["RFU"], cube["ULF"] = cube["DRF"], cube["RFU"], cube["ULF"], cube["LFD"]
	# Left Side Corners
	cube["LFU"], cube["DLF"], cube["RFD"], cube["URF"] = cube["DLF"], cube["RFD"], cube["URF"], cube["LFU"]

	return cube

def Fp(cube):
	# Face Corners
	cube["FRD"], cube["FLD"], cube["FLU"], cube["FRU"] = cube["FLD"], cube["FLU"], cube["FRU"], cube["FRD"]
	# Right Side Corners
	cube["RFU"], cube["DRF"], cube["LFD"], cube["ULF"] = cube["DRF"], cube["LFD"], cube["ULF"], cube["RFU"]
	# Left Side Corners
	cube["RFD"], cube["DLF"], cube["LFU"], cube["URF"] = cube["DLF"], cube["LFU"], cube["URF"], cube["RFD"]

	return cube

def F2(cube):
	# Face Corners
	cube["FLU"], cube["FRD"], cube["FRU"], cube["FLD"] = cube["FRD"], cube["FLU"], cube["FLD"], cube["FRU"]
	# Right Side Corners
	cube["ULF"], cube["DRF"], cube["LFD"], cube["RFU"] = cube["DRF"], cube["ULF"], cube["RFU"], cube["LFD"]
	# Left Side Corners
	cube["URF"], cube["DLF"], cube["LFU"], cube["RFD"] = cube["DLF"], cube["URF"], cube["RFD"], cube["LFU"]

	return cube

def B(cube):
	# Face Corners
	cube["BRD"], cube["BLD"], cube["BLU"], cube["BRU"] = cube["BLD"], cube["BLU"], cube["BRU"], cube["BRD"]
	# Right Side Corners
	cube["RBD"], cube["DLB"], cube["LBU"], cube["URB"] = cube["DLB"], cube["LBU"], cube["URB"], cube["RBD"]
	# Left Side Corners
	cube["RBU"], cube["DRB"], cube["LBD"], cube["ULB"] = cube["DRB"], cube["LBD"], cube["ULB"], cube["RBU"]

	return cube

def Bp(cube):
	# Face Corners
	cube["BLD"], cube["BRD"], cube["BRU"], cube["BLU"] = cube["BRD"], cube["BRU"], cube["BLU"], cube["BLD"]
	# Right Side Corners
	cube["LBU"], cube["DLB"], cube["RBD"], cube["URB"] = cube["DLB"], cube["RBD"], cube["URB"], cube["LBU"]
	# Left Side Corners
	cube["LBD"], cube["DRB"], cube["RBU"], cube["ULB"] = cube["DRB"], cube["RBU"], cube["ULB"], cube["LBD"]

	return cube

def B2(cube):
	# Face Corners
	cube["BRU"], cube["BLD"], cube["BLU"], cube["BRD"] = cube["BLD"], cube["BRU"], cube["BRD"], cube["BLU"]
	# Right Side Corners
	cube["URB"], cube["DLB"], cube["RBD"], cube["LBU"] = cube["DLB"], cube["URB"], cube["LBU"], cube["RBD"]
	# Left Side Corners
	cube["ULB"], cube["DRB"], cube["RBU"], cube["LBD"] = cube["DRB"], cube["ULB"], cube["LBD"], cube["RBU"]

	return cube
	
def L(cube):
	# Face Corners
	cube["LBD"], cube["LFD"], cube["LFU"], cube["LBU"] = cube["LFD"], cube["LFU"], cube["LBU"], cube["LBD"]
	# Right Side Corners
	cube["BLD"], cube["DLF"], cube["FLU"], cube["ULB"] = cube["DLF"], cube["FLU"], cube["ULB"], cube["BLD"]
	# Left Side Corners
	cube["BLU"], cube["DLB"], cube["FLD"], cube["ULF"] = cube["DLB"], cube["FLD"], cube["ULF"], cube["BLU"]

	return cube

def Lp(cube):
	# Face Corners
	cube["LFD"], cube["LBD"], cube["LBU"], cube["LFU"] = cube["LBD"], cube["LBU"], cube["LFU"], cube["LFD"]
	# Right Side Corners
	cube["FLU"], cube["DLF"], cube["BLD"], cube["ULB"] = cube["DLF"], cube["BLD"], cube["ULB"], cube["FLU"]
	# Left Side Corners
	cube["FLD"], cube["DLB"], cube["BLU"], cube["ULF"] = cube["DLB"], cube["BLU"], cube["ULF"], cube["FLD"]

	return cube

def L2(cube):
	# Face Corners
	cube["LBU"], cube["LFD"], cube["LFU"], cube["LBD"] = cube["LFD"], cube["LBU"], cube["LBD"], cube["LFU"]
	# Right Side Corners
	cube["ULB"], cube["DLF"], cube["BLD"], cube["FLU"] = cube["DLF"], cube["ULB"], cube["FLU"], cube["BLD"]
	# Left Side Corners
	cube["ULF"], cube["DLB"], cube["BLU"], cube["FLD"] = cube["DLB"], cube["ULF"], cube["FLD"], cube["BLU"]

	return cube
	
def R(cube):
	# Face Corners
	cube["RFD"], cube["RBD"], cube["RBU"], cube["RFU"] = cube["RBD"], cube["RBU"], cube["RFU"], cube["RFD"]
	# Right Side Corners
	cube["FRD"], cube["DRB"], cube["BRU"], cube["URF"] = cube["DRB"], cube["BRU"], cube["URF"], cube["FRD"]
	# Left Side Corners
	cube["FRU"], cube["DRF"], cube["BRD"], cube["URB"] = cube["DRF"], cube["BRD"], cube["URB"], cube["FRU"]

	return cube

def Rp(cube):
	# Face Corners
	cube["RBD"], cube["RFD"], cube["RFU"], cube["RBU"] = cube["RFD"], cube["RFU"], cube["RBU"], cube["RBD"]
	# Right Side Corners
	cube["BRU"], cube["DRB"], cube["FRD"], cube["URF"] = cube["DRB"], cube["FRD"], cube["URF"], cube["BRU"]
	# Left Side Corners
	cube["BRD"], cube["DRF"], cube["FRU"], cube["URB"] = cube["DRF"], cube["FRU"], cube["URB"], cube["BRD"]

	return cube

def R2(cube):
	# Face Corners
	cube["RFU"], cube["RBD"], cube["RBU"], cube["RFD"] = cube["RBD"], cube["RFU"], cube["RFD"], cube["RBU"]
	# Right Side Corners
	cube["URF"], cube["DRB"], cube["FRD"], cube["BRU"] = cube["DRB"], cube["URF"], cube["BRU"], cube["FRD"]
	# Left Side Corners
	cube["URB"], cube["DRF"], cube["FRU"], cube["BRD"] = cube["DRF"], cube["URB"], cube["BRD"], cube["FRU"]

	return cube
	
def U(cube):
	# Face Corners
	cube["ULF"], cube["URF"], cube["URB"], cube["ULB"] = cube["URF"], cube["URB"], cube["ULB"], cube["ULF"]
	# Right Side Corners
	cube["LFU"], cube["FRU"], cube["RBU"], cube["BLU"] = cube["FRU"], cube["RBU"], cube["BLU"], cube["LFU"]
	# Left Side Corners
	cube["LBU"], cube["FLU"], cube["RFU"], cube["BRU"] = cube["FLU"], cube["RFU"], cube["BRU"], cube["LBU"]

	return cube

def Up(cube):
	# Face Corners
	cube["URF"], cube["ULF"], cube["ULB"], cube["URB"] = cube["ULF"], cube["ULB"], cube["URB"], cube["URF"]
	# Right Side Corners
	cube["RBU"], cube["FRU"], cube["LFU"], cube["BLU"] = cube["FRU"], cube["LFU"], cube["BLU"], cube["RBU"]
	# Left Side Corners
	cube["RFU"], cube["FLU"], cube["LBU"], cube["BRU"] = cube["FLU"], cube["LBU"], cube["BRU"], cube["RFU"]

	return cube

def U2(cube):
	# Face Corners
	cube["ULB"], cube["URF"], cube["URB"], cube["ULF"] = cube["URF"], cube["ULB"], cube["ULF"], cube["URB"]
	# Right Side Corners
	cube["BLU"], cube["FRU"], cube["LFU"], cube["RBU"] = cube["FRU"], cube["BLU"], cube["RBU"], cube["LFU"]
	# Left Side Corners
	cube["BRU"], cube["FLU"], cube["LBU"], cube["RFU"] = cube["FLU"], cube["BRU"], cube["RFU"], cube["LBU"]

	return cube

def D(cube):
	# Face Corners
	cube["DLB"], cube["DRB"], cube["DRF"], cube["DLF"] = cube["DRB"], cube["DRF"], cube["DLF"], cube["DLB"]
	# Right Side Corners
	cube["LBD"], cube["BRD"], cube["RFD"], cube["FLD"] = cube["BRD"], cube["RFD"], cube["FLD"], cube["LBD"]
	# Left Side Corners
	cube["LFD"], cube["BLD"], cube["RBD"], cube["FRD"] = cube["BLD"], cube["RBD"], cube["FRD"], cube["LFD"]

	return cube

def Dp(cube):
	# Face Corners
	cube["DRB"], cube["DLB"], cube["DLF"], cube["DRF"] = cube["DLB"], cube["DLF"], cube["DRF"], cube["DRB"]
	# Right Side Corners
	cube["RFD"], cube["BRD"], cube["LBD"], cube["FLD"] = cube["BRD"], cube["LBD"], cube["FLD"], cube["RFD"]
	# Left Side Corners
	cube["RBD"], cube["BLD"], cube["LFD"], cube["FRD"] = cube["BLD"], cube["LFD"], cube["FRD"], cube["RBD"]

	return cube

def D2(cube):
	# Face Corners
	cube["DLF"], cube["DRB"], cube["DRF"], cube["DLB"] = cube["DRB"], cube["DLF"], cube["DLB"], cube["DRF"]
	# Right Side Corners
	cube["FLD"], cube["BRD"], cube["LBD"], cube["RFD"] = cube["BRD"], cube["FLD"], cube["RFD"], cube["LBD"]
	# Left Side Corners
	cube["FRD"], cube["BLD"], cube["LFD"], cube["RBD"] = cube["BLD"], cube["FRD"], cube["RBD"], cube["LFD"]

	return cube



# Cube Rotations

def X(cube):
	cube = R(cube)
	cube = Lp(cube)

	return cube

def Xp(cube):
	cube = Rp(cube)
	cube = L(cube)

	return cube

def X2(cube):
	cube = R2(cube)
	cube = L2(cube)

	return cube

def Y(cube):
	cube = U(cube)
	cube = Dp(cube)

	return cube

def Yp(cube):
	cube = Up(cube)
	cube = D(cube)

	return cube

def Y2(cube):
	cube = U2(cube)
	cube = D2(cube)

	return cube

def Z(cube):
	cube = F(cube)
	cube = Bp(cube)

	return cube

def Zp(cube):
	cube = Fp(cube)
	cube = B(cube)

	return cube

def Z2(cube):
	cube = F2(cube)
	cube = B2(cube)

	return cube