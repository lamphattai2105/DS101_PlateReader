prefix_filename = "Models/character1_best_map.hdf5"
num_files = 7
with open(prefix_filename, 'wb') as f:
	for idx in range(num_files):
		with open(prefix_filename + '_part_' + str(idx + 1), 'rb') as chunk_file:
			chunk = chunk_file.read()
			f.write(chunk)
