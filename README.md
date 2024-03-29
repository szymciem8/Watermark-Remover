# Watermark-Remover

![Made with Python](https://img.shields.io/badge/Python-FFD43B?style=flat&logo=python&logoColor=blue)
![Tensorflow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat&logo=tensorflow&logoColor=white)
[![Made with Jupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat&logo=Jupyter)](https://jupyter.org/try)
![Made with AWS](https://img.shields.io/badge/Amazon_AWS-232F3E?style=flat&logo=amazon-aws&logoColor=white)


Open-source application for watermark removal based on CNN. 

## How to use

```python
python3 watermark_remover.py --image input.png
```

**Exmaple**

<table>
  <tr>
     <td>Before</td>
     <td>After</td>
  </tr>
  <tr>
    <td><img src="test_images/input.png" width=475></td>
    <td><img src="test_images/output.png" width=475></td>
  </tr>
 </table>

## Docker
Application can be run with docker. 

### Build

```bash
docker build . -t watermark_remover
```

### Run
```bash
docker run -v$(pwd):/home -p 8888:8888 watermark_remover
```

Or if you want to retrain the model you need access to your S3 for which you have to define keys in .env file. Then you can run this command. 

```bash
docker run -v$(pwd):/home -p 8888:8888 --env-file .env watermark_remover .env
```
