import boto3
import get_animals
import requests
import time
import os
from urllib.parse import urlparse
bucket_name="animalimagesfromscrapping"
bucket_to_save_images = "buckettosaveimagesofanimalsforbigdata"
def handler(event,context):
    r = requests.get("https://misanimales.com/")
    f = open("/tmp/file.html", "w", encoding="utf8")
    f.writelines(r.text)
    f.close()
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/file.html', bucket_name,'html_files/file.html')
    time.sleep(10)
    s3.meta.client.download_file(bucket_name, 'html_files/file.html', '/tmp/file.html')
    f = open("/tmp/file.html", "r", encoding="utf8")
    images=get_animals.get_animals(f)
    f.close()
    for image in images:
        url = image.get("src")
        if url.startswith("http"):
            a = urlparse(url)
            filename=os.path.basename(a.path)
            img_file= requests.get(url)
            f=open(f"/tmp/{filename}","wb")
            f.write(img_file.content)
            f.close()
            s3.meta.client.upload_file(f"/tmp/{filename}", bucket_to_save_images,f'images/{filename}')
    return {
        'statusCode': 200,
        'body': 'Logs generated!'
    }