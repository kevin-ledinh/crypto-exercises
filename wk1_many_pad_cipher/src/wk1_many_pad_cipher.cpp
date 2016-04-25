//============================================================================
// Name        : wk1_many_pad_cipher.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <fstream>
#include  <iomanip>
#include <sstream>

using namespace std;

#define MAXNOOFCIPHERTXT 10

static string cipherTexts[] = {"315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba5025b8cc57ee59418ce7dc6bc41556bdb36bbca3e8774301fbcaa3b83b220809560987815f65286764703de0f3d524400a19b159610b11ef3e",
"234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb74151f6d551f4480c82b2cb24cc5b028aa76eb7b4ab24171ab3cdadb8356f",
"32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de81230b59b7afb5f41afa8d661cb",
"32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee4160ead45aef520489e7da7d835402bca670bda8eb775200b8dabbba246b130f040d8ec6447e2c767f3d30ed81ea2e4c1404e1315a1010e7229be6636aaa",
"3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de81230b59b73fb4302cd95d770c65b40aaa065f2a5e33a5a0bb5dcaba43722130f042f8ec85b7c2070",
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d79eccf52ff111284b4cc61d11902aebc66f2b2e436434eacc0aba938220b084800c2ca4e693522643573b2c4ce35050b0cf774201f0fe52ac9f26d71b6cf61a711cc229f77ace7aa88a2f19983122b11be87a59c355d25f8e4",
"32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af51373fd9b4af511039fa2d96f83414aaaf261bda2e97b170fb5cce2a53e675c154c0d9681596934777e2275b381ce2e40582afe67650b13e72287ff2270abcf73bb028932836fbdecfecee0a3b894473c1bbeb6b4913a536ce4f9b13f1efff71ea313c8661dd9a4ce",
"315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e9417df7c95bba410e9aa2ca24c5474da2f276baa3ac325918b2daada43d6712150441c2e04f6565517f317da9d3",
"271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f40462f9cf57f4564186a2c1778f1543efa270bda5e933421cbe88a4a52222190f471e9bd15f652b653b7071aec59a2705081ffe72651d08f822c9ed6d76e48b63ab15d0208573a7eef027",
"466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d66f1d559ba520e89a2cb2a83",
};
static string targetCipher = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904";
static int key[512];
static int scoreBoard[512];

static void RunXorStrings(void);
static string xorString(string a, string b, ofstream * outputFile);
static uint8_t ConvertCharToHex(char c);
static void PrintScoreBoard(int baseScore, int size, ofstream * outputFile);
static void ClearScoreBoard(void);
static void updateKey(string a, ofstream * outputFile);
static void getPlainText(string a, ofstream * outputFile);

static void RunCribDrag(void);
static void CribDragAlg(ofstream * outputFile);

int main() {
	size_t dummy;
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	RunXorStrings();
//	RunCribDrag();
	cout << "Done" << endl; // prints !!!Hello World!!!
	cin >> dummy;
	return 0;
}

static void RunXorStrings(void)
{
	cout << __FUNCTION__ << endl;
	int i, j;
	ofstream outputFile("xoredString.txt", ios::trunc);

	for (i = 0; i < 8; i++)
	{
		for (j = (i + 1); j < MAXNOOFCIPHERTXT; j++)
		{
			outputFile << "[ " << (i+1) << " ^ " << (j+1) << " ]" << "\r\n";
			outputFile << xorString(cipherTexts[i], cipherTexts[j], &outputFile);
		}
		PrintScoreBoard(MAXNOOFCIPHERTXT - 2 - i, 400, &outputFile);
		updateKey(cipherTexts[i], &outputFile);
		getPlainText(targetCipher, &outputFile);
		ClearScoreBoard();
		outputFile << endl << endl << endl;
	}
	//update key
	outputFile.close();
}

/*
 * Xor two string together and print out the result string
 *
 *  */
static string xorString(string a, string b, ofstream * outputFile)
{
	string retStr = "";
	size_t maxStrSize = 0;
	int scoreBoardIdx = 0;
	int hexStrA = 0;
	int hexStrB = 0;
	int dummyChar;
	ofstream * myfile  = outputFile;

	(*myfile) << a << endl;
	(*myfile) << b << endl;

	if( a.length() >= b.length())
	{
		maxStrSize = b.length();
	}
	else
	{
		maxStrSize = a.length();
	}
	retStr = retStr + "\r\n";
	for (size_t i = 0; i < (maxStrSize - 1); i++)
	{
		hexStrA = hexStrA | ( ConvertCharToHex(a[i]) << 4 );
		hexStrB = hexStrB | ( ConvertCharToHex(b[i]) << 4 );
		i++;
		hexStrA = ( hexStrA | ConvertCharToHex(a[i]) ) & 0xff;
		hexStrB = ( hexStrB | ConvertCharToHex(b[i]) ) & 0xff;

		(*myfile) << setfill('0') << setw(2) << hex << (hexStrA ^ hexStrB);

		dummyChar = (hexStrA ^ hexStrB) & 0xff;

		if( ((dummyChar >= 0x41) & (dummyChar <= 0x5a)) |((dummyChar >= 0x61) & (dummyChar <= 0x7a)))
		{
			retStr = retStr + (char)dummyChar;
			scoreBoard[scoreBoardIdx]++;
		}
		else if (dummyChar == 0x00)
		{
			retStr = retStr + " ";
			scoreBoard[scoreBoardIdx]++;
		}
		else
		{
			retStr = retStr + "-";
		}
		scoreBoardIdx++;
		hexStrA = 0;
		hexStrB = 0;
	}

	retStr = retStr + "\r\n";
	return retStr;
}

