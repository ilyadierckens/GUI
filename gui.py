# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import PyQt5
# import RPi.GPIO as GPIO
import time
import subprocess
import update


#### 		Variabelen creëren en default 0 maken 		###

x = 0
bseatp = 0
brakep = 0
hornp = 0
seatswitchp = 0
bnextpagep = 0
forwardp = 0
neutralp = 0
reversep = 0
status = " Neutral"
parkingbrakep = 0
fluidp = 0
slider1changen = 0
slider2changen = 0
slider3changen = 0
sb = 0
bb = 0
hs = 0
se = 0
pe = 0
fl = 0
gloeilampohm = 89.3
c1V = 0
c1A = 0
psV = 0
psA = 0
liftupV = 0
liftupA = 0
liftdownV = 0
liftdownA = 0
tiltupV = 0
tiltupA = 0
tiltdownV = 0
tiltdownA = 0
V3rdV = 0
A3rdA = 0
V4thV = 0
A4thA = 0
p1pressed = 0
homepagen = 0
conclusiony = 0
progupdaten = 0
piupdaten = 0


###		Klasse PiLogic maken met alle Pi functies	###

class PiLogic():
	# GPIO.setwarnings(False)		# GPIO warnings uitzetten
	# GPIO.setmode(GPIO.BCM)		#

		# GPIO pinnen als uitgang  #
	# GPIO.setup(1,GPIO.OUT)
	# GPIO.setup(2,GPIO.OUT)
	# GPIO.setup(3,GPIO.OUT)
	# GPIO.setup(4,GPIO.OUT)
	# GPIO.setup(5,GPIO.OUT)
	# GPIO.setup(6,GPIO.OUT)
	# GPIO.setup(7,GPIO.OUT)
	# GPIO.setup(8,GPIO.OUT)


	def piseatbelt():				#	SeatbeltSwitch relais activeren/deactiveren
		global sb
		if (sb == 0):
			# GPIO.output(1,GPIO.HIGH)
			sb = 1

		else:
			# GPIO.output(1,GPIO.LOW)
			sb = 0

	def pibrake():					# 	BrakeSwitch relais activeren/deactiveren
		global bb
		if (bb == 0):
			# GPIO.output(2,GPIO.HIGH)
			bb = 1

		else:
			# GPIO.output(2,GPIO.LOW)
			bb = 0

	def pihorn():					#	HornSwitch relais activeren/deactiveren
		global hs
		if (hs == 0):
			# GPIO.output(3,GPIO.HIGH)
			hs = 1

		else:
			# GPIO.output(3,GPIO.LOW)
			hs = 0

	def piseat():					#	SeatSwitch relais activeren/deactiveren
		global se
		if (se == 0):
			# GPIO.output(4,GPIO.HIGH)
			se = 1

		else:
			# GPIO.output(4,GPIO.LOW)
			se = 0

	def piparking():				#	ParkingBreak relais activeren/deactiveren
		global pe
		if (pe == 0):
			# GPIO.output(5,GPIO.HIGH)
			pe = 1

		else:
			# GPIO.output(5,GPIO.LOW)
			pe = 0

	def pifluid():					#	BrakeFluidSwitch relais activeren/deactiveren
		global fl
		if (fl == 0):
			# GPIO.output(6,GPIO.HIGH)
			fl = 1

		else:
			# GPIO.output(6,GPIO.LOW)
			fl = 0

	def piforwardon():
		# GPIO.output(7,GPIO.HIGH)
		PiLogic.pireverseoff()

	def piforwardoff():
		# GPIO.output(7,GPIO.LOW)
		print("forwardoff")

	def pireverseon():
		# GPIO.output(8,GPIO.HIGH)
		PiLogic.piforwardoff()

	def pireverseoff():
		# GPIO.output(8,GPIO.LOW)
		print("reverseoff")


###		Klasse die al de logica van het programma maakt 	###

