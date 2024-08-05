import boto3

docdb = boto3.client('docdb-elastic')

class Elastic_DocDB:
    def __init__(self, name):
        self.name = name

    def create_db_cluster(self):
        resp = docdb.create_cluster(
            adminUserName='emmanuel',
            adminUserPassword='emmanuel',
            authType='PLAIN_TEXT',
            clusterName='my-docdb-cluster',
            shardCapacity=2,
            shardCount=1,
            backupRetentionPeriod=1
        )

        print(resp)

DB_Environment = Elastic_DocDB('DB_Environment')
DB_Environment.create_db_cluster()