# Midi to mindustry code converter
## How to use
### 1. Install software
    1. Python3 (https://www.python.org/downloads/)
    2. Mido library (pip install mido)
    3. Pathlib library (pip install pathlib)
    4. Mindustry (https://github.com/Anuken/Mindustry/releases)
    5. BetaMindy mod for Mindustry (https://github.com/sk7725/BetaMindy/releases) (you can download it from the game)
### 2. Get mid
Just find it in internet. But if anything, it would be better if the song was played purely on 1 instrument, and the piano would be best.
And place it to midi folder, btw
### 3. Decode midi
    1. Use [python3 main.py]
    2. Type 1
    3. Type mid file name without .mid
    4. Wait for the end of decoding (time depends on the number of notes in the mid)
### 4. Convert to mindustry cpu code™
    1. Use [python3 main.py] (or dont, if you didnt kill the previos one)
    2. Type 2
    3. Type file name of decoded mid without .mid
    4. Type channel to use (mostly 0, but sometimes it can be different - you can find it by looking on console, while your mid is beeing decode; if your mid uses more than 1 channel, repeat theese actions for evry channel)
### 5. Paste the cpu code™ into mindustry
    1. Open result folder, open foler with name of your midi, and open file with needed channel
    2. Copy all code (if it is longer, than 1000 strs, go to known issues)
    3. Open mindustry, place cpu then (tier 2-3), music block, and connect cpu with music block
    4. Enjoy music!

## Known bugs and issues
### My mid have many instruments, what i have to do?
    1. Repeat actions from 4th paragraph for every channel (if you haven't done so yet)
    2. Repeat actions from 5th paragraph for every channel (for evry cpu you may have personal music block; also you have to sync all of the cpus, you can do it with t3 cpus by don't give them cryogenics, and activating them by giving them cryogenics all at once)
    3. Select needed instrument for every cpu
    4. Enjoy better music!

### My cpu code™ is longer than 100 strs, what i have to do?
Mindustry cpus usually have 1000 strs limit, and so:
If it is near 1000 strs, you can just ignore it, you will lost small part of song.
If it is much more than 1000 strs, you should wait some time, when dev of this strange programm will make full guide for it.

### I dont undetstand steps about mindustry, what i have to do?
I intended this program to be for those who are familiar with the minds of the minds, but if you don't know what it is, you can try this game.
If you don't understand something at all, you can write to known iusses and post your problem there.