class ProgramLogic():

	def clear():			#Functie om alle text van je scherm te doen
		global bnextpagep
		global p1pressed


		lhome.hide()

		l1.hide()
		lc1.hide()
		pc1off.hide()
		pc1on.hide()
		lc1V.hide()
		lc1A.hide()
		lps.hide()
		ppsoff.hide()
		ppson.hide()
		lpsV.hide()
		lpsA.hide()
		lliftup.hide()
		pliftupoff.hide()
		pliftupon.hide()
		lliftupV.hide()
		lliftupA.hide()
		lliftdown.hide()
		pliftdownoff.hide()
		pliftdownon.hide()
		lliftdownV.hide()
		lliftdownA.hide()
		ltiltup.hide()
		ptiltupoff.hide()
		ptiltupon.hide()
		ltiltupV.hide()
		ltiltupA.hide()
		ltiltdown.hide()
		ptiltdownoff.hide()
		ptiltdownon.hide()
		ltiltdownV.hide()
		ltiltdownA.hide()
		l3rd.hide()
		p3rdon.hide()
		p3rdoff.hide()
		l3rdV.hide()
		l3rdA.hide()
		l4th.hide()
		p4thon.hide()
		p4thoff.hide()
		l4thV.hide()
		l4thA.hide()


		if (p1pressed == 1):
			ProgramLogic.pageonepressed()
			p1pressed = 0
		else:
			pc1off.hide()
			pc1on.hide()
			ppsoff.hide()
			ppson.hide()
			pliftdownoff.hide()
			pliftdownon.hide()
			pliftupoff.hide()
			pliftdownoff.hide()
			ptiltupoff.hide()
			ptiltupon.hide()
			ptiltdownoff.hide()
			ptiltdownoff.hide()
		bnexthomepage.hide()
		bpreviousehome.hide()

		l2.hide()
		bseat.hide()
		lseattitle.hide()
		pwit.hide()
		psdeac.hide()
		pwit2.hide()
		psactivated.hide()
		lseatoff.hide()
		lseaton.hide()
		bbrake.hide()
		lbraketitle.hide()
		pwit3.hide()
		pbdeac.hide()
		pwit4.hide()
		pbactivated.hide()
		lbrakeoff.hide()
		lbrakeon.hide()
		bhorn.hide()
		lhorntitle.hide()
		pwit5.hide()
		phdeac.hide()
		pwit6.hide()
		phactivated.hide()
		lhornoff.hide()
		lhornon.hide()
		bseatswitch.hide()
		lseatswitchtitle.hide()
		lseatswitchoff.hide()
		lseatswitchon.hide()
		pwit7.hide()
		pswdeac.hide()
		pwit8.hide()
		pswactivated.hide()
		bforward.hide()
		lforwardtitle.hide()
		lstatus.hide()
		lstatusc.hide()
		bneutral.hide()
		breverse.hide()
		bparkingbrake.hide()
		lparkingtitle.hide()
		lparkingoff.hide()
		lparkingon.hide()
		pwit9.hide()
		ppadeac.hide()
		pwit10.hide()
		ppaactivated.hide()
		bfluid.hide()
		lfluidtitle.hide()
		lfluidoff.hide()
		lfluidon.hide()
		pwit11.hide()
		pflactivated.hide()
		pwit12.hide()
		pfldeac.hide()
		bnextpage.hide()
		bprevious.hide()

		l3.hide()
		lTireA.hide()
		slider1.hide()
		lTireV.hide()
		pwheel.hide()
		loilp.hide()
		slider2.hide()
		loilV.hide()
		poil.hide()
		ltiltingp.hide()
		slider3.hide()
		ltiltV.hide()
		ptilt.hide()

		l4.hide()
		bupdate.hide()
		bupdatepi.hide()
		pdiagnostic.hide()
		ldiag.hide()
		lconclusion.hide()
		lstage1.hide()
		lstage2.hide()
		lstage3.hide()
		lconc1.hide()
		lconc2.hide()

		l5.hide()

	def showpage_one_logic():
		if (homepagen == 0):
			ProgramLogic.showpage_one_1()

		else:
			ProgramLogic.showpage_one_2()

	def showpage_one_1():
		l1.show()

		lc1.show()
		pc1off.show()
		lc1V.show()
		lc1A.show()
		if (c1V > 0):
			pc1on.show()
			pc1off.hide()
		else:
			pc1off.show()
			pc1on.hide()

		lps.show()
		ppsoff.show()
		lpsV.show()
		lpsA.show()
		if (psV > 0):
			ppson.show()
			ppsoff.hide()
		else:
			ppsoff.show()
			ppson.hide()

		lliftup.show()
		pliftupoff.show()
		lliftupV.show()
		lliftupA.show()
		if (liftupV > 0):
			pliftupon.show()
			pliftupoff.hide()
		else:
			pliftupoff.show()
			pliftupon.hide()

		lliftdown.show()
		pliftdownoff.show()
		lliftdownV.show()
		lliftdownA.show()
		if (liftdownV > 0):
			pliftdownon.show()
			pliftdownoff.hide()
		else:
			pliftdownoff.show()
			pliftdownon.hide()

		ltiltup.show()
		ptiltupoff.show()
		ltiltupV.show()
		ltiltupA.show()
		if (tiltupV > 0):
			ptiltupon.show()
			ptiltupoff.hide()
		else:
			ptiltupoff.show()
			ptiltupon.hide()

		ltiltdown.show()
		ptiltdownoff.show()
		ltiltdownV.show()
		ltiltdownA.show()
		if (tiltdownV > 0):
			ptiltdownon.show()
			ptiltdownoff.hide()
		else:
			ptiltdownoff.show()
			ptiltdownon.hide()

		bnexthomepage.show()

	def hidepage_one_1():
		l1.hide()

		lc1.hide()
		pc1off.hide()
		lc1V.hide()
		lc1A.hide()
		pc1on.hide()

		lps.hide()
		ppsoff.hide()
		lpsV.hide()
		lpsA.hide()
		ppson.hide()

		lliftup.hide()
		pliftupoff.hide()
		lliftupV.hide()
		lliftupA.hide()
		pliftupon.hide()

		lliftdown.hide()
		pliftdownoff.hide()
		lliftdownV.hide()
		lliftdownA.hide()
		pliftdownon.hide()

		ltiltup.hide()
		ptiltupoff.hide()
		ltiltupV.hide()
		ltiltupA.hide()
		ptiltupon.hide()

		ltiltdown.hide()
		ptiltdownoff.hide()
		ltiltdownV.hide()
		ltiltdownA.hide()
		ptiltdownon.hide()

		bnexthomepage.hide()

	def showpage_one_2():
		l1.show()

		l3rd.show()
		p3rdoff.show()
		l3rdV.show()
		l3rdA.show()
		if (V3rdV > 0):
			p3rdon.show()
			p3rdoff.hide()
		else:
			p3rdoff.show()
			p3rdon.hide()

		l4th.show()
		p4thoff.show()
		l4thV.show()
		l4thA.show()
		if (V4thV > 0):
			p4thon.show()
			p4thoff.hide()
		else:
			p4thoff.show()
			p4thon.hide()

		bpreviousehome.show()

	def hidepage_one_2():
		l3rd.hide()
		p3rdon.hide()
		p3rdoff.hide()
		l3rdV.hide()
		l3rdA.hide()

		l4th.hide()
		p4thon.hide()
		p4thoff.hide()
		l4thV.hide()
		l4thA.hide()

	def showpage_two_logic():
		if (bnextpagep == 0):
			ProgramLogic.showpage_two_1()

		elif (bnextpagep == 1):
			ProgramLogic.showpage_two_2()

		elif (bnextpagep == 2):
			ProgramLogic.showpage_two_3()

	def showpage_two_1():				#	Functie die eerste deel van pagina twee toont
		l2.show()
		bseat.show()
		lseattitle.show()
		pwit.show()
		pwit2.show()
		if (bseatp == 0):
			psdeac.show()

		else:
			psactivated.show()
		lseatoff.show()
		lseaton.show()

		bbrake.show()
		lbraketitle.show()
		pwit3.show()
		pwit4.show()
		if (brakep == 0):
			pbdeac.show()
		else:
			pbactivated.show()
		lbrakeoff.show()
		lbrakeon.show()

		bhorn.show()
		lhorntitle.show()
		pwit5.show()
		pwit6.show()
		if (hornp == 0):
			phdeac.show()
		else:
			phactivated.show()
		lhornoff.show()
		lhornon.show()

		bnextpage.show()


	def showpage_two_2 () :			# Functie tweede deel van pagina twee toont

		l2.show()
		bseatswitch.show()
		lseatswitchtitle.show()
		lseatswitchoff.show()
		lseatswitchon.show()
		pwit7.show()
		pwit8.show()
		if (seatswitchp == 0):
			pswdeac.show()
		else:
			pswactivated.show()

		bforward.show()
		lforwardtitle.show()
		lstatus.show()
		lstatusc.show()
		bneutral.show()
		breverse.show()

		bnextpage.show()
		bprevious.show()

	def showpage_two_3():			#	Functie om derde deel van pagina twee te tonen

		l2.show()

		bparkingbrake.show()
		lparkingtitle.show()
		lparkingoff.show()
		lparkingon.show()
		if (parkingbrakep == 0):
			ppadeac.show()
		else:
			ppaactivated.show()
		pwit9.show()
		pwit10.show()

		bfluid.show()
		lfluidtitle.show()
		lfluidoff.show()
		lfluidon.show()
		if (fluidp == 0):
			pfldeac.show()
		else:
			pflactivated.show()
		pwit11.show()
		pwit12.show()

		bprevious.show()

	def hidepage_two_2():
		bseatswitch.hide()
		lseatswitchtitle.hide()
		lseatswitchoff.hide()
		lseatswitchon.hide()
		pwit7.hide()
		pwit8.hide()
		if (seatswitchp == 0):
			pswdeac.hide()
		else:

			pswactivated.hide()

		bforward.hide()
		lforwardtitle.hide()
		lstatus.hide()
		lstatusc.hide()
		bneutral.hide()
		breverse.hide()



	def hidepage_two_3():
		bparkingbrake.hide()
		lparkingtitle.hide()
		lparkingoff.hide()
		lparkingon.hide()
		if (parkingbrakep == 0):
			ppadeac.hide()
		else:
			ppaactivated.hide()
		pwit9.hide()
		pwit10.hide()

		bfluid.hide()
		lfluidtitle.hide()
		lfluidoff.hide()
		lfluidon.hide()
		if (fluidp == 0):
			pfldeac.hide()
		else:
			pflactivated.hide()
		pwit11.hide()
		pwit12.hide()

	def showpage_three():
		l3.show()
		lTireA.show()
		slider1.show()
		lTireV.show()
		pwheel.show()

		loilp.show()
		slider2.show()
		loilV.show()
		poil.show()

		ltiltingp.show()
		slider3.show()
		ltiltV.show()
		ptilt.show()


	def showpage_four():
		l4.show()
		bupdate.show()
		bupdatepi.show()
		pdiagnostic.show()
		ldiag.show()
		lstage1.show()
		lstage2.show()
		lstage3.show()
		lconclusion.show()
		lconc1.show()
		lconc2.show()



