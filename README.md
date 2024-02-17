# DMV4

Data collection script for MonsterVision4. Since MV4 is most likely not going to be done before a scrimmage match on Feb 18th, this is going to stand in it's place. While it's not the program we would hope it is (ie. recognizing April Tags, object detection, etc.), this will assist with building the final object detection model by periodically taking pictures with an OAK camera and saving it to disk.

## MVP (Minimum Viable Product)

- [x] Collects data at a specified interval
- [x] Saves content to disk (does not matter if some content is corrupted, so long as most of them survive)
- [x] Runs on boot

## TODO

- [x] Import lib
	- [x] depthai
	- [x] opencv-contrib-python
- [x] Data collection
	- [x] ~~Working picture save~~ (video is much better for data collection)
	- [x] Working video save (framerate is super weird, further testing required)
	- [x] Test which method is more space efficient (use 1080p15, 30 if more data is wanted)
- [x] Test configurations:
	- [x] Mono camera
	- [x] ~~Stereo cameras~~ (use mono camera)
	- [x] ~~All cameras~~ (use mono camera)
- [x] Run on boot (either cronjob, .bashrc, or something)
- [ ] Make sure contents are saved properly after shutdown
