python-inspector
================

<a href='https://travis-ci.org/sebdah/python_inspector'><img src='https://secure.travis-ci.org/sebdah/python_inspector.png?branch=master'></a>

This module helps you to track down which Python method that called your method.
It can be helpful when debugging code in some situations. All you need to do
is to import the module to your project and call `inspector.trace()` (and 
catch the output rows).

## Installation

The `python-inspector` is available trough `pip`, simple run

    pip install python-inspector

## Requirements

Python version >2.5 and <3.0

## Example usage

Here's a simple example usage of the `inspector`

	#!/usr/bin/env python

	"""
	Testing the Python call inspector
	"""
	import sys
	import inspector

	def func2():
	    """
	    Example method
	    """
	    # This is the method you want to debug

	    # Your code here

	    print 'TRACE OUTPUT:'
	    for log_row in inspector.trace():
	        print log_row

	    # More code
	    
	    return True

	def func1():
	    """
	    Example method
	    """
	    return func2()

	def call_me():
	    """
	    Call this function to test
	    """
	    return func1()

	call_me()

	sys.exit(0)

In this example we debug `func2()` using the `inspector`. The output generated
will look like this:

	TRACE OUTPUT:
	t.py:29 in method func1
		return func2()
	t.py:35 in method call_me
		return func1()
	t.py:37 in method <module>
		call_me()

## Documentation for `inspector`

The `inspector` module is really simple and does only contain one function, 
`trace`.

### Function `trace`

The docstring explains this pretty well.

	Trace the current method call and return an array of log lines

    Kwargs:
        depth (int)::
            How many deep do you want to dig, i.e. how many callers to show.
            Set to 0 to get all calls. (default 0)
        one_line_response (bool)::
            Write the response log lines on one row (default False)
        basename_only::
            Return the filename without path (default False)

    Returns:
        List of strings (loglines), [str, str..]

#### Return data

The method returns a list of log lines (strings). I.e. `[str, str ...]`

## Release notes

### 0.2.0 (2013-01-07)

- Made the script available under Apache license 2.0
- Added `python-inspector` to `pip`

### 0.1.0 (2012-12-05)

- Initial release
