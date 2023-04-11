# Proctoring_system-2022-23-Project

Project Name : Proctify

###################################################################################################################################################

Proctify : 

 An online proctoring system is an advanced AI integrated tool that has been created for ensuring a cheat-proof test environment when the candidate is attempting an online test from a remote location. It increases the scope for the administrator to conduct online exams from any remote location without worrying about any sort of misleading act or attempt during the test.


###################################################################################################################################################

TechStack ->
 Python
   Detection : 
       OpenCV
      MediaPipe
      Selenium
      Matplotlib
      Subprocess
      time
      pyautogui

   GUI : 
      Tkinter
      TTkTheme
      FPDF

   Database : 
      SQL
      PyMySQL 

###################################################################################################################################################

 
 How To Run: 

  -> Make a venv using Python -m venv venv
  -> Activate the venv using venv/Scripts/activate
  -> Install all the above mentioned libraries
  -> Activate your MySQL
  -> Start login.py

###################################################################################################################################################

Working of the Application - 

   -> Firstly there is a user validation window that redirects the user to our proctify app if the user is validated.

   -> Also there is also a registration form for each test session in which the user has to fill his/her details to be able to start proctoring and attempt the test.

   -> When the user registers and clicks start proctoring then only the real proctoring starts.

   -> Now the app accesses the camera of the user's device and then sends frame-by-frame data to each of the detection modules.

   -> Firstly the frame is sent to head pose detection modules that make a face mesh on user's face and direct a line from the nose and analyze that line's position on a 2D plane to get the direction in which the user is looking.

   -> Then the same frame is sent to detection modules that analyzes the presence or absence of any user in the frame and reports the user missing if no one is recognized in the frame.

   -> Then the frame is sent to the Multiple face detection module that uses the haarcascade frontal face to detect multiple faces in the frame.

   -> The frame is then sent to object detection modules that analyzes the frame to look for any objects like cell phone laptop and other cheating equipments

   -> Also the app takes the current url of the browser window at very short intervals  to match it with the actual test url so as to detect any browser tab switches.

   -> If any sort of suspicious activity is recorded in  any frame then the data is stored in a data file in real time.
    
   -> The stored data is then presented in a well ordered manner in the form of a pdf as a report.


Group Members:
   Tushar Kesarwani
   Sanjay Dutta
   Peketi Sai Dheeraj
   Aditya Omar
   Arpit Mittal

Mentors:
   Anurag Gupta
   Gautam Kumar





