import time

import schedule
from contracts.schema import CompraSchema

# from lib.classes import APICollector
from tools.aws.client import S3Client

schema = CompraSchema
aws = S3Client()


def apiCollector(schema, aws, repeat):
    # response = APICollector(schema, aws).start(repeat)
    print("Executei")
    return


schedule.every(1).minutes.do(apiCollector, schema, aws, 50)

while True:
    schedule.run_pending()
    time.sleep(1)
