# De-identifing Program 

This is a Python program for dealing with masking specific columns of dataset.


## Example Code

```shellscript
python main.py --path data/caschool.csv --cols county district --save masked/caschool.csv --mapping masked/mapping_caschool.csv
```

```
python main.py --path data/BostonHousing.csv --cols rad --save masked/BostonHousing.csv --mapping masked/mapping_Boston.csv  
```

## Options

* `--path`, `-p` : path of target data
* `--cols`, `-c`: de-identifying target column
* `--prefix` : prefix of masked data
* `--save` : path of masked dataset
* `--mapping` : path of mapping table

## Author

[Yoonsik Jung](https://yoonsik-jung-opt.github.io/) (Mathematical Optimization and Operations Research Lab., Korea Univ)
ys_jung@korea.ac.kr

## License

Commercial usage is not allowed