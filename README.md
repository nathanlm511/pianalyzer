# Pianalyzer

A simple flask web app that classifies piano music using a convolutional neural network that analyzes midi notes.

Try out the application [here](https://aqueous-bastion-23196.herokuapp.com/)!

## How It Works 
1. The midi file is converted to JSON by the third party javascript library [midi-parser-js](https://github.com/colxi/midi-parser-js)
2. The JSON is then manually converted into an image with pitch on the y-axis and time on the x-axis
3. The image can then be passed through a previously trained Keras model that classifies the image

## The ML Model
The model uses a blah blah blah

