"""
    File: asgard.py
    Description: This file contains the main application code for the Asgard GUI.
    The Asgard GUI is a graphical user interface for controlling Thor.
    Asgard allows users to send commands to Thor the robotic arm
    and monitor its state.
    https://github.com/AngelLM/Thor
    https://github.com/AngelLM/Asgard 
"""


import sys
# pip install PySide6
from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from gui import Ui_MainWindow
from about import Ui_Dialog as About_Ui_Dialog

import serial_port_finder as spf
from serial_read_thread_class import SerialThreadClass

# pip install pyserial
import serial

# Create a serial object
s0 = serial.Serial()


class AsgardGUI(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

        self.getSerialPorts()

        self.SerialThreadClass = SerialThreadClass()
        self.SerialThreadClass.serialSignal.connect(self.update_console)

        self.actionAbout.triggered.connect(self.launch_about_window)
        self.actionExit.triggered.connect(self.close_application)

        self.HomeButton.pressed.connect(self.send_homing_cycle_command)
        self.ZeroPositionButton.pressed.connect(
            self.send_zero_position_command)
        self.KillAlarmLockButton.pressed.connect(self.send_kill_alarm_command)

        self.G0MoveRadioButton.clicked.connect(self.feed_rate_box_hide)
        self.G1MoveRadioButton.clicked.connect(self.feed_rate_box_hide)

        self.FKGoButtonArt1.pressed.connect(self.fk_move_art1)
        self.FKSliderArt1.valueChanged.connect(self.fk_slider_update_art1)
        self.SpinBoxArt1.valueChanged.connect(self.fk_spinbox_update_art1)
        self.FKDec10ButtonArt1.pressed.connect(self.fk_dec10_art1)
        self.FKDec1ButtonArt1.pressed.connect(self.fk_dec1_art1)
        self.FKDec0_1ButtonArt1.pressed.connect(self.fk_dec0_1_art1)
        self.FKInc0_1ButtonArt1.pressed.connect(self.fk_inc0_1_art1)
        self.FKInc1ButtonArt1.pressed.connect(self.fk_inc1_art1)
        self.FKInc10ButtonArt1.pressed.connect(self.fk_inc10_art1)

        self.FKGoButtonArt2.pressed.connect(self.fk_move_art2)
        self.FKSliderArt2.valueChanged.connect(self.fk_slider_update_art2)
        self.SpinBoxArt2.valueChanged.connect(self.fk_spinbox_update_art2)
        self.FKDec10ButtonArt2.pressed.connect(self.fk_dec_10_art2)
        self.FKDec1ButtonArt2.pressed.connect(self.fk_dec1_art2)
        self.FKDec0_1ButtonArt2.pressed.connect(self.fk_dec0_1_art2)
        self.FKInc0_1ButtonArt2.pressed.connect(self.fk_inc0_1_art2)
        self.FKInc1ButtonArt2.pressed.connect(self.fk_inc1_art2)
        self.FKInc10ButtonArt2.pressed.connect(self.fk_inc10_art2)

        self.FKGoButtonArt3.pressed.connect(self.fk_move_art3)
        self.FKSliderArt3.valueChanged.connect(self.FKSliderUpdateArt3)
        self.SpinBoxArt3.valueChanged.connect(self.FKSpinBoxUpdateArt3)
        self.FKDec10ButtonArt3.pressed.connect(self.FKDec10Art3)
        self.FKDec1ButtonArt3.pressed.connect(self.FKDec1Art3)
        self.FKDec0_1ButtonArt3.pressed.connect(self.FKDec0_1Art3)
        self.FKInc0_1ButtonArt3.pressed.connect(self.FKInc0_1Art3)
        self.FKInc1ButtonArt3.pressed.connect(self.FKInc1Art3)
        self.FKInc10ButtonArt3.pressed.connect(self.FKInc10Art3)

        self.FKGoButtonArt4.pressed.connect(self.FKMoveArt4)
        self.FKSliderArt4.valueChanged.connect(self.FKSliderUpdateArt4)
        self.SpinBoxArt4.valueChanged.connect(self.FKSpinBoxUpdateArt4)
        self.FKDec10ButtonArt4.pressed.connect(self.FKDec10Art4)
        self.FKDec1ButtonArt4.pressed.connect(self.FKDec1Art4)
        self.FKDec0_1ButtonArt4.pressed.connect(self.FKDec0_1Art4)
        self.FKInc0_1ButtonArt4.pressed.connect(self.FKInc0_1Art4)
        self.FKInc1ButtonArt4.pressed.connect(self.FKInc1Art4)
        self.FKInc10ButtonArt4.pressed.connect(self.FKInc10Art4)

        self.FKGoButtonArt5.pressed.connect(self.FKMoveArt5)
        self.FKSliderArt5.valueChanged.connect(self.FKSliderUpdateArt5)
        self.SpinBoxArt5.valueChanged.connect(self.FKSpinBoxUpdateArt5)
        self.FKDec10ButtonArt5.pressed.connect(self.FKDec10Art5)
        self.FKDec1ButtonArt5.pressed.connect(self.FKDec1Art5)
        self.FKDec0_1ButtonArt5.pressed.connect(self.FKDec0_1Art5)
        self.FKInc0_1ButtonArt5.pressed.connect(self.FKInc0_1Art5)
        self.FKInc1ButtonArt5.pressed.connect(self.FKInc1Art5)
        self.FKInc10ButtonArt5.pressed.connect(self.FKInc10Art5)

        self.FKGoButtonArt6.pressed.connect(self.FKMoveArt6)
        self.FKSliderArt6.valueChanged.connect(self.FKSliderUpdateArt6)
        self.SpinBoxArt6.valueChanged.connect(self.FKSpinBoxUpdateArt6)
        self.FKDec10ButtonArt6.pressed.connect(self.FKDec10Art6)
        self.FKDec1ButtonArt6.pressed.connect(self.FKDec1Art6)
        self.FKDec0_1ButtonArt6.pressed.connect(self.FKDec0_1Art6)
        self.FKInc0_1ButtonArt6.pressed.connect(self.FKInc0_1Art6)
        self.FKInc1ButtonArt6.pressed.connect(self.FKInc1Art6)
        self.FKInc10ButtonArt6.pressed.connect(self.FKInc10Art6)

        self.FKGoAllButton.pressed.connect(self.FKMoveAll)

        self.GoButtonGripper.pressed.connect(self.MoveGripper)
        self.SliderGripper.valueChanged.connect(self.SliderUpdateGripper)
        self.SpinBoxGripper.valueChanged.connect(self.SpinBoxUpdateGripper)
        self.Dec10ButtonGripper.pressed.connect(self.Dec10Gripper)
        self.Dec1ButtonGripper.pressed.connect(self.Dec1Gripper)
        self.Inc1ButtonGripper.pressed.connect(self.Inc1Gripper)
        self.Inc10ButtonGripper.pressed.connect(self.Inc10Gripper)

        self.SerialPortRefreshButton.pressed.connect(self.getSerialPorts)
        self.ConnectButton.pressed.connect(self.connectSerial)

        self.ConsoleButtonSend.pressed.connect(self.send_serial_command)
        self.ConsoleInput.returnPressed.connect(self.send_serial_command)

# ------------------------ LAUNCH ABOUT WINDOW --------------------------- #
    def launch_about_window(self):
        self.dialogAbout = QtWidgets.QDialog()
        self.ui = AboutDialog(self.dialogAbout)
        self.dialogAbout.exec()

# -------------------- SEND HOMING CYCLE COMMAND ------------------------- #
    def send_homing_cycle_command(self):
        if s0.isOpen():
            messageToSend = "$H"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

# ---------------------- SEND ZERO POSITION COMMAND ---------------------- #
    def send_zero_position_command(self):
        if s0.isOpen():
            messageToSend = "G0 A0 B0 C0 D0 X0 Y0 Z0"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

# ---------------------- SEND KILL ALARM COMMAND ------------------------- #
    def send_kill_alarm_command(self):
        if s0.isOpen():
            messageToSend = "$X"
            messageToConsole = ">>> " + messageToSend
            s0.write(messageToSend.encode('UTF-8'))
            self.ConsoleOutput.appendPlainText(messageToConsole)

# ---------------------- FEED RATE BOX HIDE ------------------------------ #
    def feed_rate_box_hide(self):
        if self.G1MoveRadioButton.isChecked():
            self.FeedRateLabel.setEnabled(True)
            self.FeedRateInput.setEnabled(True)
        else:
            self.FeedRateLabel.setEnabled(False)
            self.FeedRateInput.setEnabled(False)

##################### FORWARD KINEMATIC ART1 METHODS #######################
# -------------------------- FK MOVE ART1 -------------------------------- #
    def fk_move_art1(self):
        """
        Handles the movement command for Art1 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message with A value
            message = typeOfMovement + "A" + \
                str(self.SpinBoxArt1.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART1 --------------------------- #
    def fk_slider_update_art1(self):
        val = self.FKSliderArt1.value()/10
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART1 -------------------------- #
    def fk_spinbox_update_art1(self):
        val = int(self.SpinBoxArt1.value()*10)
        self.FKSliderArt1.setValue(val)

# ---------------------- FK DECREASE 10 ART1 ----------------------------- #
    def fk_dec10_art1(self):
        val = self.SpinBoxArt1.value()-10
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK DECREASE 1 ART1 ------------------------------ #
    def fk_dec1_art1(self):
        val = self.SpinBoxArt1.value()-1
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK DECREASE 0.1 ART1 ---------------------------- #
    def fk_dec0_1_art1(self):
        val = self.SpinBoxArt1.value()-0.1
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK INCREASE 0.1 ART1 ---------------------------- #
    def fk_inc0_1_art1(self):
        val = self.SpinBoxArt1.value()+0.1
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK INCREASE 1 ART1 ------------------------------ #
    def fk_inc1_art1(self):
        val = self.SpinBoxArt1.value()+1
        self.SpinBoxArt1.setValue(val)

# ---------------------- FK INCREASE 10 ART1 ----------------------------- #
    def fk_inc10_art1(self):
        val = self.SpinBoxArt1.value()+10
        self.SpinBoxArt1.setValue(val)

##################### FORWARD KINEMATIC ART2 METHODS #######################
# -------------------------- FK MOVE ART2 -------------------------------- #
    def fk_move_art2(self):
        """
        Handles the movement command for Art2 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message with B and C values
            message = typeOfMovement + "B" + \
                str(self.SpinBoxArt2.value()) + " C" + \
                str(self.SpinBoxArt2.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART2 --------------------------- #
    def fk_slider_update_art2(self):
        val = self.FKSliderArt2.value()/10
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART2 -------------------------- #
    def fk_spinbox_update_art2(self):
        val = int(self.SpinBoxArt2.value()*10)
        self.FKSliderArt2.setValue(val)

# ---------------------- FK DECREASE 10 ART2 ----------------------------- #
    def fk_dec_10_art2(self):
        val = self.SpinBoxArt2.value()-10
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK DECREASE 1 ART2 ------------------------------ #
    def fk_dec1_art2(self):
        val = self.SpinBoxArt2.value()-1
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK DECREASE 0.1 ART2 ---------------------------- #
    def fk_dec0_1_art2(self):
        val = self.SpinBoxArt2.value()-0.1
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK INCREASE 0.1 ART2 ---------------------------- #
    def fk_inc0_1_art2(self):
        val = self.SpinBoxArt2.value()+0.1
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK INCREASE 1 ART2 ------------------------------ #
    def fk_inc1_art2(self):
        val = self.SpinBoxArt2.value()+1
        self.SpinBoxArt2.setValue(val)

# ---------------------- FK INCREASE 10 ART2 ----------------------------- #
    def fk_inc10_art2(self):
        val = self.SpinBoxArt2.value()+10
        self.SpinBoxArt2.setValue(val)

##################### FORWARD KINEMATIC ART3 METHODS #######################
# -------------------------- FK MOVE ART3 -------------------------------- #
    def fk_move_art3(self):
        """
        Handles the movement command for Art3 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message
            message = typeOfMovement + "D" + \
                str(self.SpinBoxArt3.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART3 --------------------------- #
    def FKSliderUpdateArt3(self):
        val = self.FKSliderArt3.value()/10
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART3 -------------------------- #
    def FKSpinBoxUpdateArt3(self):
        val = int(self.SpinBoxArt3.value()*10)
        self.FKSliderArt3.setValue(val)

# ---------------------- FK DECREASE 10 ART3 ----------------------------- #
    def FKDec10Art3(self):
        val = self.SpinBoxArt3.value()-10
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK DECREASE 1 ART3 ------------------------------ #
    def FKDec1Art3(self):
        val = self.SpinBoxArt3.value()-1
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK DECREASE 0.1 ART3 ---------------------------- #
    def FKDec0_1Art3(self):
        val = self.SpinBoxArt3.value()-0.1
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK INCREASE 0.1 ART3 ---------------------------- #
    def FKInc0_1Art3(self):
        val = self.SpinBoxArt3.value()+0.1
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK INCREASE 1 ART3 ------------------------------ #
    def FKInc1Art3(self):
        val = self.SpinBoxArt3.value()+1
        self.SpinBoxArt3.setValue(val)

# ---------------------- FK INCREASE 10 ART3 ----------------------------- #
    def FKInc10Art3(self):
        val = self.SpinBoxArt3.value()+10
        self.SpinBoxArt3.setValue(val)

##################### FORWARD KINEMATIC ART4 METHODS #######################
# -------------------------- FK MOVE ART4 -------------------------------- #
    def FKMoveArt4(self):
        """
        Handles the movement command for Art4 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message
            message = typeOfMovement + "X" + \
                str(self.SpinBoxArt4.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART4 --------------------------- #
    def FKSliderUpdateArt4(self):
        val = self.FKSliderArt4.value()/10
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART4 -------------------------- #
    def FKSpinBoxUpdateArt4(self):
        val = int(self.SpinBoxArt4.value()*10)
        self.FKSliderArt4.setValue(val)

# ---------------------- FK DECREASE 10 ART4 ----------------------------- #
    def FKDec10Art4(self):
        val = self.SpinBoxArt4.value()-10
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK DECREASE 1 ART4 ------------------------------ #
    def FKDec1Art4(self):
        val = self.SpinBoxArt4.value()-1
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK DECREASE 0.1 ART4 ---------------------------- #
    def FKDec0_1Art4(self):
        val = self.SpinBoxArt4.value()-0.1
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK INCREASE 0.1 ART4 ---------------------------- #
    def FKInc0_1Art4(self):
        val = self.SpinBoxArt4.value()+0.1
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK INCREASE 1 ART4 ------------------------------ #
    def FKInc1Art4(self):
        val = self.SpinBoxArt4.value()+1
        self.SpinBoxArt4.setValue(val)

# ---------------------- FK INCREASE 10 ART4 ----------------------------- #
    def FKInc10Art4(self):
        val = self.SpinBoxArt4.value()+10
        self.SpinBoxArt4.setValue(val)

##################### FORWARD KINEMATIC ART5 METHODS #######################
# En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
# -------------------------- FK MOVE ART5 -------------------------------- #
    def FKMoveArt5(self):
        """
        Handles the movement command for Art5 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message with Y value
            message = typeOfMovement + "Y" + \
                str(self.SpinBoxArt5.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART5 --------------------------- #
    def FKSliderUpdateArt5(self):
        val = self.FKSliderArt5.value()/10
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART5 -------------------------- #
    def FKSpinBoxUpdateArt5(self):
        val = int(self.SpinBoxArt5.value()*10)
        self.FKSliderArt5.setValue(val)

# ---------------------- FK DECREASE 10 ART5 ----------------------------- #
    def FKDec10Art5(self):
        val = self.SpinBoxArt5.value()-10
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK DECREASE 1 ART5 ------------------------------ #
    def FKDec1Art5(self):
        val = self.SpinBoxArt5.value()-1
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK DECREASE 0.1 ART5 ---------------------------- #
    def FKDec0_1Art5(self):
        val = self.SpinBoxArt5.value()-0.1
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK INCREASE 0.1 ART5 ---------------------------- #
    def FKInc0_1Art5(self):
        val = self.SpinBoxArt5.value()+0.1
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK INCREASE 1 ART5 ------------------------------ #
    def FKInc1Art5(self):
        val = self.SpinBoxArt5.value()+1
        self.SpinBoxArt5.setValue(val)

# ---------------------- FK INCREASE 10 ART5 ----------------------------- #
    def FKInc10Art5(self):
        val = self.SpinBoxArt5.value()+10
        self.SpinBoxArt5.setValue(val)

##################### FORWARD KINEMATIC ART6 METHODS #######################
# En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
# -------------------------- FK MOVE ART6 -------------------------------- #
    def FKMoveArt6(self):
        """
        Handles the movement command for Art6 using the specified feed rate
        and movement type.

        Method checks if the serial connection is open.
        If it is, it determines the type of movement (G1 for controlled
        movement with a specified feed rate or G0 for rapid movement
        without a feed rate).
        It then constructs the movement command message and sends it to
        the serial port. The command is also displayed in the console output.
        If the serial connection is not open, it calls the noSerialConnection 
        method to handle the error.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message with Z value
            message = typeOfMovement + "Z" + \
                str(self.SpinBoxArt6.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- FK SLIDER UPDATE ART6 --------------------------- #
    def FKSliderUpdateArt6(self):
        val = self.FKSliderArt6.value()/10
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK SPINBOX UPDATE ART6 -------------------------- #
    def FKSpinBoxUpdateArt6(self):
        val = int(self.SpinBoxArt6.value()*10)
        self.FKSliderArt6.setValue(val)

# ---------------------- FK DECREASE 10 ART6 ----------------------------- #
    def FKDec10Art6(self):
        val = self.SpinBoxArt6.value()-10
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK DECREASE 1 ART6 ------------------------------ #
    def FKDec1Art6(self):
        val = self.SpinBoxArt6.value()-1
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK DECREASE 0.1 ART6 ---------------------------- #
    def FKDec0_1Art6(self):
        val = self.SpinBoxArt6.value()-0.1
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK INCREASE 0.1 ART6 ---------------------------- #
    def FKInc0_1Art6(self):
        val = self.SpinBoxArt6.value()+0.1
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK INCREASE 1 ART6 ------------------------------ #
    def FKInc1Art6(self):
        val = self.SpinBoxArt6.value()+1
        self.SpinBoxArt6.setValue(val)

# ---------------------- FK INCREASE 10 ART6 ----------------------------- #
    def FKInc10Art6(self):
        val = self.SpinBoxArt6.value()+10
        self.SpinBoxArt6.setValue(val)

# FK Every Articulation Functions
# En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
# -------------------------- FK MOVE ALL -------------------------------- #
    def FKMoveAll(self):
        """
        Moves all axes based on the current input values and 
        selected movement type.

        This method checks if the serial connection is open. 
        If it is, it constructs a movement command based on the selected 
        movement type (G1 or G0) and the values from various input widgets.
        The  command is then sent to the connected device via the 
        serial connection, and the command is also displayed in the
        console output.
        If the serial connection is not open, it calls the noSerialConnection method.

        Parameters: None

        Returns: None
        """
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the G1 movement type radio button is selected
            if self.G1MoveRadioButton.isChecked():
                # Set the movement type to G1 (controlled movement)
                typeOfMovement = "G1 "
                # Get the feed rate value from the input and format it
                feedRate = " F" + str(self.FeedRateInput.value())
            else:
                # Set the movement type to G0 (rapid movement)
                typeOfMovement = "G0 "
                # No feed rate for rapid movement
                feedRate = ""
            # Construct the movement command message with A, B, C, D, X, Y, and Z values
            message = typeOfMovement + "A" + str(self.SpinBoxArt1.value()) + " B" + str(self.SpinBoxArt2.value()) + " C" + str(self.SpinBoxArt2.value()) + " D" + str(
                self.SpinBoxArt3.value()) + " X" + str(self.SpinBoxArt4.value()) + " Y" + str(self.SpinBoxArt5.value()) + " Z" + str(self.SpinBoxArt6.value()) + feedRate
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# -------------------------- MOVE GRIPPER ------------------------------- #
# En realidad esto no va así, hay que calcular el movimiento acoplado. Proximamente.
    def MoveGripper(self):
        # Check if the serial connection is open
        if s0.isOpen():
            # Construct the gripper control message with the SpinBoxGripper value
            message = "M3 S" + str((255/100) * self.SpinBoxGripper.value())
            # Add a newline character to the message to send
            messageToSend = message + "\n"
            # Format the message for console output
            messageToConsole = ">>> " + message
            # Send the message to the serial port
            s0.write(messageToSend.encode('UTF-8'))
            # Display the message in the console output
            self.ConsoleOutput.appendPlainText(messageToConsole)
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- SLIDER UPDATE GRIPPER --------------------------- #
    def SliderUpdateGripper(self):
        val = self.SliderGripper.value()
        self.SpinBoxGripper.setValue(val)

# ---------------------- SPINBOX UPDATE GRIPPER -------------------------- #
    def SpinBoxUpdateGripper(self):
        val = int(self.SpinBoxGripper.value())
        self.SliderGripper.setValue(val)

# ---------------------- DECREASE 10 GRIPPER ----------------------------- #
    def Dec10Gripper(self):
        val = self.SpinBoxGripper.value()-10
        self.SpinBoxGripper.setValue(val)

# ---------------------- DECREASE 1 GRIPPER ------------------------------ #
    def Dec1Gripper(self):
        val = self.SpinBoxGripper.value()-1
        self.SpinBoxGripper.setValue(val)

# ---------------------- INCREASE 1 GRIPPER ------------------------------ #
    def Inc1Gripper(self):
        val = self.SpinBoxGripper.value()+1
        self.SpinBoxGripper.setValue(val)

# ---------------------- INCREASE 10 GRIPPER ----------------------------- #
    def Inc10Gripper(self):
        val = self.SpinBoxGripper.value()+10
        self.SpinBoxGripper.setValue(val)

#################### SERIAL CONNECT METHODS ################################
# ----------------------- GET SERIAL PORTS ------------------------------- #
    def getSerialPorts(self):
        self.SerialPortComboBox.clear()
        self.SerialPortComboBox.addItems(spf.serial_ports())

# ------------------------ CONNECT SERIAL -------------------------------- #
    def connectSerial(self):
        """
        Connects to the serial port using the selected serial port
        and baud rate from the combo boxes.

        This method performs the following steps:
        1. Retrieves the selected serial port from the SerialPortComboBox.
        2. Retrieves the selected baud rate from the BaudRateComboBox.
        3. Checks if a serial port and baud rate are selected.
        4. Configures the serial port with the selected settings.
        5. Attempts to open the serial port and start the serial thread.
        6. Handles exceptions if the serial port cannot be opened.
        7. Calls appropriate methods if no serial port or baud rate is selected.

        Raises:
            Exception: If there is an error opening the serial port.
        """
        # Get the selected serial port from the combo box
        serialPort = self.SerialPortComboBox.currentText()
        # Get the selected baud rate from the combo box
        baudrate = self.BaudRateComboBox.currentText()
        # Check if a serial port is selected
        if serialPort != "":
            # Check if a baud rate is selected
            if baudrate != "":
                # Set the serial port
                s0.port = serialPort
                # Set the baud rate
                s0.baudrate = baudrate
                # Set the timeout for the serial connection
                s0.timeout = 1
                try:
                    # Close the serial port if it is already open
                    s0.close()
                    # Open the serial port
                    s0.open()
                    # Start the serial thread
                    self.SerialThreadClass.start()
                except Exception as e:
                    # Print an error message if the serial port cannot be opened
                    print("error opening serial port: " + str(e))
            else:
                # Handle the case where no baud rate is selected
                self.blankBaudRate()
        else:
            # Handle the case where no serial port is selected
            self.blankSerialPort()

# ---------------------- SERIAL DISCONNECTED ----------------------------- #
    def serialDisconnected(self):
        self.RobotStateDisplay.setStyleSheet(
            'background-color: rgb(255, 0, 0)')
        self.RobotStateDisplay.setText("Disconnected")

# ------------------------ UPDATE CONSOLE -------------------------------- #
    def update_console(self, dataRead):
        # Check if the verbose output checkbox is checked
        verboseShow = self.ConsoleShowVerbosecheckBox.isChecked()
        # Check if the OK response checkbox is checked
        okShow = self.ConsoleShowOkRespcheckBox.isChecked()
        # Check if the data read contains "MPos" (verbose data)
        isDataReadVerbose = "MPos" in dataRead
        # Check if the data read contains "ok" (OK response)
        isDataOkResponse = "ok" in dataRead

        # Check if the data read indicates the serial connection is disconnected
        if dataRead == "SERIAL-DISCONNECTED":
            # Close the serial port
            s0.close()
            # Handle the serial disconnection
            self.serialDisconnected()
            # Print a message indicating the serial connection is lost
            print("Serial Connection Lost")
        else:
            # If the data read is not verbose and not an OK response
            if not isDataReadVerbose and not isDataOkResponse:
                # Display the data read in the console output
                self.ConsoleOutput.appendPlainText(dataRead)
            # If the data read is an OK response and the OK response checkbox is checked
            elif isDataOkResponse and okShow:
                # Display the data read in the console output
                self.ConsoleOutput.appendPlainText(dataRead)
            # If the data read is verbose data
            elif isDataReadVerbose:
                # Update the forward kinematic position display with the data read
                self.updateFKPosDisplay(dataRead)
                # If the verbose output checkbox is checked
                if verboseShow:
                    # Display the data read in the console output
                    self.ConsoleOutput.appendPlainText(dataRead)

# ---------------------- SEND SERIAL COMMAND ----------------------------- #
    def send_serial_command(self):
        # Get the text from the console input and add a newline character
        messageToSend = self.ConsoleInput.text() + "\n"
        # Format the message for console output
        messageToConsole = ">>> " + self.ConsoleInput.text()
        # Check if the serial connection is open
        if s0.isOpen():
            # Check if the message to send is not empty
            if messageToSend != "":
                # Send the message to the serial port
                s0.write(messageToSend.encode('UTF-8'))
                # Display the message in the console output
                self.ConsoleOutput.appendPlainText(messageToConsole)
                # Clear the console input
                self.ConsoleInput.clear()
        else:
            # Handle the case where the serial connection is not open
            self.noSerialConnection()

# ---------------------- UPDATE FK POS DISPLAY --------------------------- #
    def updateFKPosDisplay(self, dataRead):
        data = dataRead[1:][:-1].split(",")
        self.updateCurrentState(data[0])
        self.FKCurrentPosValueArt1.setText(data[1][5:][:-2]+"º")
        self.FKCurrentPosValueArt2.setText(data[2][:-2]+"º")
        self.FKCurrentPosValueArt3.setText(data[4][:-2]+"º")
        self.FKCurrentPosValueArt4.setText(data[5][:-2]+"º")
        self.FKCurrentPosValueArt5.setText(data[6][:-2]+"º")
        self.FKCurrentPosValueArt6.setText(data[7][:-2]+"º")

# ---------------------- UPDATE CURRENT STATE ---------------------------- #
    def updateCurrentState(self, state):
        self.RobotStateDisplay.setText(state)
        if state == "Idle" or state == "Run":
            self.RobotStateDisplay.setStyleSheet(
                'background-color: rgb(0, 255, 0)')
        elif state == "Home":
            self.RobotStateDisplay.setStyleSheet(
                'background-color: rgb(85, 255, 255)')
        elif state == "Alarm":
            self.RobotStateDisplay.setStyleSheet(
                'background-color: rgb(255, 255, 0)')
        elif state == "Hold":
            self.RobotStateDisplay.setStyleSheet(
                'background-color: rgb(255, 0, 0)')
        else:
            self.RobotStateDisplay.setStyleSheet(
                'background-color: rgb(255, 255, 255)')

# ------------------------- BLANK SERIAL PORT ---------------------------- #
    def blankSerialPort(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msg = "There is not a Serial Port value indicated to establish the connection."
        msg += "\nPlease check it and try to connect again."
        msgBox.setText(msg)
        msgBox.exec()

# ------------------------- BLANK BAUD RATE ------------------------------ #
    def blankBaudRate(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msg = "There is not a Baud Rate value indicated to establish the connection."
        msg += "\nPlease check it and try to connect again."
        msgBox.setText(msg)
        msgBox.exec()

# ------------------------- NO SERIAL CONNECTION ------------------------- #
    def noSerialConnection(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msg = "The connection has not been established yet."
        msg += "\nPlease establish the connection before trying to control."
        msgBox.setText(msg)
        msgBox.exec()

# ------------------------- CLOSE APPLICATION ---------------------------- #
    def close_application(self):
        sys.exit()


# ---------------------- ABOUT DIALOG CLASS ------------------------------- #
class AboutDialog(About_Ui_Dialog):
    def __init__(self, dialog):
        About_Ui_Dialog.__init__(self)
        self.setupUi(dialog)


# -------------------------- MAIN FUNCTION ------------------------------- #
def main():
    app = QtWidgets.QApplication(sys.argv)
    mwindow = QtWidgets.QMainWindow()

    prog = AsgardGUI(mwindow)

    mwindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
