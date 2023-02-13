# Pavement Crack Detection

Crack Detection software for SME

## Team Members:

- Daniel Villalba

- Alder Fulton

- Jessica Parks

- Akash Gupta

- Noor Alhaidari

## Team Proposal Video

<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/811482/sp/81148200/embedIframeJs/uiconf_id/27551951/partner_id/811482?iframeembed=true&playerId=kaltura_player&entry_id=1_siorryyn&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[hotspots.plugin]=1&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid=1_neoe0o8v" width="640" height="396" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-downloads allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="SME_Proposal_Video"></iframe>

## Team Purpose:

Look at images provided by SME gathered by drone footage to identify/detect cracks in pavement.

## Expected Outcomes:

*These will become more specific the more we learn about pavement cracks and meet with sponsor*

- An alogrithm that identifies cracks using image segmentation and global thresholding  techniques

- Build off global threholding model with local or dynamic thresholding algorithm

- Classification of different sizes and types of cracks

## Code  
### IMPORTANT: Do not run any of these scripts outside of the `src/` directory. All of these scripts currently use relative paths. This will be fixed in the future.

`LoadImage.py`: Loads in an image and cuts it into equally sized squares. To run this code,
you need to have a `data\` folder containing the image file.

`SaveCutImages.py`: Takes the image dictionary loaded in by `LoadImage.py` and saves each cut
to its own .tif file. To run this code, you need to have a `results\` folder.
