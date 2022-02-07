# -*- coding: utf-8 -*-

# Inspection tool for FreeCAD macro development.
# Author: Darek L (aka dprojects)
# Version: 1.0 (entry level)
# Latest version: https://github.com/dprojects/scanObjects

import FreeCAD, Draft, Spreadsheet
from PySide import QtGui, QtCore


# ############################################################################
# Qt Main
# ############################################################################
	

def showQtGUI():
	
	class QtMainClass(QtGui.QDialog):
		
		# ############################################################################
		# database
		# ############################################################################

		# database for selection
		dbSO = [] # objects
		dbSL = [] # labels
		dbSI = -1 # index
			
		# ############################################################################
		# init
		# ############################################################################

		def __init__(self):
			super(QtMainClass, self).__init__()
			self.initUI()

		def initUI(self):

			# window
			self.result = userCancelled
			self.setGeometry(10, 10, 1200, 600)
			self.setWindowTitle("scanObjects - inspection tool for macro development")
			self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

			# ############################################################################
			# selection view
			# ############################################################################

			# label
			self.objectsL = QtGui.QLabel("Select object:", self)
			self.objectsL.move(10, 10)
			
			self.list = QtGui.QListView(self)
			self.list.setMinimumSize(150, 400)
			self.list.setMaximumSize(150, 400)
			self.list.move(10, 30)

			# init db
			self.addSelection("", FreeCAD.activeDocument().Objects)

			# ############################################################################
			# info box
			# ############################################################################

			# label
			self.i0L = QtGui.QLabel("Usage:", self)
			self.i0L.move(10, 440)

			# label
			self.i1L = QtGui.QLabel("→ \t | go deeper", self)
			self.i1L.move(10, 460)

			# label
			self.i2L = QtGui.QLabel("← \t | go back", self)
			self.i2L.move(10, 480)

			# label
			self.i3L = QtGui.QLabel("↑ ↓ \t | select object", self)
			self.i3L.move(10, 500)
			
			# ############################################################################
			# output 1
			# ############################################################################

			# label
			self.o1L = QtGui.QLabel("dir():", self)
			self.o1L.move(180, 10)
			
			self.o1 = QtGui.QTextEdit(self)
			self.o1.setMinimumSize(250, 400)
			self.o1.setMaximumSize(250, 400)
			self.o1.move(180, 30)

			# ############################################################################
			# output 2
			# ############################################################################

			# label
			self.o2L = QtGui.QLabel("__dict__:", self)
			self.o2L.move(450, 10)
			
			self.o2 = QtGui.QTextEdit(self)
			self.o2.setMinimumSize(200, 400)
			self.o2.setMaximumSize(200, 400)
			self.o2.move(450, 30)

			# ############################################################################
			# output 3
			# ############################################################################

			# label
			self.o3L = QtGui.QLabel("__doc__:", self)
			self.o3L.move(670, 10)
			
			self.o3 = QtGui.QTextEdit(self)
			self.o3.setMinimumSize(300, 140)
			self.o3.setMaximumSize(300, 140)
			self.o3.move(670, 30)

			# ############################################################################
			# output 4
			# ############################################################################

			# label
			self.o4L = QtGui.QLabel("getAllDerivedFrom():", self)
			self.o4L.move(670, 240)
			
			self.o4 = QtGui.QTextEdit(self)
			self.o4.setMinimumSize(300, 70)
			self.o4.setMaximumSize(300, 70)
			self.o4.move(670, 260)

			# ############################################################################
			# output 5
			# ############################################################################

			# label
			self.o5L = QtGui.QLabel("Content:", self)
			self.o5L.move(180, 440)
			
			self.o5 = QtGui.QTextEdit(self)
			self.o5.setMinimumSize(1000, 120)
			self.o5.setMaximumSize(1000, 120)
			self.o5.move(180, 460)

			# ############################################################################
			# output 6
			# ############################################################################

			# label
			self.o6L = QtGui.QLabel("<class 'str'>:", self)
			self.o6L.move(670, 340)
			
			self.o6 = QtGui.QTextEdit(self)
			self.o6.setMinimumSize(510, 70)
			self.o6.setMaximumSize(510, 70)
			self.o6.move(670, 360)

			# ############################################################################
			# output 7
			# ############################################################################

			# label
			self.o7L = QtGui.QLabel("<class 'float'>:", self)
			self.o7L.move(670, 180)
			
			self.o7 = QtGui.QTextEdit(self)
			self.o7.setMinimumSize(300, 30)
			self.o7.setMaximumSize(300, 30)
			self.o7.move(670, 200)

			# ############################################################################
			# output 8
			# ############################################################################

			# label
			self.o8L = QtGui.QLabel("<class 'list'>:", self)
			self.o8L.move(980, 10)
			
			self.o8 = QtGui.QTextEdit(self)
			self.o8.setMinimumSize(200, 300)
			self.o8.setMaximumSize(200, 300)
			self.o8.move(980, 30)

			# ############################################################################
			# keyboard keys
			# ############################################################################

			QtGui.QShortcut(QtGui.QKeySequence("left"), self, self.keyLeft)
			QtGui.QShortcut(QtGui.QKeySequence("right"), self, self.keyRight)

			# ############################################################################
			# show
			# ############################################################################

			self.show()
		
		# ############################################################################
		# actions auto define
		# ############################################################################

		def setOutput(self, iObj):

				index = iObj.indexes()[0].row()

				# ########################################				
				# output 1
				# ########################################

				skip = 0

				try:
					result = dir(self.dbSO[self.dbSI][index])
				except:
					skip = 1

				try:
					if skip == 0:
	
						o1 = ""
						for row in result:
							o1 += row + "\n"
						
						self.o1.setPlainText(o1)
					else:
						self.o1.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 2
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index].__dict__
				except:
					skip = 1

				try:
					if skip == 0:
	
						o2 = ""
						for row in result:
							o2 += row + "\n"
						
						self.o2.setPlainText(o2)
					else:
						self.o2.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 3
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index].__doc__
				except:
					skip = 1

				try:
					if skip == 0:
						self.o3.setPlainText(result)
					else:
						self.o3.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 4
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index].getAllDerivedFrom()
				except:
					skip = 1

				try:
					if skip == 0:
	
						o4 = ""
						for row in result:
							o4 += row + "\n"
						
						self.o4.setPlainText(o4)
					else:
						self.o4.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 5
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index].Content
				except:
					skip = 1

				try:
					if skip == 0:
						self.o5.setPlainText(result)
					else:
						self.o5.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 6
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index]
				except:
					skip = 1

				try:
					if skip == 0 and isinstance(result, str):
						self.o6.setPlainText(str(result))
					else:
						self.o6.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 7
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index]
				except:
					skip = 1

				try:
					if skip == 0 and isinstance(result, float):
						self.o7.setPlainText(str(result))
					else:
						self.o7.setPlainText("")
				except:
					skip = 1

				# ########################################				
				# output 8
				# ########################################

				skip = 0

				try:
					result = self.dbSO[self.dbSI][index]
				except:
					skip = 1

				try:
					if skip == 0 and isinstance(result, list):
	
						o8 = ""
						for row in result:
							o8 += str(row) + "\n"
						
						self.o8.setPlainText(o8)
					else:
						self.o8.setPlainText("")
				except:
					skip = 1
	
		# ############################################################################
		# functions
		# ############################################################################

		def updateSelection(self):

			model = QtGui.QStandardItemModel(self.list)
			
			for o in self.dbSL[self.dbSI]:
				item = QtGui.QStandardItem(str(o))
				model.appendRow(item)
				self.list.setModel(model)
			
			self.list.selectionModel().selectionChanged.connect(self.setOutput)			

		def removeSelection(self):

			# stop remove if there is only init objects list
			if self.dbSI > 0:

				self.dbSO.pop()
				self.dbSL.pop()
				self.dbSI = self.dbSI - 1
				
				self.updateSelection()

		def addSelection(self, iObj, iList):

			# init selection view
			if iObj == "":
				self.dbSO.append(iList)
				self.dbSI = self.dbSI + 1
				self.dbSL.append([ o.Label for o in self.dbSO[self.dbSI] ])

			# if object is list (eg. faces, edges)
			elif isinstance(iObj, list):

				self.dbSO.append(iObj)
				self.dbSL.append(iObj)
				self.dbSI = self.dbSI + 1

			# all objects types
			else:

				tmpO = []
				tmpL = []
				for o in iList:
					try:
						if hasattr(iObj, o):
							tmpO.append(getattr(iObj, o))
							tmpL.append(str(o))
					except:
						skip = 1

				self.dbSO.append(tmpO)
				self.dbSL.append(tmpL)
				self.dbSI = self.dbSI + 1

			# update selection list
			self.updateSelection()

		# ############################################################################
		# actions for keyboard keys
		# ############################################################################

		def keyLeft(self):
			self.removeSelection()

		def keyRight(self):

			try:
				index = self.list.currentIndex().row()
				Obj = self.dbSO[self.dbSI][index]
				
				if isinstance(Obj, str):
					skip = 1
				elif isinstance(Obj, float):
					skip = 1
				elif isinstance(Obj, list):
					newList = Obj
					self.addSelection(Obj, newList)
				else:
					newList = dir(Obj)
					self.addSelection(Obj, newList)
			except:
				skip = 1
	
	# ############################################################################
	# final settings
	# ############################################################################

	userCancelled = "Cancelled"
	userOK = "OK"
	
	form = QtMainClass()
	form.exec_()
	
	if form.result == userCancelled:
		pass

# ###################################################################################################################
# MAIN
# ###################################################################################################################


showQtGUI()


# ###################################################################################################################
