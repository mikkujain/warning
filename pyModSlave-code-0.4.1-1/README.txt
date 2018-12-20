This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. 

1.Description 
pyModSlave is a free python-based implementation of a ModBus slave application for simulation purposes.
2.Software
pyModSlave is based on modbus-tk <http://code.google.com/p/modbus-tk/>, pySerial <http://pyserial.sourceforge.net/> and pyQt4 <http://www.riverbankcomputing.co.uk>.
3.Compatibility
Tested with python 2.7.2 (most probably is compatible with previous versions of python)
4.Installation 
- Download and install the latest python 2.x version 
- Download and install modbus-tk, pySerial and pyQt4.
- Download pyModSlave and run using the command : 'python pyModSlaveQt.py' from the installation folder. 
5.Usage
Starts a TCP/RTU ModBus Slave.Builds 4 data blocks (coils,discrete inputs,input registers,holding registers) and sets random values. You can also set values for individual registers.
6.To configure the logging level set the 'LoggingLevel' in pyModSlave.ini file
- CRITICAL : 50
- ERROR : 40
- WARNING : 30 [default]
- INFO : 20
- DEBUG : 10
- NOTSET : 0

For Windows a pre-compiled binary is availiable. It does not require installation, just unzip and run.
You can easily build the standalone 'exe' version using the command : 'python cx_frz_create_exe.py build' from the installation folder (you will need to install 'cx_freeze' package). 

