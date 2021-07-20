your_file_name = 'models/cat_best_map.hdf5'
CHUNK_SIZE = 40*1024*1024
file_number = 1
with open(your_file_name, 'rb') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open(your_file_name + '_part_' + str(file_number), 'wb') as chunk_file:
            chunk_file.write(chunk)
        file_number += 1
        chunk = f.read(CHUNK_SIZE)
