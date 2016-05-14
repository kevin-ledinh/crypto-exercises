//============================================================================
// Name        : wk3_sha256.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>

#include <string>
using std::string;

#include "filters.h"

#include "hex.h"
using CryptoPP::HexEncoder;
using CryptoPP::HexDecoder;

#include "sha.h"
using CryptoPP::SHA256;

using namespace std;
using namespace CryptoPP;

// Prototypes
void GetSHA256(CryptoPP::HashTransformation& hash, char * message, int msg_size, byte * SHAOutput, int OutputSize);
void DisplayByteArray( const string ArrayName, byte * ByteArray, int ArraySize );


const int BlockSize = 1024; // 1kB
static byte message[ BlockSize ] = {0};
static byte signature[ SHA256::DIGESTSIZE ] = {0};

int main() {
	// Global variables
	SHA256 sha;
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	ifstream myfile ("sample1.mp4", ios::binary|ios::ate);

	int FileSize;
	streampos currentRdPos;
	int NumberOfBlocks = 0;
	int LastBlockSize = 0;

	if( myfile.is_open() )
	{

		// Get File parameters
		FileSize = myfile.tellg();
		NumberOfBlocks = ( FileSize / BlockSize );
		LastBlockSize = FileSize % BlockSize;
		cout << "File size is: " << FileSize << " bytes.\n";
		cout << "Number of blocks are: " << NumberOfBlocks << endl;
		cout << "Last block size is: " << LastBlockSize << endl;

		// Get the SHA256 of the last block first
		currentRdPos = FileSize - LastBlockSize;
		myfile.seekg (currentRdPos, ios::beg);
		myfile.read( ( char * ) message, LastBlockSize); // break here OMG
		cout << "Current file pos: " << myfile.tellg() << endl;


		sha.Update( (const byte * ) message, LastBlockSize);
		sha.Final(signature);
		DisplayByteArray( "First hash: ", signature, SHA256::DIGESTSIZE);

		// Calculate SHA256 of the rest of the file
		// Get 1 block at a time and calculate SHA256 of one block
		for(int i = ( NumberOfBlocks - 1 ); i >= 0; i--)
		{
			// Read the next 1kB of data
			memset( message, 0x00, BlockSize );
			currentRdPos = BlockSize * i;
			myfile.seekg (currentRdPos, ios::beg);
//			cout << "Current file pos: " << myfile.tellg() << endl;
			myfile.read( ( char * ) message, BlockSize);

			// Get the hash of the current data
			sha.Update( (const byte * ) message, BlockSize);
			sha.Update( (const byte * ) signature, SHA256::DIGESTSIZE);
			sha.Final(signature);
		}
		//print out the hash of the first block here
		DisplayByteArray( "Last hash: ", signature, SHA256::DIGESTSIZE);

	}

	myfile.close();
	return 0;
}

void GetSHA256(CryptoPP::HashTransformation& hash, char * message, int msg_size, byte * PreHash, byte * SHAOutput, int OutputSize)
{
	byte digest[ SHA256::DIGESTSIZE ];

	hash.CalculateDigest( digest, ( byte * ) message, msg_size );

	if (OutputSize == SHA256::DIGESTSIZE )
	{
		memcpy( SHAOutput , digest , OutputSize );
	}

}

void DisplayByteArray( const string ArrayName, byte * ByteArray, int ArraySize )
{
	string SHAOutputStr;
	SHAOutputStr.clear();
	StringSource(ByteArray, ArraySize, true,
		new HexEncoder(
			new StringSink(SHAOutputStr)
		) // HexEncoder
	); // StringSource
	cout << ArrayName << SHAOutputStr << endl;
}
