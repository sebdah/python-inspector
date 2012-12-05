python-call-inspector
=====================

This module helps you to track down which Python method that called your method.
It can be helpful when debugging code in some situations. All you need to do
is to import the module to your project and call `inspector.trace()` (and 
catch the output rows).

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

The `trace` function takes the following parameters:

#### Input parameters

***depth*** (default: `0`)
How many calls back do you want to dump? `0` will return all calls.

***one_line_response*** (default: `False`)
By default the `trace` will return multiple lines. You can turn that behavior
off by setting this to `True`.

#### Return data

The method returns a list of log lines (strings). I.e. `[str, str ...]`

## Release notes

### 0.1 (2012-12-05)

- Initial release
