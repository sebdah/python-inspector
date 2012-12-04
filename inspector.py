"""
Python inspector used to simply find out which Python method and line that 
called 'your' method.
"""

import inspect

class Inspector:
    """
    Inspector class
    """
    def __init__(self):
        """
        Constructor
        """
        pass

    def inspect(self, depth=0):
        """
        Inspect the current method and return an array of log lines

        depth:  How many deep do you want to dig, i.e. how many callers to show
                Set to 0 to get all
        """
        data = []
        inspector = inspect.getouterframes(inspect.currentframe())
        current_depth = 0
        for i in range(1, len(inspector)):
            # Do only recurse to the given depth
            if current_depth >= depth and depth != 0:
                break
            current_depth += 1

            # Do the actual inspection
            # _ number 1 is the frame
            # _ number 2 is the index
            _, filename, line_no, function_name, lines, _ = inspector[i]
            log = '%(filename)s:%(line_no)i in method %(function_name)s' % {
                'filename': filename,
                'line_no': line_no,
                'function_name': function_name,
            }

            for line in lines:
                log += ('\n\t%s' % line.strip()).rstrip('\n')

            data.append(log)

        return data
