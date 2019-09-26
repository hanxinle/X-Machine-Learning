# pyhon开发环境配置

* 系统 Ubuntu 16.04
* 版本 Python 3.6

相对于系统自带的Python,Anaconda方便对不同的项目进行不同的管理,每个环境可以不同的开发环境,免去了频繁设置的繁琐和包管理,项目移植时环境配置问题.使用Anaconda需要掌握环境管理和package管理.
这里给出[官方的教程链接](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#specifying-a-location-for-an-environment),下面用中文简要摘抄一些内容.

### Anaconda 环境管理

conda 版本查看

conda --version 

更新conda
conda update conda

更新anaconda

conda update anaconda

更新python

conda update python

查看已经创建的环境

conda env list

创建环境

conda create -n <env_name> python=x.x

x.x 指定了Python的版本,可在后面跟着包的名字,创建环境时自动安装指定开发包.

创建环境后,需要激活开发环境,在创建结束后,系统都会提示相应的激活和关闭环境命令,一般而言如下,

conda activate <env_name> | source activate <env_name> | activate <env_name>

conda deactivate <env_name> | source deactivate <env_name> | activate <env_name>

共享开发环境,网络教材场会提供.yml文件,即可完成开发环境共享,跟着作者说明执行相应命令.

复制开发环境

conda create -n <env_clone_name> --clone <env_source_name>

删除环境

conda remove -n <env_name> --all

### Anaconda 包管理

通过conda 命令安装

conda install <package_name> = x.x.x 
(x.x.x指定版本,可缺省)

查看已经安装的packages

conda list

查看某个指定环境的已安装包

conda list -n <env_name>

给指定环境安装package

conda install -n <env_name> <package_name>

如果不用-n指定环境名称，则被安装在当前活跃环境

更新package

conda update -n <env_name> <package_name>

删除package

conda remove -n <env_name> <package_name>

更新conda，保持conda最新

conda update conda

有些package通过conda install 命令无法直接安装,那么则需要搜索并且根据提示安装.如下,

anaconda search -t conda <package_name>

可以看到以列表形式给出了所有相关的库,注意查看支持的Python版本和操作系统,在name中,复制内容到下面的参数<>中,

anaconda show <name_value>

此时会给出package的版本信息,注意最后一句,会给出安装命令,执行即可安装.


### jupyter notebook使用教程

[(转)jupyter notebook教程](https://jackpopc.github.io/2019/09/14/jupyter/)
