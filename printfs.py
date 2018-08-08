import os

top = os.getcwd()

print('cwd: ', top)

files = os.listdir('.')
print('Files: ', ', '.join(files))


# for root, dirs, files in os.walk(top):
#     print(root)
#     print('{:<4}'.format(', '.join(files)))