import os 
import tkinter as tk
from tkinter import filedialog
from PIL import Image as img



class Main:
	def __init__(self):
		self.files = {}

		self.main = tk.Tk()
		self.main.title("Image to PDF Converter")
		self.main.geometry('300x300')

		self.label = tk.Label(text="Image to PDF converter",fg="red",font=("Bahnschrift",15,"bold"))
		self.label.grid(padx=40,pady=15)

		self.upload_btn = tk.Button(self.main,fg="blue",text="Insert Pictures",command=self.upload)
		self.upload_btn.grid(padx=45, pady=10)

		self.download_btn = tk.Button(self.main,text="Get PDF",fg="green",command=self.save)
		self.download_btn.grid(padx=30,pady=10)
		self.btn_dis(self.download_btn)

		self.main.mainloop()

	def upload(self):
		self.files['filename'] = filedialog.askopenfilenames(filetypes=[("JPG","*.jpg"),("PNG","*.png"),("JPEG","*.jpeg")],initialdir=os.getcwd(),title="Pilih file")
		if self.files['filename'] !=0:
			self.btn_en(self.download_btn)
		print(self.files)

	def save(self):
		self.list = []
		for file in self.files['filename']:
			self.list.append(img.open(file).convert('RGB'))
			saveFile = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File')
			self.list[0].save(f'{saveFile}.pdf', save_all=True, append_images = self.list[1:])
			self.btn_dis(self.download_btn)


		
	def btn_en(self,state):
		state['state'] = 'active'

	def btn_dis(self,state):
		state['state'] = 'disabled'

Main()
