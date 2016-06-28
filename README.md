# Pigeonhole Heuristic 
A heuristic for the pigeonhole problem implemented using the Python
heuristic interface of [WASP](https://github.com/alviano/wasp).

## Usage
Use the heuristic together with [WASP](https://github.com/alviano/wasp)
on the `plugins` branch, compiled with `make SCRIPT=python`. To run the
heuristic on the sample instance, execute
```shell
# ground the instance
gringo pigeonhole-encoding.lp pigeonhole-sample-instance.lp > sample.gringo
# call the solver using the python heuristic 
cat sample.gringo | wasp --heuristic-interpreter=python --heuristic-scriptname=heuristic
```
