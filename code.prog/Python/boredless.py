Python 3.7.6 (default, Dec 30 2019, 19:38:28) 
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable. Visit
http://www.python.org/download/mac/tcltk/ for current information.
>>> destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'Sao Paolo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index
