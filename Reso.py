#Python resoluation check
import os


#The file being analized
inputFile = "Blakes 7 - 1x01 - The Way Back-DXDd1zO9F1I.mkv"

outputFile = "output.mp4"

#The Windows Shell command to look up the Width of the file
widthCommand = "MediaInfo.exe --inform=" + '\"' + "Video;%Width%" + '\"' + " " + '\"' + inputFile + '\"'

#Running the Windows Shell Command to get the width
width = os.popen(widthCommand).read()

#The Windows Shell Command to look up the Height
heightCommand = "MediaInfo.exe --inform=" + '\"' + "Video;%Height%" + '\"' + " " + '\"' + inputFile + '\"'

#Running the command
height = os.popen(heightCommand).read()

#for debuging, will be del later
print(widthCommand)
print(heightCommand)
print(width)
print(height)

# A slector for the videoPreset
# This whole section needs work!

if width <= '720':
	print("SD Video")
	videoPreset = 1
elif width == '1280':
	print("720p")
	videoPreset = 2
elif width > '1280':
		print("1080?")
		videoPreset = 3
else:
	print("Some Sort of Error!")
	videoPreset = 0

print(videoPreset)

if videoPreset == 0:
	print("Error!")
	handbreakPreset = 0
elif videoPreset == 1:
	handbreakPreset = "Roku 480p30"
elif videoPreset == 2:
	handbreakPreset = "Roku 720p30 Surround"
elif videoPreset == 3:
	handbreakPreset = "Roku 1080p30 Surround"
else:
	print("Error Exiting!")

# Time to genrate the HandBreakCLI.exe command!
print(handbreakPreset)

handBreakCommand = 'HandBrakeCLI.exe' + ' -Z ' + '\"' + handbreakPreset + '\" ' + '-i ' + '\"' + inputFile + '\"' + " " + "-o " + outputFile

print("tring to transcode with command : " + handBreakCommand)
os.popen(handBreakCommand)
print("DONE!")
