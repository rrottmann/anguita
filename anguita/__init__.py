'''
Fast approximation of tanh with good enough results.

Written by Reiner Rottmann <reiner AT rottmann.it>
Released under MIT License
'''
import math

def tanh(x):
    '''
     tanh(x)

        Return the hyperbolic tangent of x.

    Efficient tanh algorithm using an approximation of the Hyperbolic function:

    Speed Improvement of the Back-Propagation on Current Generation
    Workstations" D. Anguita, G. Parodi and R. Zunino. Proceedings of the World
    Congress on Neural Networking, 1993.
    '''
    if x > 1.92033:
        return 0.96016
    if x > 0:
        return 0.96016 - 0.26037 * (x - 1.92033) * (x - 1.92033)
    if x <= -1.92033:
        return -0.96016
    if x < 0:
        return 0.26037 * (x + 1.92033) * (x + 1.92033) - 0.96016

def compare():
    '''
    Compare the math.tanh with anguita.tanh with values from -1..1
    '''
    print 'The approximation of tanh is not precise, but much faster:'
    print '\t'.join(['x', 'math.tanh', 'anguita.tanh', 'delta'])
    for x in [x * 0.1 for x in range(-10, 10)][1:]:
        if x == 0:
            continue
        accurate = math.tanh(x)
        approx = tanh(x)
        delta = accurate - approx
        print '\t'.join([str(x), str(accurate), str(approx), str(delta)])

if __name__ == '__main__':
    compare()
