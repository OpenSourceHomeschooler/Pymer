import Tkinter as Tk
windows = True
try:
	from winsound import Beep
except:
	windows = False
import threading
import time

class timer:
	root = Tk.Tk()
	hourVar = Tk.StringVar()
	minuteVar = Tk.StringVar()
	secondVar = Tk.StringVar()
	heading = 0 
	hours = 0
	minutes = 0
	seconds = 0
	filler1 = None
	filler2 = None
	begin = 0
	stop = False
	ending = None
	afterVar = None
	soundAfter = None
	contSound = True
	def __init__(self):
		self.hourVar.set('0')
		self.minuteVar.set('0')
		self.secondVar.set('0')
		self.heading = Tk.Label(self.root, text="Pymer")
		self.hours = Tk.Entry(self.root, width=3, textvariable=self.hourVar)
		self.filler1 = Tk.Label(self.root, text=":")
		self.minutes = Tk.Entry(self.root, width=3, textvariable=self.minuteVar)
		self.filler2 = Tk.Label(self.root, text=":")
		self.seconds = Tk.Entry(self.root, width=3, textvariable=self.secondVar)
		self.begin = Tk.Button(self.root, text='Start', command=self.start)
		self.heading.pack()
		self.hours.pack(side=Tk.LEFT)
		self.filler1.pack(side=Tk.LEFT)
		self.minutes.pack(side=Tk.LEFT)
		self.filler2.pack(side=Tk.LEFT)
		self.seconds.pack(side=Tk.LEFT)
		self.begin.pack(side=Tk.BOTTOM)
		self.root.mainloop()

	def start(self):
		hour = self.hours.get()
		minute = self.minutes.get()
		second = self.seconds.get()
		starting = int(time.time())
		addition = int(hour) * 60 * 60 + int(minute) * 60 + int(second)
		self.ending = starting + addition
		self.hours.pack_forget()
		self.filler1.pack_forget()
		self.minutes.pack_forget()
		self.filler2.pack_forget()
		self.seconds.pack_forget()
		self.begin.pack_forget()
		self.hours = Tk.Label(self.root, text="")
		self.minutes = Tk.Label(self.root, text="")
		self.seconds = Tk.Label(self.root, text="")
		self.hours.pack(side=Tk.BOTTOM)
		self.minutes.pack(side=Tk.BOTTOM)
		self.seconds.pack(side=Tk.BOTTOM)
		self.begin.pack(side=Tk.BOTTOM)
		self.recursiveTimer()

	def recursiveTimer(self):
		self.begin['text'] = 'Stop'
		self.begin['command'] = self.quit
		self.root.update_idletasks()
		difference = self.ending - int(time.time())
		hour = str( difference / (60 * 60) )
		minute = str( (difference % (60 * 60)) / 60 )
		second = str(difference % 60)
		timeStr = hour + ' : ' + minute + ' : ' + second 
		self.minutes['text'] = timeStr
		self.afterVar = self.root.after(1, self.recursiveTimer)
		if self.stop:
			self.quit()
		if self.ending < time.time():
			self.root.after_cancel(self.afterVar)
			self.begin['command'] = self.startStopSound
			self.sound()


	def sound(self):
		self.begin['command'] = self.startStopSound
		self.root.update_idletasks()
		if windows:
			Beep(500, 100)
		time.sleep(0.3)
		self.soundAfter = self.root.after(1, self.sound)
		if not self.contSound:
			self.quitSound()
		
	def startStopSound(self):
		self.contSound = False

	def quitSound(self):
		self.root.after_cancel(self.soundAfter)
		self.contSound = True
		self.hours.pack_forget()
		self.minutes.pack_forget()
		self.seconds.pack_forget()
		self.begin.pack_forget()
		self.hours = Tk.Entry(self.root, width=2, textvariable=self.hourVar)
		self.minutes = Tk.Entry(self.root, width=2, textvariable=self.minuteVar)
		self.seconds = Tk.Entry(self.root, width=2, textvariable=self.secondVar)
		self.hours.pack(side=Tk.LEFT)
		self.filler1.pack(side=Tk.LEFT)
		self.minutes.pack(side=Tk.LEFT)
		self.filler2.pack(side=Tk.LEFT)
		self.seconds.pack(side=Tk.LEFT)
		self.begin.pack(side=Tk.BOTTOM)
		self.begin['text'] = 'Start'
		self.begin['command'] = self.start

	def quit(self):
		self.root.after_cancel(self.afterVar)
		self.hours.pack_forget()
		self.minutes.pack_forget()
		self.seconds.pack_forget()
		self.begin.pack_forget()
		self.hours = Tk.Entry(self.root, width=2, textvariable=self.hourVar)
		self.minutes = Tk.Entry(self.root, width=2, textvariable=self.minuteVar)
		self.seconds = Tk.Entry(self.root, width=2, textvariable=self.secondVar)
		self.hours.pack(side=Tk.LEFT)
		self.filler1.pack(side=Tk.LEFT)
		self.minutes.pack(side=Tk.LEFT)
		self.filler2.pack(side=Tk.LEFT)
		self.seconds.pack(side=Tk.LEFT)
		self.begin.pack(side=Tk.BOTTOM)
		self.stop = True
		self.begin['text'] = 'Start'
		self.begin['command'] = self.start
		self.stop = False


myTimer = timer()
