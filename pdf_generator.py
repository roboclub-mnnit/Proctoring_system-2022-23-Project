from fpdf import FPDF 
from Detection import data


def pdf_gen():
 ch = 50
 m= 10
 pw = 210-2*m

 pdf = FPDF()

 pdf.add_page()




 

 pdf.image('Assets\Images\ICON2_img.jpg',x = pw/2, y = None, w = 20, h = 20, type = 'JPG')
 pdf.set_font('Arial', '', 36)
 pdf.cell(w=0, h=10,align='C', txt = "Proctify" + data.name,border=0, ln=1)
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 pdf.set_font('Arial', '', 12)
 # for info of user
 pdf.cell(w=0, h=10, txt = "Name : " + data.name,border=1, ln=1)
 pdf.cell(w=0, h=10, txt = "Registration N0.: "+ str(data.roll),border=1, ln=1)
 pdf.cell(w=0, h=10, txt = "Test_URL :"+data.test_url,border=1, ln=1)

 # for procturing info
 pdf.cell(w=pw/2, h=10, txt = "Duration : 10 min",border=1, ln=0)
 pdf.cell(w=pw/2, h=10, txt = "Calculator : Enabled",border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 # Head Movement
 # 
 if(data.Left!=0):
  pdf.cell(w=pw/2, h=10, txt = "Suspicious Head Movement : Left",border=1, ln=0)
 if(data.Right!=0):
  pdf.cell(w=pw/2, h=10, txt = "Suspicious Head Movement : Right",border=1, ln=1)
 if(data.up!=0):
  pdf.cell(w=pw/2, h=10, txt = "Suspicious Head Movement : Up",border=1, ln=0)
 if(data.down!=0):
  pdf.cell(w=pw/2, h=10, txt = "Suspicious Head Movement : Down",border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

# Cell Phone

 if(data.object_List['cell phone']!=0):
  pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=1)
  pdf.image('Nature.jpg',x = 10, y = None, w = pw/2, h = 40, type = 'JPG')

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 if(data.object_List['cell phone']!=0):
  pdf.cell(w=pw/2, h=10, txt = "Laptop Detected",border=1, ln=1)
  pdf.image('Nature.jpg',x = 10, y = None, w = pw/2, h = 40, type = 'JPG')
  pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

# User Missing

 if(data.usermiss!=0):
  pdf.cell(w=pw/2, h=10, txt = "User Out of Frame",border=1, ln=1)
  
  pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

# Multiple Face
 if(data.multiple_count!=0):
  pdf.cell(w=pw/2, h=10, txt = "Multiple Face Detected",border=1, ln=1)
  pdf.image('Nature.jpg',x = 10, y = None, w = pw/2, h = 40, type = 'JPG')
  pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

# Tab Switch
 if(data.tabswitch == True):
  pdf.set_fill_color(r=0,g=128,b=128)
  pdf.cell(w=0, h=10,fill=True, txt = "Tab Switch Detected",border=1, ln=1)
  for val in data.URL:
   pdf.cell(w=pw/2, h=10, txt =val,border=1, ln=1)
  pdf.image('Nature.jpg',x = 10, y = None, w = pw/2, h = 40, type = 'JPG')
  pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 
# Background Apps
 pdf.set_fill_color(r=0,g=128,b=128)
 
 pdf.cell(w=0, h=10,fill=True, txt = "Background Apps Running",border=1, ln=1)
 for val in data.softwares:
  pdf.cell(w=pw/2, h=10, txt = val,border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)

 # To be decided
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=0)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=1)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=0)
 pdf.cell(w=pw/2, h=10, txt = "Cell Phone Detected",border=1, ln=1)

 pdf.cell(w=0, h=10, txt = "",border=2, ln=1)
 pdf.set_fill_color(r=0,g=128,b=128)
 pdf.cell(w=pw/2, h=10,fill=True, txt = "Random Photo",border=1, ln=1) 

 pdf.image('Nature.jpg',x = 10, y = None, w = pw/2, h = 40, type = 'JPG')





 pdf.set_xy(x=10, y= 220) # or use pdf.ln(50)


 pdf.output(f'./result.pdf','F')
 print('PDF Generated')

pdf_gen()