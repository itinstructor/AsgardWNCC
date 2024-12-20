import sys
# Import the glob module to find all the pathnames matching a specified pattern
import glob
# Import the pySerial module to handle serial communication
# pip install pyserial
import serial


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    # Check if the platform is Windows
    if sys.platform.startswith('win'):
        # Generate a list of possible COM port names (COM1 to COM256)
        ports = ['COM%s' % (i + 1) for i in range(256)]

    # Check if the platform is Linux or Cygwin
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # Find all the serial ports in /dev/ that match the pattern /dev/tty[A-Za-z]*
        ports = glob.glob('/dev/tty[A-Za-z]*')

    # Check if the platform is macOS
    elif sys.platform.startswith('darwin'):
        # Find all the serial ports in /dev/ that match the pattern /dev/tty.*
        ports = glob.glob('/dev/tty.*')
    else:
        # Raise an error if the platform is unsupported
        raise EnvironmentError('Unsupported platform')

    # Initialize an empty list to store the available serial ports
    result = []

    # Iterate over each port in the list of ports
    for port in ports:
        try:
            s = serial.Serial(port)  # Try to open the serial port
            s.close()                # Close the serial port
            # If successful, add the port to the result list
            result.append(port)
        except (OSError, serial.SerialException):
            pass  # Ignore the errors and continue with the next port
      # Return the list of available serial ports
    return result


def main():
    # Call the serial_ports() function to get the list of available serial ports
    ports = serial_ports()

    # Print the list of available serial ports
    print('Available serial ports:')
    for port in ports:
        print(port)

    # Check if the list of available serial ports is empty
    if not ports:
        print('No serial ports available')
    else:
        print(f'Found {len(ports)} serial port(s)')


if __name__ == '__main__':
    main()
