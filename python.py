 import wave#open audio file using python builtin module wave
 good_morning=wave.open("good_morning.wav","r")
 good_morning=good_morning.readframe(-1)#convert wave object to byte
 #-1 means to read all piece of information in wave audio obj
 #if size 1khz and of 2 sec time then total piece information is 2000piece per sec 
 #because of frequency measure and noise it large its size
 print(good_morning[:10])


 #convert byte from audio file to int use numpy
 import numpy as np
 signal_gm=np.frombuffer(good_morning,dtype='int16')#convert byte to integer
 print(signal_gm[:10])#10 of 96000 piece of data per sec
 #frame rate is speed at which frame are provided to listner=length or number of wave array obj/duration of audio file
 #frame rate is freq=48khz
 framerate_gm=good_morning.getframerate()#48000 op using wave module
 #now can calculate duration of file=length of array/frame rate
 time_gm = np.linspace(start=0 , stop = len(signal_gm)/framerate_gm , num=signal_gm)#start and stop =duration
 #return every spaced value betwn start and stop
 #figureout timestamp where each soundwave value occur
 time_gm[:10]#each value time in sec where each sound wave byte occur
 #visualize sound wave matplot






