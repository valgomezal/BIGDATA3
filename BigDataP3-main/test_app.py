
from punto1.get_animals import get_animals
from punto2.create_item import create_item

import requests
import unittest


class GetAnimals(unittest.TestCase):
    def test_find_animals(self):
        r = requests.get("https://misanimales.com/")
        f = open("file.html", "w", encoding="utf8")
        f.writelines(r.text)
        f.close()
        f2 = open("file.html", "r", encoding="utf8")
        self.assertEqual(len(get_animals(f2)) > 0, True)
        f2.close()

    def test_get_labels(self):
        element = {
            'Labels':
         [
            {
                'Name': 'Fish', 
                'Confidence': 97.00613403320312, 
                'Instances': [
                    {
                        'BoundingBox': 
                        {
                            'Width': 0.868877112865448, 
                            'Height': 0.42535024881362915, 
                            'Left': 0.0983937680721283, 
                            'Top': 0.2854614853858948
                        }, 
                        'Confidence': 97.00613403320312
                    }
                ], 
                'Parents': [
                    {
                        'Name': 'Animal'
                    }, 
                    {
                        'Name': 'Sea Life'
                    }
                ], 
                'Aliases': [], 
                'Categories': [
                    {
                        'Name': 'Animals and Pets'
                    }
                ]
            }, 
            {
                'Name': 'Sea Life', 
                'Confidence': 97.00613403320312, 
                'Instances': [], 
                'Parents': [
                    {'Name': 'Animal'}
                ], 
                'Aliases': [], 
                'Categories': [
                    {'Name': 'Animals and Pets'}
                    ]
            }, 
            {
                'Name': 'Animal', 
                'Confidence': 97.00613403320312, 
                'Instances': [], 
                'Parents': [], 
                'Aliases': [], 
                'Categories': [
                    {'Name': 'Animals and Pets'}
                ]
            }, 
            {
                'Name': 'Halibut', 
                'Confidence': 94.02330780029297, 
                'Instances': [], 
                'Parents': [
                    {'Name': 'Animal'}, 
                    {'Name': 'Fish'}, 
                    {'Name': 'Sea Life'}
                ], 
                'Aliases': [{'Name':'Flounder'}], 
                'Categories': [{'Name': 'Animals and Pets'}]}, 
            {
                    'Name': 'Food', 
                    'Confidence': 63.40612030029297, 
                    'Instances': [], 
                    'Parents': [], 
                    'Aliases': [], 
                    'Categories': [{'Name': 'Food and Beverage'}]}], 
                'LabelModelVersion': '3.0', 
                'ResponseMetadata': {
                    'RequestId': 'b529c938-e94b-4024-853b-a81183e17cdb',
                    'HTTPStatusCode': 200, 
                    'HTTPHeaders': {
                        'x-amzn-requestid': 'b529c938-e94b-4024-853b-a81183e17cdb', 
                        'content-type': 'application/x-amz-json-1.1', 
                        'content-length': '983', 
                        'date': 'Fri, 25 Nov 2022 00:36:38 GMT'
                    }, 
                    'RetryAttempts': 0
                }
        }
        item = create_item(element["Labels"], "s3bucketurl")
        self.assertEqual("indice" in item, True)
        self.assertEqual("route" in item, True)
        self.assertEqual("info" in item, True)


if __name__ == "__main__":
    unittest.main()
