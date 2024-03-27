# Classify Radio Signals from Outer Space with Keras

![Allen Telescope](Allen_Telescope.jpg)

[Allen Telescope Array](https://flickr.com/photos/93452909@N00/5656086917) by [brewbooks](https://www.flickr.com/people/93452909@N00) is licensed under [CC BY 2.0](https://creativecommons.org/licenses/by/2.0/)

[Coursera Project Link](https://www.coursera.org/projects/classify-radio-signals-space-keras-cnn)

This project demonstrates the process of using a Convolutional Neural Network (CNN) to classify space signals into four categories: "squiggle", "narrowband", "noise", and "narrowbanddrd".

## Setup Instructions

- Create a virtual environment.
- Unzip `dataset.zip`.
- Activate the virtual environment and install dependencies:

```sh
.venv\Scripts\Activate.ps1
pip install --upgrade pip ipykernel scikit-learn tensorflow pandas numpy matplotlib seaborn livelossplot
pip freeze > requirements.txt
```

## Training Process

The training involves the following steps:

### Step 1: Import Libraries

- Essential libraries and modules are imported.
- TensorFlow's version is printed to ensure compatibility.

### Step 2: Load and Preprocess SETI Data

- The SETI dataset, transformed into images, is loaded.
- Data is reshaped to fit the model requirements.

### Step 3: Plot 2D Spectrograms

- Spectrograms of the signals are plotted to visualize the data.

### Step 4: Create Training and Validation Data Generators

- ImageDataGenerators are used for data augmentation to improve model robustness.

### Step 5: CNN Architecture

- The CNN model is defined with layers designed to capture spatial hierarchies in the data.

### Step 6: Schedule Learning Rate and Compile Model

- An exponential decay learning rate schedule is implemented.
- The model is compiled with the Adam optimizer.

### Step 7: Callbacks

- Callbacks including model checkpointing and plot losses are set up to monitor training.

### Step 8: Model Training

- The model is trained using the defined data generators and callbacks.

### Step 9: Model Evaluation, Prediction, Classification Report

- The model's performance is evaluated on a validation set.
- A classification report and confusion matrix provide detailed performance metrics.

## Conclusion

This project outlines a comprehensive approach to classifying radio signals from space using a CNN with Keras. It covers the end-to-end process, from data preprocessing and model definition to training, evaluation, and interpretation of results.
