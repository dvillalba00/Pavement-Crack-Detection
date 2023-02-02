# Pavement Crack Detection

Crack Detection software for SME

## Team Members:

- Daniel Villalba

- Alder Fulton

- Jessica Parks

- Akash Gupta

- Noor Alhaidari

## Team Purpose:

Look at images provided by SME gathered by drone footage to identify/detect cracks in pavement.

## Expected Outcomes:

*These will become more specific the more we learn about pavement cracks and meet with sponsor*

- An algorithm that can correctly identify cracks

- Classification of different sizes and types of cracks

## Code

`LoadImage.py`: Loads in an image and cuts it into equally sized squares. To run this code,
you need to have a `data\` folder containing the image file.

`SaveCutImages.py`: Takes the image dictionary loaded in by `LoadImage.py` and saves each cut
to its own .tif file. To run this code, you need to have a `results\` folder.
