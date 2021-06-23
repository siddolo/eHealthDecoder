'''
eHealth EU Digital COVID Certificate Decoder

Pasquale 'sid' Fiorillo
https://github.com/siddolo/eHealthDecoder
'''

import sys
import zlib
import cbor2
import json
from base45 import b45decode, b45encode
from cose.messages import Enc0Message, CoseMessage

[QrCodeData] = sys.argv[1:]
HealthCertificateVersion = QrCodeData[2]
Base45EncodedData = QrCodeData[4:]
ZlibCompressedData = b45decode(Base45EncodedData)
COSESignedDocument = zlib.decompress(ZlibCompressedData)
CBORBinaryDocument = CoseMessage.decode(COSESignedDocument)
JSONDocument = cbor2.loads(CBORBinaryDocument.payload)
print(f'Health Certificate Version: {HealthCertificateVersion}')
print(json.dumps(JSONDocument, indent=4))

