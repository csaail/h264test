import h264decoder

# List the contents of the module
print(dir(h264decoder))

# Check if H264Decoder is present in the module
if 'H264Decoder' in dir(h264decoder):
    print("H264Decoder class is present in the module.")
else:
    print("H264Decoder class is not present in the module.")
