# Space Oddity

In this guide you will find all you need to setup the environment and be able to play this game.

## Install OpenAL Soft

PyOpenAL requires the shared OpenAL library. Follow the steps below for Mac OS:

1. Go to [this](https://openal-soft.org) link and download the latest OpenAL Soft release in source form.
2. Download [CMake](https://cmake.org/download/) in your computer.
3. Extract the sources.
4. Using your favorite shell, go into the build/ directory, and run:

   ```
   cmake ..
   ```

5. After the previous step is finished, you can then build it, typically using GNU Make:

   ```
   make
   ```

   ```
   make install
   ```

## Install PyOpenAL

To install PyOpenAL we recommend creating an isolated environment for this project using a python virtual environment.

### Setup virtual environment

Follow the steps below to create and activate your virtual environment for this project.

1. Once you have downloaded the project's [folder](https://github.com/elkinnarvaez/space-oddity/archive/refs/heads/master.zip), go inside that folder.

   ```
   cd space-oddity
   ```

2. Create the environment (if you already did, please go to the next step)

   ```
   pip install virtualenv
   ```

   ```
   mkdir env
   ```

   ```
   virtualenv env
   ```

3. Initialize environemnt

   ```
   source env/bin/activate
   ```

### Install library

To install PyOpenAL you can use pip.

```
pip install PyOpenAL
```

## Download sounds

The sounds are a little bit big in size, so we have located them outside this repository. You can download them from [here](https://www.dropbox.com/sh/myas2x5rosyptra/AACQHzOMwTWYZSu8vGaTtB0ca?dl=0). Once you have downloaded them, please place the sound's folder inside the project's folder.

## Run program

Type the following command in your terminal to run the program and start the game.

```
python space-oddity.py
```