### Functies om knoppen actief of niet te maken ###

	def bseatpressed():
		global n
		n = 1
		PiLogic.piseatbelt()

	def bbrakepressed():
		global n
		n = 2
		PiLogic.pibrake()

	def bhornpressed():
		global n
		n = 3
		PiLogic.pihorn()

	def bseatswitchpressed():
		global n
		n = 4
		PiLogic.piseat()


	def bforwardpressed():
		global n
		n = 5
		PiLogic.piforwardon()

	def bneutralpressed():
		global n
		n = 6
		PiLogic.piforwardoff()
		PiLogic.pireverseoff()

	def breversepressed():
		global n
		n = 7
		PiLogic.pireverseon()

	def bparkingpressed():
		global n
		n = 8
		PiLogic.piparking()

	def bfluidpressed():
		global n
		n = 9
		PiLogic.pifluid()

	def bnexthomepagepressed():
		global homepagen
		homepagen = homepagen + 1
		ProgramLogic.showpage_one_2()
		bpreviousehome.show()

	def bpreviousehomepressed():
		global homepagen
		homepagen = homepagen - 1
		ProgramLogic.hidepage_one_2()
		bpreviousehome.hide()

	def bnextpagepressed():
		global bnextpagep
		bnextpagep = bnextpagep + 1

		if (bnextpagep == 0):
			ProgramLogic.hidepage_two_2()
			ProgramLogic.showpage_two_1()

		if (bnextpagep == 1):
			ProgramLogic.showpage_two_2()
			bprevious.show()

		if (bnextpagep == 2):
			ProgramLogic.hidepage_two_2()
			ProgramLogic.showpage_two_3()
			bprevious.show()
			bnextpage.hide()



	def bpreviouspressed():
		global bnextpagep
		bnextpagep = bnextpagep - 1
		#print (bnextpagep)


		if (bnextpagep == 0):
			ProgramLogic.hidepage_two_2()
			ProgramLogic.showpage_two_1()
			bprevious.hide()

		if (bnextpagep == 1):
			ProgramLogic.showpage_two_2()
			ProgramLogic.hidepage_two_3()
			bprevious.show()
			bnextpage.show()

	def pageonepressed():
		global p1pressed


		if (p1pressed == 0):
			p1pressed = 1

		else:
			p1pressed = 0




	def buttonstatus():
		if (n == 1):

			global bseatp

			if (bseatp == 0):
				bseat.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				psactivated.show()
				psdeac.hide()
				bseatp = 1

			else:
				bseat.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				psactivated.hide()
				psdeac.show()
				bseatp = 0

		if (n == 2):

			global brakep

			if (brakep == 0):
				bbrake.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				pbactivated.show()
				pbdeac.hide()
				brakep = 1

			else:
				bbrake.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				pbactivated.hide()
				pbdeac.show()
				brakep = 0

		if (n == 3):

			global hornp

			if (hornp == 0):
				bhorn.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				phactivated.show()
				phdeac.hide()
				hornp = 1

			else:
				bhorn.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				phactivated.hide()
				phdeac.show()
				hornp = 0

		if (n == 4):

			global seatswitchp

			if (seatswitchp == 0):
				bseatswitch.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				pswactivated.show()
				pswdeac.hide()
				seatswitchp = 1

			else:
				bseatswitch.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				pswactivated.hide()
				pswdeac.show()
				seatswitchp = 0

		if (n == 5):

			global forwardp
			global neutralp
			global reversep

			if (forwardp == 0):
				bforward.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				forwardp = 1
				bneutral.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				neutralp = 0
				breverse.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				reversep = 0
				lstatusc.resize(500, 15)
				lstatusc.setText(" Forward")

			else:
				bforward.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				forwardp = 0
				bneutral.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				neutralp = 1
				lstatusc.setText(" Neutral")

		if (n == 6):

			if (neutralp == 0):
				bneutral.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				neutralp = 1
				breverse.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				reversep = 0
				bforward.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				forwardp = 0
				lstatusc.setText(" Neutral")


		if (n == 7):

			if (reversep == 0):
				breverse.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				reversep = 1
				bneutral.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				neutralp = 0
				bforward.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				forwardp = 0
				lstatusc.resize(500, 15)
				lstatusc.setText(" Reverse")

			else:
				breverse.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				reversep = 0
				bneutral.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				neutralp = 1
				lstatusc.setText(" Neutral")

		if (n == 8):

			global parkingbrakep

			if (parkingbrakep == 0):
				bparkingbrake.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				ppaactivated.show()
				ppadeac.hide()
				parkingbrakep = 1

			else:
				bparkingbrake.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				ppaactivated.hide()
				ppadeac.show()
				parkingbrakep = 0


		if (n == 9):

			global fluidp

			if (fluidp == 0):
				bfluid.setStyleSheet("QPushButton {font: bold 10px; background-color: Lime; border-radius: 4px; border: 4px solid black}")
				pflactivated.show()
				pfldeac.hide()
				fluidp = 1

			else:
				bfluid.setStyleSheet("QPushButton {font: bold 10px; background-color: White; border-radius: 4px; border: 4px solid black}")
				pflactivated.hide()
				pfldeac.show()
				fluidp = 0

	def clear_page_two():
		bseat.hide()
		lseattitle.hide()
		pwit.hide()
		pwit2.hide()
		psdeac.hide()
		psactivated.hide()
		lseatoff.hide()
		lseaton.hide()

		bbrake.hide()
		lbraketitle.hide()
		pwit3.hide()
		pwit4.hide()
		pbdeac.hide()
		pbactivated.hide()
		lbrakeoff.hide()
		lbrakeon.hide()

		bhorn.hide()
		lhorntitle.hide()
		pwit5.hide()
		pwit6.hide()
		phdeac.hide()
		phactivated.hide()
		lhornoff.hide()
		lhornon.hide()

	def slider1change():
		slider1changen = slider1.value()
		lTireV.setText(str(slider1changen) + " Ω")
		lTireV.resize(500, 15)

	def slider2change():
		slider2changen = slider2.value()
		loilV.setText(str(slider2changen) + " Ω")
		loilV.resize(500, 15)

	def slider3change():
		slider3changen = slider3.value()
		ltiltV.setText(str(slider3changen) + " Ω")
		ltiltV.resize(500,15)



	def update():

		global conclusiony
		global progupdaten


		if (progupdaten == 0):
			lstage1.setText("Updating...")
			lstage2.setText("Downloading latest program version:..............")
			lstage2.hide()
			lstage2.show()
			lstage1.hide()
			lstage1.show()
			update.programupdate()
			time.sleep(0.5)
			lstage2.setText("Downloading latest program version:.[DONE]")
			progupdaten = 1

			if (conclusiony == 0):
				lconc1.setText("GUI program update [OK]")
				conclusiony = 1

			else:
				lconc2.setText("GUI program update [OK]")
				conclusiony = 2

			lconc1.hide()
			lconc1.show()
			lconc2.hide()
			lconc2.show()

		else:
			 QMessageBox.about(w, "Warning", "Programma is al updated!")




	def updatepi():

		global conclusiony
		global piupdaten

		if (piupdaten == 0):
			piupdaten = 1
			lstage1.setText("Updating...")
			lstage2.setText("Checking updates for pi:.................")
			lstage2.hide()
			lstage2.show()
			lstage1.hide()
			lstage1.show()
			piupdate = subprocess.call(["sudo", "apt-get" , "update"])
			if (piupdate == 0):
				lstage2.setText("Checking updates for pi:.............[DONE]")
				if (conclusiony == 0):
					lconc1.setText("Raspberry pi update [OK]")
					conclusiony = 1

				else:
					lconc2.setText("Raspberry pi update [OK]")
					conclusiony = 2

				lconc1.hide()
				lconc1.show()
				lconc2.hide()
				lconc2.show()

			else:
				lstage2.setText("Checking updates for pi:.............[FAILED]")
				if (conclusiony == 0):
					lconc1.setText("Raspberry pi update [FAILED]")
					conclusiony = 1

				else:
					lconc2.setText("Raspberry pi update [FAILED]")
					conclusiony = 2

			lstage2.hide()
			lstage2.show()
		else:
			QMessageBox.about(w, "Warning", "Raspberry pi is al updated!")












