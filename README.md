# EDA Development

This project is a collection of open source tools used for Exploratory Data Analysis (EDA).

## Setup
`tox` is the preferred virtual environment management tool when not behind a proxy.  When dealing with a `proxy` on Windows I've found it easier to configure Anaconda.  That being the case, you'll find both options in the project, use the one that best suits your needs.

### Conda
You can create an environment from scratch, use the `eda_dev39.yml`, or use an existing environment (as long as the packages are installed).  You'll find the typical `cheet-sheets` in the `/docs/conda` folder.

### Clone - recursive to get submodules
```shell
$ git clone --recurse-submodules https://github.com/c-w-m/eda_dev.git  ## https or
$ git clone --recurse-submodules git@github.com:c-w-m/eda_dev.git      ## ssh
```

## Directory Layout
| Directory      | Description            |
|----------------|------------------------|
| docs/*         | links and notes        |
| ipynb/*        | demo notebooks         |
| src/*          | submodules             |
| src/demo       | examples               |
| src/*          | monte carlo            |

## Submodules
The following open-source projects were forked to allow experimental changes without formal pull request review in the source repository.

```
cd src
git submodule add https://github.com/c-w-m/matplotlib.git
git submodule add https://githuhttps://github.com/c-w-m/pandas.git
git submodule add https://github.com/c-w-m/pyGeometry.git
git submodule add https://github.com/c-w-m/Spirograph.git
git submodule add https://github.com/c-w-m/pyexcel-ods.git
```
#### Removing Submodules
```shell
# Remove the submodule entry from .git/config
git submodule deinit -f src/<submodule_name>

# Remove the submodule directory from the super-project's .git/modules 
directory
rm -rf .git/modules/src/<submodule_name>     #nix
rd /s /q '.git\modules\src\<submodule_name>' #win

# Remove the entry in .gitmodules and remove the submodule directory located at path/to/submodule
git rm -f src/<submodule_name>
```

## Forked Projects
These are in `src/`

| Directory  | Description            |
|------------|------------------------|
| matplotlib | plotting               |
| pandas     | data analysis          |
| pyGeometry | geometry               |
| Spirograph | Turtle drawing         |

## Demo
Example projects that demonstrate visualization code snippets.

These are in `src/demo/`

| Directory      | URL                          |
|----------------|------------------------------|
| altair-examples | https://github.com/madewitt/altair-examples.git |
| Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project | https://github.com/micgonzalez/Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project |
| data_viz_python_tutorial | https://github.com/micgonzalez/Data-Visualization-of-Pokemon-Data-with-Python-and-Seaborn_side_project.git |
| EDA-with-Seaborn | https://github.com/Devesh1997Yadav/EDA-with-Seaborn.git |
| file_IO | |
| handy_data_viz_functions | https://github.com/manukalia/handy_data_viz_functions.git |
| matplotlib-challenge | https://github.com/malvika/matplotlib-challenge.git |
| python-data-exploration | https://github.com/MartinSeeler/python-data-exploration.git |
| Seaborn-Basics | https://github.com/ashish-mehta-mlp/Seaborn-Basics.git |
| Understanding-Seaborn | https://github.com/kb22/Understanding-Seaborn.git |

## MC
Example projects that demonstrate monte carlo code snippets.

These are in `src/mc/`

| Directory      | URL                          |
|----------------|------------------------------|
| Black-Scholes-Option-Pricing-with-Monte-Carlo- | https://github.com/aldodec/Black-Scholes-Option-Pricing-with-Monte-Carlo-.git |
| MJHMC | https://github.com/rueberger/MJHMC.git |
| Monte_Carlo | https://nbviewer.jupyter.org/url/alphabench.com/data/Monte_Carlo.ipynb |
| MonteCarloMethodsInFinance | https://github.com/olafSmits/MonteCarloMethodsInFinance.git |
| Plot-and-Monte-Carlo-Simulation | https://github.com/creixotradeos/Plot-and-Monte-Carlo-Simulation.git |
| PyPlan | https://github.com/shankarj/PyPlan.git |
| VaR-Monte-Carlo-Evaluation | https://github.com/aldodec/VaR-Monte-Carlo-Evaluation.git |

## Jupyter Notebooks
Remember to use `ipykernel` to expose your python environment in Jupyterlab.
```shell
$ conda activate eda_dev39
(eda_dev39) $ python -m ipykernel install --user --name=eda_dev39
(eda_dev39) $ jupyter lab
```

## Anaconda Environment
### Create and Load Conda Environment From `yml` File
```shell
(base) $ conda env create -f eda_dev39.yml
(base) $ conda activate eda_dev39 
(eda_dev39) $ cd ipynb
(eda_dev39) $ jupyter lab
```

### Install New Conda Environment Packages
```shell
(eda_dev39) $ conda install <package name>
```

### Update Conda Environment Packages
```shell
(eda_dev39) $ conda update <package name>
```

### Export Conda Environment
```shell
(eda_dev39) $ conda env export > eda_dev39.yml
```

### Get Conda Environment
```shell
(eda_dev39) $ conda info -e
```

### Remove Conda Environment
```shell
(eda_dev39) $ conda remove -n <env_name> -all
```