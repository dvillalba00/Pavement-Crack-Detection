# Pavement Crack Detection

Crack Detection software for SME

# Table of Contents
* [Project Description](#project-description)
* [Installation](#installation)
* [Running the project](#running-the-project)



## Project Description

### Team Purpose

Analyze the images from drone footage provided by SME identify cracks in asphalt pavement. This is achieved by segmenting the image and using thresholding methods.

### Expected Outcomes

- An model that identifies cracks using image segmentation and global thresholding techniques
- Produce image that is thresholded and identifies cracks
- Allow different types of thresholding methods to be used for image

### Team Members

- Daniel Villalba
- Alder Fulton
- Jessica Parks
- Akash Gupta
- Noor Alhaidari

### Team Proposal Video

[Proposal Video](https://mediaspace.msu.edu/media/SME_Proposal_Video/1_zyp7lfsq)

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/811482/sp/81148200/embedIframeJs/uiconf_id/27551951/partner_id/811482?iframeembed=true&playerId=kaltura_player&entry_id=1_zyp7lfsq&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_kdkj3z0c" width="640" height="396" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="SME_Proposal_Video"></iframe>



## Installation

view `INSTALL.md` for more information on installation and setup



## Running the project

### Code

* `InteractiveCrackDetection.ipynb`: jupyter notebook containing code that walks through each step of our image segmentation and thresholding process. Comments are included in the notebook for users to understand each step in our model from beginning to end. 

* `src`: directory containing the functions created and used to execute `InteractiveCrackDetection.ipynb`

### Running the code

1. Clone the repository locally: `git clone https://gitlab.msu.edu/villalb7/Pavement-Crack-Detection.git`

2. Move into the Pavement-Crack-Detection folder: `cd Pavement-Crack-Detection`

3. Make a `data` folder in the repository: `mkdir data`

4. Upload the `.tif` image into the `data` folder that is to be thresholded

5. Now the environment is set up for the jupyter notebook. While in the Pavement-Crack-Detection folder, open jupyter notebook locally from your terminal.

6. Open the `InteractiveCrackDetection.ipynb` and follow along with the image segmentation and thresholding steps in the notebook.