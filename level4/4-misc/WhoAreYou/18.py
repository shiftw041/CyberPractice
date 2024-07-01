def swap_nibbles(filename, new_filename):
    with open(filename, 'rb') as original_file, open(new_filename, 'wb') as new_file:
        while True:
            byte = original_file.read(4)
            if not byte:
                break   
            swapped_byte = byte[::-1]
            new_file.write(swapped_byte)
swap_nibbles('WhoAreYou.jpg', 'swapped_image.jpg')

