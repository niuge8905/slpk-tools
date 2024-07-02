import gzip

# Writing to a gzip file
with gzip.open('./data/file.gz', 'wt') as f:
    f.write('Hello, world!')

# Reading from a gzip file
with gzip.open('./data/file.gz', 'rt') as f:
    content = f.read()

print(content)