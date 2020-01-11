import os
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
pathForFile=path+ "/file"

result = {}
def path():
    basepath = str(pathForFile)
    for file in os.listdir(basepath):
        if os.path.isfile(os.path.join(basepath, file)):
            r = basepath+ "/" + file
            filepath, filenames = os.path.split(r)
            result.update({filenames.split(".")[1]: os.path.join(filepath, filenames)})
    return result

