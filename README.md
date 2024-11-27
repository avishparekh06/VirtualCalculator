Virtual Calculator

Overview

The Virtual Calculator is a Python-based project that utilizes computer vision to interpret hand gestures as input for performing basic calculator operations.
This project leverages the OpenCV and MediaPipe libraries to detect hand landmarks and interpret pinch gestures for user interaction.

Features

	•	Gesture Recognition: Detects hand movements using MediaPipe and calculates distances between landmarks to identify pinch gestures.
	•	Pinch-to-Click Mechanism: Interprets the pinch gesture (thumb and index finger touch) as a click for interactive input.
	•	Real-Time Processing: Processes gestures in real-time for seamless user experience.

Technologies Used

	•	Python: The programming language used for implementation.
	•	OpenCV: For image processing and hand detection.
	•	MediaPipe: For advanced hand landmark detection and tracking.
 Usage

	1.	Position your hand within the webcam frame.
	2.	Perform a pinch gesture (thumb and index finger touch) to simulate a click.
	3.	Use the pinch gesture to interact with the calculator operations displayed on the screen.

How It Works

	•	The program detects hand landmarks in real-time using MediaPipe.
	•	The distance between the thumb and index finger is calculated to determine if a pinch gesture is performed.
	•	Pinch gestures are interpreted as “clicks,” enabling the user to interact with the calculator.
 
 Acknowledgments

	•	Thanks to the creators of OpenCV and MediaPipe for their powerful libraries.
	•	Inspiration for this project stemmed from the intersection of accessibility and computer vision.
