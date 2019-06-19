## About

This commandline utility converts time tracking reports exported by toggl as csv into a simple csv list with the time in decimal hour format.

### Usage
```
usage: csvformat.py [-h] [-o O] inputfile

Convert toggl time HH:MM:SS to hour decimal format.

positional arguments:
  inputfile   Path to the input file (.csv)

  optional arguments:
    -h, --help  show this help message and exit
      -o O        name of the output file

python csvformat.py reportlist_graveyardshift.csv -o tasks_gys_hours.csv
```

#### Example input
```
Project,Client,Title,Duration
Graveyard shift,CrustyCrab,Make burgers,05:28:15
Graveyard shift,CrustyCrab,Clean toilets,00:23:29
Graveyard shift,CrustyCrab,Mop floors,02:37:22
Graveyard shift,CrustyCrab,Mop ceiling,02:35:44
Graveyard shift,CrustyCrab,Hear scary story,00:54:55
...

```

#### Example output
```

Make burgers,5.48
Clean toilets,0.4
Mop floors,2.63
Mop ceiling,2.6
Hear scary story,0.92
...
```
