from struct import pack, unpack
#math.pi
pack("f",3.1415) # b"V\x0eI@"
unpack("f",b"V\x0eI@")

a,b,c=unpack("hil",b'\x03\x00\x00\x00\x0e\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00')

