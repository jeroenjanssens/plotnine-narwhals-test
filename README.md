# plotnine-narwhals-test

A demonstration of an experimental version of [plotnine](https://plotnine.org)
that uses [narwhals](https://narwhals-dev.github.io/narwhals/) internally, so that:

- [polars](https://pola.rs) dataframes (and PyArrow tables) work natively and
  are **not** converted to pandas;
- [pandas](https://pandas.pydata.org) is **not** required, and not imported;
- aesthetics can be **narwhals expressions** (`aes(y=nw.col("hwy") * 0.425)`),
  and string expressions such as `"factor(cyl)"` and `"np.log(displ)"` keep
  working;
- a polars `Enum` is treated as an ordered categorical, and a polars
  `Categorical` as an unordered one;
- densities, violins and linear smooths no longer need statsmodels.

## View it without running it

[`notebook.ipynb`](notebook.ipynb) is a Jupyter version of the marimo
notebook, including all its outputs, which GitHub renders directly. It is
generated from `notebook.py` with:

```bash
uv run --with nbformat marimo export ipynb notebook.py -o notebook.ipynb \
    --include-outputs --sort top-down -f
```

## Run it on molab

(This requires a molab account.)


[![Open in molab](https://molab.marimo.io/molab-shield.svg)](https://molab.marimo.io/github/jeroenjanssens/plotnine-narwhals-test/blob/main/notebook.py)

## Run it locally

With [uv](https://docs.astral.sh/uv/), either use the project environment
(see `pyproject.toml`):

```bash
uv run marimo edit notebook.py
```

or let marimo create an isolated sandbox from the inline script metadata of
the notebook:

```bash
uvx marimo edit --sandbox notebook.py
```

Neither environment contains pandas:

```bash
uv run python -c "import plotnine, polars; import sys; print('pandas' in sys.modules)"
```

## The wheels

The `wheels/` directory has development builds of the two packages, which are
not on PyPI yet:

- `plotnine-0.16.0+narwhals`: the `narwhals` branch of plotnine, with pandas
  and statsmodels moved to an optional `pandas` extra;
- `mizani-0.14.7+optionalpandas`: the `optional-pandas` branch of mizani, in
  which pandas is an optional dependency.
