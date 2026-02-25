# dynasub

Use `${var}` syntax to substitute variables into Python code at runtime.

## Install

```bash
pip install dynasub
```

## Usage

```python
import dynasub

keywords = ['sum', 'max', 'min']
data = [[3,1,2],[1,2,3],[2,3,1]]

for i in keywords:
    result_${i} = sorted(data, key=lambda x: ${i}(x))

print(result_sum)
print(result_max)
print(result_min)
```

Just put `import dynasub` at the top of your file. Any line containing `${varname}` will have the variable substituted in at runtime before the line executes.

## Why?

When you have repetitive lines that differ only by a keyword — especially with lambdas or complex expressions — you can loop over the keywords and use `${i}` instead of duplicating code.
