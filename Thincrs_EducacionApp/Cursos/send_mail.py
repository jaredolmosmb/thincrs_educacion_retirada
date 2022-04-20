import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

with sshtunnel.SSHTunnelForwarder(
    ('18.222.146.90'),
    ssh_username='ubuntu', ssh_password='secret1',
    remote_bind_address=('develop-instance.cici1guul97n.us-east-2.rds.amazonaws.com', 3306)
) as tunnel:
    connection = mysql.connector.connect(
        user='develop_thincrs', password='Thincrs_password2021',
        host='127.0.0.1', port=tunnel.local_bind_port,
        database='develop_thincrs',
    )
    # Do stuff
    print(connection)
    connection.close()