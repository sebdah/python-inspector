"""
Python inspector used to simply find out which Python method and line that 
called 'your' method.
"""

import os
import inspect

def trace(depth=0, one_line_response=False, basename_only=False):
    """
    Trace the current method call and return an array of log lines

    depth::
        How many deep do you want to dig, i.e. how many callers to show
        Set to 0 to get all
    one_line_response::
        Write the response log lines on one row
    basename_only::
        If this is True, then only return the filename, not the path
    """
    data = []
    inspector = inspect.getouterframes(inspect.currentframe())
    current_depth = 0
    for i in range(2, len(inspector)):
        # Do only recurse to the given depth
        if current_depth >= depth and depth != 0:
            break
        current_depth += 1

        # Do the actual inspection
        # _ number 1 is the frame
        # _ number 2 is the index
        _, filename, line_no, function_name, lines, _ = inspector[i]

        # Only print the filename
        if basename_only:
            filename = os.path.basename(filename)

        if one_line_response:
            log = '%(filename)s:%(line_no)i in method %(function_name)s: ' % {
                'filename': filename,
                'line_no': line_no,
                'function_name': function_name,
            }
            log += str(('\t%s' % lines[0].strip()).rstrip('\n'))
        else:
            log = '%(filename)s:%(line_no)i in method %(function_name)s' % {
                'filename': filename,
                'line_no': line_no,
                'function_name': function_name,
            }

            for line in lines:
                log += ('\n\t%s' % line.strip()).rstrip('\n')

        data.append(log)

    return data
