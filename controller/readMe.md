
First you install boost.python
$sudo apt-get install libboost-all-dev

/Gymbal_Control/Controller you can find setup.py, you should  build this file. run command below.

$python setup.py build

Then you get servo.so -> include this file to Python path (then you can import servo what is in ConnectCppWithPython.py)
There will be your file (directory name can be changed due to ARM CPU) /home/Gymbal_Control/Controller/build/lib.linux-i686-2.6, paste it to Desktop and include python path to desktop (simplest way)

You can change your directory following this : 

$vim .profile

then add this code to bottom

////

#set Python PATH
export PATH = /usr/local/bin:$PATH
export PYTHONPATH =~/Desktop/python

///
