import boto3

class S3Client:
    def __init__(self, access_key, secret_key, bucket_name, bucket_region):
        assert access_key != ''
        assert secret_key != ''
        assert bucket_name != ''
        assert bucket_region != ''
        
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.bucket_region =bucket_region
        self.client = None
    
    def get_client(self):
        assert self.access_key != ''
        assert self.secret_key != ''
        assert self.bucket_name != ''
        assert self.bucket_region != ''

        if(self.client is None):
            self.client = boto3.client('s3', aws_access_key_id=self.access_key, aws_secret_access_key=self.secret_key)
        return self.client

    def upload(self, file_location, key):
        client = self.get_client()
        try:
            client.put_object(Body=file_location, Bucket=self.bucket_name, Key=key)
        except Exception as e:
            print("S3 Connection Error: {}".format(e.args[0]))
