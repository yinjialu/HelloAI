## 一键恢复环境

```zsh
conda env create -f environment.yml
```

## 激活环境

```zsh
conda activate helloAI
```

## 安装依赖

```zsh
conda install flask requests numpy
```

记录环境信息

```zsh
conda env export > environment.yml
```

可选：使用 --no-builds 参数可以让 environment.yml 更通用，避免平台依赖

```zsh
conda env export --no-builds > environment.yml
```