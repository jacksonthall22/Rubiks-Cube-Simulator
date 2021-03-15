import time
import random

import Move2
import Move3
# import Move4
# import Pll
# import Oll
# import Subsets (works in progress)

def relevantInformation():
	"""
	==========================================
	RUBIK'S CUBE SCRAMBLER AND SOLVE SIMULATOR
	==========================================

		Below is some relevant information to understanding this program.
	
	
	
	Cube State
	----------
			Rather than trying to keep track of the permutation and orientation of each 
		individual piece, this program simulates the Rubik's Cube by storing the color of
		each sticker location on the cube.
		
			The state of the cube is kept track of using the dictionary CURRENT_CUBE_STATE_3.
		Each key is a position of a sticker on the cube, and their corresponsing values are
		"w", "g", "o", "r", "y", or "b" to indicate the color of the sticker in those
		positions. The sticker positions are denoted by a string of capital letters, one for
		centers, two for edges, or three for corners.
		
			Center pieces are simply referred to as the face they are on (L, R, F, B, U, or
		D). By convention, CURRENT_CUBE_STATE_3 assumes the green face as front and white on
		top, meaning position U will always be "w", position F will always be "green", etc.
		
			For edges, the first letter is simply the face the sticker is on. The second is
		the letter of the face closest to the sticker. In other words, the second letter can
		be determined by looking at the edge piece the sticker is on, and seeing what face
		the other sticker on that edge piece is on.
		
			Corners follow the same rule. The only thing to note is the order of the
		second two letters--the first letter is still the letter of the face it is on, but
		the second two letters are always ordered such that its left/right position comes
		before its up/down position when looking at the face the sticker is on. For
		example, the bottom left sticker on the front face would be labelled "FLD" as
		opposed to "FDL".
		
			The following is the complete lettering of positions on the cube's net where
		intersection is the front face:
		
						    __________________
						   |				  |
						   |  ULB   UB   URB  |
						   |				  |
						   |  UL    U    UR   |
						   |				  |
						   |  ULF   UF   URF  |
		 ___________________________________________________________________________
		|  				   |				  |					 |					|
		|  LBU   LU   LFU  |  FLU   FU   FRU  |  RFU   RU   RBU  |  BRU   BU   BLU  |
		|  				   |				  |					 |					|
		|  LB    L    LF   |  FL    F    FR   |  RF    R    RB   |  BR    B    BL   |
		|  				   |				  |					 |					|
		|  LBD   LD   LFD  |  FLD   FD   FRD  |  RFD   RD   RBD  |  BRD   BD   BLD  |
		 ___________________________________________________________________________
						   |				  |
						   |  DLF   DF   DRF  |
						   |				  |
						   |  DL    D    DR   |
						   |				  |
						   |  DLB   DB   DRB  |
						    __________________
	
	
	
	Sticker Cycles
	--------------
		
			There are 6 * 3 = 24 possible turns one can make on the cube (excluding M, E, and 
		S--visit https://ruwix.com/the-rubiks-cube/notation/advanced/ for more information
		on move notation). The only difference from standard notation is that, in the program,
		counterclockwise moves are denoted with a "p" following the face's letter instead of
		an apostrophe. 
		
			Each move has its own function which cycles the sticker colors to simulate a turn
		of the cube. The turn of each face affects 20 stickers and has five separate cycles,
		which cycle four stickers each. Two of these cycles affect pieces on the face being
		turned and the other three affect the stickers on the "band" that runs around
		(perpendicular to) the face being turned.
		
			I will refer to the five cycles as Face Corners (FCs), Face Edges (FEs), Right
		Side Corners (RSCs), Side Edges (SEs), and Left Side Corners (LSCs). FCs and FEs are
		corner and edge stickers which are on the face being turned and that remain in the same
		plane after performing the turn. The SEs are the edge stickers that are on the "band"
		around the face. The RSCs and LSCs are the corner stickers on this band. When holding
		the face being turned on the top of the cube, the RSC stickers are the corner stickers
		on the right of the band and the LSC stickers are those on the left. (When reading 
		Right/Left Side Corners, think "Right/Left Side-Corners" as opposed to 
		"Right/Left-Side Corners".)
		
			Below is a table of the stickers that correspond to each cycle when an F move is
		applied to the cube. Find the positions on the cube's net of the pieces in each cycle
		to make sense of this system.
		
				Cycle 					Pieces in cycle
				-----					---------------
				Face Corners 			FLU, FRU, FRD, FLD
		
				Face Edges 				FL,  FU,  FR,  FD
		
				Right Side Corners 		LFD, ULF, RFU, DRF
		
				Side Edges 				LF,  UF,  RF,  DF
		
				Left Side Corners		LFU, URF, RFD, DLF
	
	"""
	pass