class Window():

	def __init__(self):								# Setup bij het opstarten

		app = QtWidgets.QApplication(sys.argv)

		global w
		w = QtWidgets.QWidget()
		w.setGeometry(0,0,800,480)								# Grote scherm
		w.setWindowTitle("Nissan 1Q2")							# Window tite

		pmain = QtWidgets.QLabel(w)							# background
		pmain.setPixmap(QtGui.QPixmap("pictures/b.png"))
		pmain.move(0,0)

		ptvh = QtWidgets.QLabel(w)							# Tvh logo
		ptvh.setPixmap(QtGui.QPixmap("pictures/tvh.png"))
		ptvh.move(30,5)

		global fontl											# Font van labels
		fontl = "font: bold 25px;"



		Window.home_page(self)								# Verwijzen naar body functie

		def xchange():											# Functie die variable x laat updaten

			global gloeilampohm

			global c1V
			global c1A
			global psV
			global psA
			global liftupV
			global liftupA
			global liftdownV
			global liftupA
			global tiltupV
			global tiltupA
			global tiltdownV
			global tiltdownA
			global V3rdV
			global A3rdA
			global V4thV
			global A4thA


			### C1 ###
			c1V = c1V + 1
			lc1V.setText(str(c1V) + "V")
			lc1V.resize(500, 30)
			if (c1V < 10):
				lc1V.move(355,140)
			else:
				lc1V.move(345,140)

			c1A = c1V/gloeilampohm
			c1A = "%.3f" % c1A
			lc1A.setText(str(c1A) + "A")
			lc1A.resize(500, 30)

			if (p1pressed == 1 and homepagen == 0):
				if (c1V > 0):
					pc1on.show()
					pc1off.hide()

				else:
					pc1off.show()
					pc1on.hide()
			else:
				pc1off.hide()
				pc1on.hide()

			### Ps/c ###
			psV = psV + 1
			lpsV.setText(str(psV) + "V")
			lpsV.resize(500, 30)
			if (psV < 10):
				lpsV.move(355,340)
			else:
				lpsV.move(345,340)

			psA = psV/gloeilampohm
			psA = "%.3f" % psA
			lpsA.setText(str(psA) + "A")
			lpsA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 0):
				if (psV > 0):
					ppson.show()
					ppsoff.hide()

				else:
					ppsoff.show()
					ppson.hide()
			else:
				pc1off.hide()
				pc1on.hide()


			### Lift up ###
			liftupV = liftupV + 1
			lliftupV.setText(str(liftupV) + "V")
			lliftupV.resize(500, 30)
			if (liftupV < 10):
				lliftupV.move(605,140)
			else:
				lliftupV.move(595,140)

			liftupA = liftupV/gloeilampohm
			liftupA = "%.3f" % liftupA
			lliftupA.setText(str(liftupA) + "A")
			lliftupA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 0):
				if (liftupV > 0):
					pliftupon.show()
					pliftupoff.hide()

				else:
					pliftupoff.show()
					pliftupon.hide()
			else:
				pliftupoff.hide()
				pliftupon.hide()

			### Lift down ###
			liftdownV = liftdownV + 1
			lliftdownV.setText(str(liftdownV) + "V")
			lliftdownV.resize(500, 30)
			if (liftdownV < 10):
				lliftdownV.move(605,340)
			else:
				lliftdownV.move(595,340)

			liftdownA = liftdownV/gloeilampohm
			liftdownA = "%.3f" % liftdownA
			lliftdownA.setText(str(liftdownA) + "A")
			lliftdownA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 0):
				if (liftdownV > 0):
					pliftdownon.show()
					pliftdownoff.hide()

				else:
					pliftdownoff.show()
					pliftdownon.hide()
			else:
				pliftupoff.hide()
				pliftupon.hide()

			### Tilt up ###
			tiltupV = tiltupV + 1
			ltiltupV.setText(str(tiltupV) + "V")
			ltiltupV.resize(500, 30)
			if (tiltupV < 10):
				ltiltupV.move(505,240)
			else:
				ltiltupV.move(495,240)

			tiltupA = tiltupV/gloeilampohm
			tiltupA = "%.3f" % tiltupA
			ltiltupA.setText(str(tiltupA) + "A")
			ltiltupA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 0):
				if (tiltupV > 0):
					ptiltupon.show()
					ptiltupoff.hide()

				else:
					ptiltupoff.show()
					ptiltupon.hide()
			else:
				ptiltupoff.hide()
				ptiltupon.hide()

			### Tilt down ###
			tiltdownV = tiltdownV + 1
			ltiltdownV.setText(str(tiltdownV) + "V")
			ltiltdownV.resize(500, 30)
			if (tiltdownV < 10):
				ltiltdownV.move(705,240)
			else:
				ltiltdownV.move(695,240)

			tiltdownA = tiltdownV/gloeilampohm
			tiltdownA = "%.3f" % tiltdownA
			ltiltdownA.setText(str(tiltdownA) + "A")
			ltiltdownA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 0):
				if (tiltdownV > 0):
					ptiltdownon.show()
					ptiltdownoff.hide()

				else:
					ptiltdownoff.show()
					ptiltdownon.hide()
			else:
				ptiltdownoff.hide()
				ptiltdownon.hide()

		### 3rd ###

			V3rdV = V3rdV + 1
			l3rdV.setText(str(V3rdV) + "V")
			l3rdV.resize(500, 30)
			if (V3rdV < 10):
				l3rdV.move(385,140)
			else:
				l3rdV.move(375,140)

			A3rdA = V3rdV/gloeilampohm
			A3rdA = "%.3f" % A3rdA
			l3rdA.setText(str(A3rdA) + "A")
			l3rdA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 1):
				if (V3rdV > 0):
					p3rdon.show()
					p3rdoff.hide()

				else:
					p3rdoff.show()
					p3rdon.hide()
			else:
				p3rdoff.hide()
				p3rdon.hide()


			V4thV = V4thV + 1
			l4thV.setText(str(V4thV) + "V")
			l4thV.resize(500, 30)
			if (V4thV < 10):
				l4thV.move(355,340)
			else:
				l4thV.move(345,340)

			A4thA = V4thV/gloeilampohm
			A4thA = "%.3f" % A4thA
			l4thA.setText(str(A4thA) + "A")
			l4thA.resize(500, 30)
			if (p1pressed == 1 and homepagen == 1):
				if (V4thV > 0):
					p4thon.show()
					p4thoff.hide()

				else:
					p4thoff.show()
					p4thon.hide()
			else:
				p4thoff.hide()
				p4thon.hide()

		timer= QtCore.QTimer()									# Om de 0,1 seconden laat het programma de functie xchange lopen
		timer.timeout.connect(xchange)
		timer.start(1000)

		sys.exit(app.exec_())									# Applicatie sluiten



	def home_page(self):

		global lhome											#lhome overal oproepbaar maken

		lhome = QtWidgets.QLabel(w)							# Home tekst
		lhome.setText("Home")
		lhome.move(450,20)
		lhome.setStyleSheet("font: bold 25px")
		lhome.show()

		Window.page_one(self)									# Verwijzen naar tweede pagina


	def page_one(self):
		global l1

		global lc1
		global lc1V
		global lc1A
		global pc1on
		global pc1off

		global lps
		global lpsV
		global lpsA
		global ppson
		global ppsoff

		global lliftup
		global lliftupV
		global lliftupA
		global pliftupon
		global pliftupoff

		global lliftdown
		global lliftdownV
		global lliftdownA
		global pliftdownon
		global pliftdownoff

		global ltiltup
		global ltiltupV
		global ltiltupA
		global ptiltupon
		global ptiltupoff

		global ltiltdown
		global ltiltdownV
		global ltiltdownA
		global ptiltdownon
		global ptiltdownoff

		global l3rd
		global l3rdV
		global l3rdA
		global p3rdon
		global p3rdoff

		global l4th
		global l4thV
		global l4thA
		global p4thon
		global p4thoff

		global bnexthomepage
		global bpreviousehome

		l1 = QtWidgets.QLabel(w)							# Tekst bij knop 1
		l1.setText("Metingen")
		l1.move(440,20)
		l1.setStyleSheet("font: bold 25px")
		l1.hide()

		###		C1		###
		lc1 = QtWidgets.QLabel(w)
		lc1.move(270,105)
		lc1.setText("C1")
		lc1.setStyleSheet("font: bold 15px; text-decoration: underline;")
		lc1.hide()

		pc1on = QtWidgets.QLabel(w)
		pc1on.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		pc1on.move(230,115)
		pc1on.hide()

		pc1off = QtWidgets.QLabel(w)
		pc1off.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		pc1off.move(230,115)
		pc1off.hide()

		lc1V = QtWidgets.QLabel(w)
		lc1V.move(355,140)
		lc1V.setStyleSheet("font: Arial; font-size: 18px;")
		lc1V.hide()

		lc1A = QtWidgets.QLabel(w)
		lc1A.move(320,155)
		lc1A.setStyleSheet("font: Arial; font-size: 18px;")
		lc1A.hide()

		###		Ps/c		###
		lps = QtWidgets.QLabel(w)
		lps.move(260,305)
		lps.setText("Ps/c")
		lps.setStyleSheet("font: bold 15px;  text-decoration: underline;")
		lps.hide()

		ppson = QtWidgets.QLabel(w)
		ppson.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		ppson.move(230,315)
		ppson.hide()

		ppsoff = QtWidgets.QLabel(w)
		ppsoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		ppsoff.move(230,315)
		ppsoff.hide()

		lpsV = QtWidgets.QLabel(w)
		lpsV.move(355,340)
		lpsV.setStyleSheet("font: Arial; font-size: 18px;")
		lpsV.hide()

		lpsA = QtWidgets.QLabel(w)
		lpsA.move(320,355)
		lpsA.setStyleSheet("font: Arial; font-size: 18px;")
		lpsA.hide()

		###		Lift up	###
		lliftup = QtWidgets.QLabel(w)
		lliftup.move(505,105)
		lliftup.setText("Lift up")
		lliftup.setStyleSheet("font: bold 15px;  text-decoration: underline;")
		lliftup.hide()

		pliftupon = QtWidgets.QLabel(w)
		pliftupon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		pliftupon.move(480,115)
		pliftupon.hide()

		pliftupoff = QtWidgets.QLabel(w)
		pliftupoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		pliftupoff.move(480,115)
		pliftupoff.hide()

		lliftupV = QtWidgets.QLabel(w)
		lliftupV.move(605,140)
		lliftupV.setStyleSheet("font: Arial; font-size: 18px;")
		lliftupV.hide()

		lliftupA = QtWidgets.QLabel(w)
		lliftupA.move(570,155)
		lliftupA.setStyleSheet("font: Arial; font-size: 18px;")
		lliftupA.hide()


		###		Lift down	###
		lliftdown = QtWidgets.QLabel(w)
		lliftdown.move(502,305)
		lliftdown.setText("Lift down")
		lliftdown.setStyleSheet("font: bold 15px;  text-decoration: underline;")
		lliftdown.hide()

		pliftdownon = QtWidgets.QLabel(w)
		pliftdownon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		pliftdownon.move(480,315)
		pliftdownon.hide()

		pliftdownoff = QtWidgets.QLabel(w)
		pliftdownoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		pliftdownoff.move(480,315)
		pliftdownoff.hide()

		lliftdownV = QtWidgets.QLabel(w)
		lliftdownV.move(605,340)
		lliftdownV.setStyleSheet("font: Arial; font-size: 18px;")
		lliftdownV.hide()

		lliftdownA = QtWidgets.QLabel(w)
		lliftdownA.move(570,355)
		lliftdownA.setStyleSheet("font: Arial; font-size: 18px;")
		lliftdownA.hide()

			###		Tilt up	###
		ltiltup = QtWidgets.QLabel(w)
		ltiltup.move(402,205)
		ltiltup.setText("Tilt up")
		ltiltup.setStyleSheet("font: bold 15px;  text-decoration: underline;")
		ltiltup.hide()

		ptiltupon = QtWidgets.QLabel(w)
		ptiltupon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		ptiltupon.move(380,215)
		ptiltupon.hide()

		ptiltupoff = QtWidgets.QLabel(w)
		ptiltupoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		ptiltupoff.move(380,215)
		ptiltupoff.hide()

		ltiltupV = QtWidgets.QLabel(w)
		ltiltupV.move(505,240)
		ltiltupV.setStyleSheet("font: Arial; font-size: 18px;")
		ltiltupV.hide()

		ltiltupA = QtWidgets.QLabel(w)
		ltiltupA.move(470,255)
		ltiltupA.setStyleSheet("font: Arial; font-size: 18px;")
		ltiltupA.hide()

			###		Tilt down	###
		ltiltdown = QtWidgets.QLabel(w)
		ltiltdown.move(602,205)
		ltiltdown.setText("Tilt down")
		ltiltdown.setStyleSheet("font: bold 15px;  text-decoration: underline;")
		ltiltdown.hide()

		ptiltdownon = QtWidgets.QLabel(w)
		ptiltdownon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		ptiltdownon.move(580,215)
		ptiltdownon.hide()

		ptiltdownoff = QtWidgets.QLabel(w)
		ptiltdownoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		ptiltdownoff.move(580,215)
		ptiltdownoff.hide()

		ltiltdownV = QtWidgets.QLabel(w)
		ltiltdownV.move(705,240)
		ltiltdownV.setStyleSheet("font: Arial; font-size: 18px;")
		ltiltdownV.hide()

		ltiltdownA = QtWidgets.QLabel(w)
		ltiltdownA.move(670,255)
		ltiltdownA.setStyleSheet("font: Arial; font-size: 18px;")
		ltiltdownA.hide()

		###		3rd		###
		l3rd = QtWidgets.QLabel(w)
		l3rd.move(295,105)
		l3rd.setText("3RD")
		l3rd.setStyleSheet("font: bold 15px; text-decoration: underline;")
		l3rd.hide()

		p3rdon = QtWidgets.QLabel(w)
		p3rdon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		p3rdon.move(260,115)
		p3rdon.hide()

		p3rdoff = QtWidgets.QLabel(w)
		p3rdoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		p3rdoff.move(260,115)
		p3rdoff.hide()

		l3rdV = QtWidgets.QLabel(w)
		l3rdV.move(385,140)
		l3rdV.setStyleSheet("font: Arial; font-size: 18px;")
		l3rdV.hide()

		l3rdA = QtWidgets.QLabel(w)
		l3rdA.move(350,155)
		l3rdA.setStyleSheet("font: Arial; font-size: 18px;")
		l3rdA.hide()

		###		4th		###
		l4th = QtWidgets.QLabel(w)
		l4th.move(295,305)
		l4th.setText("4TH")
		l4th.setStyleSheet("font: bold 15px; text-decoration: underline;")
		l4th.hide()

		p4thon = QtWidgets.QLabel(w)
		p4thon.setPixmap(QtGui.QPixmap("pictures/c1on.png"))
		p4thon.move(260,315)
		p4thon.hide()

		p4thoff = QtWidgets.QLabel(w)
		p4thoff.setPixmap(QtGui.QPixmap("pictures/c1off.png"))
		p4thoff.move(260,315)
		p4thoff.hide()

		l4thV = QtWidgets.QLabel(w)
		l4thV.move(385,340)
		l4thV.setStyleSheet("font: Arial; font-size: 18px;")
		l4thV.hide()

		l4thA = QtWidgets.QLabel(w)
		l4thA.move(350,355)
		l4thA.setStyleSheet("font: Arial; font-size: 18px;")
		l4thA.hide()

		###		next page button 	###
		next = QtGui.QIcon("pictures/next.png");
		bnexthomepage = QtWidgets.QPushButton(w)
		bnexthomepage.clicked.connect(ProgramLogic.hidepage_one_1)
		bnexthomepage.clicked.connect(ProgramLogic.bnexthomepagepressed)
		bnexthomepage.resize(60,60)
		bnexthomepage.move(720,235)
		bnexthomepage.setIcon(next)
		bnexthomepage.setIconSize(QtCore.QSize(60,60))
		bnexthomepage.setStyleSheet("border: none;")
		bnexthomepage.hide()

		###		Previous button		###
		previous = QtGui.QIcon("pictures/previous.png");
		bpreviousehome = QtWidgets.QPushButton(w)
		bpreviousehome.clicked.connect(ProgramLogic.showpage_one_1)
		bpreviousehome.clicked.connect(ProgramLogic.bpreviousehomepressed)
		bpreviousehome.resize(60,60)
		bpreviousehome.move(210,235)
		bpreviousehome.setIcon(previous)
		bpreviousehome.setIconSize(QtCore.QSize(60,60))
		bpreviousehome.setStyleSheet("border: none;")
		bpreviousehome.hide()

		Window.page_two(self)


	def page_two(self):

		global l2
		global bseat
		global lseattitle
		global lseatoff
		global lseaton
		global pwit
		global psdeac
		global pwit2
		global psactivated

		global bbrake
		global lbraketitle
		global lbrakeoff
		global lbrakeon
		global pwit3
		global pbdeac
		global pwit4
		global pbactivated

		global bhorn
		global lhorntitle
		global lhornoff
		global lhornon
		global pwit5
		global phdeac
		global pwit6
		global phactivated

		global bseatswitch
		global lseatswitchtitle
		global lseatswitchoff
		global lseatswitchon
		global pwit7
		global pswdeac
		global pwit8
		global pswactivated

		global bforward
		global lforwardtitle
		global lstatusc
		global lstatus
		global bneutral
		global breverse

		global bparkingbrake
		global lparkingtitle
		global lparkingoff
		global lparkingon
		global pwit9
		global ppadeac
		global pwit10
		global ppaactivated


		global bfluid
		global lfluidtitle
		global lfluidoff
		global lfluidon
		global pwit11
		global pwit12
		global pfldeac
		global pflactivated

		global bnextpage
		global bprevious


		l2 = QtWidgets.QLabel(w)							# Titel pagina 2
		l2.setText("Schakelaars")
		l2.move(420,20)
		l2.setStyleSheet(fontl)
		l2.hide()


		###		 Seatbelt switch	###
		seatbelt= QtGui.QIcon("pictures/seatbelt.png");
		bseat = QtWidgets.QPushButton(w)
		bseat.clicked.connect(ProgramLogic.bseatpressed)
		bseat.clicked.connect(ProgramLogic.buttonstatus)
		bseat.resize(70,70)
		bseat.move(280,102)
		bseat.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bseat.setIcon(seatbelt)
		bseat.setIconSize(QtCore.QSize(70,70))
		bseat.hide()

		lseattitle = QtWidgets.QLabel(w)
		lseattitle.setText("Seatbelt switch")
		lseattitle.move(390,95)
		lseattitle.setStyleSheet("font: bold; font-size: 18px;")
		lseattitle.hide()

		pwit = QtWidgets.QLabel(w)
		pwit.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit.move(390,125)
		pwit.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit.hide()

		psdeac = QtWidgets.QLabel(w)
		psdeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		psdeac.move(390,125)
		psdeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		psdeac.hide()

		pwit2 = QtWidgets.QLabel(w)
		pwit2.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit2.move(390,150)
		pwit2.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit2.hide()

		psactivated = QtWidgets.QLabel(w)
		psactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		psactivated.move(390,150)
		psactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		psactivated.hide()

		lseatoff = QtWidgets.QLabel(w)
		lseatoff.setText("Off")
		lseatoff.move(425,124)
		lseatoff.setStyleSheet("font: Arial; font-size: 15px;")
		lseatoff.hide()

		lseaton = QtWidgets.QLabel(w)
		lseaton.setText("On")
		lseaton.move(425,150)
		lseaton.setStyleSheet("font: Arial; font-size: 15px;")
		lseaton.hide()


		###		Brakeswitch 	###
		brake = QtGui.QIcon("pictures/brake.png");
		bbrake = QtWidgets.QPushButton(w)
		bbrake.clicked.connect(ProgramLogic.bbrakepressed)
		bbrake.clicked.connect(ProgramLogic.buttonstatus)
		bbrake.resize(70,70)
		bbrake.move(280,230)
		bbrake.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bbrake.setIcon(brake)
		bbrake.setIconSize(QtCore.QSize(60,60))
		bbrake.hide()

		lbraketitle = QtWidgets.QLabel(w)
		lbraketitle.setText("Brake Switch")
		lbraketitle.move(390,225)
		lbraketitle.setStyleSheet("font: bold; font-size: 18px;")
		lbraketitle.hide()

		pwit3 = QtWidgets.QLabel(w)
		pwit3.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit3.move(390,255)
		pwit3.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit3.hide()

		pbdeac = QtWidgets.QLabel(w)
		pbdeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		pbdeac.move(390,255)
		pbdeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pbdeac.hide()

		pwit4 = QtWidgets.QLabel(w)
		pwit4.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit4.move(390,280)
		pwit4.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit4.hide()

		pbactivated = QtWidgets.QLabel(w)
		pbactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		pbactivated.move(390,280)
		pbactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pbactivated.hide()

		lbrakeoff = QtWidgets.QLabel(w)
		lbrakeoff.setText("Off")
		lbrakeoff.move(425,255)
		lbrakeoff.setStyleSheet("font: Arial; font-size: 15px;")
		lbrakeoff.hide()

		lbrakeon = QtWidgets.QLabel(w)
		lbrakeon.setText("On")
		lbrakeon.move(425,280)
		lbrakeon.setStyleSheet("font: Arial; font-size: 15px;")
		lbrakeon.hide()


		###		Horn Switch 	###
		horn = QtGui.QIcon("pictures/horn.png");
		bhorn = QtWidgets.QPushButton(w)
		bhorn.clicked.connect(ProgramLogic.bhornpressed)
		bhorn.clicked.connect(ProgramLogic.buttonstatus)
		bhorn.resize(70,70)
		bhorn.move(280,350)
		bhorn.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bhorn.setIcon(horn)
		bhorn.setIconSize(QtCore.QSize(60,60))
		bhorn.hide()

		lhorntitle = QtWidgets.QLabel(w)
		lhorntitle.setText("Horn Switch")
		lhorntitle.move(390,345)
		lhorntitle.setStyleSheet("font: bold; font-size: 18px;")
		lhorntitle.hide()

		pwit5 = QtWidgets.QLabel(w)
		pwit5.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit5.move(390,375)
		pwit5.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit5.hide()

		phdeac = QtWidgets.QLabel(w)
		phdeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		phdeac.move(390,375)
		phdeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		phdeac.hide()

		pwit6 = QtWidgets.QLabel(w)
		pwit6.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit6.move(390,400)
		pwit6.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit6.hide()

		phactivated = QtWidgets.QLabel(w)
		phactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		phactivated.move(390,400)
		phactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		phactivated.hide()

		lhornoff = QtWidgets.QLabel(w)
		lhornoff.setText("Off")
		lhornoff.move(425,375)
		lhornoff.setStyleSheet("font: Arial; font-size: 15px;")
		lhornoff.hide()

		lhornon = QtWidgets.QLabel(w)
		lhornon.setText("On")
		lhornon.move(425,400)
		lhornon.setStyleSheet("font: Arial; font-size: 15px;")
		lhornon.hide()


		###		Seat Switch 	###
		seatswitch = QtGui.QIcon("pictures/seatswitch.png");
		bseatswitch = QtWidgets.QPushButton(w)
		bseatswitch.clicked.connect(ProgramLogic.bseatswitchpressed)
		bseatswitch.clicked.connect(ProgramLogic.buttonstatus)
		bseatswitch.resize(70,70)
		bseatswitch.move(280,102)
		bseatswitch.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bseatswitch.setIcon(seatswitch)
		bseatswitch.setIconSize(QtCore.QSize(70,70))
		bseatswitch.hide()

		lseatswitchtitle = QtWidgets.QLabel(w)
		lseatswitchtitle.setText("Seat Switch")
		lseatswitchtitle.move(390,95)
		lseatswitchtitle.setStyleSheet("font: bold; font-size: 18px;")
		lseatswitchtitle.hide()

		pwit7 = QtWidgets.QLabel(w)
		pwit7.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit7.move(390,125)
		pwit7.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit7.hide()

		pswdeac = QtWidgets.QLabel(w)
		pswdeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		pswdeac.move(390,125)
		pswdeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pswdeac.hide()

		pwit8 = QtWidgets.QLabel(w)
		pwit8.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit8.move(390,150)
		pwit8.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit8.hide()

		pswactivated = QtWidgets.QLabel(w)
		pswactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		pswactivated.move(390,150)
		pswactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pswactivated.hide()

		lseatswitchoff = QtWidgets.QLabel(w)
		lseatswitchoff.setText("Off")
		lseatswitchoff.move(425,124)
		lseatswitchoff.setStyleSheet("font: Arial; font-size: 15px;")
		lseatswitchoff.hide()

		lseatswitchon = QtWidgets.QLabel(w)
		lseatswitchon.setText("On")
		lseatswitchon.move(425,150)
		lseatswitchon.setStyleSheet("font: Arial; font-size: 15px;")
		lseatswitchon.hide()

		###		F/N/R Switch 	###
		forward = QtGui.QIcon("pictures/forward.png");
		neutral = QtGui.QIcon("pictures/neutral.png");
		reverse = QtGui.QIcon("pictures/reverse.png");
		bforward = QtWidgets.QPushButton(w)
		bforward.clicked.connect(ProgramLogic.bforwardpressed)
		bforward.clicked.connect(ProgramLogic.buttonstatus)
		bforward.resize(70,70)
		bforward.move(280,230)
		bforward.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bforward.setIcon(forward)
		bforward.setIconSize(QtCore.QSize(70,70))
		bforward.hide()

		lforwardtitle = QtWidgets.QLabel(w)
		lforwardtitle.setText("Forward/Reverse Switch")
		lforwardtitle.move(390,225)
		lforwardtitle.setStyleSheet("font: bold; font-size: 18px;")
		lforwardtitle.hide()

		lstatus = QtWidgets.QLabel(w)
		lstatus.setText("Status:")
		lstatus.move(390,330)
		lstatus.setStyleSheet("font: bold; font-size: 14px;")
		lstatus.hide()

		lstatusc = QtWidgets.QLabel(w)
		lstatusc.setText(" Neutral")
		lstatusc.move(440,330)
		lstatusc.setStyleSheet("font: bold; font-size: 14px; color: Green")
		lstatusc.hide()

		bneutral = QtWidgets.QPushButton(w)
		bneutral.clicked.connect(ProgramLogic.bneutralpressed)
		bneutral.clicked.connect(ProgramLogic.buttonstatus)
		bneutral.resize(70,70)
		bneutral.move(280,310)
		bneutral.setStyleSheet("QPushButton {background-color: Lime; border-radius: 4px; border: 4px solid black}")
		bneutral.setIcon(neutral)
		bneutral.setIconSize(QtCore.QSize(70,70))
		bneutral.hide()

		breverse = QtWidgets.QPushButton(w)
		breverse.clicked.connect(ProgramLogic.breversepressed)
		breverse.clicked.connect(ProgramLogic.buttonstatus)
		breverse.resize(70,70)
		breverse.move(280,390)
		breverse.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		breverse.setIcon(reverse)
		breverse.setIconSize(QtCore.QSize(70,70))
		breverse.hide()

		### Parking brake switch ###
		parkingbrake= QtGui.QIcon("pictures/parkingbrake.png");
		bparkingbrake = QtWidgets.QPushButton(w)
		bparkingbrake.clicked.connect(ProgramLogic.bparkingpressed)
		bparkingbrake.clicked.connect(ProgramLogic.buttonstatus)
		bparkingbrake.resize(70,70)
		bparkingbrake.move(280,102)
		bparkingbrake.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bparkingbrake.setIcon(parkingbrake)
		bparkingbrake.setIconSize(QtCore.QSize(60,60))
		bparkingbrake.hide()

		lparkingtitle = QtWidgets.QLabel(w)
		lparkingtitle.setText("Parking brake")
		lparkingtitle.move(390,95)
		lparkingtitle.setStyleSheet("font: bold; font-size: 18px;")
		lparkingtitle.hide()

		pwit9 = QtWidgets.QLabel(w)
		pwit9.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit9.move(390,125)
		pwit9.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit9.hide()

		ppadeac = QtWidgets.QLabel(w)
		ppadeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		ppadeac.move(390,125)
		ppadeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		ppadeac.hide()

		pwit10 = QtWidgets.QLabel(w)
		pwit10.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit10.move(390,150)
		pwit10.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit10.hide()

		ppaactivated = QtWidgets.QLabel(w)
		ppaactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		ppaactivated.move(390,150)
		ppaactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		ppaactivated.hide()

		lparkingoff = QtWidgets.QLabel(w)
		lparkingoff.setText("Off")
		lparkingoff.move(425,124)
		lparkingoff.setStyleSheet("font: Arial; font-size: 15px;")
		lparkingoff.hide()

		lparkingon = QtWidgets.QLabel(w)
		lparkingon.setText("On")
		lparkingon.move(425,150)
		lparkingon.setStyleSheet("font: Arial; font-size: 15px;")
		lparkingon.hide()

		###		BrakeFluid switch 	###
		fluid = QtGui.QIcon("pictures/fluid.png");
		bfluid = QtWidgets.QPushButton(w)
		bfluid.clicked.connect(ProgramLogic.bfluidpressed)
		bfluid.clicked.connect(ProgramLogic.buttonstatus)
		bfluid.resize(70,70)
		bfluid.move(280,230)
		bfluid.setStyleSheet("QPushButton {background-color: White; border-radius: 4px; border: 4px solid black}")
		bfluid.setIcon(fluid)
		bfluid.setIconSize(QtCore.QSize(60,60))
		bfluid.hide()

		lfluidtitle = QtWidgets.QLabel(w)
		lfluidtitle.setText("Brake Fluid Switch")
		lfluidtitle.move(390,225)
		lfluidtitle.setStyleSheet("font: bold; font-size: 18px;")
		lfluidtitle.hide()

		pwit11 = QtWidgets.QLabel(w)
		pwit11.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit11.move(390,255)
		pwit11.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit11.hide()

		pfldeac = QtWidgets.QLabel(w)
		pfldeac.setPixmap(QtGui.QPixmap("pictures/redcolor.png"))
		pfldeac.move(390,255)
		pfldeac.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pfldeac.hide()

		pwit12 = QtWidgets.QLabel(w)
		pwit12.setPixmap(QtGui.QPixmap("pictures/whitecolor.png"))
		pwit12.move(390,280)
		pwit12.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pwit12.hide()

		pflactivated = QtWidgets.QLabel(w)
		pflactivated.setPixmap(QtGui.QPixmap("pictures/greencolor.png"))
		pflactivated.move(390,280)
		pflactivated.setStyleSheet("border-radius: 1px; border: 1px solid black")
		pflactivated.hide()

		lfluidoff = QtWidgets.QLabel(w)
		lfluidoff.setText("Off")
		lfluidoff.move(425,255)
		lfluidoff.setStyleSheet("font: Arial; font-size: 15px;")
		lfluidoff.hide()

		lfluidon = QtWidgets.QLabel(w)
		lfluidon.setText("On")
		lfluidon.move(425,280)
		lfluidon.setStyleSheet("font: Arial; font-size: 15px;")
		lfluidon.hide()


		### Next page switch ###
		next = QtGui.QIcon("pictures/next.png");
		bnextpage = QtWidgets.QPushButton(w)
		bnextpage.clicked.connect(ProgramLogic.clear_page_two)
		bnextpage.clicked.connect(ProgramLogic.bnextpagepressed)
		bnextpage.resize(60,60)
		bnextpage.move(720,235)
		bnextpage.setIcon(next)
		bnextpage.setIconSize(QtCore.QSize(60,60))
		bnextpage.setStyleSheet("border: none;")
		bnextpage.hide()

		### Previous page switch ###
		previous = QtGui.QIcon("pictures/previous.png");
		bprevious = QtWidgets.QPushButton(w)
		bprevious.clicked.connect(ProgramLogic.bpreviouspressed)
		bprevious.resize(60,60)
		bprevious.move(210,235)
		bprevious.setIcon(previous)
		bprevious.setIconSize(QtCore.QSize(60,60))
		bprevious.setStyleSheet("border: none;")
		bprevious.hide()


		Window.page_three(self)


	def page_three(self):

		global l3

		global slider1
		global lTireA
		global lTireV
		global pwheel

		global loilp
		global slider2
		global loilV
		global poil

		global ltiltingp
		global slider3
		global ltiltV
		global ptilt



		### 	Tire Angle Sensor    ####
		l3 = QtWidgets.QLabel(w)							# Tekst bij knop 3
		l3.setText("Potentiometers")
		l3.move(415,20)
		l3.setStyleSheet(fontl)
		l3.hide()

		lTireA = QtWidgets.QLabel(w)
		lTireA.setText("Tire Angle")
		lTireA.move(280,100)
		lTireA.setStyleSheet("font: bold; font-size: 18px;")
		lTireA.hide()

		slider1 = QSlider(Qt.Horizontal, w)
		slider1.setMinimum(1800)
		slider1.setMaximum(2600)
		slider1.setValue(2200)
		slider1.valueChanged.connect(ProgramLogic.slider1change)
		slider1.setGeometry(280,130,400,30)
		slider1.hide()

		lTireV = QtWidgets.QLabel(w)
		lTireV.setText("2200 Ω")
		lTireV.move(280,160)
		lTireV.setStyleSheet("font: bold; font-size: 14px;")
		lTireV.hide()

		pwheel = QtWidgets.QLabel(w)
		pwheel.setPixmap(QtGui.QPixmap("pictures/wheel.png"))
		pwheel.move(710,110)
		pwheel.hide()


		### 	Oil Pressure	###
		loilp = QtWidgets.QLabel(w)
		loilp.setText("Oil Pressure")
		loilp.move(280,220)
		loilp.setStyleSheet("font: bold; font-size: 18px;")
		loilp.hide()

		slider2 = QSlider(Qt.Horizontal, w)
		slider2.setMinimum(1800)
		slider2.setMaximum(2600)
		slider2.setValue(2200)
		slider2.valueChanged.connect(ProgramLogic.slider2change)
		slider2.setGeometry(280,250,400,30)
		slider2.hide()

		loilV = QtWidgets.QLabel(w)
		loilV.setText("2200 Ω")
		loilV.move(280,280)
		loilV.setStyleSheet("font: bold; font-size: 14px;")
		loilV.hide()

		poil = QtWidgets.QLabel(w)
		poil.setPixmap(QtGui.QPixmap("pictures/oil.png"))
		poil.move(710,230)
		poil.hide()


		###		Tilt Angle	   ###
		ltiltingp = QtWidgets.QLabel(w)
		ltiltingp.setText("Tilt Angle")
		ltiltingp.move(280,330)
		ltiltingp.setStyleSheet("font: bold; font-size: 18px;")
		ltiltingp.hide()

		slider3 = QSlider(Qt.Horizontal, w)
		slider3.setMinimum(1800)
		slider3.setMaximum(2600)
		slider3.setValue(2200)
		slider3.valueChanged.connect(ProgramLogic.slider3change)
		slider3.setGeometry(280,370,400,30)
		slider3.hide()

		ltiltV = QtWidgets.QLabel(w)
		ltiltV.setText("2200 Ω")
		ltiltV.move(280,400)
		ltiltV.setStyleSheet("font: bold; font-size: 14px;")
		ltiltV.hide()

		ptilt = QtWidgets.QLabel(w)
		ptilt.setPixmap(QtGui.QPixmap("pictures/tilt.png"))
		ptilt.move(710,350)
		ptilt.hide()

		Window.page_four(self)




	def page_four(self):

		global l4
		global bupdate
		global bupdatepi
		global pdiagnostic
		global ldiag
		global lconclusion
		global lconc1
		global lconc2
		global lstage1
		global lstage2
		global lstage3

		l4 = QtWidgets.QLabel(w)							# Tekst bij knop 4
		l4.setText("Functies")
		l4.move(450,20)
		l4.setStyleSheet(fontl)
		l4.hide()

		updateicon = QtGui.QIcon("pictures/update.png");
		bupdate = QtWidgets.QPushButton(w)
		bupdate.clicked.connect(ProgramLogic.update)
		bupdate.resize(60,60)
		bupdate.move(265,110)
		bupdate.setIcon(updateicon)
		bupdate.setIconSize(QtCore.QSize(50,50))
		bupdate.setStyleSheet("QPushButton{  background-color: White;border-radius: 4px;border: 4px solid black;}")
		bupdate.hide()

		updatepiicon = QtGui.QIcon("pictures/rasp.png");
		bupdatepi = QtWidgets.QPushButton(w)
		bupdatepi.clicked.connect(ProgramLogic.updatepi)
		bupdatepi.resize(60,60)
		bupdatepi.move(265,190)
		bupdatepi.setIcon(updatepiicon)
		bupdatepi.setIconSize(QtCore.QSize(50,50))
		bupdatepi.setStyleSheet("QPushButton{  background-color: White;border-radius: 4px;border: 4px solid black;}")
		bupdatepi.hide()

		pdiagnostic = QtWidgets.QLabel(w)
		pdiagnostic.setPixmap(QtGui.QPixmap("pictures/diagnose.png"))
		pdiagnostic.setStyleSheet("border-radius: 1px; border: 1px solid black;")
		pdiagnostic.move(390,100)
		pdiagnostic.hide()

		ldiag = QtWidgets.QLabel(w)
		ldiag.setText("Diagnose:")
		ldiag.move(395,100)
		ldiag.setStyleSheet("font-family: Arial; font: bold;font-size: 15px;")
		ldiag.hide()

		lstage1 = QtWidgets.QLabel(w)
		lstage1.setText("No function selected....")
		lstage1.move(475,101)
		lstage1.setStyleSheet("font-style: italic ;font-family: Arial; font-size: 15px;")
		lstage1.hide()

		lstage2 = QtWidgets.QLabel(w)
		lstage2.move(475,121)
		lstage2.setStyleSheet("font-style: italic ;font-family: Arial; font-size: 15px;")
		lstage2.hide()

		lstage3 = QtWidgets.QLabel(w)
		lstage3.move(475,141)
		lstage3.setStyleSheet("font-style: italic ;font-family: Arial; font-size: 15px;")
		lstage3.hide()

		lconclusion = QtWidgets.QLabel(w)
		lconclusion.setText("Conclusie:")
		lconclusion.move(395,285)
		lconclusion.setStyleSheet("font-family: Arial; font: bold;font-size: 15px;")
		lconclusion.hide()

		lconc1 = QtWidgets.QLabel(w)
		lconc1.move(475,285)
		lconc1.setStyleSheet("font-style: italic ;font-family: Arial; font-size: 15px;")
		lconc1.hide()

		lconc2 = QtWidgets.QLabel(w)
		lconc2.move(475,305)
		lconc2.setStyleSheet("font-style: italic ;font-family: Arial; font-size: 15px;")
		lconc2.hide()

		Window.page_five(self)


	def page_five(self):

		global l5

		l5 = QtWidgets.QLabel(w)							# Tekst bij knop 5
		l5.setText("Knop 5")
		l5.move(450,20)
		l5.setStyleSheet(fontl)
		l5.hide()







		Window.main_buttons(self)


	def main_buttons(self):

		fbutton = ("font: Arial; font-size: 18px; color: black; background-color: #205173; border-radius: 4px; ")


		bhome = QtWidgets.QPushButton(w)						# Home knop
		bhome.clicked.connect(ProgramLogic.clear)
		bhome.clicked.connect(lhome.show)
		bhome.setText("Home")
		bhome.resize(150,35)
		bhome.move(25,70)
		bhome.setStyleSheet(fbutton)

		b1 = QtWidgets.QPushButton(w)						# Knop 1
		b1.clicked.connect(ProgramLogic.clear)
		b1.clicked.connect(ProgramLogic.showpage_one_logic)
		b1.clicked.connect(ProgramLogic.pageonepressed)
		b1.setText("Metingen")
		b1.resize(150,35)
		b1.move(25,130)
		b1.setStyleSheet(fbutton)

		b2 = QtWidgets.QPushButton(w)						# Knop 2
		b2.clicked.connect(ProgramLogic.clear)
		b2.clicked.connect(ProgramLogic.showpage_two_logic)
		b2.setText("Schakelaars")
		b2.resize(150,35)
		b2.move(25,190)
		b2.setStyleSheet(fbutton)

		b3 = QtWidgets.QPushButton(w)						# Knop 3
		b3.clicked.connect(ProgramLogic.clear)
		b3.clicked.connect(ProgramLogic.showpage_three)
		b3.setText("Potentiometers")
		b3.resize(150,35)
		b3.move(25,250)
		b3.setStyleSheet(fbutton)

		b4 = QtWidgets.QPushButton(w)						# Knop 4
		b4.clicked.connect(ProgramLogic.clear)
		b4.clicked.connect(ProgramLogic.showpage_four)
		b4.setText("Functies")
		b4.resize(150,35)
		b4.move(25,310)
		b4.setStyleSheet(fbutton)

		b5 = QtWidgets.QPushButton(w)						# Knop 5
		b5.clicked.connect(ProgramLogic.clear)
		b5.clicked.connect(l5.show)
		b5.setText("Info")
		b5.resize(150,35)
		b5.move(25,370)
		b5.setStyleSheet(fbutton)

		bexit = QtWidgets.QPushButton(w)						# Exit knop
		bexit.clicked.connect(w.close)
		bexit.setText("Exit")
		bexit.resize(150,35)
		bexit.move(25,430)
		bexit.setStyleSheet("font: Arial; font-size: 18px; background-color: #DB162F; border-radius: 4px")






		w.show()									# Applicatie tonen








Window()	# Start de applicatie
