class Bucket:
    def __init__(self, record):
        '''
        Constructor for this class.
        Initialize important bucket data.

        @param record: Dict object extract to event AWS S3
        '''
        self.record = record


    def name(self):
        '''
        Read record and extract name to bucket.

        >>> record = { "s3": { "bucket": { "name": "my.super.bucket.used.in.development" } } }
        >>> Bucket(record).name()
        'my.super.bucket.used.in.development'

        '''
        return self.record['s3']['bucket']['name']


    def key(self):
        '''
        Read record and extract key to bucket.

        >>> record = { "s3": { "object": { "key": "my/super/key/wit/super.path" } } }
        >>> Bucket(record).key()
        'my/super/key/wit/super.path'

        '''
        return self.record['s3']['object']['key']


if __name__ == "__main__":
    import doctest
    doctest.testmod(report=False, raise_on_error=True)