/*
 * Print out the current scoreboard
 * */
static void PrintScoreBoard(int baseScore, int size, ofstream * outputFile)
{
	ofstream * myFile = outputFile;
	for (int i = 0; i < (size / 2); i++)
	{
		if(scoreBoard[i] > baseScore)
		{
			(*myFile) << setfill('0') << setw(1) << scoreBoard[i];
			scoreBoard[i] = 1;
		}
		else
		{
			(*myFile) << "-"; scoreBoard[i] = 0;
		}
	}
	(*myFile) << endl;
}
static void ClearScoreBoard(void)
{
	for (int i = 0; i < 512; i++)
	{
		scoreBoard[i] = 0;
	}
}
/*
 * Update the key array using the cipher text and
 * */
static void updateKey(string a, ofstream * outputFile)
{
	int maxStrSize = a.length();
	ofstream * myfile = outputFile;

	for (int i = 0; i < 512; i++)
	{
		if( scoreBoard[i] == 1)
		{
			key[i] = (ConvertCharToHex(a[i*2]) << 4 );
			key[i] |= ConvertCharToHex(a[(i*2)+1]);
			key[i] ^= 0x20;
			(*myfile) << setfill('0') << setw(2) << hex << key[i];
		}
		else
		{
			(*myfile) << "--";
		}
		if(i >= (maxStrSize / 2))
		{
			break;
		}
	}
	(*myfile) << "key: " << endl;
}

static void getPlainText(string a, ofstream * outputFile)
{
	int maxStrSize = a.length();
	int tempByte;
	ofstream * myfile = outputFile;

	for (int i = 0; i < maxStrSize; i++)
	{
		if( key[i/2] != 0 )
		{
			tempByte = (((ConvertCharToHex(a[i]) << 4 ) | ConvertCharToHex(a[++i]))) ^ key[i/2];
			(*myfile) << setfill('0') << setw(2) << hex << tempByte;
		}
		else
		{
			i = i + 1;
			(*myfile) << "--";
		}
	}
	(*myfile) << endl;
	for (int i = 0; i < maxStrSize; i++)
	{
		if( key[i/2] != 0 )
		{
			tempByte = (((ConvertCharToHex(a[i]) << 4 ) | ConvertCharToHex(a[++i]))) ^ key[i/2];
			(*myfile) << " "<< (char)tempByte;
		}
		else
		{
			i = i + 1;
			(*myfile) << "--";
		}
	}
	(*myfile) << endl;
}
static uint8_t ConvertCharToHex(char c)
{
	uint8_t retVal = 0;
	switch(c)
	{
	case '0':
		retVal = 0;
		break;
	case '1':
		retVal = 1;
		break;
	case '2':
		retVal = 2;
		break;
	case '3':
		retVal = 3;
		break;
	case '4':
		retVal = 4;
		break;
	case '5':
		retVal = 5;
		break;
	case '6':
		retVal = 6;
		break;
	case '7':
		retVal = 7;
		break;
	case '8':
		retVal = 8;
		break;
	case '9':
		retVal = 9;
		break;
	case 'a':
	case 'A':
		retVal = 10;
		break;
	case 'b':
	case 'B':
		retVal = 11;
		break;
	case 'c':
	case 'C':
		retVal = 12;
		break;
	case 'd':
	case 'D':
		retVal = 13;
		break;
	case 'e':
	case 'E':
		retVal = 14;
		break;
	case 'f':
	case 'F':
		retVal = 15;
		break;
	default:
		break;
	}
	return retVal;
}

static void RunCribDrag(void)
{
	cout << __FUNCTION__ << endl;
	ofstream outputFile("cribDrag.txt", ios::trunc);
	if(outputFile.is_open())
	{
			CribDragAlg(&outputFile);
	}
	outputFile.close();
}

static void CribDragAlg(ofstream * outputFile)
{
	int i, j;
	uint8_t TestWord[] = " the ";
	uint8_t ResultWord[sizeof(TestWord)];
	ofstream * myFile = outputFile;
	for(i = 0; i < (cipherTexts[1].length() - sizeof(TestWord)); i++)
	{
		for(j = 0; j < sizeof(TestWord); j++)
		{
			ResultWord[j] = cipherTexts[1][i + j] ^ TestWord[j];
			(*myFile) << ResultWord[j] << "-";
		}
		(*myFile) << "\r\n";
	}
}
