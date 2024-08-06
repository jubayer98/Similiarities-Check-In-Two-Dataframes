# import important libraries
import pandas as pd
import os

# load and read file
df = pd.read_csv('file.tsv', sep='\t')

# columns (replace with your columns name) needed for check the similarities
df_filtered = df.loc[:, ['FASTQ_FILE', 'MD5']]

# set the directory path to the folder containing .md5sum files
folder_path = 'directory_that_contains_md5sum_files'

# list all files that end with .md5sum
md5_files = [f for f in os.listdir(folder_path) if f.endswith('.md5sum')]

# initialize an empty DataFrame to store all the data
all_md5_data = pd.DataFrame()

# loop through each file, read its contents, and append to the dataframe
for file in md5_files:
    file_path = os.path.join(folder_path, file)
    data = pd.read_csv(file_path, header=None, names=['MD5', 'Filename'], delim_whitespace=True)
    all_md5_data = pd.concat([all_md5_data, data], ignore_index=True)

### SIMILARITY CHECK - COMMENT OUT BASED ON YOUR NEED ###

# check if columns are identical
#similar = df_filtered['FASTQ_FILE'].equals(all_md5_data['Filename'])
#print(similar)  # returns True if all elements match exactly, False otherwise

# check if both columns contain the same values (ignoring order)
#similar = set(df_filtered['FASTQ_FILE']) == set(all_md5_data['Filename'])
#print(similar)  # returns True if all elements match exactly, False otherwise

# check if the statistical properties of both columns are similar
#similar_mean = df_filtered['colX'].mean() == all_md5_data['colY'].mean()
#similar_std = df_filtered['colX'].std() == all_md5_data['colY'].std()
#print('Similar Mean:', similar_mean)
#print('Similar Standard Deviation:', similar_std)

# check if values are approximately equal within some tolerance
#tolerance = 0.01  # define tolerance
#similar_within_tolerance = (df_filtered['colX'] - all_md5_data['colY']).abs().max() <= tolerance
#print(similar_within_tolerance)

### CROSS-CHECK SIMILARITES USING LEFT MERGE FUNCTION ###

# merge the dataframes
merged_df = pd.merge(df_filtered, all_md5_data, on='MD5', how='left', indicator=True)

# create the flag column
merged_df['Match'] = merged_df['_merge'] == 'both'

# drop the _merge column if not needed
merged_df.drop(columns=['_merge'], inplace=True)

# save the DataFrame to a Text file with hash as the separator
merged_df.to_csv('filename.txt', sep='#', index=False)
