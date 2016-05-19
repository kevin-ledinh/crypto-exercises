import gmpy2
import sys as Sys
from gmpy2 import mpz
#from sets import Set


def printProgress (iteration, total, prefix = '', suffix = '', decimals = 2, barLength = 100):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
    """
    filledLength    = int(round(barLength * iteration / float(total)))
    percents        = round(100.00 * (iteration / float(total)), decimals)
    bar             = '#' * filledLength + '-' * (barLength - filledLength)
    Sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, percents, '%', suffix)),
    Sys.stdout.flush()
    if iteration == total:
        print("\n")
    return


p='13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171'

g='11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568'

h='3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333'

B = 2 ** 20
x1 = 0
x0 = 0
list1 = []

print "mpz(p).num_digits(): {}".format( mpz(p).num_digits() )
print "mpz(g).num_digits(): {}".format( mpz(g).num_digits() )
print "mpz(h).num_digits(): {}".format( mpz(h).num_digits() )

print "p is prime: {}".format( gmpy2.is_prime( mpz( p ) ) )
print "gcd( p, g ): {}".format( gmpy2.gcd( mpz( p ) , mpz( g ) ) )

print("Build x1 table ...")

# Populate a list of ( h / ( g ^ x0 ) ) values
for x1 in range( 0 , B ):
    # calculate ( g ^ x0 )
    g_Pow_x1 = pow( mpz( g ) , x1 , mpz( p ) )
    #print "{} {}".format("g_Pow_x0: ", g_Pow_x0 )

    # calculate inverse of ( g ^ x0 ) using Fermat's formular
    g_Pow_x1_inv = pow( mpz( g_Pow_x1 ) , mpz( p ) - 2 , mpz( p ) )
    #print "{} {}".format("g_Pow_x0_inv: ", g_Pow_x0_inv )

    # check that the inverse is correct
    #product = gmpy2.f_divmod( mpz( g_Pow_x0 ) * mpz( g_Pow_x0_inv ) , mpz( p ) )
    #print "{} {}".format("remainder: ", product[1] )

    # calculate h / ( g ^ x0 )
    # result = h * g_Pow_x0_inv
    result = gmpy2.f_divmod( mpz( h ) * mpz( g_Pow_x1_inv ) , mpz( p ) )
    list1.append( result[1] )
    #print "{} {}".format("h / ( g ^ x0 ) mod p: ", result[1] )
    printProgress( x1 , B , prefix = 'Progress:', suffix = 'Complete', barLength = 50 )

print("\n")
print "{} {}".format("list1 len: ", len( list1 ) )
print("Find x0 in x1 table ...")

# Compare the list of ( h / ( g ^ x0 ) ) values
for x0 in range( 0 , B ):
    # Compute ( B * x0 )
    temp = mpz( x0 ) * B

    # Compute ( g ^ ( x0 * B ) )
    result = pow( mpz( g ) , mpz( temp ) , mpz( p ) )

    printProgress( x0 , B , prefix = 'Progress:', suffix = 'Complete', barLength = 50 )
    try:    
        x1 = list1.index( result )
    except ValueError:
        continue
    else:
        print("\n")
        print "x0: {} - x1: {}".format( x0, x1 )
        break       

x = mpz( x0 ) * B + mpz( x1 )
print "x00 * B + x1 = {}".format( mpz( x ) )
print "( g * x ) mod p = {}".format( pow( mpz( g ) , mpz( x ) , mpz( p ) ) )

