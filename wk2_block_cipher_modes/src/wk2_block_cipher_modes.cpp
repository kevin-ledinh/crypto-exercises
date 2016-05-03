//============================================================================
// Name        : wk2_block_cipher_modes.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include "osrng.h"
using CryptoPP::AutoSeededRandomPool;

#include <iostream>
using std::cout;
using std::cerr;
using std::endl;

#include <string>
using std::string;

#include <cstdlib>
using std::exit;

#include "cryptlib.h"
using CryptoPP::Exception;

#include "hex.h"
using CryptoPP::HexEncoder;
using CryptoPP::HexDecoder;

#include "filters.h"
using CryptoPP::StringSink;
using CryptoPP::StringSource;
using CryptoPP::StreamTransformationFilter;

#include "aes.h"
using CryptoPP::AES;

#include "ccm.h"
using CryptoPP::CBC_Mode;
using CryptoPP::CTR_Mode;

#include "assert.h"
using namespace std;

static byte CBCKey[] = { 0x14, 0x0b, 0x41, 0xb2, 0x2a, 0x29, 0xbe, 0xb4, 0x06, 0x1b, 0xda, 0x66, 0xb6, 0x74, 0x7e, 0x14 };
static byte CTRKey[] = { 0x36, 0xf1, 0x83, 0x57, 0xbe, 0x4d, 0xbd, 0x77, 0xf0, 0x50, 0x51, 0x5c, 0x73, 0xfc, 0xf9, 0xf2 };

static byte CBCiv1[] = { 0x4c, 0xa0, 0x0f, 0xf4, 0xc8, 0x98, 0xd6, 0x1e, 0x1e, 0xdb, 0xf1, 0x80, 0x06, 0x18, 0xfb, 0x28 };
static byte CBCiv2[] = { 0x5b, 0x68, 0x62, 0x9f, 0xeb, 0x86, 0x06, 0xf9, 0xa6, 0x66, 0x76, 0x70, 0xb7, 0x5b, 0x38, 0xa5 };

static string CBCCipherTxt1 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81";
static string CBCCipherTxt2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253";


// remember to remove the iv in CRT mode before decrypting the cipher text
static string CRTCipherTxt1 = "0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329";
static string CRTCipherTxt2 = "e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451";

static byte CRT1[] = { 0x69, 0xdd, 0xa8, 0x45, 0x5c, 0x7d, 0xd4, 0x25, 0x4b, 0xf3, 0x53, 0xb7, 0x73, 0x30, 0x4e, 0xec };
static byte CRT2[] = { 0x77, 0x0b, 0x80, 0x25, 0x9e, 0xc3, 0x3b, 0xeb, 0x25, 0x61, 0x35, 0x8a, 0x9f, 0x2d, 0xc6, 0x17 };

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!

	string plain = "CBC Mode Test";
	string cipher, encoded, recovered;

	/*********************************\
	\*********************************/

	// Pretty print key
	encoded.clear();
	StringSource(CBCKey, sizeof(CBCKey), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CBCkey: " << encoded << endl;

	encoded.clear();
	StringSource(CTRKey, sizeof(CTRKey), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CRTkey: " << encoded << endl;

	// Pretty print iv
	encoded.clear();
	StringSource(CBCiv1, sizeof(CBCiv1), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CBCiv1: " << encoded << endl;

	// Pretty print iv
	encoded.clear();
	StringSource(CBCiv2, sizeof(CBCiv2), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CBCiv2: " << encoded << endl;

	cout << "CBCCipherTxt1 length: " << CBCCipherTxt1.length() << endl;


	encoded.clear();
	StringSource(CRT1, sizeof(CRT1), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CRT1:   " << encoded << endl;

	encoded.clear();
	StringSource(CRT2, sizeof(CRT2), true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "CRT2:   " << encoded << endl;


	/*********************************\
	\*********************************/
#if 0
	try
	{
		cout << "plain text: " << plain << endl;

		CBC_Mode< AES >::Encryption e;
		e.SetKeyWithIV(key, sizeof(key), iv);

		// The StreamTransformationFilter removes
		//  padding as required.
		StringSource s(plain, true,
			new StreamTransformationFilter(e,
				new StringSink(cipher)
			) // StreamTransformationFilter
		); // StringSource

#if 0
		StreamTransformationFilter filter(e);
		filter.Put((const byte*)plain.data(), plain.size());
		filter.MessageEnd();

		const size_t ret = filter.MaxRetrievable();
		cipher.resize(ret);
		filter.Get((byte*)cipher.data(), cipher.size());
#endif
	}
	catch(const CryptoPP::Exception& e)
	{
		cerr << e.what() << endl;
		exit(1);
	}
	/*********************************\
	\*********************************/

	// Pretty print
	encoded.clear();
	StringSource(cipher, true,
		new HexEncoder(
			new StringSink(encoded)
		) // HexEncoder
	); // StringSource
	cout << "cipher text: " << encoded << endl;

#endif
	/*********************************\
	\*********************************/
	string cipher_raw;
	{
		CryptoPP::HexDecoder decoder;
		decoder.Put((byte*)CRTCipherTxt1.data(), CRTCipherTxt1.size());
		decoder.MessageEnd();

		long long size = decoder.MaxRetrievable();
		cipher_raw.resize(size);
		decoder.Get((byte*)cipher_raw.data(), cipher_raw.size());
		// If we print this string it's completely rubbish:
		// std::cout << "Raw cipher: " << cipher_raw << std::endl;
	}

	try
	{
	    CTR_Mode< AES >::Decryption d;
	    d.SetKeyWithIV( CTRKey, sizeof(CTRKey), CRT1 );

	    // The StreamTransformationFilter removes
	    //  padding as required.
	    StringSource ss3( cipher_raw, true,
	        new StreamTransformationFilter( d,
	            new StringSink( recovered )
	        ) // StreamTransformationFilter
	    ); // StringSource

	    cout << "CRT cipher recovered text: " << recovered << endl;
	}
	catch( CryptoPP::Exception& e )
	{
	    cerr << e.what() << endl;
	    exit(1);
	}
#if 0
	string CBCcipher_raw;
	{
		CryptoPP::HexDecoder decoder;
		decoder.Put((byte*)CBCCipherTxt2.data(), CBCCipherTxt2.size());
		decoder.MessageEnd();

		long long size = decoder.MaxRetrievable();
		CBCcipher_raw.resize(size);
		decoder.Get((byte*)CBCcipher_raw.data(), CBCcipher_raw.size());
		// If we print this string it's completely rubbish:
		// std::cout << "Raw cipher: " << cipher_raw << std::endl;
	}
	try
	{
		CBC_Mode< AES >::Decryption d;
		d.SetKeyWithIV(CBCKey, sizeof(CBCKey), CBCiv1);

		// The StreamTransformationFilter removes
		//  padding as required.
		StringSource s(CBCcipher_raw, true,
			new StreamTransformationFilter(d,
				new StringSink(recovered)
			) // StreamTransformationFilter
		); // StringSource

#if 0
		StreamTransformationFilter filter(d);
		filter.Put((const byte*)cipher.data(), cipher.size());
		filter.MessageEnd();

		const size_t ret = filter.MaxRetrievable();
		recovered.resize(ret);
		filter.Get((byte*)recovered.data(), recovered.size());
#endif

		cout << "CBC recovered text: " << recovered << endl;
	}
	catch(const CryptoPP::Exception& e)
	{
		cerr << e.what() << endl;
		exit(1);
	}
#endif
	/*********************************\
	\*********************************/
	return 0;
}
