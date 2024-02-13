# DMV4

Data collection script for MonsterVision4. Since MV4 is most likely not going to be done before a scrimmage match on Feb 18th, this is going to stand in it's place. While it's not the program we would hope it is (ie. recognizing April Tags, object detection, etc.), this will assist with building the final object detection model by periodically taking pictures with an OAK camera and saving it to disk.

## MVP (Minimum Viable Product)

- [ ] Collects data at a specified interval
- [ ] Saves content to disk (does not matter if some videos/images are corrupted, so long as most of them survive)
- [ ] Runs on boot

## TODO

- [ ] Import lib
	- [ ] depthai
	- [ ] opencv-contrib-python
- [ ] Data collection
	- [ ] Working picture save
	- [ ] Working video save
	- [ ] Test which method is more space efficient
- [ ] Test configurations:
	- [ ] Mono camera
	- [ ] Stereo cameras
	- [ ] All cameras
- [ ] Make sure contents are saved properly after shutdown
- [ ] Run on boot (either cronjob, .bashrc, or something)
