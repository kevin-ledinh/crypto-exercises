import urllib2
import sys

TARGET = 'http://crypto-class.appspot.com/po?er='

iv = [ 0xf2, 0x0b, 0xdb, 0xa6, 0xff, 0x29, 0xee, 0xd7, 0xb0, 0x46, 0xd1, 0xdf, 0x9f, 0xb7, 0x00, 0x00 ]
c1 = [ 0xf2, 0x0b, 0xdb, 0xa6, 0xff, 0x29, 0xee, 0xd7, 0xb0, 0x46, 0xd1, 0xdf, 0x9f, 0xb7, 0x00, 0x00 ]
c2 = [ 0x58, 0xb1, 0xff, 0xb4, 0x21, 0x0a, 0x58, 0x0f, 0x74, 0x8b, 0x4a, 0xc7, 0x14, 0xc0, 0x01, 0xbd ]
c3 = [ 0xbd, 0xf3, 0x02, 0x93, 0x62, 0x66, 0x92, 0x6f, 0xf3, 0x7d, 0xbf, 0x70, 0x35, 0xd5, 0xee, 0xb4 ]
temp = [ 0xf2, 0x0b, 0xdb, 0xa6, 0xff, 0x29, 0xee, 0xd7, 0xb0, 0x46, 0xd1, 0xdf, 0x9f, 0xb7, 0x00, 0x00 ]
guess_ = [ 0x12, 0x34, 0x56, 0x78, 0x90, 0x9a, 0xba, 0x7f, 0xde, 0x6e, 0x5a, 0x1a, 0x95, 0x29, 0x56, 0x45 ]

#f20bdba6ff29eed7b046d1df9fb70000
#58b1ffb4210a580f748b4ac714c001bd
#4a61044426fb515dad3f21f18aa577c0
#bdf302936266926ff37dbf7035d5eeb4
#c1 = [ 0x58, 0xb1, 0xff, 0xb4, 0x21, 0x0a, 0x58, 0x0f, 0x74, 0x8b, 0x4a, 0xc7, 0x14, 0xc0, 0x01, 0xbd ]
#c2 = [ 0x4a, 0x61, 0x04, 0x44, 0x26, 0xfb, 0x51, 0x5d, 0xad, 0x3f, 0x21, 0xf1, 0x8a, 0xa5, 0x77, 0xc0 ]
#c3 = [ 0xbd, 0xf3, 0x02, 0x93, 0x62, 0x66, 0x92, 0x6f, 0xf3, 0x7d, 0xbf, 0x70, 0x35, 0xd5, 0xee, 0xb4 ]

#--------------------------------------------------------------
# padding oracle
#--------------------------------------------------------------
class PaddingOracle(object):
    def query(self, q):
        target = TARGET + urllib2.quote(q)    # Create query URL
        req = urllib2.Request(target)         # Send HTTP request to server
        try:
            f = urllib2.urlopen(req)          # Wait for response
        except urllib2.HTTPError, e:          
            #print "We got: %d" % e.code       # Print response code
            if e.code == 404:
                return True # good padding
            return False # bad padding


def createArg(iv_, c1_, c2_):
    #joinStr = "".join([chr(x) for (x) in iv_])
    joinStr = "".join([chr(x) for (x) in c1_])
    joinStr += "".join([chr(x) for (x) in c2_])
    return joinStr

