'#!/usr/bin/env python

# Import dependencies
import depthai as dai
import cv2
import time
from datetime import datetime

# 1080p FPS size/5s
# 60fps (defaults to 35fps)
# 35fps = 17.4MiB
# 30fps = 14.8MiB
# 25fps = 12.5MiB
# 20fps =  8.2MiB
# 15fps =  4.7MiB
FRAMERATE = 15
SECONDS = 10
DISPLAY = False
FILE_LIMIT = 0

# Create a pipeline
pipeline = dai.Pipeline()

# Create a colour camera
cam = pipeline.create(dai.node.ColorCamera)
cam.setBoardSocket(dai.CameraBoardSocket.RGB)
cam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
cam.setVideoSize(1920, 1080)
cam.setFps(FRAMERATE)
#rgb_cam.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

# Create stream link?
video_out = pipeline.create(dai.node.XLinkOut)
video_out.setStreamName('video')
video_out.input.setBlocking(False)
video_out.input.setQueueSize(1)
cam.video.link(video_out.input)

def record():
	# Create a video writer
	output_name = f"output {datetime.now()}.avi".replace(' ', '_')
	out = cv2.VideoWriter(
		f"/home/pi/oakd-lite-testing/outputs/{output_name}", # Output filename
		cv2.VideoWriter_fourcc(*'x264'), # FourCC recording format
		FRAMERATE, # FPS
		(1920, 1080), # Resolution
	)

	try:
		#Open the camera and start recording
		with dai.Device(pipeline) as device:
			frame_count = 0

			video = device.getOutputQueue(name='video', maxSize=1, blocking=False)
			print(f"Recording for {SECONDS} seconds")
			while True:
				# Get a frame from the output queue
				frame = video.get().getCvFrame()

				# Write the frame to the writer
				out.write(frame)
				frame_count += 1

				# Show the frame
				if DISPLAY:
					cv2.namedWindow("video", cv2.WINDOW_NORMAL)
					cv2.resizeWindow("video", 1280, 720)
					cv2.imshow("video", frame)

				if cv2.waitKey(1) == ord('s') or frame_count >= FRAMERATE*SECONDS: break

	except KeyboardInterrupt:
		print("Stopping DMV...")
		if out: out.release() # Crashes here
		print("Closed video writer")
		return -1

	print(f"Saving video {output_name}...")
	if out: out.release()
	print(f"Output saved!\n")
	return 1

if cam: print("OAK camera found, running pipeline...")

# Run the pipeline with the camera device
if FILE_LIMIT > 0:
	print(f"Record {FILE_LIMIT} files:")
	for _ in range(FILE_LIMIT):
		ret = record()
		if cv2.waitKey(1) == ord('q') or ret <= 0: break
else:
	print(f"Record infinite files:")
	while True:
		ret = record()
		if cv2.waitKey(1) == ord('q') or ret <= 0: break

# Close everything nicely
if DISPLAY: cv2.destroyAllWindows()

print("Exiting DMV4")
time.sleep(3)
