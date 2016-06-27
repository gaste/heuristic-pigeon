# Pigeonhole Heuristic 
A heuristic for the pigeonhole problem implemented using the Python heuristic
interface of [WASP](https://github.com/alviano/wasp).

## Usage
Use the heuristic together with [HWASP](https://github.com/Yarrick13/hwasp)
on the heuristic branch. To run the heuristic on the sample instance, execute
```
gringo pigeonhole-encoding.asp pigeonhole-sample-instance.asp | hwasp --heuristic-interpreter=python --heuristic-scriptname=heuristic
```
