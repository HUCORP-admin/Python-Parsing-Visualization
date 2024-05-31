import re


# constants
UART_PATTERN = r'<inf> main: (?P<sensor>.*),(?P<reading>.*),(?P<value>[-+]?\d*\.\d+|\d+),(?P<timestamp>\d+)'


def time_to_duration(t, b):
    return (t - b)/1000

def parse_serial(file):
    data = []
    with open(file, 'r') as f:
        base = 0
        for line in f.readlines():
            match = re.search(UART_PATTERN, line)
            if match:
                # extract values
                sensor = match.group('sensor')
                reading = match.group('reading')
                value = float(match.group('value'))
                timestamp = int(match.group('timestamp'))

                # specify base time
                if not data:
                    base = timestamp

                # store values in data
                time = time_to_duration(timestamp, base)
                row = {'sensor': sensor, 'reading': reading, 'value': value, 'time': time}
                data.append(row)

    return data