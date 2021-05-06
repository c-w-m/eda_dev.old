# EDA Development

This project is a collection of open source tools used for Exploratory Data Analysis (EDA).

## Setup
`tox` is the preferred virtual environment management tool when not behind a proxy.  When dealing with a `proxy` on Windows I've found it easier to configure Anaconda.  That being the case, you'll find both options in the project, use the one that best suits your needs.

### Clone - recursive to get submodules
```shell
$ git clone --recurse-submodules git clone https://github.com/c-w-m/eda_dev.git  ## https or
$ git clone --recurse-submodules git clone git@github.com:c-w-m/eda_dev.git      ## ssh
```



## Submodules
Visualization consists of multiple submodules

```
cd src
git submodule add https://github.com/c-w-m/matplotlib.git
git submodule add https://github.com/c-w-m/pandas.git
git submodule add https://github.com/c-w-m/pyGeometry.git
```


## Contents
| Directory      | Description           |
|----------------|-----------------------|
