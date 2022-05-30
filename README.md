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

1. Download yaml-searcher

    ```bash
    curl -L https://github.com/mgla96/yaml-searcher/releases/download/v0.1.5/yaml-searcher > yaml-searcher
    ```

2. Add execution permissions

    ```bash
    chmod +x yaml-searcher
    ```

3. Place in executable PATH or call directly

## Notes / Gotchas

* zsh uses square brackets for globbing/pattern matching

  when passing square brackets in search argument for yaml-searcher, you must either escape them or quote argument

  **yaml-file.yaml**
  ```yaml
  hello:
    - world: "output"
    - world: "output2"
  ```

  **command**
  ```bash
  ./yaml-searcher 'hello[0]' < yaml-file.yaml
  ```
  ```bash
  ./yaml-searcher hello\[0\] < yaml-file.yaml
  ```
  **returns**
  ```bash
  world: output
  ```