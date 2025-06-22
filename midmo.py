from tkinter import messagebox
from sys import exit
import subprocess

while True:
	try:
		messagebox.showwarning("Error","Error!")
		subprocess.Popen()
	except KeyboardInterrupt:
		exit()

