"""Test module"""
import os
from pathlib import Path
import unittest
from datatransfer.storage import S3Storage
from datatransfer import settings


# Create your tests here.
TEST_FILE_LIST = ['test_csv.csv', 'test_json.json', 'test_xml.xml']
TEST_CONTENT = b'THIS SHOULD STILL BE HERE'

class TestS3Upload(unittest.TestCase):
    """Test class for uploading to S3 Bucket"""
    def test_01_setup(self):
        """Setup test files"""
        directory = './tests/files/'
        if not os.path.exists(directory):
            os.makedirs(directory)

        for file_name in TEST_FILE_LIST:
            Path(os.path.join(directory, file_name)).touch()
            with open(os.path.join(directory, file_name),'wb') as test_file:
                test_file.write(TEST_CONTENT)
            test_file.close

    def test_upload_to_s3_bucket(self):
        """Uploads the test files to S3"""
        conf = {
            'path': 'tests',
            'AWS_S3_HOST': settings.WRITE_AWS_S3_HOST,
            'AWS_S3_BUCKET_NAME': settings.WRITE_AWS_S3_BUCKET_NAME,
            'AWS_ACCESS_KEY_ID': settings.WRITE_AWS_ACCESS_KEY_ID,
            'AWS_SECRET_ACCESS_KEY': settings.WRITE_AWS_SECRET_ACCESS_KEY,
            'AWS_S3_REGION': settings.WRITE_AWS_S3_REGION,
            'USE_IAM_CREDS': settings.USE_IAM_CREDS,
        }
        storage = S3Storage(conf)
        for file_name in TEST_FILE_LIST:
            with open(os.path.join('./tests/files/', file_name), 'rb') as tempfile:
                data = tempfile.read()
                storage.write_file(file_name, data)
