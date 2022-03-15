## Hate Speech Analysis with HappyTransformer

## Introduction

Hate speech covers many forms of expressions which advocate, incite, promote or justify hatred, violence and discrimination against a person or group of persons for a variety of reasons. It poses grave dangers for the cohesion of a democratic society, the protection of human rights and the rule of law.

This is an artificial intelligence based tool that is designed to analyze hate speeches in real-time audios and texts.

In recent years, the increasing propagation of hate speech on social media and the urgent need for effective countermeasures have drawn significant investment from governments, companies, and researchers. A large number of methods have
been developed for automated hate speech detection online. This aims to classify textual content into non-hate or hate speech.


![](github-readme-content/banner-image.png)


## Features
- Analyze hate speech in real-time audios.
- Analyze hate speech in texts data.


## Technologies & Frameworks

- Python 3.8
- happytransformer
- pyperclip
- pynput
- mysql_connector
- speech_recognition


### What is happytransformer?

Happy Transformer is a package built on top of Hugging Face's transformer library that makes it easy to utilize state-of-the-art NLP models.

### What is pyperclip?

Pyperclip is a cross-platform Python module for copy and paste clipboard functions. It works with Python 2 and 3. Install on Windows: pip install pyperclip. Install on Linux/macOS: pip3 install pyperclip.

### What is pynput?

The pynput library allows you to control and monitor/listen to your input devices such as they keyboard and mouse. The pynput. mouse allows you control and monitor the mouse, while the pynput. keyboard allows you to control and monitor the keyboard.

### mysql_connector?

MySQL Connector/Python is a standardized database driver for Python platforms and development. Additionally, MySQL Connector/Python 8.0 supports the new X DevAPI for development with MySQL Server 8.0.


## Architecture & Model

This hate speech detection system is using a happytransformer framework form Hugging-Face AI community.

As a hate speech classification model, we are using the "Hate-speech-CNERG/dehatebert-mono-english" BERT pre-trained model to do the hate speech analysis, it is an open-source model.

![](github-readme-content/hsmodel.jpg)

Model Link:- [dehatebert-mono-english](https://huggingface.co/Hate-speech-CNERG/dehatebert-mono-english)

### What is a BERT model?

BERT is an open source machine learning framework for natural language processing (NLP). BERT is designed to help computers understand the meaning of ambiguous language in text by using surrounding text to establish context. The BERT framework was pre-trained using text from Wikipedia and can be fine-tuned with question and answer datasets.

BERT, which stands for Bidirectional Encoder Representations from Transformers, is based on Transformers, a deep learning model in which every output element is connected to every input element, and the weightings between them are dynamically calculated based upon their connection.


### What is a HuggingFaces?

The AI community building the future, build, train and deploy state of the art models powered by the reference open source in machine learning.

## Hate Speech Detection System

In this repository, there are two different types of applications are available. Those are "00-real-time-audio-processing" and "01-text-processing-copy-paste-method", both applications depends on "Hate-speech-CNERG/dehatebert-mono-english" BERT model.
