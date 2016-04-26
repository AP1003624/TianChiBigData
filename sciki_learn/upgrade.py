# coding=utf8
# Create by 吴俊 on 2016/4/4

# pip一次性更新所有包
import pip
from subprocess import call
for dist in pip.get_installed_distributions():
    call("pip install --upgrade " + dist.project_name, shell=True)
