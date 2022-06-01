to connect postgress to data studio obtain the following from bash - server:
openssl req -newkey rsa:2048 -nodes -keyout client.key -x509 -days 365 -out client.crt

jdbc:postgresql://ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/dd56ic503d1hq5?ssl=true&sslmode=verify-ca