# coding: utf-8
import os
from androguard.core.bytecodes.apk import *
from tools import logTool

OUTPUT_PATH = "/data/confuse_apk"

algorithms = ["transformAndroidManifest", "renameclasses", "reverseorder", \
              "encString", "encArrays", "remDebugInfo", "reorder", "nontrivialjunk", \
              "insertnops", "insertFunctionIndirection", "doci", "renameMethods", "renameFields"]

# algorithms=['renameMethods']

droidc_path = '/home/tuomao/Desktop/anroid_security/android-av/droidc'


# 单一算法混淆
def single_confuse_apk(apk):

    (filepath, apk_name) = os.path.split(apk)
    # 使用droidc的时候 工作路径必须与apk在同一个路径之下
    os.chdir(filepath)
    print("当前工作路径:"+os.getcwd())
    apk_package = fast_get_package_name(apk)
    for algorithm in algorithms:
        command = '{0} -{1} {2} {3} {4}'
        output_dir = os.path.join(OUTPUT_PATH, algorithm)
        ensure_idr(output_dir)
        output_apk = os.path.join(output_dir,apk_name)

        temp_apk ='temp.apk'
        # 确保文件不存在
        if os.path.exists(temp_apk):
            os.system('rm %s'%(temp_apk))

        # 混淆apk
        command = command.format(droidc_path, algorithm, apk,temp_apk,apk_package)
        logTool.logger.info(command)
        os.system(command)

        # 将临时文件移动到目标文件夹下面
        if os.path.exists(temp_apk):
            mv_command ='mv %s %s'%(temp_apk,output_apk)
            os.system(mv_command)
            logTool.logger.info('%s 混淆算法成功'%(algorithm))
        else:
            logTool.logger.error('%s 混淆算法失败'%(algorithm))
    print('%s 处理完成'%(apk))

# 多种算法混淆
def multi_confuse_apk(apk):
    confuse_algorithms=['-renameclasses','-reverseorder','-reorder','-insertFunctionIndirection','-nontrivialjunk']
    # confuse_algorithms=['-insertFunctionIndirection']
    algorithm=' '.join(confuse_algorithms)
    (filepath, apk_name) = os.path.split(apk)
    # 使用droidc的时候 工作路径必须与apk在同一个路径之下
    os.chdir(filepath)
    print("当前工作路径:"+os.getcwd())
    apk_package = fast_get_package_name(apk)

    command = '{0} {1} {2} {3} {4}'
    output_dir = os.path.join(OUTPUT_PATH, 'multi')
    ensure_idr(output_dir)
    output_apk = os.path.join(output_dir,apk_name)

    temp_apk ='temp.apk'
    # 确保文件不存在
    if os.path.exists(temp_apk):
        os.system('rm %s'%(temp_apk))

    # 混淆apk
    command = command.format(droidc_path, algorithm, apk,temp_apk,apk_package)
    logTool.logger.info(command)
    os.system(command)

    # 将临时文件移动到目标文件夹下面
    if os.path.exists(temp_apk):
        mv_command ='mv %s %s'%(temp_apk,output_apk)
        os.system(mv_command)
        logTool.logger.info('%s 混淆算法成功'%(algorithm))
    else:
        logTool.logger.error('%s 混淆算法失败'%(algorithm))
    print('%s 处理完成'%(apk))

def fast_get_package_name(apk_path):
    apk = APK(apk_path)
    return apk.get_package()


# 创建目录
def ensure_idr(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


# single_confuse_apk('/home/tuomao/Downloads/Gen_Signature_Android2.apk')
# multi_confuse_apk('/home/tuomao/Downloads/Gen_Signature_Android2.apk')
# single_confuse_apk('/home/tuomao/Downloads/com.douban.daily_181.apk')
# multi_confuse_apk('/home/tuomao/Downloads/com.douban.daily_181.apk')
single_confuse_apk('/home/tuomao/Downloads/com.douban.daily_181.apk')