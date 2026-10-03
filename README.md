## Arduino Hardware Token/Deadman Switch

INTRO:
This project, is a basic one which utilizes an arduino uno’s connction to the computer via usb to lock and unlock the computer when plugged in or unplugged.
The entire pipe-line will be written in adruinos ide Langues otherise c++ and in python.


Phase 1: Send signals.
This section is relatively small due to the uno not having much of a function here.
This part of the project turns the Arduino Uno into a continuous security beacon. Since an Uno cannot talk to Windows directly, it acts as a deadman switch constantly sending a heartbeat signal over USB to let our Python script know it is plugged in. Instead of using delay(), which completely freezes the microcontroller's processor, this code uses non-blocking timing via millis().
The Arduino continuously checks the internal processor clock. Only when exactly 1000ms (1 second) have passed does it send the signal. This keeps the board highly responsive and prevents it from flooding your computer's CPU with data.

Check the .c++ file for the full code.(A .ino file is also included in the repo if you want to use it for yourself.) 


Phase 2

The python script acts like a listener, it runs continuously in the background on your pc. It listens to the USB port for the uno’s heartbeat signal. If the hardware is unplugged or stops responding, it immediately fires a command towindows to lock the computer. The python script utilizes pyserial to monitor the heart-beat beacon sent by the uno. Then we set a timeout buffer/timeout interval for every 3 seconds. This ensures that the python script does not accidentally miss the uno’s signal. This is due to the uno sending signals every second missing these signals tell the python script the uno isn’t active/responsive anymore.

Check the .PY file for the full code.


Extra:
 As an extra feature for more fancy security, I have impelemented a feature that causes the pc to lock instantly should the script crash.


How to:
Before running the script, you must tell Python which USB port your Arduino is plugged into.
Right click the windows start button and select device manager.
Expand the ports section and look for Arduino Uno if you have a third party board it may be names something different like: USB serial – (com 6)
Open communication.py in an ide and update the PORT variable line to match the port
Then upload the .ino file to your arduino via the Arduino IDE. 
Open a cmd window pointing to the python script and run it or run it in vs code or however you like.
Then test the pipeline.

If any of the following happen,

– Error: SerialException: PermissionError
Close the Serial Monitor in the Arduino IDE so Python can access the port.

– The PC locks even when the Arduino is plugged in
Fix: Double-check your Device Manager COM port number and ensure the Arduino's on-board LED stays lit.

-The Python script crashes immediately
Run pip install pyserial in your command terminal.

Warning: If not done properly, you could risk being in a continuous lock out loop in your system but can be easily bypassed by shutting down or restarting.

