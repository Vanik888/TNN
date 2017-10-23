### Basic comands to generate inputs, outputs and weights
* Generating inputs, outputs and weights
```
python2.7 file_generator.py -w -i -P EXAMPLES_COUNT -M OUTPUTS_COUNT -N
INPUTS_COUNT
```

* Generating only inputs and outputs
```
python2.7 file_generator.py -i -P EXAMPLES_COUNT -M OUTPUTS_COUNT -N INPUTS_COUNT
```

* Generating only weights
```
python2.7 file_generator.py -w -P EXAMPLES_COUNT -M OUTPUTS_COUNT -N INPUTS_COUNT
```

### Comands to start network
* calculate weights and exit
```
python2.7 main.py
```
* calculate weights and draw errors graph (initial weights would be generated during start of script)
```
python2.7 main.py --draw_errors
```

* calculate weights and draw errors graph (initial weights would be read from file PA-A-weights.dat)
```
python2.7 main.py --draw_errors --read_weights
```