#! /usr/bin/env python3
"""
mereni2
"""

import sys
import matplotlib.pyplot

def main():
    """ main """
    input_file = sys.argv[1]
    input_file_obj = open(input_file, 'r')

    if not input_file_obj:
        print("file %s not found", input_file)
        exit(1)

    pure_data = input_file_obj.read()

    data = {}
    data['x'] = []
    data['y'] = []

    for line in pure_data.split('\n'):
        if not line:
            continue

        columns = line.split(';')
        data['x'].append(columns[0])
        data['y'].append(columns[1])

    print(data['x'])
    print(data['y'])
    matplotlib.pyplot.plot(data['x'], data['y'], 'ro')
    matplotlib.pyplot.axis([0, 21, 0, 19])
    matplotlib.pyplot.show()

if __name__ == '__main__':
    main()
