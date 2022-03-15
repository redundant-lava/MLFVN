# MLFVN
MLF Visual Novel is built using Ren'Py. See the [Ren'Py Documentation](https://www.renpy.org/doc/html/index.html) for more information

## Current Build
The MLF Visual Novel is still in development. To run the most recent build, download the zip file for your system:  
>[mlfvn-1.0-pc.zip](https://github.com/redundant-lava/MLFVN/blob/main/mlfvn-1.0-pc.zip) for Windows and Linux Systems.  
>[mlfvn-1.0-mac.zip](https://github.com/redundant-lava/MLFVN/blob/main/mlfvn-1.0-mac.zip) for Mac. 

## Explanation of Files
All game files are in the `game` folder

### Script
`script.rpy` is the frame file that contains all the setup code for the VN script, and links to the next chapter
#### Endings
The VN currently supports four possible endings:  
- `true_ending.rpy` is the true ending of the VN.  
- `bad_ending.rpy` contains two variations of the bad ending.  
- `happy_ending.rpy` contains two varations of the happy ending.   
- `neutral_ending.rpy` contains a neutral ending.  

There should be no return statements in the ending files as they should all jump back to the `ending_screen` label in the main script file.

#### Chapters
Each chapter is in its own `.rpy` file, titled `ch_##.rpy` where ## is the chapter number.  
Each chapter starts with a `label ch_##:` and ends with a `jump` to the next chapter. There should be no return statements in the chapter files as all game endings should direct to the appropriate ending file and then the ending screen.

#### Branches
- Wine Aunt Branch - *not implemented*

### Visual Assets
Backgrounds and Character Sprites are located in `game/images`.  There are limitted original assets complete at this time. Placeholder assets are all black and white and marked "PLACEHOLDER" (14.03.2022)

### User Interface
Files related to the GUI are in `game/gui`.  

### Custom Game Mechanics
Currently all custom game mechanics are handled within the script file.  
#### Character Metrics
*Affection Meter*
stored in global variable `aff`.  
*Amnesia Meter*
Stored in global variable `amn`.  
*Luka Affection Meter*
Stored in global variable `Laff`. 

#### Decision History
*not implemented*
#### Animations and Transitions
*not implemented*

## Contact Developers
email redundantlava@gmail.com if you are intereseted in helping with the code implementation of this VN.