if __name__ == "__main__":
    po = PaddingOracle()

    index = len( c1 ) - 1

    #print c1
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x01
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break
    
    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 
    #print c1
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x02
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x02
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x03
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x03
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x03
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x04
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x04
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x04
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x04
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x05
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x05
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x05
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x05
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x05
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x06
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x06
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x06
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x06
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x06
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x06
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x07
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x07
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x07
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x07
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x07
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x07
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x07
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x08
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x08
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x08
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x08
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x08
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x08
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x08
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x08
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x09
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x09
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x09
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x09
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x09
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x09
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x09
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x09
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x09
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0a
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0a
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0a
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0a
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0a
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0a
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0a
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0a
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0a
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0a
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x0b
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0b
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0b
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0b
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0b
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0b
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0b
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0b
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0b
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0b
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0b
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 11 ] = c1[ index + 11 ] ^ guess_[ index + 11 ] ^ 0x0c
    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x0c
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0c
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0c
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0c
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0c
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0c
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0c
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0c
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0c
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0c
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0c
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 12 ] = c1[ index + 12 ] ^ guess_[ index + 12 ] ^ 0x0d
    temp[ index + 11 ] = c1[ index + 11 ] ^ guess_[ index + 11 ] ^ 0x0d
    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x0d
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0d
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0d
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0d
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0d
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0d
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0d
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0d
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0d
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0d
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0d
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 13 ] = c1[ index + 13 ] ^ guess_[ index + 13 ] ^ 0x0e
    temp[ index + 12 ] = c1[ index + 12 ] ^ guess_[ index + 12 ] ^ 0x0e
    temp[ index + 11 ] = c1[ index + 11 ] ^ guess_[ index + 11 ] ^ 0x0e
    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x0e
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0e
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0e
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0e
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0e
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0e
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0e
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0e
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0e
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0e
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0e
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 14 ] = c1[ index + 14 ] ^ guess_[ index + 14 ] ^ 0x0f
    temp[ index + 13 ] = c1[ index + 13 ] ^ guess_[ index + 13 ] ^ 0x0f
    temp[ index + 12 ] = c1[ index + 12 ] ^ guess_[ index + 12 ] ^ 0x0f
    temp[ index + 11 ] = c1[ index + 11 ] ^ guess_[ index + 11 ] ^ 0x0f
    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x0f
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x0f
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x0f
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x0f
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x0f
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x0f
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x0f
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x0f
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x0f
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x0f
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x0f
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )
    index = index - 1 

    temp[ index + 15 ] = c1[ index + 15 ] ^ guess_[ index + 15 ] ^ 0x10
    temp[ index + 14 ] = c1[ index + 14 ] ^ guess_[ index + 14 ] ^ 0x10
    temp[ index + 13 ] = c1[ index + 13 ] ^ guess_[ index + 13 ] ^ 0x10
    temp[ index + 12 ] = c1[ index + 12 ] ^ guess_[ index + 12 ] ^ 0x10
    temp[ index + 11 ] = c1[ index + 11 ] ^ guess_[ index + 11 ] ^ 0x10
    temp[ index + 10 ] = c1[ index + 10 ] ^ guess_[ index + 10 ] ^ 0x10
    temp[ index + 9 ] = c1[ index + 9 ] ^ guess_[ index + 9 ] ^ 0x10
    temp[ index + 8 ] = c1[ index + 8 ] ^ guess_[ index + 8 ] ^ 0x10
    temp[ index + 7 ] = c1[ index + 7 ] ^ guess_[ index + 7 ] ^ 0x10
    temp[ index + 6 ] = c1[ index + 6 ] ^ guess_[ index + 6 ] ^ 0x10
    temp[ index + 5 ] = c1[ index + 5 ] ^ guess_[ index + 5 ] ^ 0x10
    temp[ index + 4 ] = c1[ index + 4 ] ^ guess_[ index + 4 ] ^ 0x10
    temp[ index + 3 ] = c1[ index + 3 ] ^ guess_[ index + 3 ] ^ 0x10
    temp[ index + 2 ] = c1[ index + 2 ] ^ guess_[ index + 2 ] ^ 0x10
    temp[ index + 1 ] = c1[ index + 1 ] ^ guess_[ index + 1 ] ^ 0x10
    for guess in range( 0, 255 ):
        temp[ index ] = c1[ index ] ^ guess ^ 0x10
        if po.query(createArg(iv, temp, c2).encode('hex')) == True:      # Issue HTTP query with the given argument
            guess_[ index ] = guess
            break

    print '{} {}: {} - {}'.format( "Index" , index , hex( guess ) , chr(guess) )


