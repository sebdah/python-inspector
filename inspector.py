"""
Python inspector used to simply find out which Python method and line that 
called 'your' method.
"""

import inspect

def trace(depth=0, one_line_response=False):
    """
    Trace the current method call and return an array of log lines

    depth::
        How many deep do you want to dig, i.e. how many callers to show
        Set to 0 to get all
    one_line_response::
        Write the response log lines on one row
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
