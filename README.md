# graphing-script

Download the script and make it executable (chmod +x graph_script.py).

You can then run ./graph_script.py --help to see the options available.

```bash

Jim@Jim-Laptop:~/scripts$ ./graph_script.py --help
usage: graph_script.py [-h] [-t TITLE] FILE plottype group dep output

positional arguments:
  FILE                  The input datafile
  plottype              The type of plot
  group                 The groups that you would like to sort by.
  dep                   The dependent variable you wish to graph.
  output                The desired output filename. Please include the
                        extension.

optional arguments:
  -h, --help            show this help message and exit
  -t TITLE, --title TITLE
                        The title of your figure.
                        
```                        
