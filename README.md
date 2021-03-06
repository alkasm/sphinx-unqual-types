With latest Sphinx master installed and running `python -m sphinx . build` (or `sphinx-build . build`) in this folder:

```
(venv) alkasm:sphinx-unqual-types$ python -m sphinx --version
__main__.py 4.0.0+
(venv) alkasm:sphinx-unqual-types$ python -m sphinx . build
Running Sphinx v4.0.0+
building [mo]: targets for 0 po files that are out of date
building [html]: targets for 1 source files that are out of date
updating environment: [new config] 1 added, 0 changed, 0 removed
reading sources... [100%] index                                                                                                                               
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] index                                                                                                                                
Exception occurred:
  File "/Users/alkasm/prog/test-sphinx/venv/lib/python3.7/site-packages/sphinx/writers/html5.py", line 776, in unknown_visit
    raise NotImplementedError('Unknown node: ' + node.__class__.__name__)
NotImplementedError: Unknown node: pending_xref_condition
The full traceback has been saved in /var/folders/1v/dvnfrhkx43x5lgg1810_2nmr0000gn/T/sphinx-err-ct6jaept.log, if you want to report the issue to the developers.
Please also report this if it was a user error, so that a better error message can be provided next time.
A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!
```

Sphinx was installed by cloning the repo, chaning to master branch, and running a `pip install .` inside a new virtual environment.