def welcome():
	print("\n")
	print("="*57)
	print(" "*7 + "RUBIK'S CUBE SCRAMBLER AND SOLVE SIMULATOR")
	print("="*57)
	
	def changePuzzle():
		print("\nThis program currently supports:\n")
		print("    A.  2x2 Rubik's Cube")
		print("    B.  3x3 Rubik's Cube")
		puzzle = input("\nWhich would you like to use? (Enter a letter) ")
		while puzzle.lower() not in ["a", "b"]:
			puzzle = input("\nPlease enter 'a' or 'b': ")
	
		if puzzle.lower() == "a":
			print("\nLoading 2x2 Rubik's Cube. Enter 'help' at any time for more options.")
			time.sleep(1.5)
			cube_2x2()
			changePuzzle()
		elif puzzle.lower() == "b":
			print("\nLoading 3x3 Rubik's Cube. Enter 'help' at any time for more options.")
			time.sleep(1.5)
			cube_3x3()
			changePuzzle()

	changePuzzle()


def cube_2x2():
	CURRENT_CUBE_STATE_2 = {
		"FLU": "G", "FRU": "G",					# F
		"FLD": "G", "FRD": "G",
		
		"BRU": "B", "BLU": "B",					# B
		"BRD": "B", "BLD": "B",
	
		"LBU": "O", "LFU": "O", 				# L
		"LBD": "O", "LFD": "O",
		
		"RFU": "R", "RBU": "R",					# R
		"RFD": "R", "RBD": "R",
		
		"ULB": "W", "URB": "W",					# U
		"ULF": "W", "URF": "W",
		
		"DLF": "Y", "DRF": "Y",					# D
		"DLB": "Y", "DRB": "Y"}
	
	SOLVED_CUBE_2 = {
		"FLU": "G", "FRU": "G",					# F
		"FLD": "G", "FRD": "G",
		
		"BRU": "B", "BLU": "B",					# B
		"BRD": "B", "BLD": "B",
	
		"LBU": "O", "LFU": "O", 				# L
		"LBD": "O", "LFD": "O",
		
		"RFU": "R", "RBU": "R",					# R
		"RFD": "R", "RBD": "R",
		
		"ULB": "W", "URB": "W",					# U
		"ULF": "W", "URF": "W",
		
		"DLF": "Y", "DRF": "Y",					# D
		"DLB": "Y", "DRB": "Y"}

	def displayCubeState(cube):
		print("\n\n           _________")
		print("          |         |")
		print("          |  {}   {}  |".format(cube["ULB"], cube["URB"]))
		print("          |         |")
		print("          |  {}   {}  |".format(cube["ULF"], cube["URF"]))
		print(" _________|_________|___________________")
		print("|         |         |         |         |")
		print("|  {}   {}  |  {}   {}  |  {}   {}  |  {}   {}  |".format(
														cube["LBU"], cube["LFU"], 
														cube["FLU"], cube["FRU"],
														cube["RFU"], cube["RBU"],
														cube["BRU"], cube["BLU"]))
		print("|         |         |         |         |")
		print("|  {}   {}  |  {}   {}  |  {}   {}  |  {}   {}  |".format(
														cube["LBD"], cube["LFD"],
														cube["FLD"], cube["FRD"],
														cube["RFD"], cube["RBD"],
														cube["BRD"], cube["BLD"]))
		print("|_________|_________|_________|_________|")
		print("          |         |")
		print("          |  {}   {}  |".format(cube["DLF"], cube["DRF"]))
		print("          |         |")
		print("          |  {}   {}  |".format(cube["DLB"], cube["DRB"]))
		print("          |_________|\n\n")

	def getMoves(cube):
		displayCubeState(cube)
		
		def checkForInvalidMoves(moves):
			while [move for move in moves if move not in possibleMoves and move.lower() not in commands] != []:
				moves = input("\nInvalid move. Type 'help' to see list of available moves.\nEnter moves separated by spaces: ").split()
			
			return moves

		possibleMoves = ["F", "F'", "F2",
						 "B", "B'", "B2",
						 "L", "L'", "L2",
						 "R", "R'", "R2",
						 "U", "U'", "U2",
						 "D", "D'", "D2",

						 "X", "X'", "X2",
						 "Y", "Y'", "Y2",
						 "Z", "Z'", "Z2",

						 "sexy", "sledge", "swirly", "green",
						 "sexy'", "sledge'", "swirly'", "green'"]

		commands = ["reset", "scramble", "help", "change"]
		
		makeNewMoves = True
		while makeNewMoves:
			moves = input("\nEnter moves separated by spaces: ").split()
			moves = checkForInvalidMoves(moves)
			
			# Solves cube
			if "reset" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['reset']":
					cube = solve(cube)
					displayCubeState(cube)
				
				# If user tries to type more than just "reset"
				else:
					moves = checkForInvalidMoves(moves)

			# Solves, then scrambles
			elif "scramble" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['scramble']":
					cube = solve(cube)
					
					scrambleToPrint = scramble(cube)
					cube = turnCube(cube, scrambleToPrint.split())
		
					print("\nScramble: ", scrambleToPrint)
				
				# If user tries to type more than just "scramble"
				else:
					moves = checkForInvalidMoves(moves)

			# Prints possible move list
			elif "help" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['help']":
					print("\nPossible Moves:\n")
					print("\tNormal moves:  F, B, L, R, U, D")
					print("\tCube rotations:  X, Y, Z")
					print("\tTriggers:  sexy (R U R' U'), sledge (R' F R F')")
					print("\n * All move types support their inverses and 180 degree turns. Examples:  R', Y2, etc."),
					print(" * Triggers also support inverses. Examples:  sexy', sledge'")
					print(" * Type 'reset' or 'scramble' at any time to solve the cube or to scramble it.")
					print(" * Enter 'change' at any time to change puzzle type.")
					# print("\n")
				
				# If user tries to type more than just "help"
				else:
					moves = checkForInvalidMoves(moves)
			
			# Change puzzle type
			elif "change" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['change']":
					makeNewMoves = False

				#If user tries to type more than just "change"
				else:
					moves = checkForInvalidMoves(moves)

			#If user entered only valid moves, turn the cube
			else:
				cube = turnCube(cube, moves)
	
	def turnCube(cube, moves):
		for move in moves:
			if move == "F":											# Normal moves (RUFBLD)
				cube = Move2.F(cube)
			elif move == "F'":
				cube = Move2.Fp(cube)
			elif move == "F2":
				cube = Move2.F2(cube)
			elif move == "B":
				cube = Move2.B(cube)
			elif move == "B'":
				cube = Move2.Bp(cube)
			elif move == "B2":
				cube = Move2.B2(cube)
			elif move == "L":
				cube = Move2.L(cube)
			elif move == "L'":
				cube = Move2.Lp(cube)
			elif move == "L2":
				cube = Move2.L2(cube)
			elif move == "R":
				cube = Move2.R(cube)
			elif move == "R'":
				cube = Move2.Rp(cube)
			elif move == "R2":
				cube = Move2.R2(cube)
			elif move == "U":
				cube = Move2.U(cube)
			elif move == "U'":
				cube = Move2.Up(cube)
			elif move == "U2":
				cube = Move2.U2(cube)
			elif move == "D":
				cube = Move2.D(cube)
			elif move == "D'":
				cube = Move2.Dp(cube)
			elif move == "D2":
				cube = Move2.D2(cube)
	
	
	
			elif move == "X":										# Cube rotations
				cube = Move2.X(cube)
			elif move == "X'":
				cube = Move2.Xp(cube)
			elif move == "X2":
				cube = Move2.X2(cube)
			elif move == "Y":
				cube = Move2.Y(cube)
			elif move == "Y'":
				cube = Move2.Yp(cube)
			elif move == "Y2":
				cube = Move2.Y2(cube)
			elif move == "Z":
				cube = Move2.Z(cube)
			elif move == "Z'":
				cube = Move2.Zp(cube)
			elif move == "Z2":
				cube = Move2.Z2(cube)
	
	
	
			elif move.lower() == "sexy":							# Triggers
				cube = Move2.R(cube)
				cube = Move2.U(cube)
				cube = Move2.Rp(cube)
				cube = Move2.Up(cube)
			elif move.lower() == "sexy'":
				cube = Move2.U(cube)
				cube = Move2.R(cube)
				cube = Move2.Up(cube)
				cube = Move2.Rp(cube)
			elif move.lower() == "sledge":
				cube = Move2.Rp(cube)
				cube = Move2.F(cube)
				cube = Move2.R(cube)
				cube = Move2.Fp(cube)
			elif move.lower() == "sledge'":
				cube = Move2.F(cube)
				cube = Move2.Rp(cube)
				cube = Move2.Fp(cube)
				cube = Move2.R(cube)
			elif move.lower() == "swirly":
				cube = Move2.R(cube)
				cube = Move2.U(cube)
				cube = Move2.Rp(cube)
				cube = Move2.Fp(cube)
			elif move.lower() == "swirly'":
				cube = Move2.F(cube)
				cube = Move2.R(cube)
				cube = Move2.Up(cube)
				cube = Move2.Rp(cube)
			elif move.lower() == "green":
				cube = Move2.R(cube)
				cube = Move2.U(cube)
				cube = Move2.Rp(cube)
				cube = Move2.U(cube)
			elif move.lower() == "green'":
				cube = Move2.R(cube)
				cube = Move2.U(cube)
				cube = Move2.Rp(cube)
				cube = Move2.U(cube)

		displayCubeState(cube)
	
		return cube
	
	def scramble(cube):
		moveFace = {"F": "F", "Fp": "F", "F2": "F",
					"R": "R", "Rp": "R", "R2": "R", 
					"U": "U", "Up": "U", "U2": "U", 
					"None": "None"}
	
		scrambleMoves = ["F", "Fp", "F2",
						 "R", "Rp", "R2", 
						 "U", "Up", "U2"]
	
		scramble = []
		scrambleToPrint = ""
		
		numScrambles = 10
		while numScrambles > 0:
			numScrambles -= 1
	
			nextMove = random.choice(scrambleMoves)
				
			if len(scramble) >= 1:
				lastMove = scramble[-1]
			elif len(scramble) == 0:
				lastMove = "None"
	
			# Prevents things like "R R2"
			while moveFace[nextMove] == moveFace[lastMove]:
				nextMove = random.choice(scrambleMoves)
	
			scramble.append(nextMove)
	
			# Changes moves like Rp to R' for printing
			nextMoveToPrint = ""
			if "p" in nextMove:
				nextMoveToPrint = nextMove.replace("p", "'")
			else:
				nextMoveToPrint = nextMove
	
			scrambleToPrint += nextMoveToPrint + " "
	
		return scrambleToPrint
	
	def solve(cube):
		for stickerColor in cube:
			cube[stickerColor] = SOLVED_CUBE_2[stickerColor]
	
		return cube

	def checkIfSolved(cube):
		
		pass

	CURRENT_CUBE_STATE_2 = getMoves(CURRENT_CUBE_STATE_2)


