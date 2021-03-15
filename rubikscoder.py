def assignValues():
	### Prints cube net
	print("       ___________\n      |  a  b  c  |\n _______________________\n|  d  |  e  f  g  |  h  |\n|  i  |  j  k  l  |  m  |\n|  n  |  o  p  q  |  r  |\n _______________________\n      |  s  t  u  |\n       ___________")
	
	getNewValues = True
	while getNewValues: ### Each loop uses a new set of values for a-u
		### Stores values for "a" through "u" as items in list
		lst = input("\nEnter values for \"a\" through \"u\" separated by spaces only:\n\n").split()
	
		### Assigns inputs in list to variables (separated by cycle)
		e = lst[4]; g = lst[6]; q = lst[16]; o = lst[14] # Face Edges
		f = lst[5]; l = lst[11]; p = lst[15]; j = lst[9] # Face Corners
		a = lst[0]; h = lst[7]; u = lst[20]; n = lst[13] # Right Side Corners
		b = lst[1]; m = lst[12]; t = lst[19]; i = lst[8] # Side Edges
		c = lst[2]; r = lst[17]; s = lst[18]; d = lst[3] # Left Side Corners
		k = lst[10]										 # Center Sticker

		move = k.upper() ### L, R, F, etc.
		print("\n\nCode for {}:".format(move))
		printCodeClockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)
		
		move = k.upper() + "p" ### L', R', F', etc.
		print("\n\nCode for {}:".format(move))
		printCodeCounterclockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)
		
		move = k.upper() + "2" ### L2, R2, F2, etc.
		print("\n\nCode for {}:".format(move))
		printCode180(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)

		"""
		getNewCode = True
		while getNewCode: ### Each loop prints a new code for a new turnDirection (with same a-u)
			
			### Asks for type of move--clockwise, counterclockwise, 180 degrees
			turnDirection = input("\nEnter move type: 1 for clockwise, 2 for counterclockwise, or 3 for 180 degrees: ")
			
			### Loops while user does not enter 'yes' or 'no'
			while turnDirection != "1" and turnDirection != "2" and turnDirection != "3":
				turnDirection = input("\nEnter 1 for clockwise, 2 for counterclockwise, or 3 for 180 degrees: ")
			
			if turnDirection == "1":
				move = k.upper() ### L, R, F, etc.
				printCodeClockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)
			elif turnDirection == "2":
				move = k.upper() + "p" ### L', R', F', etc.
				printCodeCounterclockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)
			elif turnDirection == "3":
				move = k.upper() + "2" ### L2, R2, F2, etc.
				printCode180(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u)

			prompt = input("\nWould you like to use the same values to generate another code? (y/n) ").lower()
			
			### Loops while user does not enter 'yes' or 'no'
			while prompt != "y" and prompt != "n":
				prompt = input("\nPlease enter 'y' or 'n': ").lower()

			### If user does not want to generate another code
			if prompt == "n":
				getNewCode = False
			"""
		prompt = input("\nWould you like to generate a code with new values for a through u? (y/n) ").lower()
		
		### Loops while user does not enter 'yes' or 'no'
		while prompt != "y" and prompt != "n":
			prompt = input("\nPlease enter 'y' or 'n': ").lower()

		### If user does not want to generate code with new values
		if prompt == "n":
			getNewValues = False

def printCodeClockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u):
	print("\n")
	print("def {}(CURRENT_CUBE_STATE, TEMP_CUBE_STATE):".format(move))
	print("---### Face Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(o, q))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(q, g))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(g, e))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(e, o))
	print("---")
	print("---### Face Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(j, p))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(p, l))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(l, f))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(f, j))
	print("---")
	print("---### Right Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(n, u))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(u, h))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(h, a))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(a, n))
	print("---")
	print("---### Side Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(i, t))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(t, m))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(m, b))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(b, i))
	print("---")
	print("---### Left Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(d, s))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(s, r))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(r, c))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(c, d))

def printCodeCounterclockwise(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u):
	print("\n")
	print("def {}(CURRENT_CUBE_STATE, TEMP_CUBE_STATE):".format(move))
	print("---### Face Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(q, o))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(o, e))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(e, g))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(g, q))
	print("---")
	print("---### Face Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(l, p))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(p, j))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(j, f))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(f, l))
	print("---")
	print("---### Right Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(h, u))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(u, n))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(n, a))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(a, h))
	print("---")
	print("---### Side Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(m, t))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(t, i))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(i, b))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(b, m))
	print("---")
	print("---### Left Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(r, s))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(s, d))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(d, c))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(c, r))

def printCode180(move, a, b, c, d, e, f, g, h, i, j, l, m, n, o, p, q, r, s, t, u):
	print("\n")
	print("def {}(CURRENT_CUBE_STATE, TEMP_CUBE_STATE):".format(move))
	print("---### Face Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(e, q))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(q, e))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(g, o))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(o, g))
	print("---")
	print("---### Face Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(f, p))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(p, f))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(j, l))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(l, j))
	print("---")
	print("---### Right Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(a, u))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(u, a))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(n, h))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(h, n))
	print("---")
	print("---### Side Edges")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(b, t))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(t, b))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(i, m))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(m, i))
	print("---")
	print("---### Left Side Corners")
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(c, s))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(s, c))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(d, r))
	print("---TEMP_CUBE_STATE[\"{}\"] = CURRENT_CUBE_STATE[\"{}\"]".format(r, d))

assignValues()

""" 
Notes
-----

a b c d e f g h i j k l m n o p q r s t u

F:
ULF UF URF LFU FLU FU FRU RFU LF FL F FR RF LFD FLD FD FRD RFD DLF DF DRF

B:
URB UB ULB RBU BRU BU BLU LBU RB BR B BL LB RBD BRD BD BLD LBD DRB DB DLB

L:
ULB UL ULF BLU LBU LU LFU FLU BL LB L LF FL BLD LBD LD LFD FLD DLB DL DLF

R:
URF UR URB FRU RFU RU RBU BRU FR RF R RB BR FRD RFD RD RBD BRD DRF DR DRB

U:
BLU BU BRU LBU ULB UB URB RBU LU UL U UR RU LFU ULF UF URF RFU FLU FU FRU

D:
FLD FD FRD LFD DLF DF DRF RFD LD DL D DR RD LBD DLB DB DRB RBD BLD BD BRD

	   ___________
	  |  a  b  c  |
 _______________________
|  d  |  e  f  g  |  h  |
|  i  |  j  k  l  |  m  |
|  n  |  o  p  q  |  r  |
 _______________________
      |  s  t  u  |
       ___________


				    __________________
				   |				  |
				   |  ULB   UB   URB  |
				   |				  |
				   |  UL    U    UR   |
				   |				  |
				   |  ULF   UF   URF  |
 __________________|__________________|_____________________________________
|  				   |				  |					 |					|
|  LBU   LU   LFU  |  FLU   FU   FRU  |  RFU   RU   RBU  |  BRU   BU   BLU  |
|  				   |				  |					 |					|
|  LB    L    LF   |  FL    F    FR   |  RF    R    RB   |  BR    B    BL   |
|  				   |				  |					 |					|
|  LBD   LD   LFD  |  FLD   FD   FRD  |  RFD   RD   RBD  |  BRD   BD   BLD  |
|__________________|__________________|__________________|__________________|
				   |				  |
				   |  DLF   DF   DRF  |
				   |				  |
				   |  DL    D    DR   |
				   |				  |
				   |  DLB   DB   DRB  |
				   |__________________|


print("			   _____________")
print("			  |			 	|")
print("			  |  {ULB}   {UB}   {URB}  |".format(CURRENT_CUBE_STATE["ULB"], CURRENT_CUBE_STATE["UB"], CURRENT_CUBE_STATE["URB"]))
print("			  |			 	|")
print("			  |  {UL}   {U}   {UR}  |".format(CURRENT_CUBE_STATE["UL"], CURRENT_CUBE_STATE["U"], CURRENT_CUBE_STATE[UR]))
print("			  |		     	|")
print("			  |  {ULF}   {UF}   {URF}  |".format(CURRENT_CUBE_STATE["ULF"], CURRENT_CUBE_STATE["UF"], CURRENT_CUBE_STATE["URF"]))
print(" _____________|_____________|___________________________")
print("|  			  |				|			  |				|")
print("|  {LBU}   {LU}   {LFU}  |  {FLU}   {FU}   {FRU}  |  {RFU}   {RU}   {RBU}  |  {BRU}   {BU}   {BLU}  |".format(
												CURRENT_CUBE_STATE["LBU"], CURRENT_CUBE_STATE["LU"], CURRENT_CUBE_STATE["LFU"], 
												CURRENT_CUBE_STATE["FLU"], CURRENT_CUBE_STATE["FU"], CURRENT_CUBE_STATE["FRU"],
												CURRENT_CUBE_STATE["RFU"], CURRENT_CUBE_STATE["RU"], CURRENT_CUBE_STATE["RBU"],
												CURRENT_CUBE_STATE["BRU"], CURRENT_CUBE_STATE["BU"], CURRENT_CUBE_STATE["BLU"]))
print("|  			  |				|			  |				|")
print("|  {LB}   {L}   {LF}  |  {FL}   {F}   {FR}  |  {RF}   {R}   {RB}  |  {BR}   {B}   {BL}  |".format(
												CURRENT_CUBE_STATE["LB"], CURRENT_CUBE_STATE["L"], CURRENT_CUBE_STATE["LF"],
												CURRENT_CUBE_STATE["FL"], CURRENT_CUBE_STATE["F"], CURRENT_CUBE_STATE["FR"],
												CURRENT_CUBE_STATE["RF"], CURRENT_CUBE_STATE["R"], CURRENT_CUBE_STATE["RB"],
												CURRENT_CUBE_STATE["BR"], CURRENT_CUBE_STATE["B"], CURRENT_CUBE_STATE["BL"]))
print("|  			  |				|			  |				|")
print("|  {LBD}   {LD}   {LFD}  |  {FLD}   {FD}   {FRD}  |  {RFD}   {RD}   {RBD}  |  {BRD}   {BD}   {BLD}  |".format(
												CURRENT_CUBE_STATE["LBD"], CURRENT_CUBE_STATE["LD"], CURRENT_CUBE_STATE["LFD"],
												CURRENT_CUBE_STATE["FLD"], CURRENT_CUBE_STATE["FD"], CURRENT_CUBE_STATE["FRD"],
												CURRENT_CUBE_STATE["RFD"], CURRENT_CUBE_STATE["RD"], CURRENT_CUBE_STATE["RBD"],
												CURRENT_CUBE_STATE["BRD"], CURRENT_CUBE_STATE["BD"], CURRENT_CUBE_STATE["BLD"]))
print(" _____________|_____________|_____________|_____________|")
print("			  |				|")
print("			  |  {DLF}   {DF}   {DRF}  |".format(CURRENT_CUBE_STATE["DLF"], CURRENT_CUBE_STATE["DF"], CURRENT_CUBE_STATE["DRF"]))
print("			  |				|")
print("			  |  {DL}   {D}   {DR}  |".format(CURRENT_CUBE_STATE["DL"], CURRENT_CUBE_STATE["D"], CURRENT_CUBE_STATE["DR"]))
print("			  |				|")
print("			  |  {DLB}   {DB}   {DRB}  |".format(CURRENT_CUBE_STATE["DLB"], CURRENT_CUBE_STATE["DB"], CURRENT_CUBE_STATE["DRB"]))
print("			  |_____________|")

			   _____________
			  |			 	|
			  |  w   w   w  |
			  |			 	|
			  |  w   w   w  |
			  |		     	|
			  |  w   w   w  |
 _____________|_____________|___________________________
|  			  |				|			  |				|
|  o   o   o  |  g   g   g  |  r   r   r  |  b   b   b  |
|  			  |				|			  |				|
|  o   o   o  |  g   g   g  |  r   r   r  |  b   b   b  |
|  			  |				|			  |				|
|  o   o   o  |  g   g   g  |  r   r   r  |  b   b   b  |
 _____________|_____________|_____________|_____________|
			  |				|
			  |  y   y   y  |
			  |				|
			  |  y   y   y  |
			  |				|
			  |  y   y   y  |
			  |_____________|

"""
