# Between-Dataset Internal Measures

Though internal Clustering Validation Measures (IVM) (e.g., [Silhouette Coefficient](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html), [Calinski-Harabasz Index](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.calinski_harabasz_score.html#sklearn.metrics.calinski_harabasz_score)) are widely used for the evaluation of clustering techniques, there exists one big problem - they cannot be used across dataset. This is because IVMs are originally designed to compare "different clusterings" of "a single dataset" to find the optimal one. 

Due to such limitation, IVMs cannot be directly used to measure and compare the cluster-label matching (i.e., the extent to which a clusters within a data matches with class labels given by a dataset). Therefore, in this repository, we introduce between-dataset internal measures  $\text{IVM}\_{btwn}$ that allows a fair comparison of clustering results across datasets. 
Using the library, you can measure how well class labels of your dataset is well clustered, and compare the result to the ones of other datasets in [the link](https://hyeonword.com/clm-datasets/).

Note that this library is developed as the product of a paper "Sanity Check for External Clustering Validation Benchmarks using Internal Validation Measures". For more informations and explanations about the concept of CLM and between-dataset internal validation measures, please refer to our paper (TBA).


### Installation

Between-dataset internal measures can be downloaded via `pip`. The library only depends on `numpy`.

```sh
pip install btwim
```

### How to use

The list of available internal measures  is as follows:
- Calinski-Harabasz 
- (More measures will appear...)

To import between-dataset internal measure package, write:
```python3
from btwim import {name_of_internal_measure} as {abbreviation}
```

For example, if you want to import between-dataset Calinski-Harabasz, type
```python3
from btwim import calinski_harabasz as ch
```

Here's the example of using between-dataset Calinski-Harabasz. `ch.btw()` gets the data (`X`) and labels (`labels`) as input and measures the score of between-dataset internal measures. If you want to use the original Calinski-Harabasz instead of the between-dataset one, use `ch.original()` instead.
```python3
from btwim import calinski_harabasz as ch
from sklearn.datasets import load_iris

X, labels = load_iris(return_X_y=True)
btw_ch_val = ch.btw(X, labels)

print(btw_ch_val)
```

### API

#### btwim.calinski_harabasz

> `btwim.calinski_harabasz.original(X, labels)`
> - Original Calinski-Harabasz Measure
> > - `X`: array, shape (n_samples, n_features) 
> >   - input data
> > - `labels`: array, shape (n_samples)
> >   - class label of the given data


> `btwim.calinski_harabasz.btw(X, labels, iter_num=20)`
> - Original Calinski-Harabasz Measure
> > - `X`: array, shape (n_samples, n_features) 
> >   - input data
> > - `labels`: array, shape (n_samples)
> >   - class label of the given data
> > - `iter_num`: int
> >   - the number of Monte Carlo simulations performed to compute the expectaiton value of the measure


### Contact

If you have any issue exploiting the library, feel free to contact us via [hj@hcil.snu.ac.kr](mailto:hj@hcil.snu.ac.kr).

### Reference

TBA