def cube_3x3():
	CURRENT_CUBE_STATE_3 = {
		"FLU": "G", "FU": "G", "FRU": "G", "FL": "G",					# F
		"FR": "G", "FLD": "G", "FD": "G", "FRD": "G",
		
		"BRU": "B", "BU": "B", "BLU": "B", "BR": "B",					# B
		"BL": "B", "BRD": "B", "BD": "B", "BLD": "B",
	
		"LBU": "O", "LU": "O", "LFU": "O", "LB": "O",					# L
		"LF": "O", "LBD": "O", "LD": "O", "LFD": "O",
		
		"RFU": "R", "RU": "R", "RBU": "R", "RF": "R",					# R
		"RB": "R", "RFD": "R", "RD": "R", "RBD": "R",
		
		"ULB": "W", "UB": "W", "URB": "W", "UL": "W",					# U
		"UR": "W", "ULF": "W", "UF": "W", "URF": "W",
		
		"DLF": "Y", "DF": "Y", "DRF": "Y", "DL": "Y",					# D
		"DR": "Y", "DLB": "Y", "DB": "Y", "DRB": "Y",
		
		"F": "G", "B": "B", "L": "O", "R": "R", "U": "W", "D": "Y"}		# Centers

	SOLVED_CUBE_3 = {
		"FLU": "G", "FU": "G", "FRU": "G", "FL": "G",					# F
		"FR": "G", "FLD": "G", "FD": "G", "FRD": "G",
		
		"BRU": "B", "BU": "B", "BLU": "B", "BR": "B",					# B
		"BL": "B", "BRD": "B", "BD": "B", "BLD": "B",
	
		"LBU": "O", "LU": "O", "LFU": "O", "LB": "O",					# L
		"LF": "O", "LBD": "O", "LD": "O", "LFD": "O",
		
		"RFU": "R", "RU": "R", "RBU": "R", "RF": "R",					# R
		"RB": "R", "RFD": "R", "RD": "R", "RBD": "R",
		
		"ULB": "W", "UB": "W", "URB": "W", "UL": "W",					# U
		"UR": "W", "ULF": "W", "UF": "W", "URF": "W",
		
		"DLF": "Y", "DF": "Y", "DRF": "Y", "DL": "Y",					# D
		"DR": "Y", "DLB": "Y", "DB": "Y", "DRB": "Y",
		
		"F": "G", "B": "B", "L": "O", "R": "R", "U": "W", "D": "Y"}		# Centers

	def displayCubeState(cube):
		print("\n\n               _____________")
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["ULB"], cube["UB"], cube["URB"]))
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["UL"], cube["U"], cube["UR"]))
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["ULF"], cube["UF"], cube["URF"]))
		print(" _____________|_____________|___________________________")
		print("|             |             |             |             |")
		print("|  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |".format(
														cube["LBU"], cube["LU"], cube["LFU"], 
														cube["FLU"], cube["FU"], cube["FRU"],
														cube["RFU"], cube["RU"], cube["RBU"],
														cube["BRU"], cube["BU"], cube["BLU"]))
		print("|             |             |             |             |")
		print("|  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |".format(
														cube["LB"], cube["L"], cube["LF"],
														cube["FL"], cube["F"], cube["FR"],
														cube["RF"], cube["R"], cube["RB"],
														cube["BR"], cube["B"], cube["BL"]))
		print("|             |             |             |             |")
		print("|  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |  {}   {}   {}  |".format(
														cube["LBD"], cube["LD"], cube["LFD"],
														cube["FLD"], cube["FD"], cube["FRD"],
														cube["RFD"], cube["RD"], cube["RBD"],
														cube["BRD"], cube["BD"], cube["BLD"]))
		print("|_____________|_____________|_____________|_____________|")
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["DLF"], cube["DF"], cube["DRF"]))
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["DL"], cube["D"], cube["DR"]))
		print("              |             |")
		print("              |  {}   {}   {}  |".format(cube["DLB"], cube["DB"], cube["DRB"]))
		print("              |_____________|\n\n")

	def getMoves(cube):
		displayCubeState(cube)
		
		def checkForInvalidMoves(moves):
			while [move for move in moves if move not in possibleMoves and move.lower() not in commands] != []:
				moves = input("\nInvalid move. Type 'help' to see list of available moves.\nEnter moves separated by spaces: ").split()
			
			return moves

		possibleMoves = ["F", "F'", "F2",
						 "B", "B'", "B2",
						 "L", "L'", "L2",
						 "R", "R'", "R2",
						 "U", "U'", "U2",
						 "D", "D'", "D2",
	
						 "f", "f'", "f2",
						 "b", "b'", "b2",
						 "l", "l'", "l2",
						 "r", "r'", "r2",
						 "u", "u'", "u2",
						 "d", "d'", "d2",
							
						 "M", "M'", "M2",
						 "E", "E'", "E2",
						 "S", "S'", "S2",
	
						 "X", "X'", "X2",
						 "Y", "Y'", "Y2",
						 "Z", "Z'", "Z2",
	
						 "sexy", "sledge", "swirly", "green",
						 "sexy'", "sledge'", "swirly'", "green'"]

		commands = ["reset", "scramble", "help", "change"]
		
		makeNewMoves = True
		while makeNewMoves:
			moves = input("\nEnter moves separated by spaces: ").split()
			moves = checkForInvalidMoves(moves)
			
			# Solves cube
			if "reset" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['reset']":
					cube = solve(cube)
					displayCubeState(cube)
				
				# If user tries to type more than just "reset"
				else:
					moves = checkForInvalidMoves(moves)

			# Solves, then scrambles
			elif "scramble" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['scramble']":
					cube = solve(cube)
					
					scrambleToPrint = scramble(cube)
					cube = turnCube(cube, scrambleToPrint.split())
		
					print("\nScramble: ", scrambleToPrint)
				
				# If user tries to type more than just "scramble"
				else:
					moves = checkForInvalidMoves(moves)

			# Prints possible move list
			elif "help" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['help']":
					print("\nPossible Moves:\n")
					print("\tNormal moves:  F, B, L, R, U, D")
					print("\tWide moves:  f, b, l, r, u, d")
					print("\tSlice moves:  M, E, S")
					print("\tCube rotations:  X, Y, Z")
					print("\tTriggers:  sexy (R U R' U'), sledge (R' F R F'), swirly (R U R' F'), green (R U R' U)")
					print("\n * All move types support their inverses and 180 degree turns. Examples:  R', b2, M2, Y', etc.")
					print(" * Triggers also support inverses. Examples:  sledge', swirly'")
					print(" * Type 'reset' or 'scramble' at any time to solve the cube or to scramble it.")
					print(" * Enter 'change' at any time to change puzzle type.")
					# print("\n")
				
				# If user tries to type more than just "help"
				else:
					moves = checkForInvalidMoves(moves)

			elif "change" in [i.lower() for i in moves]:
				if str([i.lower() for i in moves]) == "['change']":
					makeNewMoves = False

				#If user tries to type more than just "change"
				else:
					moves = checkForInvalidMoves(moves)

			#If user just entered valid moves, turn the cube
			else:
				cube = turnCube(cube, moves)
	
	def turnCube(cube, moves):
		for move in moves:
			if move == "F":											# Normal moves (RUFBLD)
				cube = Move3.F(cube)
			elif move == "F'":
				cube = Move3.Fp(cube)
			elif move == "F2":
				cube = Move3.F2(cube)
			elif move == "B":
				cube = Move3.B(cube)
			elif move == "B'":
				cube = Move3.Bp(cube)
			elif move == "B2":
				cube = Move3.B2(cube)
			elif move == "L":
				cube = Move3.L(cube)
			elif move == "L'":
				cube = Move3.Lp(cube)
			elif move == "L2":
				cube = Move3.L2(cube)
			elif move == "R":
				cube = Move3.R(cube)
			elif move == "R'":
				cube = Move3.Rp(cube)
			elif move == "R2":
				cube = Move3.R2(cube)
			elif move == "U":
				cube = Move3.U(cube)
			elif move == "U'":
				cube = Move3.Up(cube)
			elif move == "U2":
				cube = Move3.U2(cube)
			elif move == "D":
				cube = Move3.D(cube)
			elif move == "D'":
				cube = Move3.Dp(cube)
			elif move == "D2":
				cube = Move3.D2(cube)
	
	
	
			elif move == "f":										# Wide moves
				cube = Move3.f(cube)
			elif move == "f'":
				cube = Move3.fp(cube)
			elif move == "f2":
				cube = Move3.f2(cube)
			elif move == "b":
				cube = Move3.b(cube)
			elif move == "b'":
				cube = Move3.bp(cube)
			elif move == "b2":
				cube = Move3.b2(cube)
			elif move == "l":
				cube = Move3.l(cube)
			elif move == "l'":
				cube = Move3.lp(cube)
			elif move == "l2":
				cube = Move3.l2(cube)
			elif move == "r":
				cube = Move3.r(cube)
			elif move == "r'":
				cube = Move3.rp(cube)
			elif move == "r2":
				cube = Move3.r2(cube)
			elif move == "u":
				cube = Move3.u(cube)
			elif move == "u'":
				cube = Move3.up(cube)
			elif move == "u2":
				cube = Move3.u2(cube)
			elif move == "d":
				cube = Move3.d(cube)
			elif move == "d'":
				cube = Move3.dp(cube)
			elif move == "d2":
				cube = Move3.d2(cube)
	
	
	
			elif move == "M":										# Middle layer moves
				cube = Move3.M(cube)
			elif move == "M'":
				cube = Move3.Mp(cube)
			elif move == "M2":
				cube = Move3.M2(cube)
			elif move == "S":
				cube = Move3.S(cube)
			elif move == "S'":
				cube = Move3.Sp(cube)
			elif move == "S2":
				cube = Move3.S2(cube)
			elif move == "E":
				cube = Move3.E(cube)
			elif move == "E'":
				cube = Move3.Ep(cube)
			elif move == "E2":
				cube = Move3.E2(cube)
	
	
	
			elif move == "X":										# Cube rotations
				cube = Move3.X(cube)
			elif move == "X'":
				cube = Move3.Xp(cube)
			elif move == "X2":
				cube = Move3.X2(cube)
			elif move == "Y":
				cube = Move3.Y(cube)
			elif move == "Y'":
				cube = Move3.Yp(cube)
			elif move == "Y2":
				cube = Move3.Y2(cube)
			elif move == "Z":
				cube = Move3.Z(cube)
			elif move == "Z'":
				cube = Move3.Zp(cube)
			elif move == "Z2":
				cube = Move3.Z2(cube)
	
	
	
			elif move.lower() == "sexy":							# Triggers
				cube = Move3.R(cube)
				cube = Move3.U(cube)
				cube = Move3.Rp(cube)
				cube = Move3.Up(cube)
			elif move.lower() == "sexy'":
				cube = Move3.U(cube)
				cube = Move3.R(cube)
				cube = Move3.Up(cube)
				cube = Move3.Rp(cube)
			elif move.lower() == "sledge":
				cube = Move3.Rp(cube)
				cube = Move3.F(cube)
				cube = Move3.R(cube)
				cube = Move3.Fp(cube)
			elif move.lower() == "sledge'":
				cube = Move3.F(cube)
				cube = Move3.Rp(cube)
				cube = Move3.Fp(cube)
				cube = Move3.R(cube)
			elif move.lower() == "swirly":
				cube = Move3.R(cube)
				cube = Move3.U(cube)
				cube = Move3.Rp(cube)
				cube = Move3.Fp(cube)
			elif move.lower() == "swirly'":
				cube = Move3.F(cube)
				cube = Move3.R(cube)
				cube = Move3.Up(cube)
				cube = Move3.Rp(cube)
			elif move.lower() == "green":
				cube = Move3.R(cube)
				cube = Move3.U(cube)
				cube = Move3.Rp(cube)
				cube = Move3.U(cube)
			elif move.lower() == "green'":
				cube = Move3.R(cube)
				cube = Move3.U(cube)
				cube = Move3.Rp(cube)
				cube = Move3.U(cube)

		displayCubeState(cube)
	
		return cube
	
	def scramble(cube):
		moveAxis = {"F": "Z", "Fp": "Z", "F2": "Z", "B": "Z", "Bp": "Z", "B2": "Z",
					"L": "X", "Lp": "X", "L2": "X", "R": "X", "Rp": "X", "R2": "X",
					"U": "Y", "Up": "Y", "U2": "Y", "D": "Y", "Dp": "Y", "D2": "Y",
					"None": "None"}
	
		moveFace = {"F": "F", "Fp": "F", "F2": "F",
					"B": "B", "Bp": "B", "B2": "B",
					"L": "L", "Lp": "L", "L2": "L", 
					"R": "R", "Rp": "R", "R2": "R", 
					"U": "U", "Up": "U", "U2": "U", 
					"D": "D", "Dp": "D", "D2": "D",
					"None": "None"}
	
		scrambleMoves = ["F", "Fp", "F2",
						 "B", "Bp", "B2",
						 "L", "Lp", "L2", 
						 "R", "Rp", "R2", 
						 "U", "Up", "U2", 
						 "D", "Dp", "D2"]
	
		scramble = []
		scrambleToPrint = ""
		
		numScrambles = 20
		while numScrambles > 0:
			numScrambles -= 1
	
			nextMove = random.choice(scrambleMoves)
				
			if len(scramble) >= 2:
				lastMove = scramble[-1]
				secondToLastMove = scramble[-2]
			elif len(scramble) == 1:
				lastMove = scramble[-1]
				secondToLastMove == "None"
			elif len(scramble) == 0:
				lastMove = "None"
				secondToLastMove = "None"
	
			# Prevents things like "R R2" and "L' R L"
			while (moveFace[nextMove] == moveFace[lastMove]) or (moveAxis[nextMove] == moveAxis[lastMove] and moveAxis[nextMove] == moveAxis[secondToLastMove]):
				nextMove = random.choice(scrambleMoves)
	
			scramble.append(nextMove)
	
			# Changes moves like Rp to R' for printing
			nextMoveToPrint = ""
			if "p" in nextMove:
				nextMoveToPrint = nextMove.replace("p", "'")
			else:
				nextMoveToPrint = nextMove
	
			scrambleToPrint += nextMoveToPrint + " "
	
		return scrambleToPrint
	
	def solve(cube):
		for stickerColor in cube:
			cube[stickerColor] = SOLVED_CUBE_3[stickerColor]
	
		return cube
	
	def checkIfSolved(cube):
		
		pass

	CURRENT_CUBE_STATE_3 = getMoves(CURRENT_CUBE_STATE_3)


welcome()