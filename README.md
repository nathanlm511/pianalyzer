# Pianalyzer

Pianalyzer is a simple flask web app that classifies piano music using a midi-note-analyzing convolutional neural network. It is hosted on Heroku, so it might run a bit slow, but it is quite accurate :)

![Pianalyzer cover photo](https://github.com/nathanlm511/pianalyzer/blob/master/static/images/pianalyze.PNG "Cover Photo")

Try out the application [here](https://aqueous-bastion-23196.herokuapp.com/)!

## How It Works 
1. The midi file is converted to JSON by the third party javascript library [midi-parser-js](https://github.com/colxi/midi-parser-js)
2. The JSON is then manually converted into an image with pitch on the y-axis and time on the x-axis
3. The image can then be passed through a trained Keras model that classifies the image
4. The requests between the front and back end are handled using Flask and Ajax
<p align="center">
  <img src="https://github.com/nathanlm511/pianalyzer/blob/master/static/images/chpn-p12.mid.json.jpg" />
</p>
<p align="center">
  Chopin's Prelude No. 12
</p>

## The ML Model
The model uses four 2D convolution layers to recognize broad and specific patterns in the notes such as chords or extensions. To train the model, a moderately small datset of 300 classical pieces and 300 jazz pieces was used. However, the model's validation accuracy was around 99%. In the future, more analysis needs to be done to decide if the model is overfit.
