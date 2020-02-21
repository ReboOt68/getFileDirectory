import os

#By:rebootORZ

def list_all_files(rootdir):
    _files = []
    l1 = os.listdir(rootdir)# 列出文件夹下的所有目录和文件
    for i in range(0,len(l1)):
        path = os.path.join(rootdir, l1[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    _files = list(set(_files))
    return _files

def list_all_dirs(rootdir):
    _dirs = []
    #result = list_all_files(rootdir)
    for dir in result1:
        dir = os.path.split(dir)
        _dirs.append(dir[0])
    _dirs = list(set(_dirs))
    return _dirs

def file_out_put(result1,result2,rootdir):
    file1 = open("FileDirectory.txt","w")
    for dir in result1:
        Relative_Path_File = dir.replace(rootdir,'').replace("\\", "/")
        file1.write(Relative_Path_File + "\n")#Relative_Path
    file1.close()

    file2 = open("DirDirectory.txt", "w")
    for dir in result2:
        Relative_Path_Dir = dir.replace(rootdir, '').replace("\\", "/")
        file2.write(Relative_Path_Dir + "\n")  # Relative_Path
    file2.close()

if __name__ == '__main__':
    rootdir = input("请输入根目录地址：\n例如：C:/Users/Ethan Hong/Desktop/www\n")
    result1 = list_all_files(rootdir)
    result2 = list_all_dirs(rootdir)
    print("\n总共:" + str(len(result1)) + "个文件," + str(len(result2)) + "个目录。\n")
    file_out_put(result1,result2,rootdir)
    print("文件字典：FileDirectory.txt\n目录字典：Dirirectory.txt\n按任意键退出...\n")
