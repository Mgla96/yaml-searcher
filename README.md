# yaml-searcher
A command line utility to search through yaml for a specific value. 

It reads yaml from stdin and outputs the value you are searching for.

## Examples

Search in yaml for result of field `hello.world`

**yaml-file.yaml**
```yaml
hello:
  world: "output"
```

redirect yaml file
```
./yaml-searcher hello.world < yaml-file.yaml
```

pipe in yaml file
```
cat yaml-file.yaml | ./yaml-searcher hello.world
```

Both will return `output`


## Installation