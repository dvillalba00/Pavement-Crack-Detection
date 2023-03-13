# Pavement Crack Detection

Crack Detection software for SME

## Team Members:

- Daniel Villalba

- Alder Fulton

- Jessica Parks

- Akash Gupta

- Noor Alhaidari

## Team Proposal Video

[Proposal Video](https://mediaspace.msu.edu/media/SME_Proposal_Video/1_zyp7lfsq)

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/811482/sp/81148200/embedIframeJs/uiconf_id/27551951/partner_id/811482?iframeembed=true&playerId=kaltura_player&entry_id=1_zyp7lfsq&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_kdkj3z0c" width="640" height="396" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="SME_Proposal_Video"></iframe>


## Team Purpose:

Look at images provided by SME gathered by drone footage to identify/detect cracks in pavement.

## Expected Outcomes:

*These will become more specific the more we learn about pavement cracks and meet with sponsor*

- An alogrithm that identifies cracks using image segmentation and global thresholding  techniques

- Build off global threholding model with local or dynamic thresholding algorithm

- Classification of different sizes and types of cracks

## Installation instructions

view `INSTALL.md` for more information on installation and setup

## Code

* `createPaths`: Create all of the folders that are passed in as a list of strings.

* `loadImage`: Loads in an image and cuts it into roughly equally sized rectangles depending on the **DIVIDE_X** and **DIVIDE_Y** global variables. This returns a dictionary of cut images where the key is a tuple representing the location of the image from the original.

* `saveCutImages`: Takes the image dictionary created by the loadImage function and saves each cut image to its own .tif file.

* `thresholdCutImages`: Takes in the dictionary of cut images and a thresholding function. It thresholds each image and applies that threshold to each image. Returns a dictionary of thresholded images with the same keys as **cut_img_dict**.

* `saveThresholdedImages`: Takes in the dictionary thresholded images created by the thresholdCutImages function. It then saves each thresholded image to its own .tif file.

## Running the code

To run the program on an image, first create a data folder on the root of the project that contains the main `.tif` file that you want thresholded.

Once the image is in the data folder, you can then run the following command in the root of the project in order to run the program.

`python3 main.py -f [FILENAME]`

## Flag options for running main.py

* `-f FILENAME`: Required. Runs the program on the file listed as FILENAME.

* `-x [number]`: Sets the pixel width for segmenting the images to the number provided. Default: 25

* `-y [number]`: Sets the pixel height for segmenting the images to the number provided. Default: 25
