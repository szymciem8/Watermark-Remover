# Watermark-Remover
## How to use

```python
python3 watermark_remover.py --image input.png
```

**Exmaple**

<table>
  <tr>
    <td>First Screen Page</td>
     <td>Holiday Mention</td>
     <td>Present day in purple and selected day in pink</td>
  </tr>
  <tr>
    <td><img src="test_images/input.png" width=400></td>
    <td><img src="test_images/output.png" width=400></td>
  </tr>
 </table>

<p float="left">
  <img
    src="test_images/input.png"
    alt="Before"
    title="Before"
    width="250">

  <img
    src="test_images/output.png"
    alt="Befor"
    title="Before"
    width="250">
</p>

Open-source application for watermark removal based on CNN. 

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
