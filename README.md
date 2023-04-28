# Pavement Crack Detection

Crack Detection software for SME

# Table of Contents
* [Project Description](#project-description)
* [Installation](#installation)
* [Running the Project](#running-the-project)
* [Future Work](#future-work)



## Project Description

#### Team Purpose

Analyze the images from drone footage provided by SME identify cracks in asphalt pavement. This is achieved by segmenting the image and using thresholding methods.

#### Expected Outcomes

- An model that identifies cracks using image segmentation and global thresholding techniques
- Produce image that is thresholded and identifies cracks
- Allow different types of thresholding methods to be used for image

#### Team Members

- Daniel Villalba
- Alder Fulton
- Jessica Parks
- Akash Gupta
- Noor Alhaidari

#### Team Proposal Video

[Proposal Video](https://mediaspace.msu.edu/media/SME_Proposal_Video/1_zyp7lfsq)

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/811482/sp/81148200/embedIframeJs/uiconf_id/27551951/partner_id/811482?iframeembed=true&playerId=kaltura_player&entry_id=1_zyp7lfsq&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_kdkj3z0c" width="640" height="396" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="SME_Proposal_Video"></iframe>

[Final Project Video](https://mediaspace.msu.edu/media/SME+Final+Presentation/1_97prlt4a)

## Installation

View [`INSTALL.md`](https://gitlab.msu.edu/villalb7/Pavement-Crack-Detection/-/blob/main/INSTALL.md) for more information on installation and setup



## Running the project

#### Code

* `InteractiveCrackDetection.ipynb`: jupyter notebook containing code that walks through each step of our image segmentation and thresholding process. Comments are included in the notebook for users to understand each step in our model from beginning to end.

* `TestingAccuracy.ipynb`: Jupyter notebook containing code that tests the accuracy of the crack detection program comparing the thresholded image with the ground truth image that we hand traced over data images.

* `DetectPavementCracks.py`: end to end version of the software that runs through images in the `data/raw_images` folder and returns segmented and stitched thresholded images in the `results` folder.

* `src`: directory containing the functions created for and used in executing `InteractiveCrackDetection.ipynb`

#### Running the code

1. Clone the repository locally: `git clone https://gitlab.msu.edu/villalb7/Pavement-Crack-Detection.git`.

2. Move into the Pavement-Crack-Detection folder: `cd Pavement-Crack-Detection`.

3. Create a `data/raw_images` folder in the root of the project.

4. Move the `.tif` images into the `data/raw_images` folder that is to be thresholded.

5. Now the environment is set up for the jupyter notebook. While in the Pavement-Crack-Detection folder, open jupyter notebook locally from your terminal.

6. Open the `InteractiveCrackDetection.ipynb` and follow along with the steps in the notebook.

7. Alternatively, you can run the `DetectPavementCracks.py` file and have the program do all the steps for you without looking at what it's doing.

#### Thresholding Functions

One of the benefits of our code is the use of custom thresholding functions. Any thresholding function can be passed in easily by setting the value `thresholding_function` under the **Globals** section in our interactive notebook. That said, some thresholding functions may not work with our code. It is possible to make these work using `try` and `except`, but it was determined that the code should not do this.

We tried the different thresholding functions from `skimage.filters`.

**Thresholding Functions that Work**
* threshold_yen
* threshold_multiotsu
* threshold_otsu
* threshold_isodata
* threshold_li
* threshold_mean
* threshold_triangle

**Thresholding Functions that do not Work**
* threshold_minimum

Other thresholding functions can be used and most should work.

## Future Work

Projects that can expand on this asphalt pavement crack detection repository:

* classify the crack severity
    * use a heat map to show location and severity of crack in pavement
    
* calculate lineal footage of the cracks in images
    * utilize an image reference scale to calculate crack length

* use image classification to identify ares of image that are pavement and are not pavement
    * may be on segmented parts of image or entire image
