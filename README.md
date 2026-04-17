# BachRNN - Bach chorales
Bach Chorales with RNN for Music Generation

<table align="center">
  <tr>
    <td align="center" style="padding-right: 12px;">
      <img src="https://github.com/user-attachments/assets/a8eeecfe-4bf8-4a3d-b02f-b7707219a122" height="300">
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/082075ba-2b70-4da4-8216-6118912aed0d" height="300">
    </td>
  </tr>
</table>

### Project Overview

This project focuses on analyzing and generating Bach-style chorales with rnn. I used the JSB Chorales dataset to study four-part harmony. And main idea is detecting the key of each chorale, and train an LSTM-based model to predict the next chord step by step. The goal of the project is to comine music theory and ai in a practical way. We analyze tonal structure with a classical music theory method. On the other side, we train a neural network to learn harmonic patterns and generate new chorale-like music.

### Why this project and What is the algorithm?

I did this project to understand how musical structure can be learned from data. Bach chorales are a very good dataset for this because they are harmonically rich.

The project has two main parts. The first part is key detection. I used the Krumhansl-Schmuckler key-finding algorithm to estimate the tonal center of a chorale. The second part is using RNN and music generation. I preprocess the chorales into fixed-length windows, normalize the MIDI and predicts the next notes for the four voices. The generated output is then converted back into MIDI format. The Krumhansl-Schmuckler algorithm is a rule-based method for identifying the key of a musical piece. It works by comparing the distribution of pitch classes in the music with predefined tonal profiles for major and minor keys. A pitch class means the note name without considering octave, so all C notes belong to the same class, all D notes belong to another class, and so on. The algorithm calculates how well the note distribution matches each possible key and selects the one with the highest score.

### How Krumhansl-Schmuckler key-finding algorithm works

First, the notes in a chorale are converted into pitch classes. Then a pitch-class distribution vector is built by counting how often each pitch class appears. After that, this vector is compared with major and minor tonal profiles using convolution-like scoring. The score is calculated for all 12 major and 12 minor keys. The key with the highest score is taken as the detected key of the chorale.

For generation, each chorale is divided into overlapping note windows. These windows become training examples. The LSTM learns temporal relationships between notes across time and across the four voices. During generation, the model predicts the next step repeatedly, starting from a seed sequence, until a full new chorale is created.

The general idea of the key-finding score is:

Score(k) = sum over i of Profile(i) × Distribution((i + k) mod 12)

Here, the pitch - class distribution of the piece is compared with a shifted major or minor key profile. The shift represents each possible tonic. The highest score gives the most likely key.



<img width="666" height="372" alt="Ekran Resmi 2026-04-16 20 42 01" src="https://github.com/user-attachments/assets/c84c4201-ef6b-408d-b2ae-f9cb4af4b52a" />

<img width="668" height="336" alt="Ekran Resmi 2026-04-16 20 42 12" src="https://github.com/user-attachments/assets/de9ac560-faab-4421-903a-0369d8378048" />

<img width="669" height="443" alt="Ekran Resmi 2026-04-16 20 42 24" src="https://github.com/user-attachments/assets/bff33549-c8b2-4f0e-a98f-e7836e13b9e9" />

<img width="670" height="312" alt="Ekran Resmi 2026-04-16 20 42 38" src="https://github.com/user-attachments/assets/442eabcd-0418-4be2-8f03-de8848a01954" />

<img width="744" height="633" alt="Ekran Resmi 2026-04-16 20 42 55" src="https://github.com/user-attachments/assets/a3524304-4126-44e9-b6f9-94ad5ef28443" />

.midi file converter -> https://miditoolbox.com/player

Google COCONET Magenta (the ML model that harmonizes melodies in a style of Bach chorales) -> https://magenta.tensorflow.org/coconet

midi library -> https://craffel.github.io/pretty-midi/instrument.html
